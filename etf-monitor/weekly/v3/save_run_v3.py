"""Save a record of one weekly workflow run into runs/<week>/workflow/, so every week and month can be reviewed later.
Writes:
  result.json.gz  the workflow's full return value and stats (final plan, committee votes, agent counts, errors)
  agents.jsonl.gz one line per agent: label, phase, final output (news leads' findings, judges, committee members)
  summary.md      agent counts by phase, failures, skipped agents
Usage: python3 -I v3/save_run_v3.py --week 2026-W46 --journal <.../workflows/wf_xxx/journal.jsonl> --result <task output file>"""
import argparse, collections, gzip, json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--week", required=True); ap.add_argument("--journal", required=True); ap.add_argument("--result")
    a = ap.parse_args()
    out = ROOT / "runs" / a.week / "workflow"; out.mkdir(parents=True, exist_ok=True)
    started, results = {}, {}
    for line in Path(a.journal).read_text().splitlines():
        try: j = json.loads(line)
        except Exception: continue
        if j.get("type") == "started": started[j["agentId"]] = {"label": j.get("label"), "phase": j.get("phase")}
        elif j.get("type") == "result": results[j["agentId"]] = j.get("result")
    rows = [{"agent": k, **v, "done": k in results, "result": results.get(k)} for k, v in started.items()]
    with gzip.open(out / "agents.jsonl.gz", "wt") as f:
        for r in rows: f.write(json.dumps(r, default=str) + "\n")
    res = {}
    if a.result and Path(a.result).exists():
        with open(a.result, "rb") as src, gzip.open(out / "result.json.gz", "wb") as dst: shutil.copyfileobj(src, dst)
        try: res = json.loads(Path(a.result).read_text())
        except Exception: res = {}
    by_phase = collections.Counter(r["phase"] or "-" for r in rows)
    failed = [r["label"] for r in rows if not r["done"]]
    errs = [f"{x.get('label') or x.get('description')}: {x.get('error')}" for x in (res.get("workflowProgress") or []) if isinstance(x, dict) and x.get("error")]
    final = res.get("result") if isinstance(res.get("result"), dict) else {}
    lines = [f"# Workflow run record, {a.week}", "", f"Agents started: {len(rows)}; finished: {len(rows) - len(failed)}; tokens: {res.get('totalTokens', 'n/a')}", "",
             "| phase | agents |", "|---|---|"] + [f"| {p} | {n} |" for p, n in sorted(by_phase.items())]
    lines += ["", f"Committee: {'unanimous' if final.get('unanimous') else 'see result.json.gz'} after {final.get('committee_rounds', '?')} round(s)",
              f"Stats: {json.dumps(final.get('stats', {}))}", "", "Not finished: " + (", ".join(failed) or "none"), "Errors: " + ("; ".join(errs) or "none"),
              "", "Read: `zcat agents.jsonl.gz | jq 'select(.phase==\"News\") | {label, result}'`"]
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    print("saved", out, "| agents", len(rows), "| not finished", len(failed))
