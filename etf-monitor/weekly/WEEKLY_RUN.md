# Weekly run

Runs every Saturday after the US close, for the ISO week just ended. Total time is about 15 minutes.

## Steps

1. **Data and quant pillars (Python, about 6 minutes).**
   ```bash
   cd etf-monitor/weekly
   python3 -I src/fetch.py --facts
   ```
2. **News pillars (10 agents in parallel, about 5 minutes).** Spawn one agent per pillar J01-J10. Each reads `config/news_agent_brief.md` with the week label and writes `runs/<week>/news/J0x.json` and `.md`. The scopes and buckets for each agent are in `config/news_agents.md`.
3. **First run of the month only: refresh the backtest.**
   ```bash
   python3 -I src/backtest.py
   ```
4. **Score and report.**
   ```bash
   python3 -I src/run_weekly.py --week 2026-W46
   ```
   Output: `runs/<week>/REPORT.md` plus `pillar_scores.csv`, `family_scores.csv`, `pillar_values.csv`; `runs/history.csv` accumulates ranks so each report shows week-over-week and month-to-date changes.
5. **Commit and push** `runs/<week>/` and `runs/history.csv`. Raw vendor data stays in the gitignored `cache/`.

## Cost

The Python part is free. The 10 news agents used about 1.3 million tokens in total for week 45, mostly cached reading of search results. On a Claude subscription this draws on your usage allowance; on the API it is a few dollars a week with Sonnet and more with Opus.

## Scheduling

A Claude Code cloud scheduled task fires every Saturday at 09:17 Dubai time and runs this file. It needs network access to Yahoo Finance, FRED, the LSE price lines and web search, which the current cloud environment allows.
