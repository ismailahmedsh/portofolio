import yfinance as yf, pandas as pd, datetime as dt, json, sys
out={}; now=pd.Timestamp.now(tz='UTC')
for t in ["VWRA.L","CSPX.L","IWDA.L","EIMI.L"]:
    try:
        tk=yf.Ticker(t); i=tk.info
        r={k:i.get(k) for k in ["bid","ask","bidSize","askSize","regularMarketPrice","currency","annualHoldingsTurnover","navPrice"]}
        rmt=i.get("regularMarketTime"); r["rmt_utc"]=str(dt.datetime.fromtimestamp(rmt,dt.timezone.utc)) if isinstance(rmt,(int,float)) else None
        b,a=r["bid"],r["ask"]
        if b and a: r["spread_bp"]=round(1e4*(a-b)/((a+b)/2),1)
        h=tk.history(period="1mo"); r["closes"]=len(h); r["last_close"]=[str(h.index[-1])[:10],round(float(h.Close.iloc[-1]),4)] if len(h) else None
        out[t]=r
    except Exception as e: out[t]={"err":repr(e)[:200]}
for t in ["EWJ","EWU","EWG","MCHI","INDA"]:
    try:
        tk=yf.Ticker(t); d=tk.dividends; h=tk.history(period="5d")
        dd=d[d.index>now-pd.Timedelta(days=365)]
        out[t]={"n_divs_365d_to_today":len(dd),"last_div":str(d.index[-1])[:10] if len(d) else None,"ttm_yield_pct":round(100*float(dd.sum())/float(h.Close.iloc[-1]),2) if len(h) else None}
    except Exception as e: out[t]={"err":repr(e)[:200]}
json.dump(out,open(sys.argv[1],"w"),indent=1,default=str); print(json.dumps(out,default=str))
