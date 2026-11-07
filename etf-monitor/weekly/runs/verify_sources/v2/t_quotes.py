import yfinance as yf, pandas as pd, datetime as dt, json
out={}
for t in ["VWRA.L","CSPX.L","IWDA.L","EIMI.L","SWDA.L"]:
    i=yf.Ticker(t).info
    rmt=i.get("regularMarketTime")
    out[t]={k:i.get(k) for k in ["bid","ask","bidSize","askSize","regularMarketPrice","currency","exchange","quoteType","annualHoldingsTurnover","sharesOutstanding","totalAssets","navPrice"]}
    out[t]["regularMarketTime"]=rmt
    out[t]["rmt_utc"]=str(dt.datetime.utcfromtimestamp(rmt)) if isinstance(rmt,(int,float)) else rmt
    b,a=i.get("bid"),i.get("ask")
    if b and a: out[t]["spread_bp"]=round(1e4*(a-b)/((a+b)/2),1)
for t in ["EWJ","EWU","EWG","MCHI","INDA"]:
    d=yf.Ticker(t).dividends
    out[t]={"n_divs":len(d),"last_div":str(d.index[-1])[:10] if len(d) else None,
            "ttm":round(float(d[d.index>d.index[-1]-pd.Timedelta(days=1)-pd.Timedelta(days=365)].sum()),4) if len(d) else None}
g=yf.Ticker("GC=F").history(period="max",interval="1mo")
out["GC=F"]={"first":str(g.index[0])[:10],"last":str(g.index[-1])[:10],"rows":len(g)}
h=yf.Ticker("VWRA.L").history(period="max")
out["VWRA.L_hist"]={"first":str(h.index[0])[:10],"last":str(h.index[-1])[:10],"rows":len(h),"last_close":float(h.Close.iloc[-1])}
print(json.dumps(out,indent=1,default=str))
