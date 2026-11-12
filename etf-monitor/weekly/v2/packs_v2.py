"""One data pack per built v2 pillar for its weekly agent (runs/<week>/packs_v2/<ID>.md). Usage: python3 -I v2/packs_v2.py --week 2026-W46"""
import argparse, json
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
SPEC = {p["id"]: p for p in json.loads((ROOT / "config" / "pillars_v2.json").read_text())["pillars"]}
LINE = ["ELG01", "ELG02", "ELG03", "ELG04", "ELG05", "ELG06", "ELG08", "ELG09", "ELG10", "CST01", "CST02_raw_gap_bps", "CST04", "CST06", "CST08", "CST10", "TAX01", "TAX03", "TAX05", "DUR01", "DUR04", "DUR06", "CON04", "CON05"]
EXPO = ["FAC01", "FAC02", "FAC03", "FAC04", "FAC05", "RSK01", "RSK02", "RSK03", "RSK05", "EXR08", "X"]
FIT = ["FIT03", "FIT04", "FIT05", "FIT06", "FIT10", "fit"]
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--week", required=True); a = ap.parse_args()
    wd = ROOT / "runs" / a.week; pk = wd / "packs_v2"; pk.mkdir(exist_ok=True)
    Lv = pd.read_csv(wd / "v2_line_values.csv", index_col=0); Ls = pd.read_csv(wd / "v2_line_scores.csv", index_col=0)
    X = pd.read_csv(wd / "v2_exposure.csv", index_col=0); F = pd.read_csv(wd / "v2_fit.csv", index_col=0); rep = (wd / "REPORT_V2.md").read_text()
    n = 0
    for pid, p in SPEC.items():
        col = next((c for c in LINE + EXPO + FIT if c == pid or c.startswith(pid + "_")), None)
        if col in EXPO and col not in X.columns: col = col + "_s" if col + "_s" in X.columns else None
        if col and col.endswith("_s"): EXPO.append(col)
        head = [f"# Pillar {pid}: {p['name']}", f"Definition: {p['definition']}", f"Source: {p['data_source']} ({p['source_status']}). Better when: {p['better_when']}. Informs: {p['decision']}.", f"Week {a.week}.", ""]
        if col in LINE:
            t = Lv[list(dict.fromkeys(c for c in ["cluster", "scope", col, "buyable"] if c in Lv))].join(Ls[list(dict.fromkeys(c for c in [pid, "line_score"] if c in Ls))], rsuffix="_score")
            body = ["## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values", t.sort_values(col).head(15).to_markdown(), t.sort_values(col).tail(15).to_markdown(), "", "## All lines (csv)", t.to_csv()]
        elif col in EXPO:
            t = X[list(dict.fromkeys(c for c in [col, col.removesuffix("_s") + "_s", "DD_excess", "RSK02", "RSK04", "X", "FAC05", "months"] if c in X and (c == col or pid == "RSK01" or c not in ("DD_excess", "RSK02", "RSK04"))))]
            body = ["## Equity groups (reference line), world reference = 50", t.sort_values(col).to_csv()]
        elif col in FIT:
            body = ["## Fit against your strategic mix", F[list(dict.fromkeys(c for c in [col, col + "_s", "fit"] if c in F))].sort_values(col).to_csv()]
        else:
            sec = [s for s in rep.split("\n## ") if pid in s]
            body = ["## From this week's report", ("\n## ".join(sec) if sec else "Not computed this week (see the coverage table in REPORT_V2.md).")]
        (pk / f"{pid}.md").write_text("\n".join(head + body) + "\n"); n += 1
    print("packs:", n)
