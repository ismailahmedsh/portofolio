"""Weekly run for engine v2: scores, the monthly deposit plan, REC07 (mix comparison), REC04 (tilt gate), pick log, report.
Usage: python3 -I v2/run_v2.py --week 2026-W46 [--backtests]"""
import argparse, json, sys
from pathlib import Path
from statistics import NormalDist
import numpy as np, pandas as pd, yaml
sys.path.insert(0, str(Path(__file__).parent)); sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import engine_v2 as E2
sys.path.insert(0, str(Path(__file__).parent))
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
    n_orders = 1 if C < 2 * 680 else 2  # never more than 2 orders (allocation 3c)
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

# ---------------- backtests (shared exposure module, point-in-time) ----------------
import exposure as XP
SLEEVE_PROXY = {"world": None, "sp500": "SPY", "ndx100": "QQQ", "exus": "EFA", "eimi": "EEM"}  # US-listed, dividend-adjusted
BAND_MAX = {"exus": 0.10, "eimi": 0.075}  # tilt candidates with long history; factor sleeves excluded (no passing splice)
TRIAL_IR_SPREAD = 0.25  # assumed spread of annual information ratios across trials (disclosed in the report)

def monthly():
    c = pd.read_pickle(CACHE / "v2_close_usd.pkl"); m = c.resample("ME").last().pct_change(fill_method=None)
    asof = c["VT"].dropna().index[-1]; dt = asof + pd.offsets.MonthEnd(0) if asof.is_month_end else asof - pd.offsets.MonthEnd(1)
    f = XP.factors(pd.read_pickle(CACHE / "v2_french.pkl")); m = m.loc[:dt]; W = XP.world_reference(m, f)
    R = pd.DataFrame({k: (W if v is None else m[v]) for k, v in SLEEVE_PROXY.items()}).loc[:dt]
    return R, f, W, asof

def sim(R, targets_fn, monthly_usd, start, end=None, comm=1.70, cap_sleeves=()):
    """Monthly deposits routed to the sleeve furthest below target (one order), commission and 10 bps spread.
    targets_fn(i, dates) -> target weights. Sleeves in cap_sleeves get at most 2 of any 12 deposits."""
    r = R.loc[start:end]; dates = r.index; hold = {k: 0.0 for k in R.columns}; vals, flows, hist = [], [], []
    for i, dt in enumerate(dates):
        for k in hold: hold[k] *= 1 + (0 if pd.isna(r.loc[dt, k]) else r.loc[dt, k])
        tg = targets_fn(i, dates); V = sum(hold.values())
        gaps = sorted(((tg.get(k, 0) * (V + monthly_usd) - hold[k], k) for k in tg), reverse=True)
        for g, k in gaps:
            if k in cap_sleeves and sum(1 for x in hist[-11:] if x == k) >= 2: continue
            break
        hold[k] += monthly_usd - comm - monthly_usd * SPREAD_BPS / 1e4; hist.append(k)
        vals.append(sum(hold.values())); flows.append(monthly_usd)
    return pd.Series(vals, dates), pd.Series(flows, dates)

def xirr(cf):
    t0 = cf[0][1]; lo, hi = -0.95, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2; npv = sum(a / (1 + mid) ** ((d - t0).days / 365.25) for a, d in cf); lo, hi = (mid, hi) if npv > 0 else (lo, mid)
    return mid

def metrics(vals, flows, periods):
    r = ((vals - flows) / vals.shift(1) - 1).dropna(); nav = (1 + r).cumprod(); yrs = len(r) / 12
    out = {"final": round(vals.iloc[-1]), "paid_in": round(flows.sum()), "mwr": round(xirr([(-f, d) for d, f in flows.items()] + [(vals.iloc[-1], vals.index[-1])]) * 100, 2),
           "twr": round((nav.iloc[-1] ** (1 / yrs) - 1) * 100, 2), "max_dd": round((nav / nav.cummax() - 1).min() * 100, 1),
           "worst_year": round(r.groupby(r.index.year).apply(lambda x: (1 + x).prod() - 1).min() * 100, 1)}
    for a, b in periods:
        v = vals.loc[a:b]; f = flows.loc[a:b]
        if len(v) < 12: out[f"mwr_{a}_{b}"] = None; continue
        prev = vals.loc[:v.index[0]].iloc[:-1]; start_val = prev.iloc[-1] if len(prev) else 0.0
        cf = ([(-start_val, v.index[0] - pd.offsets.MonthEnd(1))] if start_val > 0 else []) + [(-x, d) for d, x in f.items()] + [(v.iloc[-1], v.index[-1])]
        out[f"mwr_{a}_{b}"] = round(xirr(cf) * 100, 2)
    return out, r

def rec07(cfg, monthly_usd):
    R, f, W, asof = monthly(); start = "2003-01-31"
    per = [("2003", "2007"), ("2008", "2014"), ("2015", "2019"), ("2020", "2026")]
    owner = {k: v["target"] for k, v in cfg["strategic_mix"].items()}
    mixes = {"Your mix " + "/".join(f"{v*100:g}" for v in owner.values()): owner, "100% world": {"world": 1.0}, "100% S&P 500": {"sp500": 1.0}, "100% Nasdaq-100": {"ndx100": 1.0},
             "80/10/10": {"world": .8, "sp500": .1, "ndx100": .1}, "60/25/15": {"world": .6, "sp500": .25, "ndx100": .15}, "50/30/20": {"world": .5, "sp500": .3, "ndx100": .2}}
    rows = []
    for n, w in mixes.items():
        v, fl = sim(R[["world", "sp500", "ndx100"]], lambda i, d, w=w: w, monthly_usd, start); o, _ = metrics(v, fl, per); rows.append({"mix": n, **o})
    return {"period": f"{start[:7]} to {asof.date()}", "periods": per,
            "proxies": "world reference (Ken French Developed market + T-bill to 2008-02, ACWI to 2008-05, then VT), SPY for the S&P 500, QQQ for the Nasdaq-100; US-listed, dividend-adjusted, before UAE withholding",
            "rows": rows}

def rec04(cfg, monthly_usd):
    R, f, W, asof = monthly(); owner = {k: v["target"] for k, v in cfg["strategic_mix"].items()}; lim = cfg["tilt_limits"]
    cands = list(BAND_MAX); start = "2008-01-31"; dates = R.loc[start:].index
    # point-in-time measures and X for every month (world measures recomputed at each date)
    Xh, FIT4 = {c: {} for c in cands}, {c: {} for c in cands}
    def ex_pp(e, ew, priors): return XP.exp_excess(e, ew, priors=priors)
    for dt in R.loc["2005-12-31":].index:
        ew = XP.raw_measures(W, W, f, dt); es = {k: XP.raw_measures(R[k].dropna(), W, f, dt) for k in list(owner) + cands}
        if any("FAC05" not in es[k] for k in owner): continue
        bP = sum(w * es[k]["FAC05"] for k, w in owner.items())
        for priors in (True, False):
            EP = sum(w * ex_pp(es[k], ew, priors) for k, w in owner.items())
            for c in cands:
                if "FAC05" not in es[c]: continue
                if priors:
                    sc = XP.score(es[c], ew)
                    Xh[c][dt] = sc["X"] if sc["risk_available"] else np.nan  # a sleeve starts only once its risk family exists (120 months)
                FIT4[c][(dt, priors)] = XP.fit04(ex_pp(es[c], ew, priors), es[c]["FAC05"], EP, bP)
    Xh = pd.DataFrame(Xh)
    Xs = Xh.rolling(3, min_periods=3).mean()  # X used for targets: mean of the last 3 month-end values
    def make_targets(priors, lag):
        state = {"t": {c: 0.0 for c in cands}, "q": None, "prev_ok": {c: False for c in cands}}
        def fn(i, ds):
            j = i - lag
            if j < 0: return dict(owner)
            d = ds[j]
            if d.month in (3, 6, 9, 12) and state["q"] != d:
                state["q"] = d; new = {}
                for c in cands:
                    x = Xs[c].get(d, np.nan); a = FIT4[c].get((d, priors), np.nan)
                    ok = (not pd.isna(x)) and x >= 55 and (not pd.isna(a)) and a > 0
                    tgt = BAND_MAX[c] * float(np.clip((x - 55) / 15, 0, 1)) if ok and state["prev_ok"][c] else 0.0
                    tgt = tgt if tgt >= 0.05 else 0.0
                    old = state["t"][c]; ch = tgt - old
                    if abs(ch) < 0.025: tgt = old  # hysteresis: changes below 2.5 points are ignored
                    elif abs(ch) > 0.05: tgt = old + np.sign(ch) * 0.05  # at most 5 points a quarter
                    new[c] = tgt; state["prev_ok"][c] = ok
                tot = sum(new.values())
                if tot > lim["total_tilt_max"]: new = {c: v * lim["total_tilt_max"] / tot for c, v in new.items()}
                state["t"] = new
            tot = sum(state["t"].values()); out = {k: v * (1 - tot) for k, v in owner.items()}; out.update({c: v for c, v in state["t"].items() if v > 0}); return out
        return fn
    per = [("2008", "2014"), ("2015", "2019"), ("2020", "2026")]
    vb, fb = sim(R, lambda i, d: owner, monthly_usd, start); ob, rb = metrics(vb, fb, per)
    res = {"rule": "Quarterly: a sleeve qualifies when its X (3-month average) is 55 or more at two consecutive quarter-ends and its expected alpha against your mix is positive; target = band max x clip((X - 55) / 15), 0 or at least 5%, changes of 2.5 to 5 points a quarter, total tilt at most 15%, at most 2 of any 12 deposits. Candidates: developed ex-US (EFA, band 10%), emerging markets (EEM, band 7.5%). Factor and small-cap sleeves excluded: no proxy passes the splice test.",
           "period": f"{start[:7]} to {asof.date()}", "periods": per, "owner_mix": ob, "n_trials": N_TRIALS, "trial_ir_spread_assumed": TRIAL_IR_SPREAD, "variants": {}}
    nd = NormalDist(); g = .5772156649; gate = True
    for priors in (True, False):
        for lag, name in [(0, "same month"), (1, "one month later")]:
            v, fl = sim(R, make_targets(priors, lag), monthly_usd, start, cap_sleeves=tuple(cands)); o, rt = metrics(v, fl, per)
            act = (rt - rb.reindex(rt.index)).dropna(); ir = act.mean() / act.std() if act.std() > 0 else 0.0
            sr0 = TRIAL_IR_SPREAD / np.sqrt(12) * ((1 - g) * nd.inv_cdf(1 - 1 / N_TRIALS) + g * nd.inv_cdf(1 - 1 / (N_TRIALS * np.e)))
            den = 1 - act.skew() * ir + (act.kurt() + 2) / 4 * ir ** 2
            dsr = nd.cdf((ir - sr0) * np.sqrt(len(act) - 1) / np.sqrt(den)) if den > 0 and act.std() > 0 else 0.0
            beats = all((o.get(f"mwr_{a}_{b}") or -99) - (ob.get(f"mwr_{a}_{b}") or 99) >= 0.25 for a, b in per)  # DECISION_RULES_V2: at least 0.25 points
            tilt_months = int(sum(1 for i in range(len(rt)) if True))
            key = f"{'with priors' if priors else 'priors = 0'}, {name}"
            res["variants"][key] = {**o, "info_ratio_annual": round(ir * np.sqrt(12), 2), "deflated_prob": round(dsr, 3), "beats_mix_every_period": beats}
            if priors: gate = gate and beats and dsr > 0.95
    res["gate_pass"] = bool(gate)
    res["latest_X"] = {c: (round(float(Xs[c].dropna().iloc[-1]), 1) if Xs[c].notna().any() else None) for c in cands}
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
    w(f"{r07['period']}, deposits of US${R['C_usd']:,.2f} a month routed to the sleeve furthest below target, US$1.70 commission and {SPREAD_BPS} bps spread per buy. Proxies: {r07['proxies']}. Per-period returns are money-weighted, starting from the balance at the start of the period. Past leadership is not a forecast.\n")
    per = r07["periods"]
    w("| Mix | Final value | Paid in | Return on your money | Time-weighted | Worst drop | Worst year | " + " | ".join(f"{a}-{b}" for a, b in per) + " |\n|" + "---|" * (7 + len(per)))
    for r in r07["rows"]: w(f"| {r['mix']} | US${r['final']:,} | US${r['paid_in']:,} | {r['mwr']:.1f}% | {r['twr']:.1f}% | {r['max_dd']:.0f}% | {r['worst_year']:.0f}% | " + " | ".join(f"{r.get(f'mwr_{a}_{b}'):.1f}%" if r.get(f'mwr_{a}_{b}') is not None else "n/a" for a, b in per) + " |")
    w("\n## May scores move money yet? (REC04 gate)\n")
    w(f"Rule tested: {r04['rule']} Period {r04['period']}, against your mix, {r04['n_trials']} trials counted. The deflated probability assumes the information ratios of the {r04['n_trials']} trials spread by {r04['trial_ir_spread_assumed']} a year; this is an assumption, not a measurement.\n")
    per = r04["periods"]
    w("| Variant | Return on your money | " + " | ".join(f"{a}-{b}" for a, b in per) + " | Information ratio | Deflated probability | Beats your mix by 0.25+ points every period |\n|" + "---|" * (5 + len(per)))
    ob = r04["owner_mix"]; w(f"| Your mix (yardstick) | {ob['mwr']:.1f}% | " + " | ".join(f"{ob.get(f'mwr_{a}_{b}'):.1f}%" for a, b in per) + " | | | |")
    for k, o in r04["variants"].items(): w(f"| Tilts, {k} | {o['mwr']:.1f}% | " + " | ".join(f"{o.get(f'mwr_{a}_{b}'):.1f}%" for a, b in per) + f" | {o['info_ratio_annual']:.2f} | {o['deflated_prob']:.2f} | {'yes' if o['beats_mix_every_period'] else 'no'} |")
    w(f"\nLatest smoothed X: " + ", ".join(f"{k} {v}" for k, v in r04["latest_X"].items()) + ".\n")
    w(f"**Gate: {'PASSED, tilts may be proposed for your confirmation' if r04['gate_pass'] else 'not passed, so scores stay display-only and every deposit follows your mix'}.** With priors set to 0, expected alpha against your mix is exactly zero, so the prior-free variants can never qualify and equal your mix: any qualification comes from the assumed priors, not from estimated returns. Only the with-priors variants decide the gate.\n")
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
    sp = R.get("splices", {})
    w("\n## Data notes\n\n- Splice tests (ELG07: 24+ months overlap, correlation 0.98+, gap 50 bps or less): " + "; ".join(f"{k[:-2]} {'used' if v['used'] else 'not used'} (correlation {v['corr']:.3f}, gap {v['gap_bps']:.0f} bps)" for k, v in sp.items()) + ". Where a splice fails, the exposure view uses the line's own London history.\n- Prices: Yahoo Finance via yfinance, LSE lines converted to USD; unofficial and for personal use.\n- Fund size is missing from Yahoo for " + str(int(L['DUR01'].isna().sum())) + " lines (for example CSPX, CNDX); it is listed as missing, not held against them.\n- Tracking difference (CST02) fails closed until fee history is collected, so line choice uses current fee plus US withholding.\n- Same-index groups come from the index named in each fund's name, confirmed by return correlation.")
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
    return f"{n} of 100 pillars have code that computes them this week (some as record or context with weight 0, as the spec defines) and {a} are scored by the event agents in the weekly workflow; the rest are listed below with the reason.\n\n" + "\n".join(out)

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
