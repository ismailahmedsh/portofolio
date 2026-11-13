import yfinance as yf, pandas as pd, json, sys
out={}; now=pd.Timestamp.now(tz='UTC')
for t in ["VWRA.L","CSPX.L","SPY","QQQ","JEPQ","JEPI","IBIT","VOO","AGG","IEF","^IRX"]:
    try:
        tk=yf.Ticker(t); h=tk.history(period="2y",auto_adjust=False); d=tk.dividends
        r={"n_closes_2y":len(h),"first":str(h.index[0])[:10] if len(h) else None,"last":[str(h.index[-1])[:10],round(float(h.Close.iloc[-1]),4)] if len(h) else None}
        dd=d[d.index>now-pd.Timedelta(days=365)]
        r["n_divs_365d"]=len(dd); r["ttm_yield_pct"]=round(100*float(dd.sum())/float(h.Close.iloc[-1]),2) if len(h) and len(dd) else 0.0
        try:
            i=tk.info; r.update({k:i.get(k) for k in ["currency","yield","dividendYield","trailingAnnualDividendYield","netExpenseRatio","totalAssets","quoteType","fundFamily"]})
        except Exception as e: r["info_err"]=repr(e)[:150]
        # forward return check (pillar 14)
        if len(h)>30: r["fwd_20d_ret_from_60d_ago"]=round(float(h.Close.iloc[-40]/h.Close.iloc[-60]-1),4)
        out[t]=r
    except Exception as e: out[t]={"err":repr(e)[:200]}
json.dump(out,open(sys.argv[1],"w"),indent=1,default=str); print(json.dumps(out,default=str,indent=0))
