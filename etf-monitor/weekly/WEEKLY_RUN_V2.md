# Weekly run v2

Engine v2 on the audited pillars (PILLARS_V2.md), the owner's strategic mix (config/portfolio_v2.yaml) and DECISION_RULES_V2.md. Runs every Saturday after the US close.

## Steps
1. **Data (about 2 minutes, facts once a month).**
   ```bash
   cd etf-monitor/weekly
   python3 -I v2/data_v2.py            # add --facts on the first Saturday of the month, --french to refresh factors
   ```
2. **Engine, plan and report (about 15 seconds; backtests on the first Saturday of the month).**
   ```bash
   python3 -I v2/run_v2.py --week <week> [--backtests]
   python3 -I v2/packs_v2.py --week <week>
   ```
   Outputs in `runs/<week>/`: `REPORT_V2.md`, `v2_plan.json` (this month's order), `v2_line_values.csv`, `v2_line_scores.csv`, `v2_exposure.csv`, `v2_fit.csv`, `packs_v2/` (one pack per pillar). `runs/plan_log.csv` keeps every week's pick (REC02).
3. **Agent workflow** `weekly-etf-review-v2` (`.claude/workflows/weekly-etf-review-v2.js` at the repository root) with args:
   `{"week": "<week>", "root": "<absolute path>/etf-monitor/weekly", "window": "<Saturday before> to <today>", "pillars": <the list in runs/<week>/built_pillars.json>, "maxAgents": 450}`.
   - One agent per computed pillar reads its pack and opens investigation rounds when something could change a decision.
   - The news loop expands round by round until saturated; then 10 event agents (EVT01-EVT10) write `runs/<week>/events/EVT0x.json`. Severity 2 fund events block buying a line, severity 3 sanctions or access events block it too, severity 1 lowers its line score.
   - The engine re-runs with the events, 13 family judges synthesise, and the committee votes under DECISION_RULES_V2.md until unanimous (default: the engine's plan, no sells).
   - Output: `runs/<week>/WEEKLY_PLAN_V2.md`.
4. **Commit and push** `runs/<week>/` and `runs/plan_log.csv`. Raw vendor data stays in the gitignored `cache/`.

## What you maintain
After each buy, add the fill to `config/portfolio_v2.yaml`. Add lines to `orderable` once you have checked them in IBKR. Change `strategic_mix` whenever you decide; log it in CHANGELOG.md.
