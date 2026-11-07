"""Write one small data pack per quant pillar (A01-I10) plus MOVERS.md, so each pillar agent reads only its own slice.
Usage: python3 -I src/packs.py --week 2026-W45   (run after run_weekly.py has written pillar_values.csv)"""
import argparse, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
import pillars as P

ROOT = Path(__file__).resolve().parents[1]
SRC = {"A": "daily adjusted close", "B": "daily adjusted close vs VT and bucket peers", "C": "daily returns and high/low/close",
       "D": "daily and weekly prices", "E": "daily, weekly and monthly returns", "F": "daily volume, high, low, close",
       "G": "fund facts from yfinance plus UCITS line check on the LSE", "H": "FRED series and CBOE VIX", "I": "fund holdings data from yfinance plus FRED DGS10"}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--week", required=True); a = ap.parse_args()
    wd = ROOT / "runs" / a.week; pk = wd / "packs"; pk.mkdir(exist_ok=True)
    V = pd.read_csv(wd / "pillar_values.csv", index_col=0); S = pd.read_csv(wd / "pillar_scores.csv", index_col=0)
    F = pd.read_csv(wd / "family_scores.csv", index_col=0)
    weeks = sorted(p.name for p in (ROOT / "runs").iterdir() if p.is_dir() and p.name < a.week and (p / "pillar_values.csv").exists())
    Vp = pd.read_csv(ROOT / "runs" / weeks[-1] / "pillar_values.csv", index_col=0) if weeks else None
    u = P.universe(); bucket = dict(zip(u.ticker, u.bucket)); ucits = dict(zip(u.ticker, u.ucits_candidate))
    readings = P.macro_readings()
    for pid, (fam, name, d) in P.REG.items():
        if fam == "J": continue
        L = [f"# Pillar {pid}: {name}", f"Family: {P.FAMILY_NAMES[fam]} (family weight {P.WEIGHTS[fam]} of 100). Better when: {'higher' if d == 1 else 'lower' if d == -1 else 'context only'}. Source: {SRC[fam]}.",
             f"Week {a.week}. Previous week available: {weeks[-1] if weeks else 'none (first run)'}.", ""]
        if fam == "H":
            x, txt = readings.get(pid, (0, "n/a"))
            L += [f"Market-wide reading: {txt}. Risk-off intensity {x:+.2f} (positive = risk-off).",
                  "Mapped to buckets by the sensitivity tables in src/pillars.py (DEFENSIVE, DURATION, USD_HURT, OIL_GAIN). Bucket scores (0-100, 50 neutral):"]
            bs = S.groupby(S.index.map(bucket))[pid].mean().round(0)
            L += [f"- {b}: {v:.0f}" for b, v in bs.items()]
        else:
            col = pd.DataFrame({"bucket": V.index.map(bucket), "value": V[pid], "score": S[pid]})
            if Vp is not None and pid in Vp: col["prev_value"] = Vp[pid].reindex(col.index); col["change"] = col.value - col.prev_value
            col["ucits"] = col.index.map(ucits)
            v = col.value.dropna()
            L += [f"Distribution across {len(v)} ETFs with data: min {v.min():.4g}, 25% {v.quantile(.25):.4g}, median {v.median():.4g}, 75% {v.quantile(.75):.4g}, max {v.max():.4g}. Missing: {col.value.isna().sum()}.", "",
                  "## Bucket medians", col.groupby("bucket").value.median().round(4).to_markdown(), "",
                  "## Best 15 by score", col.sort_values("score", ascending=False).head(15).round(4).to_markdown(), "",
                  "## Worst 15 by score", col.sort_values("score").head(15).round(4).to_markdown(), "",
                  "## Owner's core proxy (VT) and its UCITS candidates' proxies", col.loc[[t for t in ["VT", "ACWI", "URTH", "VOO", "QQQ", "VWO", "AGG", "GLD"] if t in col.index]].round(4).to_markdown(), "",
                  "## All 200 (value, score)", col[["bucket", "value", "score"]].round(4).to_csv()]
        (pk / f"{pid}.md").write_text("\n".join(L) + "\n")
    # Movers summary for the news planner
    M = [f"# Biggest moves, week {a.week}", "", "## 1-week return: 15 worst and 15 best", V["A01"].sort_values().head(15).round(4).to_markdown(), "",
         V["A01"].sort_values().tail(15).round(4).to_markdown(), "", "## 1-week return by bucket (median)",
         V.groupby(V.index.map(bucket))["A01"].median().sort_values().round(4).to_markdown(), "",
         "## Volatility regime 1m/1y, 10 highest", V["C06"].sort_values().tail(10).round(2).to_markdown(), "",
         "## Volume spike frequency 3m, 10 highest", V["F05"].sort_values().tail(10).round(3).to_markdown(), "",
         "## Macro readings"] + [f"- {k} {P.REG[k][1]}: {t} (risk-off {x:+.2f})" for k, (x, t) in readings.items()] + [
         "", "## Composite rank: 10 best and 10 worst", F.sort_values("composite", ascending=False)[["bucket", "composite"]].head(10).round(1).to_markdown(),
         F.sort_values("composite")[["bucket", "composite"]].head(10).round(1).to_markdown()]
    (pk / "MOVERS.md").write_text("\n".join(M) + "\n")
    print("packs:", len(list(pk.glob("*.md"))))

if __name__ == "__main__":
    main()
