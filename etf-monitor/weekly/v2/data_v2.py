"""Fetch prices, volumes and fund facts for the UCITS universe (all lines converted to USD), FX, Ken French factors.
Writes ../cache/v2_*.pkl (gitignored). Usage: python3 -I v2/data_v2.py [--facts]"""
import io, json, sys, time, zipfile
from pathlib import Path
import pandas as pd, requests, yfinance as yf

ROOT = Path(__file__).resolve().parents[1]; CACHE = ROOT / "cache"; CACHE.mkdir(exist_ok=True)
EXTRA_LINES = {  # lines the approved design names that the universe builders missed; kept only if yfinance returns data
    "ACWD.L": ("SPDR MSCI ACWI UCITS ETF (Acc) USD line", "IE00B44Z5B48", "global"),
    "SPYY.L": ("SPDR MSCI ACWI IMI UCITS ETF", "IE00B3YLTY66", "global"),
    "EXUS.L": ("Xtrackers MSCI World ex USA UCITS ETF 1C", "IE0006WW1TQ4", "developed_ex_us"),
}

def universe():
    import glob
    u = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(str(ROOT / "config" / "universe_ucits_*.csv")))]).drop_duplicates("ticker")
    for t, (n, isin, sc) in EXTRA_LINES.items():
        if t not in set(u.ticker):
            u = pd.concat([u, pd.DataFrame([{"ticker": t, "name": n, "isin": isin, "scope": sc, "currency": "USD", "ter": None, "accumulating": "yes", "verified": "pending"}])])
    u.loc[u.ticker == "VWRA.L", "ter"] = 0.14  # fee cut effective 2026-07-28 (Vanguard notice, J10 week 45)
    return u.reset_index(drop=True)

def fetch(tickers, start="2003-01-01"):
    frames = {}
    for i in range(0, len(tickers), 40):
        ch = tickers[i:i + 40]
        for a in range(3):
            try:
                df = yf.download(ch, start=start, auto_adjust=False, actions=False, group_by="ticker", threads=False, progress=False); break
            except Exception as e:
                print("retry", e, file=sys.stderr); time.sleep(15)
        for t in ch:
            try:
                d = df[t].dropna(how="all")
                if len(d): frames[t] = d
            except KeyError: pass
        time.sleep(1)
    return frames

def french():
    out = {}
    for name in ["Developed_5_Factors", "Developed_Mom_Factor", "Emerging_5_Factors"]:
        url = f"https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/{name}_CSV.zip"
        z = zipfile.ZipFile(io.BytesIO(requests.get(url, timeout=60).content))
        raw = z.read(z.namelist()[0]).decode("latin-1").splitlines()
        rows = []
        for line in raw:
            parts = [p.strip() for p in line.split(",")]
            if len(parts) > 1 and parts[0].isdigit() and len(parts[0]) == 6: rows.append(parts)
            elif rows and (len(parts) <= 1 or not parts[0].isdigit()): break  # stop after the monthly block
        hdr = [h.strip() for h in next(l for l in raw if l.startswith(",")).split(",")][1:]
        df = pd.DataFrame([r[1:] for r in rows], index=pd.to_datetime([r[0] for r in rows], format="%Y%m"), columns=hdr[:len(rows[0]) - 1]).astype(float) / 100
        out[name] = df.resample("ME").last() if False else df
    return out

if __name__ == "__main__":
    u = universe()
    fx = ["GBPUSD=X", "EURUSD=X"]
    refs = ["VT", "ACWI", "SPY", "QQQ", "EFA", "EEM", "^NDX", "^GSPC"]
    fr = fetch(list(u.ticker) + fx + refs)
    keep = [t for t in u.ticker if t in fr]
    print("lines with data:", len(keep), "of", len(u), "| missing:", [t for t in u.ticker if t not in fr])
    gbp = fr["GBPUSD=X"]["Close"]; eur = fr["EURUSD=X"]["Close"]
    cur = dict(zip(u.ticker, u.currency))
    close, vol, usdvol, rawusd = {}, {}, {}, {}
    for t in keep + refs:
        d = fr.get(t)
        if d is None: continue
        c = (d["Adj Close"] if "Adj Close" in d else d["Close"]).copy(); c[c <= 0] = None  # dividend-adjusted, for returns
        raw = d["Close"].copy(); raw[raw <= 0] = None
        k = cur.get(t, "USD")
        if k in ("GBX", "GBp"): c = c / 100 * gbp.reindex(c.index).ffill()
        elif k == "GBP": c = c * gbp.reindex(c.index).ffill()
        elif k == "EUR": c = c * eur.reindex(c.index).ffill()
        fxs = (gbp.reindex(raw.index).ffill() / (100 if k in ("GBX", "GBp") else 1)) if k in ("GBX", "GBp", "GBP") else (eur.reindex(raw.index).ffill() if k == "EUR" else 1)
        close[t] = c; rawusd[t] = raw * fxs; vol[t] = d["Volume"]; usdvol[t] = d["Volume"] * raw * fxs
    pd.DataFrame(close).to_pickle(CACHE / "v2_close_usd.pkl"); pd.DataFrame(rawusd).to_pickle(CACHE / "v2_rawclose_usd.pkl"); pd.DataFrame(vol).to_pickle(CACHE / "v2_vol.pkl"); pd.DataFrame(usdvol).to_pickle(CACHE / "v2_usdvol.pkl")
    u["has_data"] = u.ticker.isin(keep); u.to_pickle(CACHE / "v2_universe.pkl")
    if not (CACHE / "v2_french.pkl").exists() or "--french" in sys.argv: pd.to_pickle(french(), CACHE / "v2_french.pkl")
    if "--facts" in sys.argv:
        facts = {}
        for t in keep:
            try:
                inf = yf.Ticker(t).info or {}
                facts[t] = {k: inf.get(k) for k in ["totalAssets", "netExpenseRatio", "fundInceptionDate", "longName", "currency", "yield", "navPrice"]}
            except Exception as e:
                facts[t] = {"error": str(e)[:100]}
            time.sleep(0.3)
        (CACHE / "v2_facts.json").write_text(json.dumps(facts, indent=1, default=str))
    print("done", pd.DataFrame(close).shape)
