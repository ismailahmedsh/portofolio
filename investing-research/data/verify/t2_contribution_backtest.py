"""Task 2: contribution-aware backtest, plain pandas (no backtest library).
Monthly CAD 1,000 contribution on the first trading day of each month.
(a) 100% XEQT.TO; (b) DIY 45% XUU.TO / 30% XEF.TO / 10% XEC.TO / 15% XIC.TO, rebalanced only with contributions
(new cash goes to the most-underweight sleeves; no selling); (c) VT in USD, CAD converted at FRED DEXCAUS (CAD per USD).
Total return via yfinance 'Adj Close' (dividends reinvested, pre-tax, no withholding tax, no commissions, fractional units).
Metrics: ending value, total contributed, XIRR (money-weighted), TWR CAGR (unit-value chain), max drawdown of the TWR index,
max drawdown of account value vs. its running peak (contribution-inclusive).
"""
import sys, datetime as dt, numpy as np, pandas as pd
D = "/home/user/portofolio/investing-research/data/verify/downloads"
OUT = "/home/user/portofolio/investing-research/data/verify/t2_backtest_output.md"
CONTRIB = 1000.0

def adj(t):
    df = pd.read_csv(f"{D}/{t.replace('.','_')}_daily.csv", index_col=0, parse_dates=True)
    s = df["Adj Close"].astype(float).dropna(); s.name = t; return s

def fx_fred():
    f = pd.read_csv(f"{D}/fred_DEXCAUS_via_webfetch.csv", index_col=0, parse_dates=True)["DEXCAUS"]
    return pd.to_numeric(f, errors="coerce").dropna()

def xirr(dates, flows):
    """Money-weighted annual return; flows negative = contribution, final positive = ending value."""
    t = np.array([(d - dates[0]).days / 365.25 for d in dates]); f = np.array(flows)
    npv = lambda r: np.sum(f / (1 + r) ** t)
    lo, hi = -0.99, 10.0
    if npv(lo) * npv(hi) > 0: return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0: hi = mid
        else: lo = mid
    return (lo + hi) / 2

def maxdd(series):
    peak = series.cummax(); return float(((series / peak) - 1).min())

def run(prices, weights, fx=None, label=""):
    """prices: DataFrame of adj closes (in native ccy); weights: dict ticker->target; fx: Series CAD per USD or None."""
    px = prices.dropna()
    start = px.index.min()
    months = pd.date_range(start, px.index.max(), freq="MS")
    cdates = [px.index[px.index >= m][0] for m in months if (px.index >= m).any()]
    cdates = sorted(set(cdates)); cdates = [d for d in cdates if d > start or d == start]
    units = {t: 0.0 for t in weights}
    fxs = fx.reindex(px.index, method="ffill") if fx is not None else pd.Series(1.0, index=px.index)
    val_cad = pd.Series(0.0, index=px.index); unit_idx = []; nav_units = 0.0; unit_price = 100.0
    flows_d, flows_v = [], []
    cset = set(cdates)
    for d in px.index:
        p = px.loc[d]; rate = float(fxs.loc[d])
        v = sum(units[t] * p[t] for t in weights) * rate
        if d in cset:
            if nav_units > 0: unit_price = v / nav_units
            # allocate contribution to underweight sleeves (contribution-only rebalancing)
            total_after = v + CONTRIB
            cur = {t: units[t] * p[t] * rate for t in weights}
            need = {t: max(total_after * w - cur[t], 0.0) for t, w in weights.items()}
            s = sum(need.values())
            alloc = {t: CONTRIB * need[t] / s for t in weights} if s > 0 else {t: CONTRIB * w for t, w in weights.items()}
            for t in weights:
                units[t] += (alloc[t] / rate) / p[t]
            nav_units += CONTRIB / unit_price
            flows_d.append(d); flows_v.append(-CONTRIB)
            v = sum(units[t] * p[t] for t in weights) * rate
        val_cad.loc[d] = v
        unit_idx.append(v / nav_units if nav_units > 0 else unit_price)
    unit_idx = pd.Series(unit_idx, index=px.index)
    end_d = px.index.max(); end_v = float(val_cad.iloc[-1])
    flows_d.append(end_d); flows_v.append(end_v)
    contributed = CONTRIB * len(cdates)
    yrs = (end_d - cdates[0]).days / 365.25
    twr = (unit_idx.iloc[-1] / unit_idx.loc[cdates[0]]) ** (1 / yrs) - 1
    return dict(label=label, start=str(cdates[0].date()), end=str(end_d.date()), months=len(cdates),
                contributed=contributed, ending=end_v, gain=end_v - contributed,
                xirr=xirr(flows_d, flows_v), twr_cagr=twr, maxdd_twr=maxdd(unit_idx), maxdd_value=maxdd(val_cad),
                final_weights={t: round(units[t] * px.loc[end_d, t] * float(fxs.loc[end_d]) / end_v, 3) for t in weights})

if __name__ == "__main__":
    fx = fx_fred()
    px_ca = pd.concat([adj(t) for t in ["XEQT.TO", "XUU.TO", "XEF.TO", "XEC.TO", "XIC.TO"]], axis=1)
    vt = adj("VT").to_frame()
    diy = {"XUU.TO": .45, "XEF.TO": .30, "XEC.TO": .10, "XIC.TO": .15}
    rows = []
    # Window 1: XEQT era (common start of all five = XEQT inception 2019-08-14)
    w1 = px_ca.dropna()
    rows.append(run(w1[["XEQT.TO"]], {"XEQT.TO": 1.0}, label="A: 100% XEQT.TO (CAD)"))
    rows.append(run(w1[list(diy)], diy, label="B: DIY 45/30/10/15 (CAD), XEQT window"))
    rows.append(run(vt[vt.index >= w1.index.min()], {"VT": 1.0}, fx=fx, label="C: 100% VT (USD->CAD at FRED DEXCAUS), XEQT window"))
    # Window 2: DIY era (common start of XUU/XEF/XEC/XIC = XUU inception 2015-02-20)
    w2 = px_ca[list(diy)].dropna()
    rows.append(run(w2, diy, label="B2: DIY 45/30/10/15 (CAD), from XUU inception"))
    rows.append(run(vt[vt.index >= w2.index.min()], {"VT": 1.0}, fx=fx, label="C2: 100% VT (USD->CAD), from 2015-02"))
    rows.append(run(w2[["XIC.TO"]], {"XIC.TO": 1.0}, label="D2: 100% XIC.TO (CAD), from 2015-02 (reference)"))
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [f"# Contribution backtest output ({ts})", "", "Monthly CAD 1,000 on first trading day of each month; yfinance Adj Close (pre-tax, no FWT, no commissions); FX = FRED DEXCAUS ffill.", "",
             "| Portfolio | Start | End | Months | Contributed CAD | Ending CAD | Gain CAD | XIRR (MWR) | TWR CAGR | MaxDD (TWR index) | MaxDD (account value) | Final weights |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['label']} | {r['start']} | {r['end']} | {r['months']} | {r['contributed']:,.0f} | {r['ending']:,.0f} | {r['gain']:,.0f} | {r['xirr']*100:.2f}% | {r['twr_cagr']*100:.2f}% | {r['maxdd_twr']*100:.1f}% | {r['maxdd_value']*100:.1f}% | {r['final_weights']} |")
    lines += ["", f"Data starts (Adj Close first date): " + "; ".join(f"{t} {px_ca[t].dropna().index.min().date()}" for t in px_ca.columns) + f"; VT {vt.index.min().date()}; FX DEXCAUS {fx.index.min().date()}..{fx.index.max().date()}"]
    open(OUT, "w").write("\n".join(lines) + "\n"); print("\n".join(lines))
