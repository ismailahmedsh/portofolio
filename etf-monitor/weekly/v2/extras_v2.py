"""Additional v2 pillars computed weekly: momentum record (MOM01-05), macro context (MAC01-04), stress shortfall (RSK04),
portfolio constraints (RSK06, RSK07, RSK08, FIT02, FIT07, FIT11), gold custody (DUR02), live record (REC01) and redundancy check (REC03)."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import pillars as P1

STRESS = [("2008-09-30", "2009-02-28", "Global financial crisis"), ("2020-02-29", "2020-03-31", "Covid crash"), ("2022-01-31", "2022-09-30", "2022 rate shock")]

def compute(R, cfg, plan):
    m, close, L, XS = R["mret"], R["close"], R["L"], R["XS"]; wref = R["world_ref"]; out = {}
    # MOM01/02 record and MOM05 display (cluster references against the world reference)
    w = m[wref]; mom = {}
    for r in XS.index:
        j = pd.concat([m[r], w], axis=1).dropna()
        if len(j) < 13: continue
        m12 = (1 + j.iloc[-13:-1]).prod() - 1
        beta = XS.loc[r, "FAC05"]; resid = j.iloc[:, 0] - beta * j.iloc[:, 1]
        mom[r] = {"MOM01": float((m12.iloc[0] - m12.iloc[1]) * 100), "MOM02": float(((1 + resid.iloc[-13:-1]).prod() - 1) * 100)}
    out["mom"] = pd.DataFrame(mom).T
    wl = close[wref].dropna(); mo = wl.resample("ME").last()
    out["MOM04"] = {"below_10m_avg": bool(mo.iloc[-1] < mo.iloc[-10:].mean()), "mom_12_1": float(mo.iloc[-2] / mo.iloc[-13] - 1) if len(mo) > 13 else None}
    out["MOM04"]["flag"] = out["MOM04"]["below_10m_avg"] and (out["MOM04"]["mom_12_1"] or 0) < 0
    wk = close.resample("W-FRI").last()
    def rel(t, n): s = wk[t].dropna(); v = wk[wref].dropna(); return float((s.iloc[-1] / s.iloc[-1 - n] - v.iloc[-1] / v.iloc[-1 - n]) * 100) if len(s) > n and len(v) > n else None
    out["MOM05"] = {k: {"4w": rel(ref, 4), "13w": rel(ref, 13), "52w": rel(ref, 52)} for k, ref in R["sleeves"].items() if ref in wk}
    vt = close["VT"].dropna(); dd = vt.iloc[-1] / vt.iloc[-252:].max() - 1; vol = vt.pct_change().iloc[-21:].std() * np.sqrt(252)
    out["MOM03"] = {"world_drawdown": round(float(dd) * 100, 1), "vol_1m": round(float(vol) * 100, 1), "crash_state": bool(dd < -0.20 and vol > 0.30)}
    # MAC01-04 context from the macro readings (FRED and VIX), never used for decisions
    try:
        rd = P1.macro_readings()
        out["MAC"] = {"MAC01 Recession indicators": [rd.get("H01"), rd.get("H02"), rd.get("H03")], "MAC02 Credit and financial stress": [rd.get("H04"), rd.get("H08")],
                      "MAC03 Volatility regime": [rd.get("H09"), rd.get("H10")], "MAC04 Rates, dollar and oil": [rd.get("H05"), rd.get("H06"), rd.get("H07")]}
    except Exception as e:
        out["MAC"] = {"error": str(e)[:120]}
    # RSK04 stress-window shortfall beyond beta (record)
    rs = {}
    for r in XS.index:
        b = XS.loc[r, "FAC05"]; v = {}
        for a, z, n in STRESS:
            x = m[r].loc[a:z]; y = m[wref].loc[a:z]
            if x.notna().sum() == len(x) and len(x) > 0: v[n] = float(((1 + x).prod() - 1 - b * ((1 + y).prod() - 1)) * 100)
        if v: rs[r] = v
    out["RSK04"] = pd.DataFrame(rs).T
    # Portfolio constraints for the owner mix
    mix = R["mix"]; sl = R["sleeves"]; mm = pd.concat([m[sl[k]] for k in mix], axis=1).dropna().iloc[-120:]; mm.columns = list(mix)
    wv = np.array([mix[k] for k in mix]); pr = mm.values @ wv
    nav = np.cumprod(1 + pr); mdd = float((nav / np.maximum.accumulate(nav) - 1).min() * 100)
    wn = np.cumprod(1 + m[wref].reindex(mm.index).values); wdd = float((wn / np.maximum.accumulate(wn) - 1).min() * 100)
    out["RSK06"] = {"mix_max_dd": round(mdd, 1), "world_max_dd": round(wdd, 1), "budget": round(wdd - 5, 1), "pass": mdd >= wdd - 5}
    cov = np.cov(mm.values.T); pv = wv @ cov @ wv; rc = wv * (cov @ wv) / pv
    out["RSK07"] = {k: {"weight": mix[k], "risk_share": round(float(rc[i]), 3), "ratio": round(float(rc[i] / mix[k]), 2), "pass": rc[i] / mix[k] <= 1.5} for i, k in enumerate(mix)}
    cur = np.cumprod(1 + pr); out["RSK08"] = {"mix_drawdown_now": round(float((cur[-1] / cur.max() - 1) * 100), 1), "world_drawdown_now": out["MOM03"]["world_drawdown"]}
    usw = {k: L.loc[sl[k], "us_weight"] for k in mix}; usw["world"] = L.loc["VWRA.L", "us_weight"]
    mix_us = sum(mix[k] * (usw[k] if not pd.isna(usw[k]) else 0) for k in mix)
    out["FIT07"] = {"mix_us_weight": round(float(mix_us) * 100, 1), "world_us_weight": round(float(usw["world"]) * 100, 1), "limit": round(float(usw["world"]) * 100 + 10, 1),
                    "pass": mix_us <= usw["world"] + 0.10, "note": "applies to score-driven tilts; your own mix is your choice and is shown for information"}
    held = [o["ticker"] for o in plan["orders"]] + list((cfg.get("positions") or {}).keys())
    out["FIT11"] = {"lines_held_or_bought": sorted(set(held)), "count": len(set(held)), "pass": len(set(held)) <= 4}
    V = plan["portfolio_value_usd"]
    out["FIT02"] = {k: (round((plan["sleeve_values"][k] - mix[k] * V) / R["C_usd"], 1) if V > 0 else 0.0) for k in mix}
    gold = L[L.scope.astype(str).str.contains("gold_physical")]
    out["DUR02"] = {t: bool("physical" in str(L.loc[t, "name"]).lower() and str(L.loc[t, "ELG01"]) == "True") for t in gold.index}
    fills = cfg.get("fills") or []
    out["REC01"] = "no fills recorded yet: the live record starts with your first logged buy" if not fills else f"{len(fills)} fills recorded"
    sc = XS[[c for c in XS.columns if c.endswith("_s")]].astype(float)
    rho = sc.corr(method="spearman"); pairs = [(a, b, round(float(rho.loc[a, b]), 2)) for i, a in enumerate(rho.index) for b in rho.index[i + 1:] if abs(rho.loc[a, b]) >= 0.7]
    out["REC03"] = {"pairs_rho_0_7_or_more": pairs, "pass_0_85": all(abs(p[2]) < 0.85 for p in pairs)}
    return out

def report_section(X, R):
    A = []; w = A.append
    w("## Portfolio limits and context\n")
    w("| Pillar | Reading | Status |\n|---|---|---|")
    r6 = X["RSK06"]; w(f"| RSK06 Drawdown budget (10 years) | Your mix {r6['mix_max_dd']}% vs world {r6['world_max_dd']}% (budget {r6['budget']}%) | {'within' if r6['pass'] else 'over'} |")
    for k, v in X["RSK07"].items(): w(f"| RSK07 Risk share, {k} | weight {v['weight']:.0%}, risk share {v['risk_share']:.0%}, ratio {v['ratio']} | {'within 1.5' if v['pass'] else 'above 1.5'} |")
    f7 = X["FIT07"]; w(f"| FIT07 US look-through weight | Your mix {f7['mix_us_weight']}% vs world {f7['world_us_weight']}% (tilt limit {f7['limit']}%) | {'within' if f7['pass'] else 'above, shown for information: your mix is your choice'} |")
    w(f"| FIT11 Lines held or bought | {', '.join(t[:-2] for t in X['FIT11']['lines_held_or_bought'])} | {'within 4' if X['FIT11']['pass'] else 'over 4'} |")
    w(f"| RSK08 Drawdown now | Your mix {X['RSK08']['mix_drawdown_now']}% from its high, world {X['RSK08']['world_drawdown_now']}% from its 52-week high | protocol at -20%: keep depositing |")
    m4 = X["MOM04"]; w(f"| MOM04 Core trend flag | VWRA below 10-month average: {'yes' if m4['below_10m_avg'] else 'no'}; 12-1 momentum {m4['mom_12_1']*100:+.1f}% | {'ON (information only)' if m4['flag'] else 'off'} |")
    m3 = X["MOM03"]; w(f"| MOM03 Momentum-crash state | world {m3['world_drawdown']}% from high, 1-month volatility {m3['vol_1m']}% | {'crash state' if m3['crash_state'] else 'normal'} |")
    w(f"| REC01 Live record | {X['REC01']} | |")
    w(f"| REC03 Redundancy | {len(X['REC03']['pairs_rho_0_7_or_more'])} scored pairs with correlation 0.7 or more across groups | {'no pair at 0.85 or more' if X['REC03']['pass_0_85'] else 'pair at 0.85 or more: merge needed'} |")
    w("\n**Your sleeves against the world (MOM05, display only)**\n\n| Sleeve | 4 weeks | 13 weeks | 52 weeks |\n|---|---|---|---|")
    for k, v in X["MOM05"].items(): w(f"| {k} | {v['4w']:+.1f} pts | {v['13w']:+.1f} pts | {v['52w']:+.1f} pts |" if v['52w'] is not None else f"| {k} | n/a | n/a | n/a |")
    w("\n**Macro context (MAC01-04, never used for decisions)**\n")
    for k, v in X["MAC"].items():
        if isinstance(v, list): w(f"- {k}: " + "; ".join(t[1] for t in v if t))
    rs = X["RSK04"]
    if len(rs):
        w("\n**Crash windows: shortfall beyond what beta explains (RSK04, record), your sleeves**\n\n| Sleeve | " + " | ".join(rs.columns) + " |\n|" + "---|" * (len(rs.columns) + 1))
        for k, ref in R["sleeves"].items():
            if ref in rs.index: w(f"| {k} | " + " | ".join(f"{x:+.1f} pts" if not pd.isna(x) else "n/a" for x in rs.loc[ref]) + " |")
    return "\n".join(A) + "\n"
