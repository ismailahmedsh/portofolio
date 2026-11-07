"""Pre-registered backtest: does acting weekly on pillar scores beat holding VT, for a US$2,500/month investor?
Only price-based families (A-E) can be rebuilt point-in-time; cost, valuation, macro and news families cannot.
Universe: today's 200 active ETFs, each eligible once it has 260 trading days of history (survivorship bias favours rotation)."""
import sys, json
from pathlib import Path
from statistics import NormalDist
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
import pillars as P

ROOT = Path(__file__).resolve().parents[1]
START, MONTHLY = "2015-01-02", 2500.0
COST_BPS, FIXED = 10, 1.70     # per side: spread plus commission (IBKR LSE tiered 0.05%, min US$1.70)
N_TRIALS = 8                   # 7 pre-registered; S8 added after S6 never triggered (cross-sectional rank cannot flag a broad fund)

def signals(adj):
    adj = adj[adj["SPY"].notna()]  # US trading days only; London-only days leave gaps that break rolling windows
    r = adj.pct_change(fill_method=None)
    f = {
        "r63": adj / adj.shift(63) - 1, "r126": adj / adj.shift(126) - 1, "r252": adj / adj.shift(252) - 1,
        "mom": adj.shift(21) / adj.shift(252) - 1, "sma200": adj / adj.rolling(200).mean() - 1,
        "vol": -r.rolling(252).std(), "mdd": adj / adj.rolling(252).max() - 1,
        "sh1": r.rolling(252).mean() / r.rolling(252).std(), "sh3": r.rolling(756, min_periods=500).mean() / r.rolling(756, min_periods=500).std(),
    }
    ok = adj.notna().rolling(260).sum() >= 260
    wk = lambda x: x.where(ok).resample("W-FRI").last()
    ranks = {k: wk(v).rank(axis=1, pct=True) for k, v in f.items()}
    comp = sum(ranks.values()) / len(ranks)
    return comp, wk(f["mom"]).rank(axis=1, pct=True)

def simulate(wret, target_fn, rebalance_every=1, delay=1, deposit_only=False):
    """wret: weekly returns (index = Fridays). target_fn(i) -> dict ticker->weight using info up to week i."""
    dates = wret.index; hold = {}; cash = 0.0; units = 0.0; nav = 1.0
    vals, navs, flows, trades, turnover = [], [], [], 0, 0.0
    last_month = None; pending = {}
    for i in range(1, len(dates)):
        # 1) mark to market over week i
        for t in list(hold):
            x = wret.iloc[i].get(t, np.nan); hold[t] *= (1 + (0 if np.isnan(x) else x))
        V = sum(hold.values()) + cash
        nav = nav * (V / prev_v) if i > 1 and prev_v > 0 else 1.0
        # 2) monthly deposit on the first Friday of a new month
        m = dates[i].to_period("M"); flow = 0.0
        if m != last_month:
            flow = MONTHLY; last_month = m; units += flow / nav; cash += flow
        # 3) rebalance or invest deposit using signal from week i - delay + 1 (delay=1 -> this Friday's close)
        j = i - delay + 1
        if j >= 1:
            tgt = target_fn(dates[j])
            if deposit_only:
                if cash > 0 and tgt:
                    t = max(tgt, key=tgt.get); c = cash * COST_BPS / 1e4 + FIXED
                    hold[t] = hold.get(t, 0) + cash - c; cash = 0; trades += 1; turnover += flow
            elif tgt and ((i % rebalance_every == 0) or cash > 0):
                if not (i % rebalance_every == 0):  # deposit only: spread over current targets
                    tgt = {t: w for t, w in tgt.items()} if not hold else {t: v / sum(hold.values()) for t, v in hold.items()}
                total = sum(hold.values()) + cash
                new = {t: total * w for t, w in tgt.items()}
                tv = sum(abs(new.get(t, 0) - hold.get(t, 0)) for t in set(new) | set(hold))
                n = sum(1 for t in set(new) | set(hold) if abs(new.get(t, 0) - hold.get(t, 0)) > 1)
                c = tv * COST_BPS / 1e4 + FIXED * n
                scale = (total - c) / total
                hold = {t: v * scale for t, v in new.items() if v > 0}; cash = 0
                trades += n; turnover += tv
        V = sum(hold.values()) + cash; prev_v = V
        vals.append(V); navs.append(nav * (V / (V - flow)) if V - flow > 0 and i > 1 else nav); flows.append(flow)
    idx = dates[1:]
    return pd.Series(vals, idx), pd.Series(flows, idx), trades, turnover

def xirr(vals, flows):
    cf = [(-f, d) for d, f in flows.items() if f] + [(vals.iloc[-1], vals.index[-1])]
    t0 = cf[0][1]
    def npv(r): return sum(a / (1 + r) ** ((d - t0).days / 365.25) for a, d in cf)
    lo, hi = -0.9, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid) > 0: lo = mid
        else: hi = mid
    return mid

def twr(vals, flows):
    r = (vals - flows) / vals.shift(1) - 1
    return r.dropna()

def stats(name, vals, flows, trades, turnover):
    r = twr(vals, flows); yrs = len(r) / 52
    navs = (1 + r).cumprod()
    out = {"strategy": name, "final_value": round(vals.iloc[-1]), "contributed": round(flows.sum()),
           "money_weighted_return": round(xirr(vals, flows) * 100, 2),
           "time_weighted_cagr": round((navs.iloc[-1] ** (1 / yrs) - 1) * 100, 2),
           "max_drawdown": round((navs / navs.cummax() - 1).min() * 100, 1),
           "volatility": round(r.std() * np.sqrt(52) * 100, 1),
           "sharpe": round(r.mean() / r.std() * np.sqrt(52), 3),
           "trades_per_year": round(trades / yrs, 1), "turnover_x_per_year": round(turnover / vals.mean() / yrs, 2),
           "cagr_2015_2019": None, "cagr_2020_2026": None}
    for k, a, b in [("cagr_2015_2019", "2015", "2019"), ("cagr_2020_2026", "2020", "2026")]:
        x = (1 + r.loc[a:b]).prod() ** (52 / len(r.loc[a:b])) - 1; out[k] = round(x * 100, 2)
    return out, r

def dsr(sr_best_weekly, sr_trials_weekly, n_obs, skew, kurt):
    nd = NormalDist(); g = 0.5772156649
    v = np.var(sr_trials_weekly, ddof=1); N = len(sr_trials_weekly)
    sr0 = np.sqrt(v) * ((1 - g) * nd.inv_cdf(1 - 1 / N) + g * nd.inv_cdf(1 - 1 / (N * np.e)))
    z = (sr_best_weekly - sr0) * np.sqrt(n_obs - 1) / np.sqrt(1 - skew * sr_best_weekly + (kurt - 1) / 4 * sr_best_weekly ** 2)
    return nd.cdf(z), sr0

if __name__ == "__main__":
    d = P.load(); u = P.universe()
    adj = d["adj"][list(u.ticker) + ["BIL"] if "BIL" not in u.ticker.values else list(u.ticker)]
    comp, mom = signals(adj)
    adj = adj[adj["SPY"].notna()]
    wk = adj.resample("W-FRI").last(); wret = wk.pct_change(fill_method=None).loc[START:]
    comp, mom = comp.loc[START:], mom.loc[START:]
    def topn(sig, n): return lambda dt: {t: 1 / n for t in sig.loc[dt].dropna().nlargest(n).index}
    vt_only = lambda dt: {"VT": 1.0}
    state = {"in": True}
    def vt_guard(dt):  # sell VT to T-bills when its composite rank < 30th pct, buy back above 50th
        x = comp.loc[dt].get("VT", np.nan)
        if state["in"] and x < .30: state["in"] = False
        elif not state["in"] and x > .50: state["in"] = True
        return {"VT": 1.0} if state["in"] else {"BIL": 1.0}
    vtd = adj["VT"][adj["SPY"].notna()].dropna()
    vt_trend = ((vtd < vtd.rolling(200).mean()) & (vtd.shift(21) / vtd.shift(252) - 1 < 0)).resample("W-FRI").last()
    vt_up = (vtd > vtd.rolling(200).mean()).resample("W-FRI").last()
    st2 = {"in": True}
    def vt_abs(dt):
        if st2["in"] and bool(vt_trend.get(dt, False)): st2["in"] = False
        elif not st2["in"] and bool(vt_up.get(dt, False)): st2["in"] = True
        return {"VT": 1.0} if st2["in"] else {"BIL": 1.0}
    runs = {
        "S0 Hold VT, deposit monthly (benchmark)": (vt_only, {}),
        "S1 Weekly switch: top 5 by composite": (topn(comp, 5), {}),
        "S2 Monthly switch: top 5 by composite": (topn(comp, 5), {"rebalance_every": 4}),
        "S3 Weekly switch: top 5 by 12-1 momentum": (topn(mom, 5), {}),
        "S4 Weekly switch: top 1 by composite": (topn(comp, 1), {}),
        "S5 Never sell; each deposit to top-ranked ETF": (topn(comp, 1), {"deposit_only": True}),
        "S6 Hold VT but sell to T-bills on weak score": (vt_guard, {}),
        "S8 Hold VT but sell to T-bills on own downtrend": (vt_abs, {}),
    }
    rows, rets = [], {}
    for name, (fn, kw) in runs.items():
        state["in"] = True; st2["in"] = True
        vals, flows, tr, to = simulate(wret, fn, **kw)
        s, r = stats(name, vals, flows, tr, to); rows.append(s); rets[name] = r
        vals2, flows2, tr2, to2 = simulate(wret, fn, delay=2, **kw) if name != list(runs)[0] else (vals, flows, tr, to)
        s2, _ = stats(name, vals2, flows2, tr2, to2); s["money_weighted_return_1w_delay"] = s2["money_weighted_return"]
        print(name, s["money_weighted_return"], s["final_value"], file=sys.stderr)
    # 80/20 core-satellite from weekly returns, rebalanced weekly at no extra cost (optimistic)
    cs = .8 * rets[list(runs)[0]] + .2 * rets["S1 Weekly switch: top 5 by composite"]
    navcs = (1 + cs).cumprod(); yrs = len(cs) / 52
    rows.append({"strategy": "S7 80% VT + 20% weekly top-5 (return blend)", "time_weighted_cagr": round((navcs.iloc[-1] ** (1 / yrs) - 1) * 100, 2),
                 "max_drawdown": round((navcs / navcs.cummax() - 1).min() * 100, 1), "sharpe": round(cs.mean() / cs.std() * np.sqrt(52), 3)})
    srs = [rets[k].mean() / rets[k].std() for k in rets]
    best = max(rets, key=lambda k: rets[k].mean() / rets[k].std())
    rb = rets[best]; p, sr0 = dsr(rb.mean() / rb.std(), srs, len(rb), rb.skew(), rb.kurt() + 3)
    res = {"period": f"{wret.index[1].date()} to {wret.index[-1].date()}", "monthly_deposit": MONTHLY,
           "cost_model": f"{COST_BPS} bps per side plus US${FIXED} per trade", "trials": N_TRIALS,
           "best_by_sharpe": best, "deflated_sharpe_probability": round(p, 3), "results": rows}
    from datetime import date
    res["run_date"] = str(date.today())
    for out in [ROOT / "runs" / f"backtest_{date.today()}.json", ROOT / "runs" / "backtest_latest.json"]:
        out.write_text(json.dumps(res, indent=1))
    print(pd.DataFrame(rows).set_index("strategy").to_string())
    print("best:", best, "DSR prob:", round(p, 3))
