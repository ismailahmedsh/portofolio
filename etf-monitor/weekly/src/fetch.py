"""Fetch daily prices and fund facts for the universe. Writes to cache/ (gitignored: vendor terms bar redistribution)."""
import json, sys, time
from pathlib import Path
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "cache"; CACHE.mkdir(exist_ok=True)

def universe():
    return pd.read_csv(ROOT / "config" / "universe.csv").fillna("")

def fetch_prices(tickers, start="2005-01-01"):
    out = {}
    for i in range(0, len(tickers), 50):
        chunk = tickers[i:i + 50]
        for attempt in range(3):
            try:
                df = yf.download(chunk, start=start, auto_adjust=False, actions=False, group_by="ticker",
                                 threads=False, progress=False)
                break
            except Exception as e:  # rate limit or network
                print("retry", attempt, e, file=sys.stderr); time.sleep(20)
        for t in chunk:
            try:
                d = df[t].dropna(how="all")
                if len(d): out[t] = d
            except KeyError:
                pass
        time.sleep(2)
    adj = pd.DataFrame({t: d["Adj Close"] for t, d in out.items()})
    close = pd.DataFrame({t: d["Close"] for t, d in out.items()})
    high = pd.DataFrame({t: d["High"] for t, d in out.items()})
    low = pd.DataFrame({t: d["Low"] for t, d in out.items()})
    vol = pd.DataFrame({t: d["Volume"] for t, d in out.items()})
    return adj, close, high, low, vol

def fetch_facts(tickers):
    facts = {}
    for t in tickers:
        rec = {"ticker": t}
        try:
            tk = yf.Ticker(t)
            info = tk.info or {}
            for k in ["longName", "netExpenseRatio", "totalAssets", "yield", "fundInceptionDate", "category",
                      "fundFamily", "navPrice", "regularMarketPrice", "trailingPE", "beta3Year", "currency", "quoteType"]:
                rec[k] = info.get(k)
            try:
                fd = tk.funds_data
                eh = fd.equity_holdings
                if eh is not None and len(eh):
                    col = eh.columns[0]
                    rec["equity_holdings"] = {str(i): (None if pd.isna(v) else float(v)) for i, v in eh[col].items()}
                bh = fd.bond_holdings
                if bh is not None and len(bh):
                    col = bh.columns[0]
                    rec["bond_holdings"] = {str(i): (None if pd.isna(v) else float(v)) for i, v in bh[col].items()}
                sw = fd.sector_weightings
                if sw: rec["sector_weightings"] = {k: float(v) for k, v in sw.items()}
                th = fd.top_holdings
                if th is not None and len(th):
                    rec["top_holdings"] = {str(i): float(r["Holding Percent"]) for i, r in th.iterrows()}
            except Exception as e:
                rec["funds_data_error"] = str(e)[:120]
        except Exception as e:
            rec["error"] = str(e)[:200]
        facts[t] = rec
        time.sleep(0.4)
    return facts

if __name__ == "__main__":
    u = universe()
    tickers = list(u.ticker)
    extra = ["^VIX", "^VIX3M"]
    ucits = sorted({x + ".L" for x in u.ucits_candidate if x})
    adj, close, high, low, vol = fetch_prices(tickers + extra + ucits)
    for name, df in [("adj", adj), ("close", close), ("high", high), ("low", low), ("vol", vol)]:
        df.to_pickle(CACHE / f"{name}.pkl")
    print("prices:", adj.shape, "first", adj.index.min().date(), "last", adj.index.max().date())
    missing = [t for t in tickers + extra + ucits if t not in adj.columns]
    print("missing:", missing)
    if "--facts" in sys.argv:
        facts = fetch_facts(tickers)
        (CACHE / "facts.json").write_text(json.dumps(facts, indent=1, default=str))
        print("facts:", sum(1 for f in facts.values() if f.get("netExpenseRatio") is not None), "with expense ratio")
