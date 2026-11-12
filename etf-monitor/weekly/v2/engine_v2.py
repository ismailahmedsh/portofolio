"""Engine v2: scores every UCITS line on the approved pillars v2 (config/pillars_v2.json).
Three separate views, never one composite: line view (within a same-index cluster), exposure view X (equity clusters, world = 50),
fit view (against the owner's strategic mix). Gates decide what may receive money."""
import json, re, sys
from pathlib import Path
import numpy as np, pandas as pd, yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src")); sys.path.insert(0, str(Path(__file__).resolve().parent))
import pillars as P1  # reuse FRED fetch with cache
import exposure as XP

ROOT = Path(__file__).resolve().parents[1]; CACHE = ROOT / "cache"
SPEC = json.loads((ROOT / "config" / "pillars_v2.json").read_text())
CFG = yaml.safe_load((ROOT / "config" / "portfolio_v2.yaml").read_text())
TD = 252
EVENTS = {}
SWAP = {"SPXS.L", "SPXP.L", "XSPU.L", "XSPX.L", "SPXD.L"}  # synthetic S&P 500 lines (names also checked for 'Swap')
B_PRIORS = {"FAC01": 1.5, "FAC02": 1.5, "FAC03": 1.0, "FAC04": 1.0, "EXR08": -0.01}  # EXR02 priors, % a year per unit (labelled priors)
ERP = 4.0

def tanh_score(x, ref, k, d=1, one_sided=False):
    if x is None or ref is None or pd.isna(x) or pd.isna(ref): return np.nan
    z = d * (x - ref) / k
    return 50 - 50 * np.tanh(max(0.0, -z)) if one_sided else 50 + 50 * np.tanh(z)

def fam_score(scores, weights):
    """Missing pillars drop out; family = 50 + c x (mean - 50), c = share of weight with data. Never fills with 50."""
    have = {k: w for k, w in weights.items() if k in scores and not pd.isna(scores[k])}
    if not have or sum(weights.values()) == 0: return np.nan, 0.0
    m = sum(scores[k] * w for k, w in have.items()) / sum(have.values()); c = sum(have.values()) / sum(weights.values())
    return 50 + c * (m - 50), c

def load():
    d = {"close": clean_units(pd.read_pickle(CACHE / "v2_close_usd.pkl")), "vol": pd.read_pickle(CACHE / "v2_vol.pkl"),
         "usdvol": pd.read_pickle(CACHE / "v2_usdvol.pkl"), "raw": clean_units(pd.read_pickle(CACHE / "v2_rawclose_usd.pkl")), "u": pd.read_pickle(CACHE / "v2_universe.pkl"),
         "french": pd.read_pickle(CACHE / "v2_french.pkl")}
    fp = CACHE / "v2_facts.json"; d["facts"] = json.loads(fp.read_text()) if fp.exists() else {}
    return d

ISSUER_WORDS = r"\b(ishares|vanguard|invesco|xtrackers|spdr|state street|hsbc|amundi|l&g|legal & general|wisdomtree|franklin|jpmorgan|j\.p\. morgan|ubs|lyxor|global x|vaneck|hanetf|first trust|core|edge|swap|physical|ucits|etf|etc|fund|usd|gbp|eur|acc|accumulating|accumulation|dist|distributing|distribution|unhedged|hedged|1c|1d|2c|class|a|b|c|plc|the|index|ii|sicav|ftse epra nareit|daily|line|eqqq)\b"
def index_key(name):
    k = re.sub(r"\(.*?\)", " ", str(name).lower()); k = re.sub(ISSUER_WORDS, " ", k)
    k = k.replace("nasdaq-100", "nasdaq 100").replace("s&p500", "s&p 500").replace("all country world", "acwi")
    return re.sub(r"[^a-z0-9&]+", " ", k).strip()

def clusters(close, u, lines):
    """Same-index groups: identical index key parsed from the fund name, confirmed by weekly-return correlation >= 0.98
    (LSE closes are noisy, so correlation alone cannot separate S&P 500 from MSCI USA). Reference = oldest line."""
    keys = {t: index_key(u.loc[t, "name"]) for t in lines}
    wk = close[lines].resample("W-FRI").last().pct_change(fill_method=None).iloc[-104:]
    first = {t: close[t].first_valid_index() for t in lines}
    assign = {}
    for t in sorted(lines, key=lambda t: first[t]):
        if t in assign: continue
        grp = [x for x in lines if x not in assign and keys[x] == keys[t] and keys[t]]
        grp = [x for x in grp if x == t or (wk[[t, x]].dropna().shape[0] >= 60 and wk[t].corr(wk[x]) >= 0.98)]
        for x in grp: assign[x] = t
    for t in lines: assign.setdefault(t, t)
    return assign

def clean_units(c):
    """Undo GBX/GBP unit switches in Yahoo series: a day-on-day ratio near 100 or 1/100 rescales the earlier segment."""
    c = c.copy()
    for t in c.columns:
        s = c[t].dropna(); r = s / s.shift(1)
        for dt, x in r[(r > 50) | (r < 0.02)].items():
            f = 100.0 if x > 1 else 0.01  # unit switch is exactly x100 or /100; keeps the genuine move on the day
            c.loc[:dt - pd.Timedelta(days=1), t] = c.loc[:dt - pd.Timedelta(days=1), t] * f
    return c

def load_events(week_dir):
    """Event agents write runs/<week>/events/EVT0x.json: {events:[{target, severity 0-3, issue, url, date}]}. Returns {ticker: [(pid, severity, issue, url)]}."""
    out = {}
    if not week_dir or not (Path(week_dir) / 'events').exists(): return out
    for f in sorted((Path(week_dir) / 'events').glob('EVT*.json')):
        try: j = json.loads(f.read_text())
        except Exception: continue
        for e in j.get('events', []):
            t = str(e.get('target', '')).strip().upper()
            if t and not t.endswith('.L') and len(t) <= 5: t += '.L'
            out.setdefault(t, []).append((j.get('pillar_id', f.stem), int(e.get('severity', 0) or 0), e.get('issue', ''), e.get('url', '')))
    return out

def run(asof=None, week_dir=None):
    global EVENTS; EVENTS = load_events(week_dir)
    d = load(); u = d["u"][d["u"].has_data].set_index("ticker"); close = d["close"]
    if asof: close = close.loc[:asof]
    lines = list(u.index); asof_ts = close.index[-1]
    cl = clusters(close, u, lines)
    sleeves = {k: cl.get(v["line"] or {"sp500": "CSPX.L", "ndx100": "CNDX.L"}[k], None) for k, v in CFG["strategic_mix"].items()}
    world_lines = [CFG["strategic_mix"]["world"]["line"]] + list(CFG["strategic_mix"]["world"].get("fallbacks") or [])
    world_ref = sleeves["world"]
    dep = CFG["deposit"]; C_usd = dep["aed_per_month"] / dep["aed_per_usd"] - dep["fx_fixed_usd"]; comm = dep["commission_min_usd"]
    facts = d["facts"]; V = {}  # pillar values per line
    # US dividend yield (for TAX01): SPY trailing 12 months
    try:
        import yfinance as yf
        div = yf.Ticker("SPY").dividends; div.index = div.index.tz_localize(None)
        us_yield = float(div.loc[asof_ts - pd.Timedelta(days=365):asof_ts].sum() / close["SPY"].dropna().iloc[-1])
    except Exception:
        us_yield = 0.012
    wkr = close.resample("W-FRI").last().pct_change(fill_method=None)
    # US look-through weight by regression of weekly returns on SPY, EFA, EEM (2 years), clipped to [0,1]
    def us_weight(t):
        X = wkr[["SPY", "EFA", "EEM"]].iloc[-104:]; y = wkr[t].iloc[-104:]
        j = pd.concat([y, X], axis=1).dropna()
        if len(j) < 60: return np.nan
        b = np.linalg.lstsq(j.iloc[:, 1:].values, j.iloc[:, 0].values, rcond=None)[0]
        b = np.clip(b, 0, None); return float(b[0] / b.sum()) if b.sum() > 0 else np.nan
    dr = close.pct_change(fill_method=None)
    # ---------- line view ----------
    for t in lines:
        s = close[t].dropna(); row = u.loc[t]; f = facts.get(t, {}); v = {}
        name = str(row["name"]); isin = str(row.get("isin") or ""); ref = cl[t]
        v["cluster"] = ref; v["name"] = name; v["scope"] = row["scope"]; v["currency"] = row["currency"]
        v["ELG01"] = isin[:2] in ("IE", "LU") if isin and isin != "nan" else None
        v["ELG02"] = row["currency"] == "USD"
        v["ELG03"] = not re.search(r"\b(2x|3x|leverag|short|inverse|daily)\b", name, re.I)
        v["ELG04"] = row["scope"] not in ("money-market",)
        v["ELG05_days"] = (asof_ts - s.index[-1]).days if len(s) else 999; v["ELG05"] = v["ELG05_days"] <= 7
        r63 = s.pct_change().iloc[-63:]; v["ELG06"] = not (r63.abs() > 0.20).any()
        v["integrity_full"] = not (s.pct_change().abs() > 0.5).any()  # corrupt history: excluded from exposure and fit views
        v["ELG08"] = t in set(CFG.get("orderable") or []) or t == "VWRA.L"
        ter = row.get("ter"); ter = float(ter) if ter is not None and not pd.isna(ter) else (f.get("netExpenseRatio") if f.get("netExpenseRatio") else np.nan)
        v["CST01"] = ter * 100 if not pd.isna(ter) else np.nan  # bps
        yt = f.get("netExpenseRatio"); v["ELG10"] = abs(float(yt) - float(ter)) * 100 if yt and not pd.isna(ter) else np.nan
        if ref != t:
            j = pd.concat([dr[t], dr[ref]], axis=1).dropna().iloc[-3 * TD:]
            v["CST04"] = float((j.iloc[:, 0] - j.iloc[:, 1]).std() * np.sqrt(TD) * 1e4) if len(j) > 200 else np.nan
            a = close[[t, ref]].dropna().iloc[-3 * TD:]
            v["CST02_raw_gap_bps"] = float(((a[t].iloc[-1] / a[t].iloc[0]) ** (TD / len(a)) - (a[ref].iloc[-1] / a[ref].iloc[0]) ** (TD / len(a))) * 1e4) if len(a) > 500 else np.nan
        else:
            v["CST04"] = np.nan; v["CST02_raw_gap_bps"] = np.nan
        tv = d["usdvol"][t].dropna().iloc[-63:]; v["CST06"] = float(np.log10(max(tv.median(), 1))) if len(tv) else np.nan
        rs = d["raw"][t].dropna() if t in d["raw"] else s; px = rs.iloc[-1] if len(rs) else np.nan  # traded price, for whole shares
        v["price_usd"] = float(px) if not pd.isna(px) else np.nan
        v["CST08"] = float(((C_usd - comm) % px) / C_usd) if px and not pd.isna(px) and px < C_usd else (1.0 if not pd.isna(px) else np.nan)
        usw = us_weight(t) if t in wkr else np.nan; v["us_weight"] = usw
        swap = t in SWAP or "swap" in name.lower(); v["swap"] = swap
        rate = 0.0 if swap else 0.15
        v["TAX01"] = float(usw * us_yield * rate * 1e4) if not pd.isna(usw) else np.nan  # bps
        v["TAX03"] = float(usw * us_yield * 0.15 * 1e4) if swap and not pd.isna(usw) else 0.0  # advantage resting on one tax rule (871(m))
        v["TAX05"] = 0.0 if str(row.get("accumulating")).lower() in ("yes", "true", "1") else 5.0
        aum = f.get("totalAssets"); v["DUR01"] = float(np.log10(aum)) if aum else np.nan
        fd = row.get("first_date"); v["DUR04"] = (asof_ts - pd.Timestamp(fd)).days / 365.25 if isinstance(fd, str) else (asof_ts - s.index[0]).days / 365.25
        v["CST10"] = (v["CST01"] if not pd.isna(v["CST01"]) else 50) + (v["TAX01"] if not pd.isna(v["TAX01"]) else 0) + 0.5 * v["TAX03"] + v["TAX05"] + (0 if v["ELG02"] else 5) + 1e4 * comm / C_usd / 15
        v["CON04"] = bool(re.search(r"china|russia", name, re.I) and row["scope"] == "single_country")
        v["CON05"] = str(row["scope"]).startswith("theme")
        V[t] = v
    L = pd.DataFrame(V).T
    issuer = L["name"].str.split().str[0]
    for t in lines:
        peers = L.index[(L.cluster == L.loc[t, "cluster"]) & (L.index != t)]
        cheap = [p for p in peers if abs((L.loc[p, "CST01"] or 0) - (L.loc[t, "CST01"] or 0)) <= 10 and abs(L.loc[p, "CST10"] - L.loc[t, "CST10"]) <= 15]
        L.loc[t, "DUR06"] = sum(2 if issuer[p] != issuer[t] else 1 for p in cheap)
    # line scores within cluster
    LS = {}
    for t in lines:
        peers = L[L.cluster == L.loc[t, "cluster"]]; single = len(peers) == 1
        med = lambda c: peers[c].astype(float).median()
        sc = {"CST01": tanh_score(L.loc[t, "CST01"], 10 if single else med("CST01"), 10, -1),
              "CST04": tanh_score(L.loc[t, "CST04"], med("CST04"), 50, -1) if not single else np.nan,
              "CST06": tanh_score(min(L.loc[t, "CST06"], 7), 6 if single else min(med("CST06"), 7), 1, 1),
              "CST08": tanh_score(L.loc[t, "CST08"], 0.0, 0.10, -1),
              "TAX01": tanh_score(L.loc[t, "TAX01"], med("TAX01"), 15, -1) if not single else tanh_score(L.loc[t, "TAX01"], 0, 15, -1),
              "TAX03": tanh_score(L.loc[t, "TAX03"], 0, 25, -1, one_sided=True),
              "TAX05": tanh_score(L.loc[t, "TAX05"], 0, 15, -1),
              "DUR01": tanh_score(min(L.loc[t, "DUR01"], 10) if not pd.isna(L.loc[t, "DUR01"]) else np.nan, 9 if single else min(med("DUR01"), 10), 1, 1),
              "DUR04": tanh_score(min(L.loc[t, "DUR04"], 15), 3 if single else min(med("DUR04"), 15), 3, 1),
              "DUR06": tanh_score(min(L.loc[t, "DUR06"], 2), 1, 1, 1)}
        cw = {"CST01": .30, "CST02": .35, "CST03": .10, "CST04": .05, "CST06": .15, "CST08": .05}
        if L.loc[t, "cluster"] == t: cw.pop("CST04")  # reference line: price noise against itself is not applicable
        cst, c1 = fam_score(sc, cw)
        tax, c2 = fam_score(sc, {"TAX01": .4, "TAX03": .4, "TAX05": .2})
        dw = {"DUR01": .4, "DUR04": .3, "DUR06": .3}
        if pd.isna(sc["DUR01"]): dw.pop("DUR01")  # Yahoo gives no fund size for this line: listed as missing, not held against coverage
        dur, c3 = fam_score(sc, dw)
        ev = [e for e in EVENTS.get(t, []) if e[0] in ("EVT01", "EVT02", "EVT05")]
        evt = 50.0 - 25.0 * max([e[1] for e in ev], default=0)  # line events are penalty-only: severity 1 -> 25, 2 -> 0
        line = (53 * cst + 21 * tax + 19 * dur + 7 * evt) / 100 if not any(pd.isna([cst, tax, dur])) else np.nan
        LS[t] = {**sc, "CST": cst, "TAX": tax, "DUR": dur, "EVT": evt, "line_score": line, "coverage": round((c1 * 53 + c2 * 21 + c3 * 19 + 7) / 100, 2)}
    LS = pd.DataFrame(LS).T
    L["EVT_block"] = [any((e[0] in ("EVT01", "EVT02", "EVT05") and e[1] >= 2) or (e[0] == "EVT07" and e[1] >= 3) for e in EVENTS.get(t, [])) for t in L.index]
    L["events"] = [json.dumps(EVENTS.get(t, [])) for t in L.index]
    L["ELG09"] = LS["coverage"] >= 0.70
    L.loc["VWRA.L", "ELG09"] = True  # core exempt
    gates = ["ELG01", "ELG02", "ELG03", "ELG04", "ELG05", "ELG06", "ELG08", "ELG09"]
    L["buyable"] = L[gates].fillna(False).astype(bool).all(axis=1) & ~L["CON04"].astype(bool) & ~L["EVT_block"].astype(bool)
    L["fail_reasons"] = [", ".join([g for g in gates if not bool(L.loc[t, g])] + (["CON04"] if L.loc[t, "CON04"] else []) + (["event"] if L.loc[t, "EVT_block"] else [])) for t in L.index]
    # ---------- exposure view X (spec-faithful, shared with REC04 via exposure.py) ----------
    XP.self_check()
    eq_scopes = lambda sc: not any(k in str(sc) for k in ["government", "corporate", "high-yield", "inflation", "em-debt", "aggregate", "money", "gold", "silver", "platinum", "palladium", "precious", "commodities", "multi_asset"])
    mret = close.resample("ME").last().pct_change(fill_method=None)
    dt = asof_ts + pd.offsets.MonthEnd(0) if asof_ts.is_month_end else asof_ts - pd.offsets.MonthEnd(1)  # last completed month
    mret = mret.loc[:dt]
    fac = XP.factors(d["french"]); W = XP.world_reference(mret, fac)
    PROXY = {"sp500": "SPY", "ndx100": "QQQ"}; proxy_by_ref = {sleeves[k]: v for k, v in PROXY.items() if sleeves.get(k)}
    for t in lines:
        if "EIMI" in t: proxy_by_ref[cl[t]] = "EEM"
    splices = {}
    def series(ref):
        if ref == world_ref: return W
        if ref in proxy_by_ref and proxy_by_ref[ref] in mret:
            sp, info = XP.spliced(mret[ref], mret[proxy_by_ref[ref]]); splices[ref] = info; return sp
        return mret[ref].dropna()
    refs = sorted({cl[t] for t in lines if eq_scopes(u.loc[t, "scope"]) and L.loc[cl[t], "integrity_full"]} | {world_ref})
    e_w = XP.raw_measures(W, W, fac, dt); E = {}; XSd = {}
    for r in refs:
        e = e_w if r == world_ref else XP.raw_measures(series(r), W, fac, dt)
        if e.get("months", 0) < 36 or "FAC05" not in e: continue
        E[r] = e; sc = XP.score(e, e_w); XSd[r] = {**{k: (round(v, 4) if isinstance(v, float) else v) for k, v in e.items()}, **{k + "_s": sc[k] for k in ["FAC01", "FAC02", "FAC03", "FAC04", "RSK01", "RSK03", "RSK05", "EXR08", "EXR06"]}, "EXR": sc["EXR"], "FAC": sc["FAC"], "RSK": sc["RSK"], "X": sc["X"]}
    XS = pd.DataFrame(XSd).T
    assert abs(XS.loc[world_ref, "X"] - 50) < 1e-9, "built-in check failed: world reference must score exactly 50"
    Eref = e_w
    # ---------- fit view against the owner's strategic mix ----------
    mix = {k: v["target"] for k, v in CFG["strategic_mix"].items()}
    cost = lambda r: float(L.loc[L.cluster == r, "CST10"].min()) if (L.cluster == r).any() else float(L.loc[r, "CST10"])
    cref = float(L.loc["VWRA.L", "CST10"])
    Ex = {r: XP.exp_excess(E[r], e_w, cost(r), cref) for r in E}
    beta_P = sum(w * E[sleeves[k]]["FAC05"] for k, w in mix.items()); E_P = sum(w * Ex[sleeves[k]] for k, w in mix.items())
    port = sum(series(sleeves[k]).reindex(mret.index).fillna(0) * w for k, w in mix.items()).iloc[-120:]
    FT = {}
    for r in set(cl.values()):
        if not L.loc[r, "integrity_full"]: continue
        y = series(r).reindex(port.index); j = pd.concat([y, port], axis=1).dropna()
        if len(j) < 36: continue
        f = {}
        dn = j[j.iloc[:, 1] < 0]; f["FIT05"] = float(dn.corr().iloc[0, 1]) if len(dn) > 10 else np.nan
        vi, vp = j.iloc[:, 0].var() * 12, j.iloc[:, 1].var() * 12; vm = (0.1 * j.iloc[:, 0] + 0.9 * j.iloc[:, 1]).var() * 12
        f["FIT06"] = 0.5 * (0.1 * vi + 0.9 * vp - vm) * 1e4
        f["FIT10"] = float((0.1 * (j.iloc[:, 0] - j.iloc[:, 1])).std() * np.sqrt(12) * 100)
        f["FIT03"] = float(j.corr().iloc[0, 1])
        f["FIT04"] = XP.fit04(Ex[r], E[r]["FAC05"], E_P, beta_P) if r in E else np.nan
        sc = {"FIT04": tanh_score(f["FIT04"], 0, 1, 1), "FIT05": tanh_score(f["FIT05"], 0.9, 0.2, -1), "FIT06": tanh_score(f["FIT06"], 0, 10, 1),
              "FIT10": 50.0 if f["FIT10"] <= 2 else tanh_score(f["FIT10"], 2, 0.5, -1, one_sided=True)}
        w = {"FIT04": .4, "FIT05": .2, "FIT06": .2, "FIT10": .2} if r in E else {"FIT05": 1 / 3, "FIT06": 1 / 3, "FIT10": 1 / 3}
        fit, _ = fam_score(sc, w)
        FT[r] = {**f, **{k + "_s": v for k, v in sc.items()}, "fit": fit}
    FT = pd.DataFrame(FT).T
    return {"world_lines": world_lines, "E": E, "Eref": Eref, "world_ref": world_ref, "W": W, "splices": splices, "dt": dt, "asof": asof_ts, "L": L, "LS": LS, "XS": XS, "FT": FT, "cl": cl, "sleeves": sleeves, "C_usd": C_usd, "us_yield": us_yield, "close": close, "mret": mret, "mix": mix}

if __name__ == "__main__":
    R = run()
    print("asof", R["asof"].date(), "lines", len(R["L"]), "clusters", len(set(R["cl"].values())), "equity clusters with X", len(R["XS"]))
    print("sleeves:", R["sleeves"])
    for k, ref in R["sleeves"].items():
        m = R["L"].index[R["L"].cluster == ref]
        print(k, R["L"].loc[m, ["CST01", "CST10", "TAX01", "swap", "buyable", "fail_reasons"]].join(R["LS"].loc[m, ["line_score", "coverage"]]).round(2).to_string())
    print(R["XS"][["X", "EXR", "FAC", "RSK", "FAC05", "months"]].sort_values("X").round(1).to_string())
