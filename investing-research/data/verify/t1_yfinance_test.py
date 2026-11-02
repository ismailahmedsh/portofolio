"""Task 1: yfinance batched download test for TSX + US ETFs. Keyless. Logs to verify_log.md"""
import sys, time, datetime as dt, json
import pandas as pd, yfinance as yf
OUT = "/home/user/portofolio/investing-research/data/verify/downloads"
LOG = "/home/user/portofolio/investing-research/data/verify/verify_log.md"
def log(s):
    print(s); open(LOG,"a").write(s+"\n")
ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
log(f"\n## yfinance batched download ({ts}) yfinance={yf.__version__}")
tickers = ["XEQT.TO","XEF.TO","XIC.TO","VFV.TO","ZAG.TO","XUU.TO","VUN.TO","XEC.TO","VT","VTI","VXUS"]
t0=time.time()
try:
    df = yf.download(tickers, start="2005-01-01", auto_adjust=False, actions=True, group_by="ticker", threads=True, progress=False)
    log(f"- call: yf.download({tickers}, start=2005-01-01, auto_adjust=False, actions=True, group_by='ticker') elapsed {time.time()-t0:.1f}s; shape={df.shape}")
    for t in tickers:
        try:
            sub = df[t].dropna(how="all")
            cols = list(sub.columns)
            log(f"- {t}: rows={len(sub)} first={sub.index.min().date()} last={sub.index.max().date()} AdjClose={'Adj Close' in cols} cols={cols}")
            sub.to_csv(f"{OUT}/{t.replace('.','_')}_daily.csv")
        except Exception as e:
            log(f"- {t}: ERROR {e!r}")
except Exception as e:
    log(f"- yf.download ERROR: {e!r}")
