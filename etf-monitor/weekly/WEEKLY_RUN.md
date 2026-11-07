# Weekly run

Runs every Saturday after the US close, for the ISO week just ended. Total time is about 15 minutes.

## Steps

1. **Data and the 90 computed pillars (Python, about 6 minutes).**
   ```bash
   cd etf-monitor/weekly
   python3 -I src/fetch.py --facts
   python3 -I src/run_weekly.py --week <week>     # first pass: computes all 90 quant pillars
   python3 -I src/packs.py --week <week>          # one data pack per pillar for its agent
   ```
   Before the workflow, copy last week's single-pass news digests, or run the 10 single-pass agents from `config/news_agents.md`, into `runs/<week>/news_round0/`. The news planner uses them as a starting map.
2. **First run of the month only: refresh the backtest.** `python3 -I src/backtest.py`
3. **Run the adaptive agent workflow** `weekly-etf-review` (saved in `.claude/workflows/weekly-etf-review.js` at the repository root) with args:
   `{"week": "<week>", "root": "<absolute path>/etf-monitor/weekly", "window": "<Saturday before> to <Saturday after>", "maxAgents": 450}`.
   What it does:
   - **Pillars.** 90 pillar agents, one per pillar, each reads its pack. Any pillar that finds something that could change a decision sends 1 to 4 investigators (data, web or both), then judges whether it is saturated; up to 3 rounds per pillar.
   - **News**, in parallel with the pillars. A planner reads the week's biggest moves and picks 5 to 15 specific topics, one explorer each. A synthesiser looks for correlations and gaps and opens the next round with new topics. This repeats until it judges the picture saturated, up to 4 rounds.
   - **Score.** 10 news-pillar scorers turn the explorer findings into `news/J01-J10.json`; the engine re-scores all 200 ETFs.
   - **Families.** 10 family judges, A to J, synthesise their pillars.
   - **Committee.** A chair drafts the plan; 5 members vote (rules, risk, macro and news, quant, UAE execution). Each objection gets an investigator, the chair revises, and they vote again, up to 4 rounds. If they are still not unanimous, the default under `DECISION_RULES.md` applies and the dissent is written down.
   - **Write.** `runs/<week>/WEEKLY_PLAN.md`.
4. **Commit and push** `runs/<week>/` and `runs/history.csv`. Raw vendor data stays in the gitignored `cache/`.

## Cost

The Python part is free. The single-pass news run used about 1.3 million tokens. The adaptive workflow runs roughly 150 to 450 agents a week, so expect several million to tens of millions of tokens per run; the week 45 figure is recorded in `runs/2026-W45/WEEKLY_PLAN.md`. On a Claude subscription this draws heavily on your usage allowance. `maxAgents` caps the spend, and anything skipped by the cap is logged in the plan.

## Scheduling

A Claude Code cloud scheduled task fires every Saturday at 09:17 Dubai time and runs this file. It needs network access to Yahoo Finance, FRED, the LSE price lines and web search, which the current cloud environment allows.
