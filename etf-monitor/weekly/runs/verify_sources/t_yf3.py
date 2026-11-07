import yfinance as yf, pandas as pd
for t in ["EWJ","EWU","EWG","MCHI","INDA"]:
    tk=yf.Ticker(t); d=tk.dividends; h=tk.history(period="5d")
    if len(d): d=d[d.index>pd.Timestamp.now(tz=d.index.tz)-pd.Timedelta(days=365)]
    px=h['Close'].iloc[-1]
    print(t,"ttm_div",round(d.sum(),4),"n",len(d),"last_div",str(d.index[-1])[:10] if len(d) else None,"px",round(px,2),"ttm_yield%",round(100*d.sum()/px,2))
