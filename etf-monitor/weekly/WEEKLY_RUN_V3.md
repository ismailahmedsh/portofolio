# Weekly run v3

Engine v3 on pillars v3 (PILLARS_V3.md), the owner's mix (config/portfolio_v2.yaml) and DECISION_RULES_V3.md. Runs every Saturday.

## Steps
1. **Data (a few minutes).**
   ```bash
   cd etf-monitor/weekly
   python3 -I v2/data_v2.py      # London (UCITS) lines; add --facts on the first Saturday of the month
   python3 -I v3/data_v3.py      # US-listed and options-income lines, distributions, macro tickers
   ```
2. **Engine, plan, report and news packs.**
   ```bash
   python3 -I v3/run_v3.py --week <week> [--backtests]   # backtests on the first Saturday of the month
   python3 -I v3/packs_v3.py --week <week>
   ```
   Outputs in `runs/<week>/`: `REPORT_V3.md`, `v3_plan.json`, `v3_us_lines.csv`, `v3_cross_wrapper.json`, `v3_options_income.csv`, `v3_macro.json`, `news_packs/`.
3. **Agent workflow** `weekly-etf-review-v3` (`.claude/workflows/weekly-etf-review-v3.js`) with args
   `{"week": "<week>", "root": "<abs path>/etf-monitor/weekly", "window": "<last Saturday> to <Friday>", "pillars": <contents of runs/<week>/news_packs/index.json>}`.
   - 24 news leads (NWS01-NWS17 without crypto, EVT01-EVT09), each choosing topics, explorer counts and rounds until its saturation test passes (caps: 4 rounds, 6 explorers a round, 18 a pillar; own budget of 260 agents).
   - Verifiers have their own budget of 24 (one per pillar), so leads and explorers can never use them up.
   - A blind verifier per pillar re-checks every +/-2 score and severity 2+, then writes `news/<ID>.json` and `events/<ID>.json`.
   - Synthesiser de-duplicates across pillars; the engine re-runs with events and news; 6 family judges; a committee of 5 votes until unanimous.
   - Output: `runs/<week>/WEEKLY_PLAN_V3.md` (one page).
4. **Save the run record** (agents' working notes are lost when the cloud machine closes):
   ```bash
   python3 -I v3/save_run_v3.py --week <week> --journal <journal.jsonl path from the workflow's completion notice> --result <output-file path from the same notice>
   ```
   Writes `runs/<week>/workflow/`: `summary.md` (agents by phase, failures), `agents.jsonl.gz` (every agent's final output), `result.json.gz` (final plan, votes, stats).
5. **Commit and push** `runs/<week>/`, `runs/plan_log.csv`, `runs/news_log.csv`.

## What you maintain
After each buy, add the fill to `config/portfolio_v2.yaml`. Add lines to `orderable` once checked in IBKR. To ever buy US-listed lines, record `us_listed.ibkr_entity` and `us_listed.w8ben_signed_on`.
