import yfinance as yf, pandas as pd, numpy as np, warnings
warnings.filterwarnings("ignore")
pd.set_option("display.width",200)
tick = ["SPY","VTI","VT","ACWI","AGG","BIL","BND","TLT","IEI","SHY","DBC","GLD","IJS","XEQT.TO","VEQT.TO","ZAG.TO","XAW.TO"]
m = yf.download(tick, start="2006-01-01", interval="1mo", auto_adjust=True, progress=False, threads=False)["Close"]
m = m[m.index < "2026-11-01"]   # drop partial Nov 2026
m.to_csv("monthly_adj_close.csv")
print("monthly rows", len(m), "last", m.index[-1].date())
print("first valid:", {c: str(m[c].first_valid_index().date()) for c in m.columns})

def stats(r, name):
    r = r.dropna()
    g = (1+r).cumprod()
    yrs = len(r)/12
    cagr = g.iloc[-1]**(1/yrs)-1
    dd = (g/g.cummax()-1).min()
    vol = r.std()*np.sqrt(12)
    cal = {y: (1+r[r.index.year==y]).prod()-1 for y in [2008,2020,2022,2025]}
    return dict(name=name, start=str(r.index[0].date()), end=str(r.index[-1].date()), CAGR=round(cagr*100,2), MaxDD=round(dd*100,1), Vol=round(vol*100,1), **{f"CY{y}":round(v*100,1) for y,v in cal.items()})

def sma_rule(eq, defn, n=10, cost=0.001, label=""):
    px = m[eq].dropna()
    sma = px.rolling(n).mean()
    sig = (px > sma).astype(int).shift(1)  # decide at month-end, hold next month
    r_eq = px.pct_change(); r_def = m[defn].reindex(px.index).pct_change().fillna(0) if defn!="CASH0" else pd.Series(0.0,index=px.index)
    r = pd.Series(np.where(sig==1, r_eq, r_def), index=px.index)
    sw = sig.diff().abs().fillna(0)
    r = r - sw*cost
    r = r[sig.notna()]
    s = stats(r, f"{eq} SMA{n} -> {defn} {label}")
    s["switches"] = int(sw.sum()); s["months_out"] = int((sig==0).sum())
    bh = stats(r_eq[sig.notna()], f"{eq} buy&hold")
    return s, bh, sig, px, sma

def mom_rule(eq, defn, n=12, cost=0.001):
    px = m[eq].dropna()
    bil = m["BIL"].reindex(px.index)
    mom = px.pct_change(n) - bil.pct_change(n).fillna(0)
    sig = (mom > 0).astype(int).shift(1)
    sig[mom.shift(1).isna()] = np.nan
    r_eq = px.pct_change(); r_def = m[defn].reindex(px.index).pct_change().fillna(0) if defn!="CASH0" else pd.Series(0.0,index=px.index)
    r = pd.Series(np.where(sig==1, r_eq, r_def), index=px.index)
    sw = sig.diff().abs().fillna(0); r = r - sw*cost; r = r[sig.notna()]
    s = stats(r, f"{eq} ABSMOM{n} -> {defn}"); s["switches"]=int(sw.sum()); s["months_out"]=int((sig==0).sum())
    return s, sig

rows=[]
for eq, defs in [("SPY",["CASH0","BIL","AGG"]),("VTI",["BIL","AGG"]),("VT",["BIL","AGG"]),("ACWI",["BIL","AGG"]),("XEQT.TO",["CASH0","ZAG.TO"]),("VEQT.TO",["CASH0","ZAG.TO"]),("XAW.TO",["ZAG.TO"])]:
    for d in defs:
        s,bh,sig,px,sma = sma_rule(eq,d); rows.append(s)
        if d==defs[0]: rows.append(bh)
        if d in ("BIL","ZAG.TO","AGG"):
            ms,msig = mom_rule(eq,d); rows.append(ms)
df = pd.DataFrame(rows); print(df.to_string())
df.to_csv("overlay_results.csv", index=False)

# Episode detail: signal state at each month-end around 2020, 2022, 2025 for SPY and VT and XEQT
for eq in ["SPY","VT","XEQT.TO"]:
    px = m[eq].dropna(); sma = px.rolling(10).mean(); st = (px>sma)
    print(f"\n{eq} month-end close vs SMA10 (True=in equity next month):")
    for per in [("2020-01-01","2020-08-01"),("2021-11-01","2023-03-01"),("2024-12-01","2025-09-01")]:
        seg = pd.DataFrame({"close":px, "sma10":sma, "above":st}).loc[per[0]:per[1]]
        print(seg.round(2).to_string())

# Daily 200-day SMA crossings for SPY and VT around tariff crash
d = yf.download(["SPY","VT"], start="2024-01-01", end="2025-12-31", interval="1d", auto_adjust=True, progress=False, threads=False)["Close"]
for eq in ["SPY","VT"]:
    px = d[eq].dropna(); sma=px.rolling(200).mean(); ab=(px>sma).astype(int); ch=ab.diff()
    cross = ch[ch!=0].loc["2025-01-01":"2025-12-31"]
    print(f"\n{eq} daily 200-day SMA crossings 2025:")
    for dt,v in cross.items(): print(" ", dt.date(), "ABOVE" if v>0 else "BELOW", "close", round(px[dt],2), "sma", round(sma[dt],2))
    peak = px.loc["2025-01-01":"2025-04-30"].max(); trough = px.loc["2025-03-01":"2025-04-30"].min()
    print("  Feb-Apr 2025 peak->trough:", round((trough/peak-1)*100,1), "% ; peak date", px.loc["2025-01-01":"2025-04-30"].idxmax().date(), "trough date", px.loc["2025-03-01":"2025-04-30"].idxmin().date())
    # GEM-style 12m abs momentum at month ends
