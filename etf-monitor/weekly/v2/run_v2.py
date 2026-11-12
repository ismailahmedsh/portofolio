"""Weekly run for engine v2: scores, the monthly deposit plan, REC07 (mix comparison), REC04 (tilt gate), pick log, report.
Usage: python3 -I v2/run_v2.py --week 2026-W46 [--backtests]"""
import argparse, json, sys
from pathlib import Path
from statistics import NormalDist
import numpy as np, pandas as pd, yaml
sys.path.insert(0, str(Path(__file__).parent)); sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import engine_v2 as E2
import extras_v2 as X2

ROOT = Path(__file__).resolve().parents[1]; CACHE = ROOT / "cache"
N_TRIALS = 26  # pillars v2 REC04 minimum; every new rule or mix edit adds one (CHANGELOG.md)
SPREAD_BPS = 10

# ---------------- monthly deposit plan ----------------
def positions(cfg, L):
    pos = {k: float(v["units"]) for k, v in (cfg.get("positions") or {}).items() if v and v.get("units")}
    if not pos:
        for f in cfg.get("fills") or []: pos[f["ticker"]] = pos.get(f["ticker"], 0) + float(f["units"])
    return {t: u * float(L.loc[t, "price_usd"]) for t, u in pos.items() if t in L.index}

def sleeve_of(t, R):
    for k, ref in R["sleeves"].items():
        if (k == "world" and t in R["world_lines"]) or R["cl"].get(t) == ref: return k
    return "other"

def plan(R, cfg):
    L, LS = R["L"], R["LS"]; C = R["C_usd"] + float(cfg.get("extra_cash_usd") or 0); comm = cfg["deposit"]["commission_min_usd"]
    val = positions(cfg, L); V = sum(val.values())
    sv = {k: sum(v for t, v in val.items() if sleeve_of(t, R) == k) for k in R["mix"]}
    gaps = {k: R["mix"][k] * (V + C) - sv[k] for k in R["mix"]}
    orders, notes, left = [], [], C
    n_orders = 1 if C < 2 * 680 else min(len(R["mix"]), int(C // 340))
    for k in sorted(gaps, key=gaps.get, reverse=True):
        if left < 340 and orders: break
        if gaps[k] <= 0 and orders: break
        amt = left if len(orders) == n_orders - 1 or n_orders == 1 else min(left, max(340.0, gaps[k]))
        if k == "world":
            cands = [t for t in R["world_lines"] if t in L.index and L.loc[t, "buyable"]]
        else:
            cands = [t for t in L.index[L.cluster == R["sleeves"][k]] if L.loc[t, "buyable"] and (LS.loc[t, "line_score"] or 0) >= 40]
        if not cands:
            notes.append(f"{k}: no line you have confirmed as buyable in IBKR, so this money goes to the next sleeve. Confirm a line in config/portfolio_v2.yaml (orderable) to open it: cheapest by all-in cost are {', '.join(L.loc[L.cluster == R['sleeves'][k]].sort_values('CST10').index[:3]) if k != 'world' else 'FWRA.L, ACWD.L'}.")
            continue
        t = min(cands, key=lambda x: L.loc[x, "CST10"]) if k != "world" else cands[0]
        px = float(L.loc[t, "price_usd"]); units = int((amt - comm) // px)
        if units < 1: notes.append(f"{k}: {t} costs US${px:,.2f} a share, more than this order; next sleeve."); continue
        cost = units * px + comm; orders.append({"sleeve": k, "ticker": t, "units": units, "price_usd": round(px, 2), "cost_usd": round(cost, 2), "gap_before_usd": round(gaps[k], 2)})
        left -= cost
        if len(orders) >= n_orders: break
    if not orders:  # never skip the deposit: world chain
        t = "VWRA.L"; px = float(L.loc[t, "price_usd"]); units = int((C - comm) // px)
        orders.append({"sleeve": "world", "ticker": t, "units": units, "price_usd": round(px, 2), "cost_usd": round(units * px + comm, 2), "gap_before_usd": round(gaps["world"], 2)})
        left = C - orders[0]["cost_usd"]
    return {"cash_usd": round(C, 2), "portfolio_value_usd": round(V, 2), "sleeve_values": {k: round(v, 2) for k, v in sv.items()}, "gaps": {k: round(v, 2) for k, v in gaps.items()},
            "orders": orders, "residue_usd": round(left, 2), "notes": notes}

# ---------------- backtests on US-listed proxies (adjusted closes) ----------------
def proxies():
    c = pd.read_pickle(CACHE / "v2_close_usd.pkl")[["VT", "SPY", "QQQ", "EFA", "EEM"]]
    v1 = pd.read_pickle(CACHE / "adj.pkl") if (CACHE / "adj.pkl").exists() else pd.DataFrame()
    for t in ["IWD", "IWM", "IWN", "QUAL", "MTUM", "USMV", "VLUE", "EWJ", "VGK", "BIL"]:
        if t in v1: c[t] = v1[t]
    return c.resample("ME").last()

def sim_mix(m, weights, monthly, start, tilt_fn=None, lag=1, comm=1.70):
    """Monthly gap routing: one order a month to the sleeve furthest below target. tilt_fn(date) -> target dict (overrides)."""
    r = m.pct_change(fill_method=None).loc[start:]; dates = r.index; hold = {k: 0.0 for k in m.columns}; vals, flows = [], []
    tg_hist = []
    sat_months = []
    for i, dt in enumerate(dates):
        for k in hold: hold[k] *= 1 + (0 if pd.isna(r.loc[dt, k]) else r.loc[dt, k])
        tg = dict(weights)
        if tilt_fn is not None and i - lag >= 0:
            tg = tilt_fn(dates[i - lag], weights)
        V = sum(hold.values()); gaps = {k: tg.get(k, 0) * (V + monthly) - hold.get(k, 0) for k in tg}
        k = max(gaps, key=gaps.get)
        if k not in weights:  # tilt sleeve: at most 2 of any 12 deposits
            recent = [x for x in sat_months if x > i - 12]
            if len(recent) >= 2: k = max(weights, key=lambda x: gaps.get(x, -1e9))
            else: sat_months.append(i)
        hold[k] = hold.get(k, 0) + monthly - comm - monthly * SPREAD_BPS / 1e4
        vals.append(sum(hold.values())); flows.append(monthly)
    return pd.Series(vals, dates), pd.Series(flows, dates)

def metrics(vals, flows, periods):
    r = ((vals - flows) / vals.shift(1) - 1).dropna()
    def xirr():
        cf = [(-f, d) for d, f in flows.items()] + [(vals.iloc[-1], vals.index[-1])]; t0 = cf[0][1]; lo, hi = -0.9, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2; npv = sum(a / (1 + mid) ** ((d - t0).days / 365.25) for a, d in cf); lo, hi = (mid, hi) if npv > 0 else (lo, mid)
        return mid
    nav = (1 + r).cumprod(); yrs = len(r) / 12
    out = {"final": round(vals.iloc[-1]), "paid_in": round(flows.sum()), "mwr": round(xirr() * 100, 2), "twr": round((nav.iloc[-1] ** (1 / yrs) - 1) * 100, 2),
           "max_dd": round((nav / nav.cummax() - 1).min() * 100, 1), "worst_year": round(r.groupby(r.index.year).apply(lambda x: (1 + x).prod() - 1).min() * 100, 1)}
    for a, b in periods: x = r.loc[a:b]; out[f"twr_{a}_{b}"] = round(((1 + x).prod() ** (12 / len(x)) - 1) * 100, 2) if len(x) > 11 else None
    return out, r

def rec07(cfg, monthly):
    m = proxies()[["VT", "SPY", "QQQ"]].rename(columns={"VT": "world", "SPY": "sp500", "QQQ": "ndx100"}); start = "2008-07-31"
    per = [("2008", "2014"), ("2015", "2019"), ("2020", "2026")]
    owner = {k: v["target"] for k, v in cfg["strategic_mix"].items()}
    mixes = {"Your mix " + "/".join(f"{int(v*100)}" for v in owner.values()): owner, "100% world": {"world": 1.0}, "100% S&P 500": {"sp500": 1.0}, "100% Nasdaq-100": {"ndx100": 1.0},
             "80/10/10": {"world": .8, "sp500": .1, "ndx100": .1}, "60/25/15": {"world": .6, "sp500": .25, "ndx100": .15}, "50/30/20": {"world": .5, "sp500": .3, "ndx100": .2}}
    rows = []
    for n, w in mixes.items():
        v, f = sim_mix(m, w, monthly, start); o, _ = metrics(v, f, per); rows.append({"mix": n, **o})
    return {"period": f"{start[:7]} to {pd.read_pickle(CACHE / 'v2_close_usd.pkl')['VT'].dropna().index[-1].date()}", "proxies": "VT world, SPY S&P 500, QQQ Nasdaq-100 (US-listed, dividend-adjusted, before UAE withholding)", "rows": rows}

def x_point_in_time(m, fr, cand, world, dt):
    """Exposure score X of cand against world, using data up to dt only (same formulas as engine_v2, EXR06 missing)."""
    j = pd.concat([m[cand], m[world]], axis=1).loc[:dt].pct_change(fill_method=None).dropna().iloc[-120:]
    if len(j) < 36: return np.nan
    def ex(y, w):
        e = {}; b = np.cov(y, w)[0, 1] / w.var(); e["beta"] = .67 * b + .33
        ff = fr.reindex(y.index).dropna(); ff = ff.loc[:dt - pd.offsets.MonthEnd(1)]
        if len(ff) >= 36:
            X = np.column_stack([np.ones(len(ff)), ff[["Mkt-RF", "SMB", "HML", "RMW", "CMAp"]].values]); co = np.linalg.lstsq(X, (y.reindex(ff.index) - ff["RF"]).values, rcond=None)[0]
            e.update(FAC01=co[3], FAC02=co[4], FAC03=co[5], FAC04=co[2] if co[4] >= -0.1 else min(co[2], 0))
        nav = (1 + y).cumprod(); e["dd"] = (nav / nav.cummax() - 1).min()
        up, dn = w > 0, w < 0
        e["RSK03"] = np.cov(y[dn], w[dn])[0, 1] / w[dn].var() - np.cov(y[up], w[up])[0, 1] / w[up].var()
        q = y.quantile(.05); e["RSK05"] = -y[y <= q].mean() / y.std()
        e["EXR08"] = ((1 + y.iloc[-60:]).prod() - (1 + w.iloc[-60:]).prod()) * 100 if len(y) >= 48 else np.nan
        return e
    a, b = ex(j.iloc[:, 0], j.iloc[:, 1]), ex(j.iloc[:, 1], j.iloc[:, 1])
    nav_w = (1 + j.iloc[:, 1]).cumprod(); ddw = (nav_w / nav_w.cummax() - 1).min()
    s = {k: E2.tanh_score(a.get(k), b.get(k), .2, 1) for k in ["FAC01", "FAC02", "FAC03", "FAC04"]}
    s["RSK01"] = E2.tanh_score((a["dd"] - a["beta"] * ddw) * 100, 0, 10, 1, True); s["RSK03"] = E2.tanh_score(a["RSK03"], b["RSK03"], .2, -1, True)
    s["RSK05"] = E2.tanh_score(a["RSK05"], b["RSK05"], .5, -1, True); s["EXR08"] = E2.tanh_score(a.get("EXR08"), b.get("EXR08"), 20, -1)
    exr, _ = E2.fam_score(s, {"EXR06": .4, "EXR08": .6}); fac, _ = E2.fam_score(s, {"FAC01": .12, "FAC02": .30, "FAC03": .28, "FAC04": .30}); rsk, _ = E2.fam_score(s, {"RSK01": .35, "RSK03": .35, "RSK05": .30})
    return (20 * exr + 40 * fac + 40 * rsk) / 100

def rec04(cfg, monthly):
    m = proxies(); fr = pd.read_pickle(CACHE / "v2_french.pkl")["Developed_5_Factors"].copy(); fr.index = fr.index + pd.offsets.MonthEnd(0)
    fr["CMAp"] = fr["CMA"] - np.polyfit(fr["HML"], fr["CMA"], 1)[0] * fr["HML"]
    owner = {k: v["target"] for k, v in cfg["strategic_mix"].items()}; lim = cfg["tilt_limits"]
    base = m[["VT", "SPY", "QQQ"]].rename(columns={"VT": "world", "SPY": "sp500", "QQQ": "ndx100"})
    cands = [c for c in ["EFA", "EEM", "IWD", "IWM", "IWN", "QUAL", "MTUM", "USMV", "VLUE", "EWJ", "VGK"] if c in m]
    mm = pd.concat([base, m[cands]], axis=1); start = "2011-12-31"
    qs = [d for d in mm.loc[start:].index if d.month in (3, 6, 9, 12)]
    X = pd.DataFrame({c: {q: x_point_in_time(m, fr, c, "VT", q) for q in qs} for c in cands})
    def tilt(dt, w):
        q = max([x for x in qs if x <= dt], default=None)
        if q is None: return dict(w)
        i = qs.index(q); qual = {c: X.loc[q, c] for c in cands if i >= 1 and X.loc[q, c] >= 55 and X.loc[qs[i - 1], c] >= 55}
        t = {c: lim["per_sleeve_max"] * float(np.clip((x - 55) / 15, 0, 1)) for c, x in qual.items()}
        t = {c: (v if v >= 0.05 else 0.0) for c, v in t.items()}; tot = sum(t.values())
        if tot > lim["total_tilt_max"]: t = {c: v * lim["total_tilt_max"] / tot for c, v in t.items()}; tot = lim["total_tilt_max"]
        out = {k: v * (1 - tot) for k, v in w.items()}; out.update({c: v for c, v in t.items() if v > 0}); return out
    per = [("2012", "2016"), ("2017", "2021"), ("2022", "2026")]
    vb, fb = sim_mix(mm, owner, monthly, start); ob, rb = metrics(vb, fb, per)
    res = {"rule": "Quarterly: sleeves with X >= 55 at two consecutive quarter-ends get a tilt of up to 10% (X 55 -> 0, X 70 -> 10%), total tilt at most 15%, at most 2 of any 12 deposits; candidates " + ", ".join(cands),
           "period": f"{start[:7]} to {pd.read_pickle(CACHE / 'v2_close_usd.pkl')['VT'].dropna().index[-1].date()}", "owner_mix": ob, "n_trials": N_TRIALS}
    gate = True
    for lag, name in [(1, "same_month"), (2, "lagged")]:
        vt_, ft_ = sim_mix(mm, owner, monthly, start, tilt_fn=tilt, lag=lag); o, rt = metrics(vt_, ft_, per)
        act = (rt - rb.reindex(rt.index)).dropna(); ir = act.mean() / act.std() if act.std() > 0 else 0
        nd = NormalDist(); g = .5772156649; sd_trials = 0.25 / np.sqrt(12)  # assumed spread of monthly IRs across trials
        sr0 = sd_trials * ((1 - g) * nd.inv_cdf(1 - 1 / N_TRIALS) + g * nd.inv_cdf(1 - 1 / (N_TRIALS * np.e)))
        z = (ir - sr0) * np.sqrt(len(act) - 1) / np.sqrt(1 - act.skew() * ir + (act.kurt() + 2) / 4 * ir ** 2); dsr = nd.cdf(z)
        beats = all((o.get(f"twr_{a}_{b}") or -99) - (ob.get(f"twr_{a}_{b}") or 99) >= 0.25 for a, b in per) and o["mwr"] - ob["mwr"] >= 0.25
        res[name] = {**o, "info_ratio_annual": round(ir * np.sqrt(12), 2), "deflated_prob": round(dsr, 3), "beats_mix_everywhere": beats}
        gate = gate and beats and dsr > 0.95
    res["gate_pass"] = bool(gate); res["latest_X"] = {c: round(float(X[c].iloc[-1]), 1) for c in cands}
    return res

# ---------------- report ----------------
def report(week, R, pl, r07, r04, cfg):
    L, LS, XS, FT = R["L"], R["LS"], R["XS"], R["FT"]; A = []; w = A.append
    w(f"# Weekly review v2, {week} (prices to {R['asof'].date()})\n")
    w("Research for the owner's own portfolio, not personal financial advice. Engine v2 on the audited pillars (PILLARS_V2.md). Yardstick: your strategic mix "
      + ", ".join(f"{k} {v:.0%}" for k, v in R["mix"].items()) + ".\n")
    w("## This month's deposit\n")
    w(f"Cash to invest: US${pl['cash_usd']:,.2f} (2,500 AED at 3.6725, minus the US$2 conversion minimum). Portfolio value on record: US${pl['portfolio_value_usd']:,.2f}.\n")
    w("| Order | Sleeve | Line | Units | Price | Cost incl. commission | Gap before |\n|---|---|---|---|---|---|---|")
    for i, o in enumerate(pl["orders"], 1): w(f"| {i} | {o['sleeve']} | {o['ticker'][:-2]} | {o['units']} | US${o['price_usd']:,.2f} | US${o['cost_usd']:,.2f} | US${o['gap_before_usd']:,.2f} |")
    w(f"\nLeft over in cash: US${pl['residue_usd']:,.2f}, carried to next month.\n")
    for n in pl["notes"]: w(f"- {n}")
    ev = [(t, e) for t in L.index for e in json.loads(L.loc[t, "events"]) if e[1] >= 1]
    blocked = [t for t in L.index if L.loc[t, "EVT_block"]]
    w("\n## Sell anything?\n")
    w("No, unless a structural event below is confirmed from its primary source. Scores, trend, drawdowns and news sentiment never sell.\n" if not blocked else f"**Structural events block buying: {', '.join(blocked)}.** Check the primary source; if confirmed, rule S1 switches any holding to the best same-index line, never into cash.\n")
    if ev:
        w("| Line | Event pillar | Severity | Issue |\n|---|---|---|---|")
        for t, e in ev[:20]: w(f"| {t[:-2]} | {e[0]} | {e[1]} | {e[2]} {'([source](' + e[3] + '))' if e[3] else ''} |")
        w("")
    w("## Your mix against the alternatives (REC07, information)\n")
    w(f"{r07['period']}, deposits of US${R['C_usd']:,.2f} a month routed to the sleeve furthest below target, US$1.70 commission and {SPREAD_BPS} bps spread per buy. Proxies: {r07['proxies']}. Past leadership is not a forecast.\n")
    w("| Mix | Final value | Paid in | Return on your money | Time-weighted | Worst drop | Worst year | 2008-2014 | 2015-2019 | 2020-2026 |\n|---|---|---|---|---|---|---|---|---|---|")
    for r in r07["rows"]: w(f"| {r['mix']} | US${r['final']:,} | US${r['paid_in']:,} | {r['mwr']:.1f}% | {r['twr']:.1f}% | {r['max_dd']:.0f}% | {r['worst_year']:.0f}% | {r['twr_2008_2014']:.1f}% | {r['twr_2015_2019']:.1f}% | {r['twr_2020_2026']:.1f}% |")
    w("\n## May scores move money yet? (REC04 gate)\n")
    w(f"Rule tested: {r04['rule']}. Period {r04['period']}, against your mix, {r04['n_trials']} trials counted.\n")
    w("| Execution | Return on your money | Time-weighted | 2012-2016 | 2017-2021 | 2022-2026 | Information ratio | Deflated probability | Beats your mix everywhere |\n|---|---|---|---|---|---|---|---|---|")
    ob = r04["owner_mix"]; w(f"| Your mix (yardstick) | {ob['mwr']:.1f}% | {ob['twr']:.1f}% | {ob['twr_2012_2016']:.1f}% | {ob['twr_2017_2021']:.1f}% | {ob['twr_2022_2026']:.1f}% | | | |")
    for k in ["same_month", "lagged"]:
        o = r04[k]; w(f"| Tilts, {k.replace('_', ' ')} | {o['mwr']:.1f}% | {o['twr']:.1f}% | {o['twr_2012_2016']:.1f}% | {o['twr_2017_2021']:.1f}% | {o['twr_2022_2026']:.1f}% | {o['info_ratio_annual']:.2f} | {o['deflated_prob']:.2f} | {'yes' if o['beats_mix_everywhere'] else 'no'} |")
    w(f"\n**Gate: {'PASSED, tilts may be proposed for your confirmation' if r04['gate_pass'] else 'not passed, so scores stay display-only and every deposit follows your mix'}.**\n")
    w("## Lines in your sleeves (line view, scored within each same-index group)\n")
    for k, ref in R["sleeves"].items():
        idx = [t for t in (R["world_lines"] if k == "world" else L.index[L.cluster == ref]) if t in L.index]
        w(f"**{k}**\n\n| Line | Fee | All-in cost a year (bps) | US withholding (bps) | Swap | Line score | Buyable | Blocked by |\n|---|---|---|---|---|---|---|---|")
        for t in sorted(idx, key=lambda x: L.loc[x, "CST10"]):
            w(f"| {t[:-2]} | {L.loc[t,'CST01']:.0f} bps | {L.loc[t,'CST10']:.1f} | {L.loc[t,'TAX01']:.1f} | {'yes' if L.loc[t,'swap'] else ''} | {LS.loc[t,'line_score']:.0f} | {'yes' if L.loc[t,'buyable'] else 'no'} | {L.loc[t,'fail_reasons'].replace('ELG08','not confirmed in IBKR').replace('ELG09','data coverage')} |")
        w("")
    w("Swap lines (SPXS, XSPU) avoid the 15% US dividend withholding through a US tax rule (section 871(m)); half that edge is charged as tax-rule risk.\n")
    w("## Exposure view: equity groups against the world (X, world = 50)\n")
    w("X combines expected-return signals (20), rewarded factor tilts (40) and crash risk beyond market exposure (40, one-sided, cannot exceed 50). Display only until the REC04 gate passes. The factor priors are assumptions, not estimates.\n")
    xs = XS.join(FT[["fit"]], how="left"); names = L["name"]
    w("| Line (group reference) | X | Expected return | Factors | Risk | Beta | Fit with your mix | Name |\n|---|---|---|---|---|---|---|---|")
    for t, r in pd.concat([xs.sort_values("X", ascending=False).head(15), xs.sort_values("X").head(8)]).iterrows():
        w(f"| {t[:-2]} | {r.X:.0f} | {r.EXR:.0f} | {r.FAC:.0f} | {r.RSK:.0f} | {r.FAC05:.2f} | {'' if pd.isna(r.fit) else f'{r.fit:.0f}'} | {str(names.get(t, ''))[:60]} |")
    w(f"\nYour sleeves: world {xs.loc[R['world_ref'], 'X']:.0f}, S&P 500 {xs.loc[R['sleeves']['sp500'], 'X']:.0f}, Nasdaq-100 {xs.loc[R['sleeves']['ndx100'], 'X']:.0f}. A low X for Nasdaq-100 reflects growth tilt (negative value loading) and deeper crashes than its beta implies, not a sell signal.\n")
    w(X2.report_section(R["extras"], R))
    cov = coverage_table(R)
    w("## Pillar coverage this week\n"); w(cov)
    w("\n## Data notes\n\n- Prices: Yahoo Finance via yfinance, LSE lines converted to USD; unofficial and for personal use.\n- Fund size is missing from Yahoo for " + str(int(L['DUR01'].isna().sum())) + " lines (for example CSPX, CNDX); it is listed as missing, not held against them.\n- Tracking difference (CST02) fails closed until fee history is collected, so line choice uses current fee plus US withholding.\n- Same-index groups come from the index named in each fund's name, confirmed by return correlation.")
    return "\n".join(A) + "\n"

BUILT = set()
def coverage_table(R):
    spec = E2.SPEC; built = BUILT
    built |= {"ELG01", "ELG02", "ELG03", "ELG04", "ELG05", "ELG06", "ELG07", "ELG08", "ELG09", "ELG10", "CST01", "CST02", "CST04", "CST06", "CST08", "CST10", "TAX01", "TAX03", "TAX05", "DUR01", "DUR04", "DUR06",
              "EXR02", "EXR08", "FAC01", "FAC02", "FAC03", "FAC04", "FAC05", "RSK01", "RSK02", "RSK03", "RSK05", "CON04", "CON05", "FIT01", "FIT03", "FIT04", "FIT05", "FIT06", "FIT10", "REC02", "REC04", "REC07",
              "MOM01", "MOM02", "MOM03", "MOM04", "MOM05", "MAC01", "MAC02", "MAC03", "MAC04", "RSK04", "RSK06", "RSK07", "RSK08", "FIT02", "FIT07", "FIT11", "DUR02", "REC01", "REC03"}
    agents = {p["id"] for p in spec["pillars"] if p["computed_by"] == "agent"}
    rows = {}
    for p in spec["pillars"]:
        f = p["family"] if p["family"] in [x["code"] for x in spec["families"]] else p["id"][:3]
        st = "agent (weekly workflow)" if p["id"] in agents else ("built" if p["id"] in built else ("not built: unverified source" if p["source_status"] != "verified" else "not built yet"))
        rows.setdefault(f, {}).setdefault(st, []).append(p["id"])
    out = ["| Family | Built and computed | Agents | Not built yet | Unverified source |", "|---|---|---|---|---|"]
    for f, d in rows.items():
        out.append(f"| {f} | {', '.join(d.get('built', [])) or '-'} | {', '.join(d.get('agent (weekly workflow)', [])) or '-'} | {', '.join(d.get('not built yet', [])) or '-'} | {', '.join(d.get('not built: unverified source', [])) or '-'} |")
    n = sum(len(v.get("built", [])) for v in rows.values()); a = sum(len(v.get("agent (weekly workflow)", [])) for v in rows.values())
    return f"{n} of 100 pillars are computed by code this week and {a} are scored by the event agents in the weekly workflow; the rest are listed below.\n\n" + "\n".join(out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--week", required=True); ap.add_argument("--backtests", action="store_true"); a = ap.parse_args()
    cfg = yaml.safe_load((ROOT / "config" / "portfolio_v2.yaml").read_text()); wd = ROOT / "runs" / a.week; wd.mkdir(parents=True, exist_ok=True)
    R = E2.run(week_dir=wd); pl = plan(R, cfg); R["extras"] = X2.compute(R, cfg, pl)
    bt = ROOT / "runs" / "v2_backtests_latest.json"
    if a.backtests or not bt.exists():
        res = {"rec07": rec07(cfg, R["C_usd"]), "rec04": rec04(cfg, R["C_usd"])}; bt.write_text(json.dumps(res, indent=1, default=str))
    res = json.loads(bt.read_text())
    R["L"].drop(columns=["name"]).to_csv(wd / "v2_line_values.csv"); R["LS"].round(2).to_csv(wd / "v2_line_scores.csv")
    R["XS"].round(3).to_csv(wd / "v2_exposure.csv"); R["FT"].round(3).to_csv(wd / "v2_fit.csv")
    (wd / "v2_plan.json").write_text(json.dumps(pl, indent=1))
    lp = ROOT / "runs" / "plan_log.csv"; row = pd.DataFrame([{"week": a.week, "asof": str(R["asof"].date()), "orders": json.dumps(pl["orders"]), "gate_pass": res["rec04"]["gate_pass"],
           "mix": json.dumps(R["mix"]), "top_X": json.dumps(R["XS"]["X"].sort_values(ascending=False).head(5).round(1).to_dict())}])
    (pd.concat([pd.read_csv(lp), row]).drop_duplicates("week", keep="last") if lp.exists() else row).to_csv(lp, index=False)
    (wd / "REPORT_V2.md").write_text(report(a.week, R, pl, res["rec07"], res["rec04"], cfg))
    (wd / "built_pillars.json").write_text(json.dumps(sorted(BUILT)))  # args.pillars for the weekly agent workflow
    print("wrote", wd / "REPORT_V2.md"); print(json.dumps(pl, indent=1)); print("gate:", res["rec04"]["gate_pass"])
