import yfinance as yf, json, sys
out={}
for t in ['JEPI.L','JEPQ.L','VUAA.L','CSPX.L','IBIT','VWRA.L','AGGH.L']:
    try:
        tk=yf.Ticker(t); i=tk.info; h=tk.history(period='1mo')
        out[t]={'yield':i.get('yield'),'dividendYield':i.get('dividendYield'),'sharesOutstanding':i.get('sharesOutstanding'),
                'last_close':[str(h.index[-1].date()),round(float(h.Close.iloc[-1]),2)] if len(h) else None,'currency':i.get('currency')}
    except Exception as e: out[t]={'err':repr(e)}
json.dump(out,open(sys.argv[1],'w'),indent=1); print(json.dumps(out))
