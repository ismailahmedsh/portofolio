"""Engine v3 on config/pillars_v3.json. Builds on engine v2 (UCITS line, exposure and fit views) and adds:
- US-listed lines with 30% investor withholding on trailing cash distributions (TAX01 v3) and their all-in cost (CST10);
- ELG07 same-index groups across wrappers (S&P 500, Nasdaq-100, world, premium-income groups) with the 36-month return check;
- the cross-wrapper line verdict: a US line wins only with a 10 bps CST10 edge, FIT12 headroom and ELG08 confirmation;
- FIT12 US-situs gauge (US$45k amber, US$54k buy limit, US$60k cap) and FIT07 US look-through of the mix;
- OPT01-OPT04 options-income table (information only: target 0 until the owner sets one);
- MAC01-MAC10 macro flags (context only, never move money);
- the news view N per fund group from runs/<week>/news/*.json (display only until REC08 passes).
Crypto is excluded by the owner (2026-11-13). Usage: import engine_v3 as E3; R = E3.run(week_dir=...)"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd, yaml
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[0]; CACHE = ROOT / "cache"
sys.path.insert(0, str(ROOT / "v2")); sys.path.insert(0, str(ROOT / "src"))
import engine_v2 as E2
import pillars as P1

SPEC = json.loads((ROOT / "config" / "pillars_v3.json").read_text())
CFG = yaml.safe_load((ROOT / "config" / "portfolio_v2.yaml").read_text())
US = CFG.get("us_listed") or {}
CAP, BUY_LIMIT, AMBER = float(US.get("cap_usd", 60000)), float(US.get("buy_limit_usd", 54000)), float(US.get("amber_usd", 45000))
US_COMM = float(US.get("commission_usd", 1.0)); US_WHT = 0.30
EDGE_BPS = 10.0
# ELG07 groups by declared benchmark (pillars v3 ELG07(a)); UCITS members come from the v2 clusters of the sleeve lines
US_GROUPS = {"world": ["VT", "ACWI"], "sp500": ["VOO", "IVV", "SPYM", "SPY"], "ndx100": ["QQQM", "QQQ"]}
PREMIUM_GROUPS = {  # underlying proxy for OPT01-OPT03, members
    "S&P 500 premium income": ("SPY", ["JEPI", "JEPI.L", "JEIP.L", "SPYI", "SPYI.L", "XYLD", "XYLU.L", "XYLP.L", "GPIX", "DIVO", "ISPY", "XDTE"]),
    "Nasdaq-100 premium income": ("QQQ", ["JEPQ", "JEPQ.L", "JEQP.L", "JEQA.L", "QQQI", "QQQI.L", "QQQP.L", "GPIQ", "FTQI", "QDTE", "QYLD", "QYLD.L", "QYLU.L", "QYLP.L", "QYLG"]),
    "Global premium income": ("ACWI", ["JEPG.L", "JEGP.L", "JEGA.L"]),
}
SLEEVE_BUCKETS = {"world": {"global_equity": 1.0}, "sp500": {"us_large_broad": 1.0}, "ndx100": {"tech_ai_semis": 0.6, "us_large_broad": 0.4}}

def load_us():
    u = pd.read_pickle(CACHE / "v3_universe.pkl").set_index("ticker")
    return {"u": u, "close": E2.clean_units(pd.read_pickle(CACHE / "v3_close_usd.pkl")), "raw": E2.clean_units(pd.read_pickle(CACHE / "v3_rawclose_usd.pkl")),
            "usdvol": pd.read_pickle(CACHE / "v3_usdvol.pkl"), "divs": pd.read_pickle(CACHE / "v3_divs_usd.pkl"),
            "facts": json.loads((CACHE / "v3_facts.json").read_text())}

def trailing_yield(t, D, asof):
    dv = D["divs"].get(t); px = D["raw"][t].dropna() if t in D["raw"] else None
    if dv is None or px is None or not len(px): return 0.0
    dv = dv[~dv.index.duplicated()]; dv.index = pd.to_datetime(dv.index).tz_localize(None) if getattr(dv.index, "tz", None) else dv.index
    return float(dv.loc[asof - pd.Timedelta(days=365):asof].sum() / px.iloc[-1])

def us_lines(D, C_usd, asof):
    """Line values for US-listed and LSE options-income lines. US: TAX01 = 30% of trailing cash distributions (always active)."""
    rows = {}
    for t, r in D["u"][D["u"].has_data].iterrows():
        s = D["close"][t].dropna()
        if not len(s): continue
        ter = float(r["ter"]) if pd.notna(r["ter"]) and str(r["ter"]).strip() not in ("", "nan") else np.nan
        y = trailing_yield(t, D, asof); us = r["venue"] == "US"
        acc = "acc" in str(r["name"]).lower() or t in ("JEQA.L", "JEGA.L", "QYLU.L", "XYLU.L")
        tax = US_WHT * y * 1e4 if us else (0.15 * 0.012 * 1e4 if "premium" in str(r["name"]).lower() or "income" in str(r["name"]).lower() else 0.0)
        tax05 = 0.0 if (acc or (us and y == 0)) else 5.0
        comm = US_COMM if us else CFG["deposit"]["commission_min_usd"]
        cst01 = ter * 100 if not pd.isna(ter) else np.nan
        tv = D["usdvol"][t].dropna().iloc[-63:] if t in D["usdvol"] else pd.Series(dtype=float)
        rows[t] = {"name": r["name"], "type": r["type"], "venue": r["venue"], "index": r["index"], "info_only": bool(r["info_only"]),
                   "CST01": cst01, "yield_12m_pct": round(y * 100, 2), "TAX01": round(tax, 1), "TAX05": tax05,
                   "after_tax_yield_pct": round(y * 100 * (1 - US_WHT) if us else y * 100, 2),
                   "CST10": (cst01 if not pd.isna(cst01) else np.nan) + tax + tax05 + 1e4 * comm / C_usd / 15,
                   "price_usd": float(D["raw"][t].dropna().iloc[-1]), "ELG05_days": int((asof - s.index[-1]).days),
                   "median_traded_usd": float(tv.median()) if len(tv) else np.nan, "years": round((s.index[-1] - s.index[0]).days / 365.25, 1),
                   "us_situs": bool(us)}
    return pd.DataFrame(rows).T

def monthly_tr(s):
    return s.resample("ME").last().pct_change(fill_method=None)

def return_check(a, b):
    """ELG07(b): monthly total-return correlation over 36 months (12 minimum) and annualised gap. Confirms, never decides."""
    j = pd.concat([monthly_tr(a), monthly_tr(b)], axis=1).dropna().iloc[-36:]
    if len(j) < 12: return np.nan, np.nan, len(j)
    g = ((1 + j.iloc[:, 0]).prod() ** (12 / len(j)) - (1 + j.iloc[:, 1]).prod() ** (12 / len(j))) * 1e4
    return float(j.corr().iloc[0, 1]), float(g), len(j)

def cross_wrapper(R, UL, D):
    L = R["L"]; cfg_pos = CFG.get("positions") or {}
    w8 = bool(US.get("w8ben_signed_on")) and bool(US.get("ibkr_entity"))
    orderable = set(CFG.get("orderable") or [])
    out = {}
    for k, us_list in US_GROUPS.items():
        uc = list(R["world_lines"]) if k == "world" else list(L.index[L.cluster == R["sleeves"][k]])
        uc = [t for t in uc if t in L.index]
        ucits = L.loc[uc, ["CST10", "buyable", "swap", "price_usd"]].copy(); ucits["venue"] = "LSE"
        best_u = ucits[ucits.buyable.astype(bool)].CST10.astype(float).idxmin() if ucits.buyable.astype(bool).any() else ucits.CST10.astype(float).idxmin()
        ref_close = R["close"][best_u].dropna()
        us_rows = []
        for t in us_list:
            if t not in UL.index: continue
            corr, gap, n = return_check(D["close"][t].dropna(), ref_close)
            us_rows.append({"ticker": t, "CST10": float(UL.loc[t, "CST10"]), "TER_bps": UL.loc[t, "CST01"], "yield_pct": UL.loc[t, "yield_12m_pct"],
                            "tax_bps": UL.loc[t, "TAX01"], "corr_36m": None if pd.isna(corr) else round(corr, 3), "gap_bps_vs_ucits": None if pd.isna(gap) else round(gap), "months": n})
        best_us = min(us_rows, key=lambda x: x["CST10"]) if us_rows else None
        edge = float(L.loc[best_u, "CST10"]) - best_us["CST10"] if best_us else np.nan
        us_ok = best_us is not None and edge >= EDGE_BPS and w8 and best_us["ticker"] in orderable
        out[k] = {"best_ucits": best_u, "best_ucits_cst10": round(float(L.loc[best_u, "CST10"]), 1),
                  "ucits_lines": {t: round(float(L.loc[t, "CST10"]), 1) for t in uc},
                  "best_us": best_us["ticker"] if best_us else None, "best_us_cst10": round(best_us["CST10"], 1) if best_us else None,
                  "us_edge_bps": round(edge, 1) if not pd.isna(edge) else None, "us_lines": us_rows,
                  "winner": best_us["ticker"] if us_ok else best_u,
                  "why": (f"{best_us['ticker']} is {edge:.0f} bps a year cheaper after the 30% dividend tax, above the {EDGE_BPS:.0f} bps hurdle" if us_ok else
                          (f"London line {best_u} is cheaper after tax ({float(L.loc[best_u,'CST10']):.0f} vs {best_us['CST10']:.0f} bps a year for {best_us['ticker']})" if edge < 0 else
                           f"{best_us['ticker']} is only {edge:.0f} bps cheaper after tax, below the {EDGE_BPS:.0f} bps hurdle" + ("" if w8 else "; US buying also needs W-8BEN and IBKR entity recorded")))}
    return out

def fit12(R, UL):
    pos = CFG.get("positions") or {}
    v = sum(float(p.get("units", 0)) * float(UL.loc[t, "price_usd"]) for t, p in pos.items() if p and t in UL.index and UL.loc[t, "us_situs"])
    band = "green" if v < AMBER else "amber" if v < BUY_LIMIT else "red" if v < CAP else "over cap"
    return {"V_us": round(v, 2), "band": band, "amber": AMBER, "buy_limit": BUY_LIMIT, "cap": CAP,
            "ready_to_buy_us": bool(US.get("w8ben_signed_on")) and bool(US.get("ibkr_entity"))}

def fit07(R):
    L = R["L"]; mix = R["mix"]
    w = {"world": L.loc["VWRA.L", "us_weight"], "sp500": 1.0, "ndx100": 0.97}
    us = sum(mix[k] * float(w[k]) for k in mix if not pd.isna(w[k]))
    return {"mix_us_weight": round(us, 3), "world_us_weight": round(float(w["world"]), 3), "by_sleeve": {k: round(float(v), 3) for k, v in w.items()}}

def opt_table(UL, D, asof):
    """OPT01-OPT03 over each line's own window, with the underlying measured over the same months (reviewer fix)."""
    rows = []
    allc = D["close"]
    for g, (proxy, members) in PREMIUM_GROUPS.items():
        if proxy not in allc: continue
        for t in members:
            if t not in UL.index or UL.loc[t, "info_only"] or D["u"].loc[t, "currency"] != "USD": continue  # GBP classes map to their USD twin (ELG02)
            j = pd.concat([monthly_tr(allc[t].dropna()), monthly_tr(allc[proxy].dropna())], axis=1).dropna()
            if len(j) < 12: continue
            up, dn = j[j.iloc[:, 1] > 0], j[j.iloc[:, 1] < 0]
            gm = lambda s: (1 + s).prod() ** (1 / len(s)) - 1 if len(s) else np.nan
            U = gm(up.iloc[:, 0]) / gm(up.iloc[:, 1]) if len(up) else np.nan
            Dn = gm(dn.iloc[:, 0]) / gm(dn.iloc[:, 1]) if len(dn) else np.nan
            ann = lambda s: (1 + s).prod() ** (12 / len(s)) - 1
            beta = float(np.cov(j.iloc[:, 0], j.iloc[:, 1])[0, 1] / j.iloc[:, 1].var())
            us = UL.loc[t, "us_situs"]
            tax_drag = UL.loc[t, "TAX01"] / 1e4 if us else 0.0
            rows.append({"group": g, "ticker": t, "venue": UL.loc[t, "venue"], "months": len(j), "since": j.index[0].strftime("%Y-%m"),
                         "line_ann_pct": round(ann(j.iloc[:, 0]) * 100, 1), "underlying_ann_pct": round(ann(j.iloc[:, 1]) * 100, 1),
                         "after_tax_ann_pct": round((ann(j.iloc[:, 0]) - tax_drag) * 100, 1),
                         "gap_after_tax_pct": round((ann(j.iloc[:, 0]) - tax_drag - ann(j.iloc[:, 1])) * 100, 1),
                         "up_capture": round(U, 2), "down_capture": round(Dn, 2), "beta": round(beta, 2),
                         "yield_pct": UL.loc[t, "yield_12m_pct"], "after_tax_yield_pct": UL.loc[t, "after_tax_yield_pct"], "CST10_bps": round(float(UL.loc[t, "CST10"]), 0)})
    return pd.DataFrame(rows)

def macro(Dus):
    """MAC01-MAC10 with the pre-registered flags of pillars v3 (context only; never move money)."""
    out = {}
    def fred(s):
        try: return P1.fred(s)
        except Exception: return None
    def chg(s, days=91):
        s = s.dropna(); p = s.loc[:s.index[-1] - pd.Timedelta(days=days)]
        return float(s.iloc[-1] - p.iloc[-1]) if len(p) else np.nan
    def pchg(s, days=91):
        s = s.dropna(); p = s.loc[:s.index[-1] - pd.Timedelta(days=days)]
        return float(s.iloc[-1] / p.iloc[-1] - 1) if len(p) else np.nan
    c = Dus["close"]
    t3, sahm = fred("T10Y3M"), fred("SAHMREALTIME")
    if t3 is not None:
        m = t3.resample("ME").mean().iloc[-6:]; inv = int((m < 0).sum())
        low24 = t3.iloc[-504:].min(); steep = (t3.iloc[-1] - low24) >= 0.75 and low24 < 0
        sv = float(sahm.iloc[-1]) if sahm is not None else np.nan
        out["MAC01"] = {"name": "Recession indicators", "reading": f"10y-3m {t3.iloc[-1]:+.2f} pts; inverted {inv} of last 6 months; Sahm {sv:.2f}",
                        "flag": bool(inv >= 3 or steep or (sv >= 0.5))}
    hy, baa = fred("BAMLH0A0HYM2"), fred("BAA10Y")
    if hy is not None:
        c3 = chg(hy); bf = False; btxt = ""
        if baa is not None:
            b = baa.dropna(); p80 = b.iloc[-5040:].quantile(0.8); bf = b.iloc[-1] >= p80 or chg(b) >= 0.5; btxt = f"; Baa-10y {b.iloc[-1]:.2f}"
        out["MAC02"] = {"name": "Credit stress", "reading": f"HY spread {hy.iloc[-1]:.2f}% (3m {c3:+.2f}){btxt}", "flag": bool(c3 >= 1.0 or bf)}
    if "^VIX" in c:
        v = c["^VIX"].dropna().iloc[-1]; ts = v / c["^VIX3M"].dropna().iloc[-1] if "^VIX3M" in c else np.nan
        out["MAC03"] = {"name": "Volatility (execution only)", "reading": f"VIX {v:.1f}, VIX/VIX3M {ts:.2f}", "flag": bool(v > 30 or ts > 1), "execution_only": True}
    ry, cpi = fred("DFII10"), fred("CPILFESL")
    if ry is not None:
        r3 = chg(ry); cf = False; ctxt = ""
        if cpi is not None:
            cm = cpi.dropna(); a3 = (cm.iloc[-1] / cm.iloc[-4]) ** 4 - 1; a12 = cm.iloc[-1] / cm.iloc[-13] - 1; cf = a3 > 0.04 and a3 > a12
            ctxt = f"; core CPI 3m ann. {a3*100:.1f}% vs 12m {a12*100:.1f}%"
        out["MAC04"] = {"name": "Real rates and inflation", "reading": f"10y TIPS {ry.iloc[-1]:.2f}% (3m {r3:+.2f}){ctxt}", "flag": bool(r3 >= 0.5 or cf)}
    usd = fred("DTWEXBGS"); aed = c["AED=X"].dropna() if "AED=X" in c else None
    dflag = pchg(usd) >= 0.04 if usd is not None else False
    dev = (aed.iloc[-2:] / 3.6725 - 1).abs() if aed is not None and len(aed) >= 2 else pd.Series([0.0])
    pflag = bool((dev > 0.002).all())  # two consecutive closes (reviewer fix: one print can be a bad tick)
    out["MAC05"] = {"name": "Dollar and AED peg", "reading": f"broad dollar 3m {pchg(usd)*100:+.1f}%; AED/USD {aed.iloc[-1]:.4f} (peg 3.6725)" if usd is not None and aed is not None else "n/a",
                    "flag": bool(dflag or pflag)}
    if "SPY" in c and "IEF" in c:
        r = c[["SPY", "IEF"]].pct_change(fill_method=None).dropna().iloc[-252:]; corr = float(r.corr().iloc[0, 1])
        out["MAC06"] = {"name": "Stock-bond correlation", "reading": f"1-year daily SPY/IEF correlation {corr:+.2f}", "flag": bool(corr > 0)}
    oil = fred("DCOILBRENTEU")
    if oil is None and "CL=F" in c: oil = c["CL=F"]
    if oil is not None:
        o3 = pchg(oil); out["MAC07"] = {"name": "Oil and growth shock", "reading": f"oil {oil.dropna().iloc[-1]:.1f} USD, 3m {o3*100:+.1f}%", "flag": bool(abs(o3) >= 0.30)}
    nfci = fred("NFCI")
    if nfci is not None:
        out["MAC08"] = {"name": "Financial conditions", "reading": f"NFCI {nfci.iloc[-1]:+.2f}", "flag": bool(nfci.iloc[-1] > 0)}
    w = c["ACWI"].dropna()
    if len(w):
        dd_ath = w.iloc[-1] / w.max() - 1; dd52 = w.iloc[-1] / w.iloc[-252:].max() - 1
        mo = w.resample("ME").last(); below = bool(mo.iloc[-1] < mo.iloc[-10:].mean()); m121 = float(mo.iloc[-2] / mo.iloc[-13] - 1)
        br = float((c["RSP"].dropna().iloc[-1] / c["RSP"].dropna().iloc[-126]) / (c["SPY"].dropna().iloc[-1] / c["SPY"].dropna().iloc[-126]) - 1) if "RSP" in c else np.nan
        out["MAC09"] = {"name": "Market drawdown, trend and breadth", "reading": f"world {dd_ath*100:.1f}% from high ({dd52*100:.1f}% from 52-week high); {'below' if below else 'above'} 10-month average; 12-1 return {m121*100:+.1f}%; equal-weight vs S&P 500 6m {br*100:+.1f}%",
                        "flag": bool(dd_ath <= -0.15 or (below and m121 < 0))}
    epu = fred("USEPUINDXD"); epf = False
    if epu is not None:
        e = epu.dropna(); epf = bool(e.rolling(7).mean().iloc[-1] > e.iloc[-1260:].quantile(0.9))
    n = sum(v["flag"] for k, v in out.items() if k not in ("MAC03",)) + int(epf)
    out["MAC10"] = {"name": "Regime count", "reading": f"{n} of 9 flags on (policy-uncertainty flag {'on' if epf else 'off'})", "flag": n >= 4,
                    "state": "calm" if n <= 1 else "watch" if n <= 3 else "stress"}
    return out

def news_view(week_dir):
    """N_g = 50 + 12.5 x sum(c x s) / sum(c) over NWS01-17 and EVT01, EVT02, EVT04-EVT08 group scores (EVT09 excluded)."""
    nd = Path(week_dir) / "news" if week_dir else None
    conf = {"high": 1.0, "medium": 0.67, "low": 0.33}
    acc = {}
    if not nd or not nd.exists(): return {}, []
    rows = []
    for f in sorted(nd.glob("*.json")):
        try: j = json.loads(f.read_text())
        except Exception: continue
        pid = j.get("pillar_id", f.stem)
        if pid == "EVT09": continue
        for g in j.get("group_scores", []):
            b = g.get("group"); s = int(g.get("score", 0) or 0); c = conf.get(str(g.get("confidence", "low")).lower(), 0.33)
            if not j.get("saturated", True): s = max(-1, min(1, s)); c = min(c, 0.33)
            acc.setdefault(b, []).append((c, s)); rows.append({"pillar": pid, "group": b, "score": s, "confidence": c, "sources": g.get("n_sources", ""), "saturated": j.get("saturated", "")})
    N = {b: round(50 + 12.5 * sum(c * s for c, s in v) / sum(c for c, s in v), 1) for b, v in acc.items() if sum(c for c, s in v) > 0}
    return N, rows

def run(week_dir=None):
    R = E2.run(week_dir=week_dir)
    D = load_us(); asof = R["asof"]
    UL = us_lines(D, R["C_usd"], max(asof, D["close"].index[-1]))
    R.update({"UL": UL, "XW": cross_wrapper(R, UL, D), "FIT12": fit12(R, UL), "FIT07": fit07(R), "OPT": opt_table(UL, D, asof), "MAC": macro(D)})
    N, nrows = news_view(week_dir); R["N"] = N; R["news_rows"] = nrows
    R["N_sleeve"] = {k: (round(sum(w * N.get(b, 50) for b, w in m.items()) / sum(m.values()), 1) if any(b in N for b in m) else None) for k, m in SLEEVE_BUCKETS.items()}
    R["Dus"] = D
    return R

if __name__ == "__main__":
    R = run()
    print(json.dumps(R["XW"], indent=1, default=str)[:3000]); print(R["FIT12"], R["FIT07"])
    print(R["OPT"].to_string()); print(json.dumps(R["MAC"], indent=1))
