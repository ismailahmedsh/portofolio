"""Task 1b: XEF.TO retry (single), Ticker.info and funds_data fields for TSX ETFs."""
import datetime as dt, time, json, yfinance as yf, pandas as pd
OUT = "/home/user/portofolio/investing-research/data/verify/downloads"
LOG = "/home/user/portofolio/investing-research/data/verify/verify_log.md"
def log(s): print(s); open(LOG,"a").write(s+"\n")
ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
log(f"\n## XEF.TO retry + info/funds_data ({ts})")
try:
    x = yf.download("XEF.TO", start="2005-01-01", auto_adjust=False, actions=True, progress=False, threads=False)
    x = x.dropna(how="all")
    log(f"- XEF.TO single retry: rows={len(x)} first={x.index.min().date()} last={x.index.max().date()} cols={[c[0] if isinstance(c,tuple) else c for c in x.columns]}")
    x.columns = [c[0] if isinstance(c,tuple) else c for c in x.columns]
    x.to_csv(f"{OUT}/XEF_TO_daily.csv")
except Exception as e:
    log(f"- XEF.TO retry ERROR {e!r}")
for sym in ["XEQT.TO","XEF.TO","VT"]:
    t = yf.Ticker(sym)
    try:
        info = t.info
        keys = sorted(info.keys())
        want = {k: info.get(k) for k in ["quoteType","longName","currency","exchange","expenseRatio","annualReportExpenseRatio","netExpenseRatio","totalAssets","yield","dividendYield","fundInceptionDate","navPrice","category","fundFamily","trailingAnnualDividendYield","ytdReturn","threeYearAverageReturn","fiveYearAverageReturn"] if k in info}
        log(f"- Ticker('{sym}').info: {len(keys)} keys; selected={json.dumps(want, default=str)}")
        log(f"  - expense-like keys: {[k for k in keys if 'xpense' in k.lower() or 'ratio' in k.lower()]}")
    except Exception as e:
        log(f"- Ticker('{sym}').info ERROR {e!r}")
    try:
        fd = t.funds_data
        res = {}
        for attr in ["description","fund_overview","fund_operations","asset_classes","top_holdings","equity_holdings","bond_holdings","bond_ratings","sector_weightings"]:
            try:
                v = getattr(fd, attr)
                if isinstance(v, pd.DataFrame):
                    res[attr] = f"DataFrame shape={v.shape} cols={list(v.columns)[:6]} idx={list(v.index)[:5]}"
                elif isinstance(v, dict):
                    res[attr] = f"dict keys={list(v.keys())[:12]}"
                elif isinstance(v, str):
                    res[attr] = f"str len={len(v)}: {v[:120]!r}"
                else:
                    res[attr] = repr(v)[:200]
            except Exception as e:
                res[attr] = f"ERR {e!r}"
        for k,v in res.items(): log(f"  - funds_data.{k}: {v}")
        try:
            fo = fd.fund_operations
            log(f"  - fund_operations full: {fo.to_dict() if isinstance(fo,pd.DataFrame) else fo}")
        except Exception as e: log(f"  - fund_operations ERR {e!r}")
    except Exception as e:
        log(f"- Ticker('{sym}').funds_data ERROR {e!r}")
    time.sleep(1)
