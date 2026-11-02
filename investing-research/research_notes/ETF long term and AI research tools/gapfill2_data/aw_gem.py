import yfinance as yf, pandas as pd, numpy as np, warnings
warnings.filterwarnings("ignore"); pd.set_option("display.width",220)
m = pd.read_csv("monthly_adj_close.csv", index_col=0, parse_dates=True)
extra = yf.download(["VEU","RPAR","SPY"], start="2006-01-01", interval="1mo", auto_adjust=True, progress=False, threads=False)["Close"]
extra = extra[extra.index < "2026-11-01"]
m = m.join(extra[["VEU","RPAR"]])
r = m.pct_change()

def port(weights, start, end=None, rebal="M"):
    w = pd.Series(weights); rr = r[w.index].loc[start:end].dropna()
    return (rr*w).sum(axis=1)   # monthly rebalanced

def stats(x, name):
    x = x.dropna(); g=(1+x).cumprod(); yrs=len(x)/12
    out = dict(name=name, start=str(x.index[0].date()), end=str(x.index[-1].date()), CAGR=round((g.iloc[-1]**(1/yrs)-1)*100,2), MaxDD=round(((g/g.cummax())-1).min()*100,1), Vol=round(x.std()*np.sqrt(12)*100,1))
    for y in [2008,2020,2022,2025]:
        s = x[x.index.year==y]; out[f"CY{y}"] = round(((1+s).prod()-1)*100,1) if len(s)==12 else None
    worst = (1+x).groupby(x.index.year).prod()-1
    worst = worst[[len(x[x.index.year==y])==12 for y in worst.index]]
    out["WorstYr"] = f"{round(worst.min()*100,1)} ({worst.idxmin()})"
    return out

ports = {
 "100% US stocks (VTI)": {"VTI":1.0},
 "60/40 (VTI/BND)": {"VTI":.6,"BND":.4},
 "All Weather (30 VTI/40 TLT/15 IEI/7.5 DBC/7.5 GLD)": {"VTI":.3,"TLT":.4,"IEI":.15,"DBC":.075,"GLD":.075},
 "Golden Butterfly (20 VTI/20 IJS/20 TLT/20 SHY/20 GLD)": {"VTI":.2,"IJS":.2,"TLT":.2,"SHY":.2,"GLD":.2},
 "Permanent (25 VTI/25 TLT/25 BIL/25 GLD)": {"VTI":.25,"TLT":.25,"BIL":.25,"GLD":.25},
 "Global 100% stocks (VT)": {"VT":1.0},
}
rows=[]
for nm,w in ports.items():
    for (s,e,tag) in [("2007-07-01",None,"ETF era 2007-07..2026-10"),("2019-12-01",None,"RPAR live window 2019-12..2026-10")]:
        try: rows.append(stats(port(w,s,e), f"{nm} [{tag}]"))
        except Exception as ex: print(nm, tag, "fail", ex)
rows.append(stats(r["RPAR"].loc["2020-01-01":], "RPAR ETF actual [2020-01..2026-10]"))
df=pd.DataFrame(rows); print(df.to_string()); df.to_csv("allweather_results.csv",index=False)

# GEM replication: SPY vs VEU (12m), gate vs BIL 12m, else AGG. Monthly, decide at month-end, 0.1% switch cost.
px = m[["SPY","VEU","BIL","AGG"]].dropna()
mom = px.pct_change(12)
choice = np.where(mom["SPY"]>mom["VEU"], "SPY", "VEU")
win = pd.Series(choice, index=px.index)
winmom = pd.Series([mom.loc[i, w] for i,w in win.items()], index=px.index)
hold = pd.Series(np.where(winmom > mom["BIL"], win, "AGG"), index=px.index).shift(1)
rr = px.pct_change()
gem = pd.Series([rr.loc[i, h] if isinstance(h,str) else np.nan for i,h in hold.items()], index=px.index)
sw = (hold != hold.shift(1)) & hold.notna() & hold.shift(1).notna()
gem = gem - sw.astype(float)*0.001
for (s,tag) in [("2008-04-01","2008-04..2026-10"),("2014-12-01","post-book 2014-12..2026-10")]:
    g = gem.loc[s:].dropna(); print("\nGEM", tag, stats(g,"GEM SPY/VEU/AGG"), "switches", int(sw.loc[s:].sum()))
    print("  SPY B&H", stats(rr["SPY"].loc[g.index],"SPY"))
    print("  60/40 SPY/AGG", stats((0.6*rr["SPY"]+0.4*rr["AGG"]).loc[g.index],"60/40"))
print("\nGEM holdings by month-end 2024-12..2025-09:"); print(hold.loc["2024-12-01":"2025-10-01"].to_string())
print("\nGEM holdings 2020-01..2020-08:"); print(hold.loc["2020-01-01":"2020-08-01"].to_string())
print("\nGEM holdings 2022:"); print(hold.loc["2021-12-01":"2023-02-01"].to_string())
yr = (1+gem.dropna()).groupby(gem.dropna().index.year).prod()-1
print("\nGEM calendar returns:"); print((yr*100).round(1).to_string())
