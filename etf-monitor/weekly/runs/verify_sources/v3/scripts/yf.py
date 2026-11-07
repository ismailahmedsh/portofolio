import yfinance as yf, pandas as pd, datetime as dt, json
out={}
for t in ["VWRA.L","CSPX.L","IWDA.L","EIMI.L"]:
    try:
        i=yf.Ticker(t).info
    except Exception as e:
        out[t]={"err":repr(e)[:200]}; continue
    r={k:i.get(k) for k in ["bid","ask","bidSize","askSize","regularMarketPrice","currency","annualHoldingsTurnover","totalAssets","navPrice"]}
    rmt=i.get("regularMarketTime"); r["regularMarketTime"]=rmt
    r["rmt_utc"]=str(dt.datetime.fromtimestamp(rmt,dt.timezone.utc)) if isinstance(rmt,(int,float)) else None
    b,a=r["bid"],r["ask"]
    if b and a: r["spread_bp"]=round(1e4*(a-b)/((a+b)/2),1); r["crossed"]=a<b
    h=yf.Ticker(t).history(period="5d"); r["last_close"]=[str(h.index[-1])[:10],round(float(h.Close.iloc[-1]),4)] if len(h) else None
    out[t]=r
for t in ["EWJ","EWU","EWG","MCHI","INDA"]:
    try:
        d=yf.Ticker(t).dividends; h=yf.Ticker(t).history(period="5d")
        dd=d[d.index>d.index.max()-pd.Timedelta(days=365)] if len(d) else d
        out[t]={"n_divs_ttm":len(dd),"last_div":str(d.index[-1])[:10] if len(d) else None,"ttm_yield_pct":round(100*float(dd.sum())/float(h.Close.iloc[-1]),2) if len(d) and len(h) else None}
    except Exception as e: out[t]={"err":repr(e)[:200]}
print(json.dumps(out,indent=1,default=str))
