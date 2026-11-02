"""Task 1d: modest rate-limit probe: 25 sequential single-ticker history calls (1y) + 25 fast_info reads, timing and any 429/YFRateLimitError."""
import time, datetime as dt, yfinance as yf
LOG="/home/user/portofolio/investing-research/data/verify/verify_log.md"
def log(s): print(s); open(LOG,"a").write(s+"\n")
ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
log(f"\n## yfinance rate-limit probe ({ts})")
syms = ["XEQT.TO","XEF.TO","XIC.TO","VFV.TO","ZAG.TO","XUU.TO","VUN.TO","XEC.TO","VT","VTI","VXUS","XAW.TO","VEQT.TO","XGRO.TO","VBAL.TO","ZSP.TO","ZEA.TO","ZEM.TO","VCN.TO","VIU.TO","VEE.TO","XBB.TO","VAB.TO","SPY","QQQ"]
ok=0; errs=[]; t0=time.time()
for s in syms:
    try:
        h = yf.Ticker(s).history(period="1y", auto_adjust=False, raise_errors=True)
        fi = yf.Ticker(s).fast_info
        _ = fi.last_price
        ok += 1
    except Exception as e:
        errs.append(f"{s}: {type(e).__name__}: {str(e)[:120]}")
el=time.time()-t0
log(f"- 25 tickers x (history(1y) + fast_info.last_price) sequential, no sleep: ok={ok} errors={len(errs)} elapsed={el:.1f}s ({el/25:.2f}s/ticker)")
for e in errs: log(f"  - {e}")
