"""100-pillar engine. Families A-I (90 pillars) are computed here from prices, fund facts and FRED.
Family J (10 news pillars) is read from runs/<week>/news/J*.json written by the news agents.
Every pillar becomes a 0-100 score (100 = best) by percentile rank across active ETFs; missing = 50 (neutral)."""
import io, json
from pathlib import Path
import numpy as np, pandas as pd, requests

ROOT = Path(__file__).resolve().parents[1]
TD = 252

# id: (family, name, direction)  direction +1 higher is better, -1 lower is better
REG = {}
def reg(fam, items):
    for i, (name, d) in enumerate(items, 1):
        REG[f"{fam}{i:02d}"] = (fam, name, d)
reg("A", [("Return 1 week", 1), ("Return 1 month", 1), ("Return 3 months", 1), ("Return 6 months", 1), ("Return 12 months", 1),
          ("Momentum 12-1 months", 1), ("Price vs 50-day average", 1), ("Price vs 200-day average", 1),
          ("Above 10-month average (Faber)", 1), ("50-day vs 200-day average", 1)])
reg("B", [("Excess return vs VT 1m", 1), ("Excess return vs VT 3m", 1), ("Excess return vs VT 6m", 1), ("Excess return vs VT 12m", 1),
          ("Rank in bucket 3m", 1), ("Rank in bucket 12m", 1), ("Excess vs bucket median 6m", 1),
          ("Relative-strength slope vs VT 13w", 1), ("Share of weeks beating VT 26w", 1), ("Information ratio vs VT 1y", 1)])
reg("C", [("Volatility 1m", -1), ("Volatility 3m", -1), ("Volatility 1y", -1), ("Volatility of volatility", -1),
          ("Downside deviation 1y", -1), ("Volatility regime 1m/1y", -1), ("Beta to VT 1y", -1), ("Correlation to VT 1y", -1),
          ("Idiosyncratic volatility 1y", -1), ("Average true range 14d %", -1)])
reg("D", [("Drawdown from 52-week high", 1), ("Max drawdown 1y", 1), ("Max drawdown 3y", 1), ("Max drawdown full history", 1),
          ("Ulcer index 1y", -1), ("CVaR 95% weekly 3y", 1), ("Skewness weekly 3y", 1), ("Kurtosis weekly 3y", -1),
          ("Days since all-time high", -1), ("Share of 3y max drawdown recovered", 1)])
reg("E", [("Sharpe 1y", 1), ("Sharpe 3y", 1), ("Sharpe 5y", 1), ("Sortino 3y", 1), ("Calmar 3y", 1), ("Martin ratio 3y", 1),
          ("Share of positive months 3y", 1), ("Worst rolling 12m return 5y", 1), ("CAGR 5y", 1), ("CAGR 10y", 1)])
reg("F", [("Average daily dollar volume 3m", 1), ("Dollar volume trend 1m/6m", 1), ("Amihud illiquidity", -1),
          ("High-low range 20d", -1), ("Volume spike frequency 3m", -1), ("History length years", 1),
          ("Missing data share", -1), ("Price jumps over 4 sigma 1y", -1), ("On-balance volume slope 3m", 1), ("Chaikin money flow 20d", 1)])
reg("G", [("Expense ratio", -1), ("Assets under management", 1), ("Fund age years", 1), ("Closure risk flag", -1),
          ("Tracking deviation vs bucket 1y", -1), ("Price vs NAV gap", -1), ("Distribution yield (context)", 0),
          ("UCITS line available on LSE", 1), ("UAE withholding drag bps", -1), ("US estate-tax exposure", -1)])
reg("H", [("Yield curve 10y-2y", 1), ("Yield curve 10y-3m", 1), ("Sahm rule", 1), ("High-yield spread trend", 1),
          ("Real yield trend 10y", 1), ("US dollar trend", 1), ("Oil trend", 1), ("Financial conditions (NFCI)", 1),
          ("VIX level", 1), ("VIX term structure", 1)])
reg("I", [("P/E", -1), ("P/B", -1), ("P/S", -1), ("P/CF", -1), ("Bond duration (bond funds)", -1), ("Earnings yield minus 10y Treasury yield", 1),
          ("Top-10 holdings weight", -1), ("Sector concentration HHI", -1), ("Largest holding weight", -1), ("P/E vs bucket median", -1)])
reg("J", [("Global macro and central banks", 1), ("US equities and earnings", 1), ("Tech, AI and semiconductors", 1),
          ("Sectors: health, industrials, utilities, clean energy", 1), ("Europe and developed ex-US", 1), ("Japan and China", 1),
          ("Emerging markets ex-China", 1), ("Middle East, Gulf and geopolitics", 1), ("Commodities", 1), ("ETF flows and fund events", 1)])
assert len(REG) == 100

FAMILY_NAMES = {"A": "Trend and momentum", "B": "Relative strength", "C": "Volatility", "D": "Drawdown and tail risk",
                "E": "Risk-adjusted return", "F": "Liquidity and trading", "G": "Cost, structure and UAE investability",
                "H": "Macro regime (bucket-mapped)", "I": "Valuation and holdings", "J": "News and events (agents)"}
# Pre-registered weights (sum 100). Cost/structure and risk-adjusted history weigh most; news and macro are context.
WEIGHTS = {"A": 12, "B": 8, "C": 10, "D": 10, "E": 15, "F": 5, "G": 20, "H": 5, "I": 5, "J": 10}

# How defensive each bucket is: used to map macro risk-off readings to bucket scores (heuristic context only).
DEFENSIVE = {"govt_bonds": 1, "gold_precious": .7, "multi_asset_alt": .3, "utilities_realestate": .4, "us_factor_dividend": .4,
             "healthcare_biotech": .4, "consumer": 0, "credit_bonds": -.3, "global_equity": -.5, "us_large_broad": -.5,
             "us_small_mid_value": -.9, "tech_ai_semis": -.8, "financials": -.6, "energy_oil": -.3, "materials_mining_metals": -.6,
             "industrials_defense_infra": -.6, "clean_energy_thematic": -.8, "developed_ex_us": -.5, "europe": -.5, "japan": -.5,
             "asia_dev_other": -.6, "em_broad": -.8, "china": -.8, "india": -.7, "latam": -.8, "mena_gulf": -.5,
             "em_asia_other": -.8, "commodities_broad": -.3}
DURATION = {"govt_bonds": 1, "credit_bonds": .6, "gold_precious": .8, "tech_ai_semis": .6, "utilities_realestate": .7, "clean_energy_thematic": .6}
USD_HURT = {"em_broad": 1, "china": .8, "india": .6, "latam": 1, "em_asia_other": .8, "commodities_broad": .8, "gold_precious": .6,
            "materials_mining_metals": .7, "developed_ex_us": .5, "europe": .5, "japan": .4, "asia_dev_other": .6, "us_large_broad": -.3}
OIL_GAIN = {"energy_oil": 1, "mena_gulf": .8, "commodities_broad": .6, "latam": .2, "consumer": -.4, "india": -.6,
            "industrials_defense_infra": -.2, "japan": -.3, "europe": -.2}

def load(cache=ROOT / "cache"):
    d = {k: pd.read_pickle(cache / f"{k}.pkl") for k in ["adj", "close", "high", "low", "vol"]}
    d["facts"] = json.loads((cache / "facts.json").read_text())
    return d

def universe():
    u = pd.read_csv(ROOT / "config" / "universe.csv").fillna("")
    return u[u.active.astype(str) == "True"].reset_index(drop=True)

def fred(series, cache=ROOT / "cache"):
    p = cache / f"fred_{series}.csv"
    try:
        r = requests.get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}", timeout=30)
        r.raise_for_status(); p.write_text(r.text)
    except Exception:
        if not p.exists(): return None
    df = pd.read_csv(p); df.columns = ["date", "v"]
    df["v"] = pd.to_numeric(df.v, errors="coerce")
    return df.dropna().set_index(pd.to_datetime(df.dropna().date)).v

def _maxdd(s):
    return float((s / s.cummax() - 1).min()) if len(s) else np.nan

def compute_quant(d, asof=None):
    u = universe(); T = list(u.ticker); bucket = dict(zip(u.ticker, u.bucket))
    adj = d["adj"].loc[:asof] if asof else d["adj"]
    adj = adj[adj["SPY"].notna()]  # US trading days only (London-only days would drop returns around US holidays)
    vol = d["vol"].reindex(adj.index); high = d["high"].reindex(adj.index); low = d["low"].reindex(adj.index); close = d["close"].reindex(adj.index)
    r = adj.pct_change(fill_method=None)
    wk = adj.resample("W-FRI").last(); wr = wk.pct_change(fill_method=None)
    mo = adj.resample("ME").last(); mr = mo.pct_change(fill_method=None)
    vt, vtw = r["VT"], wr["VT"]
    V = pd.DataFrame(index=T, columns=list(REG), dtype=float)
    def ret(t, n): s = adj[t].dropna(); return s.iloc[-1] / s.iloc[-1 - n] - 1 if len(s) > n else np.nan
    for t in T:
        s = adj[t].dropna(); rt = r[t].dropna(); w = wr[t].dropna(); m = mr[t].dropna()
        if len(s) < 260: continue
        sma50, sma200 = s.rolling(50).mean().iloc[-1], s.rolling(200).mean().iloc[-1]
        m10 = mo[t].dropna().rolling(10).mean().iloc[-1]
        V.loc[t, ["A01", "A02", "A03", "A04", "A05"]] = [ret(t, 5), ret(t, 21), ret(t, 63), ret(t, 126), ret(t, 252)]
        V.loc[t, "A06"] = s.iloc[-22] / s.iloc[-253] - 1 if len(s) > 253 else np.nan
        V.loc[t, ["A07", "A08", "A09", "A10"]] = [s.iloc[-1] / sma50 - 1, s.iloc[-1] / sma200 - 1, float(mo[t].dropna().iloc[-1] > m10), sma50 / sma200 - 1]
        for k, n in zip(["B01", "B02", "B03", "B04"], [21, 63, 126, 252]):
            V.loc[t, k] = ret(t, n) - ret("VT", n)
        ratio = np.log(wk[t] / wk["VT"]).dropna().iloc[-13:]
        V.loc[t, "B08"] = np.polyfit(np.arange(len(ratio)), ratio.values, 1)[0] if len(ratio) == 13 else np.nan
        ex = (w - vtw).dropna()
        V.loc[t, "B09"] = (ex.iloc[-26:] > 0).mean()
        exd = (rt - vt).dropna().iloc[-TD:]
        V.loc[t, "B10"] = exd.mean() / exd.std() * np.sqrt(TD) if exd.std() > 0 else np.nan
        r1 = rt.iloc[-TD:]
        V.loc[t, ["C01", "C02", "C03"]] = [rt.iloc[-21:].std() * np.sqrt(TD), rt.iloc[-63:].std() * np.sqrt(TD), r1.std() * np.sqrt(TD)]
        rv = rt.rolling(21).std().iloc[-TD:]; V.loc[t, "C04"] = rv.std() / rv.mean()
        V.loc[t, "C05"] = np.sqrt((np.minimum(r1, 0) ** 2).mean()) * np.sqrt(TD)
        V.loc[t, "C06"] = V.loc[t, "C01"] / V.loc[t, "C03"]
        j = pd.concat([r1, vt], axis=1).dropna(); cov = np.cov(j.iloc[:, 0], j.iloc[:, 1])
        beta = cov[0, 1] / cov[1, 1]; V.loc[t, ["C07", "C08"]] = [beta, j.corr().iloc[0, 1]]
        V.loc[t, "C09"] = (j.iloc[:, 0] - beta * j.iloc[:, 1]).std() * np.sqrt(TD)
        tr = pd.concat([high[t] - low[t], (high[t] - close[t].shift()).abs(), (low[t] - close[t].shift()).abs()], axis=1).max(axis=1)
        V.loc[t, "C10"] = tr.iloc[-14:].mean() / close[t].iloc[-1]
        s1, s3 = s.iloc[-TD:], s.iloc[-3 * TD:]
        V.loc[t, "D01"] = s.iloc[-1] / s1.max() - 1
        V.loc[t, ["D02", "D03", "D04"]] = [_maxdd(s1), _maxdd(s3), _maxdd(s)]
        dd1 = (s1 / s1.cummax() - 1) * 100; V.loc[t, "D05"] = np.sqrt((dd1 ** 2).mean())
        w3 = w.iloc[-156:]; q = w3.quantile(.05)
        V.loc[t, ["D06", "D07", "D08"]] = [w3[w3 <= q].mean(), w3.skew(), w3.kurt()]
        V.loc[t, "D09"] = (s.index[-1] - s.idxmax()).days
        trough = s3.loc[(s3 / s3.cummax()).idxmin()]; peak = s3.loc[:(s3 / s3.cummax()).idxmin()].max()
        V.loc[t, "D10"] = (s.iloc[-1] - trough) / (peak - trough) if peak > trough else 1.0
        def sharpe(x, n): x = x.iloc[-n:]; return x.mean() / x.std() * np.sqrt(TD) if len(x) >= n * .9 else np.nan
        V.loc[t, ["E01", "E02", "E03"]] = [sharpe(rt, TD), sharpe(rt, 3 * TD), sharpe(rt, 5 * TD)]
        r3 = rt.iloc[-3 * TD:]; dd = np.sqrt((np.minimum(r3, 0) ** 2).mean())
        V.loc[t, "E04"] = r3.mean() / dd * np.sqrt(TD) if dd > 0 else np.nan
        cagr3 = (s3.iloc[-1] / s3.iloc[0]) ** (TD / len(s3)) - 1
        V.loc[t, "E05"] = cagr3 / abs(_maxdd(s3)) if _maxdd(s3) < 0 else np.nan
        u3 = np.sqrt((((s3 / s3.cummax() - 1)) ** 2).mean()); V.loc[t, "E06"] = cagr3 / u3 if u3 > 0 else np.nan
        V.loc[t, "E07"] = (m.iloc[-36:] > 0).mean()
        V.loc[t, "E08"] = (mo[t].dropna().pct_change(12, fill_method=None).iloc[-60:]).min() if len(m) >= 72 else np.nan
        V.loc[t, "E09"] = (s.iloc[-1] / s.iloc[-5 * TD]) ** .2 - 1 if len(s) > 5 * TD else np.nan
        V.loc[t, "E10"] = (s.iloc[-1] / s.iloc[-10 * TD]) ** .1 - 1 if len(s) > 10 * TD else np.nan
        dv = (vol[t] * close[t]).dropna()
        V.loc[t, "F01"] = dv.iloc[-63:].mean(); V.loc[t, "F02"] = dv.iloc[-21:].mean() / dv.iloc[-126:].mean()
        V.loc[t, "F03"] = (rt.abs() / dv.reindex(rt.index)).replace(np.inf, np.nan).iloc[-63:].mean() * 1e9
        V.loc[t, "F04"] = ((high[t] - low[t]) / close[t]).iloc[-20:].mean()
        v3 = vol[t].iloc[-63:]; V.loc[t, "F05"] = (v3 > 3 * vol[t].iloc[-252:].median()).mean()
        V.loc[t, "F06"] = (s.index[-1] - s.index[0]).days / 365.25
        V.loc[t, "F07"] = adj[t].loc[s.index[0]:].isna().mean()
        z = (r1 - r1.mean()) / r1.std(); V.loc[t, "F08"] = (z.abs() > 4).sum()
        obv = (np.sign(rt) * vol[t].reindex(rt.index)).cumsum().iloc[-63:]
        V.loc[t, "F09"] = np.polyfit(np.arange(len(obv)), obv.values, 1)[0] / vol[t].iloc[-63:].mean() if len(obv) == 63 else np.nan
        hl = (high[t] - low[t]).replace(0, np.nan)
        mfm = ((close[t] - low[t]) - (high[t] - close[t])) / hl
        V.loc[t, "F10"] = (mfm * vol[t]).iloc[-20:].sum() / vol[t].iloc[-20:].sum()
    # bucket-relative pillars
    for k, src in [("B05", "A03"), ("B06", "A05")]:
        V[k] = V.groupby(pd.Series(bucket))[src].rank(pct=True)
    V["B07"] = V["A04"] - V.groupby(pd.Series(bucket))["A04"].transform("median")
    # G: cost, structure, UAE investability
    f = d["facts"]; asof_ts = adj.index[-1]
    ucits_live = {c[:-2] for c in d["adj"].columns if c.endswith(".L") and d["adj"][c].dropna().shape[0] > 250}
    umap = dict(zip(u.ticker, u.ucits_candidate))
    r1y = r.iloc[-TD:]
    d10 = fred("DGS10"); ust10 = float(d10.iloc[-1]) / 100 if d10 is not None else None
    for t in T:
        fi = f.get(t, {})
        er = fi.get("netExpenseRatio"); aum = fi.get("totalAssets"); y = fi.get("yield")
        inc = fi.get("fundInceptionDate")
        age = (asof_ts - pd.to_datetime(inc, unit="s")).days / 365.25 if isinstance(inc, (int, float)) else V.loc[t, "F06"]
        V.loc[t, ["G01", "G02", "G03"]] = [er, aum, age]
        V.loc[t, "G04"] = float((aum or 0) < 100e6 or (age or 0) < 3)
        peers = [x for x in T if bucket[x] == bucket[t]]
        med = r1y[peers].median(axis=1)
        V.loc[t, "G05"] = (r1y[t] - med).std() * np.sqrt(TD)
        nav, px = fi.get("navPrice"), fi.get("regularMarketPrice")
        V.loc[t, "G06"] = abs(px / nav - 1) if nav and px else np.nan
        V.loc[t, "G07"] = y
        has_ucits = umap.get(t, "") in ucits_live
        V.loc[t, "G08"] = float(has_ucits)
        yy = (y or 0)
        V.loc[t, "G09"] = (0.15 if has_ucits else 0.30) * yy * 1e4  # bps of value lost to withholding
        V.loc[t, "G10"] = 0.0 if has_ucits else 1.0
        eh = fi.get("equity_holdings") or {}
        # Yahoo reports these ratios inverted (earnings, book, sales, cash-flow yields); convert to multiples.
        inv = lambda x: 1 / x if x and x > 0 else np.nan
        pe = fi.get("trailingPE") or inv(eh.get("Price/Earnings"))
        V.loc[t, ["I01", "I02", "I03", "I04"]] = [pe, inv(eh.get("Price/Book")), inv(eh.get("Price/Sales")), inv(eh.get("Price/Cashflow"))]
        V.loc[t, "I05"] = (fi.get("bond_holdings") or {}).get("Duration")
        V.loc[t, "I06"] = (1 / pe - ust10) if pe and pe > 0 and ust10 is not None else np.nan
        th = fi.get("top_holdings") or {}; sw = fi.get("sector_weightings") or {}
        V.loc[t, "I07"] = sum(th.values()) if th else np.nan
        V.loc[t, "I08"] = sum(v * v for v in sw.values()) if sw else np.nan
        V.loc[t, "I09"] = max(th.values()) if th else np.nan
    V["I10"] = V["I01"] / V.groupby(pd.Series(bucket))["I01"].transform("median")
    return V.astype(float), bucket

def macro_readings():
    """Each reading is a risk-off intensity in [-1, 1] (positive = risk-off) plus the raw value for the report."""
    out = {}
    def z(s, lookback=1260):
        s = s.dropna().iloc[-lookback:]; return float((s.iloc[-1] - s.mean()) / s.std()) if len(s) > 50 else 0.0
    def chg(s, days=63):
        s = s.dropna(); i = s.index[-1] - pd.Timedelta(days=int(days * 1.45)); prev = s.loc[:i]
        return float(s.iloc[-1] - prev.iloc[-1]) if len(prev) else 0.0
    def clip(x): return float(np.clip(x, -1, 1))
    t2 = fred("T10Y2Y"); t3 = fred("T10Y3M"); sahm = fred("SAHMREALTIME"); hy = fred("BAMLH0A0HYM2")
    ry = fred("DFII10"); usd = fred("DTWEXBGS"); oil = fred("DCOILWTICO"); nfci = fred("NFCI")
    vix = pd.read_pickle(ROOT / "cache" / "adj.pkl")[["^VIX", "^VIX3M"]].dropna()
    if t2 is not None: out["H01"] = (clip(-t2.iloc[-1] / 0.5) if t2.iloc[-1] < 0 else 0.0, f"{t2.iloc[-1]:.2f} pts ({t2.index[-1].date()})")
    if t3 is not None: out["H02"] = (clip(-t3.iloc[-1] / 0.5) if t3.iloc[-1] < 0 else 0.0, f"{t3.iloc[-1]:.2f} pts ({t3.index[-1].date()})")
    if sahm is not None: out["H03"] = (clip((sahm.iloc[-1] - 0.25) / 0.25), f"{sahm.iloc[-1]:.2f} ({sahm.index[-1].date()})")
    if hy is not None: c = chg(hy); out["H04"] = (clip(c / 0.75), f"{hy.iloc[-1]:.2f}%, 3m change {c:+.2f} ({hy.index[-1].date()})")
    if ry is not None: c = chg(ry); out["H05"] = (clip(c / 0.5), f"{ry.iloc[-1]:.2f}%, 3m change {c:+.2f}")
    if usd is not None: c = usd.iloc[-1] / usd.dropna().loc[:usd.index[-1] - pd.Timedelta(days=91)].iloc[-1] - 1; out["H06"] = (clip(c / 0.04), f"{usd.iloc[-1]:.1f}, 3m change {c:+.1%}")
    if oil is not None: c = oil.iloc[-1] / oil.dropna().loc[:oil.index[-1] - pd.Timedelta(days=91)].iloc[-1] - 1; out["H07"] = (clip(c / 0.2), f"US${oil.iloc[-1]:.1f}, 3m change {c:+.1%} ({oil.index[-1].date()})")
    if nfci is not None: out["H08"] = (clip(nfci.iloc[-1] / 0.5), f"{nfci.iloc[-1]:.2f} ({nfci.index[-1].date()})")
    if len(vix):
        out["H09"] = (clip(z(vix["^VIX"]) / 2), f"VIX {vix['^VIX'].iloc[-1]:.1f}")
        ts = vix["^VIX"].iloc[-1] / vix["^VIX3M"].iloc[-1]; out["H10"] = (clip((ts - 0.9) / 0.15), f"VIX/VIX3M {ts:.2f}")
    return out

def macro_bucket_scores(readings, buckets):
    """Turn risk-off readings into bucket scores in [-1, 1] per H pillar."""
    S = {}
    for k, (x, _) in readings.items():
        if k == "H05": S[k] = {b: -x * DURATION.get(b, .2) for b in buckets}
        elif k == "H06": S[k] = {b: -x * USD_HURT.get(b, 0) for b in buckets}
        elif k == "H07": S[k] = {b: -x * OIL_GAIN.get(b, 0) * -1 for b in buckets}  # oil up (x>0) helps OIL_GAIN>0 buckets
        else: S[k] = {b: x * DEFENSIVE.get(b, 0) for b in buckets}
    return S

def news_scores(week_dir):
    out = {}; meta = {}
    for p in sorted(Path(week_dir).glob("J*.json")):
        j = json.loads(p.read_text()); pid = j["pillar_id"]
        out[pid] = {b: v["score"] * {"high": 1, "medium": .75, "low": .4}.get(v.get("confidence", "low"), .4)
                    for b, v in j["bucket_scores"].items()}
        meta[pid] = j
    return out, meta

def score(V, bucket, macro, news):
    P = pd.DataFrame(index=V.index, columns=list(REG), dtype=float)
    for k, (fam, name, d) in REG.items():
        if fam in "H":
            P[k] = [50 + 50 * macro.get(k, {}).get(bucket[t], 0) for t in V.index]
        elif fam == "J":
            P[k] = [50 + 25 * news.get(k, {}).get(bucket[t], 0) for t in V.index]
        elif d == 0:
            P[k] = 50.0
        else:
            x = V[k] * d
            P[k] = (x.rank(pct=True) * 100).fillna(50)
    F = pd.DataFrame({fam: P[[k for k in REG if k[0] == fam]].mean(axis=1) for fam in FAMILY_NAMES})
    F["composite"] = sum(F[f] * w for f, w in WEIGHTS.items()) / sum(WEIGHTS.values())
    return P, F
