import yfinance as yf, json, sys
out={}
for t in ["VWRA.L","CSPX.L","IWDA.L","EIMI.L"]:
    try:
        tk=yf.Ticker(t); info=tk.info
        h=tk.history(period="10d",interval="1d",auto_adjust=False)
        out[t]={"bid":info.get("bid"),"ask":info.get("ask"),"bidSize":info.get("bidSize"),"askSize":info.get("askSize"),
          "currency":info.get("currency"),"regularMarketPrice":info.get("regularMarketPrice"),"yield":info.get("yield"),"dividendYield":info.get("dividendYield"),
          "trailingAnnualDividendYield":info.get("trailingAnnualDividendYield"),"netExpenseRatio":info.get("netExpenseRatio"),"totalAssets":info.get("totalAssets"),
          "hist_rows":len(h),"hist_last":h.tail(3)[["High","Low","Close","Volume"]].round(4).reset_index().astype(str).values.tolist()}
    except Exception as e:
        out[t]={"error":repr(e)[:300]}
print(json.dumps(out,indent=1,default=str))
