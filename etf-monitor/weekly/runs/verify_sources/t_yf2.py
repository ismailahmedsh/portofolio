import yfinance as yf
for t in ["EWJ","EWU","EWG","MCHI","INDA","VT"]:
    try:
        i=yf.Ticker(t).info; print(t,"yield",i.get("yield"),"dividendYield",i.get("dividendYield"),"trailingAnnualDividendYield",i.get("trailingAnnualDividendYield"))
    except Exception as e: print(t,"ERR",repr(e)[:200])
for t in ["VWRA.L","CSPX.L","EIMI.L"]:
    h=yf.Ticker(t).history(period="max",interval="1mo",auto_adjust=True)
    print(t,"monthly rows",len(h),"first",str(h.index[0])[:10] if len(h) else None,"last",str(h.index[-1])[:10] if len(h) else None, "nan_close",int(h['Close'].isna().sum()) if len(h) else None)
d=yf.Ticker("VWRA.L").history(period="max",interval="1d",auto_adjust=False)
print("VWRA.L daily rows",len(d),str(d.index[0])[:10],str(d.index[-1])[:10])
