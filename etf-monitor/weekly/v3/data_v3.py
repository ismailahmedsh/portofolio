"""Fetch the v3 additions: US-listed lines (config/universe_us_core.csv, universe_us_new_types.csv) and the LSE options-income
lines, converted to USD, with trailing 12-month cash distributions (Dividends only; Capital Gains excluded, TAX01 v3), plus the
macro tickers MAC01-MAC10 read from yfinance. Crypto is excluded by the owner (2026-11-13): bitcoin rows are not fetched.
Writes ../cache/v3_*.pkl (gitignored). Usage: python3 -I v3/data_v3.py"""
import json, sys, time
from pathlib import Path
import pandas as pd, yfinance as yf

ROOT = Path(__file__).resolve().parents[1]; CACHE = ROOT / "cache"; CACHE.mkdir(exist_ok=True)
EXCLUDED_TYPES = {"bitcoin", "bitcoin_etn_lse"}  # owner decision 2026-11-13: crypto off for now
MACRO = ["AED=X", "EURUSD=X", "GBPUSD=X", "JPY=X", "CNY=X", "INR=X", "CL=F", "^VIX", "^VIX3M", "HYG", "IEF", "TIP", "^TNX", "SPY", "QQQ", "ACWI", "VT", "^GSPC", "^NDX", "RSP", "^BXM"]

def universe_us():
    rows = []
    for f in ["universe_us_core.csv", "universe_us_new_types.csv"]:
        d = pd.read_csv(ROOT / "config" / f, dtype=str); d["file"] = f; rows.append(d)
    u = pd.concat(rows).drop_duplicates("ticker", keep="first")
    u = u[~u["type"].isin(EXCLUDED_TYPES)].copy()
    u["info_only"] = (u.leveraged == "yes") | (u.single_stock == "yes") | u["type"].eq("leveraged_info") | u.ticker.isin(["BTCI", "SVOL", "YMAX", "ULTY"])
    u["venue"] = ["LSE" if t.endswith(".L") else "US" for t in u.ticker]
    return u.reset_index(drop=True)

def fetch(tickers, start="2000-01-01"):
    frames = {}
    for i in range(0, len(tickers), 30):
        ch = tickers[i:i + 30]
        for a in range(3):
            try:
                df = yf.download(ch, start=start, auto_adjust=False, actions=True, group_by="ticker", threads=False, progress=False); break
            except Exception as e:
                print("retry", e, file=sys.stderr); time.sleep(15)
        for t in ch:
            try:
                d = df[t].dropna(how="all", subset=["Close"])
                if len(d): frames[t] = d
            except KeyError: pass
        time.sleep(1)
    return frames

if __name__ == "__main__":
    u = universe_us()
    fr = fetch(list(u.ticker) + [m for m in MACRO if m not in set(u.ticker)])
    gbp = fr["GBPUSD=X"]["Close"]; eur = fr["EURUSD=X"]["Close"]
    cur = {}
    for t in u.ticker[u.venue == "LSE"]:
        try: cur[t] = yf.Ticker(t).fast_info.get("currency") or "USD"
        except Exception: cur[t] = "USD"
        time.sleep(0.2)
    close, raw, usdvol, divs, facts = {}, {}, {}, {}, {}
    for t, d in fr.items():
        k = cur.get(t, "USD")
        f = (gbp.reindex(d.index).ffill() / (100 if k in ("GBX", "GBp") else 1)) if k in ("GBX", "GBp", "GBP") else (eur.reindex(d.index).ffill() if k == "EUR" else 1.0)
        c = (d["Adj Close"] if "Adj Close" in d else d["Close"]).where(lambda s: s > 0)
        close[t] = c * f; raw[t] = d["Close"].where(lambda s: s > 0) * f
        usdvol[t] = d["Volume"] * d["Close"] * f
        if "Dividends" in d:
            dv = d["Dividends"]; dv = dv[dv > 0]; divs[t] = (dv * (f.reindex(dv.index) if hasattr(f, "reindex") else f))
    for t in u.ticker:
        if t not in fr: continue
        try:
            inf = yf.Ticker(t).info or {}
            facts[t] = {k: inf.get(k) for k in ["totalAssets", "netExpenseRatio", "fundInceptionDate", "longName", "currency", "yield"]}
        except Exception as e: facts[t] = {"error": str(e)[:100]}
        time.sleep(0.25)
    u["currency"] = [cur.get(t, "USD") for t in u.ticker]; u["has_data"] = u.ticker.isin(fr)
    pd.DataFrame(close).to_pickle(CACHE / "v3_close_usd.pkl"); pd.DataFrame(raw).to_pickle(CACHE / "v3_rawclose_usd.pkl")
    pd.DataFrame(usdvol).to_pickle(CACHE / "v3_usdvol.pkl"); pd.to_pickle(divs, CACHE / "v3_divs_usd.pkl")
    u.to_pickle(CACHE / "v3_universe.pkl"); (CACHE / "v3_facts.json").write_text(json.dumps(facts, indent=1, default=str))
    print("lines with data:", int(u.has_data.sum()), "of", len(u), "| missing:", list(u.ticker[~u.has_data]), "| LSE currencies:", cur)
