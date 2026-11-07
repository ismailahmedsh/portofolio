# Investing research: long-term ETFs and an AI research toolkit

Self-contained study produced 2026-11-02 to 2026-11-03. Start with the three files in bold.

| File | What it is |
|------|------------|
| 00-framework.md | Goal G0, 15 research pillars, 15 research audit pillars, 15 planning pillars, 15 plan audit pillars, agent plan and loop rules |
| **reports/ETF long term and AI research tools.md** | Consolidated research report (about 11,700 words) with the "Canonical facts" section that resolves every cross-file contradiction |
| **plan/plan_v5.md** | The approved plan (P1 to P15) for a Canadian citizen resident in the UAE. v1 to v4 are kept for history with change lists |
| **reviews/final_verdict.md** | Cycle record and the three reviewers' final verdicts |
| research_notes/ | Eight note files from two research rounds, each with Takeaway, Cited Findings, Inferences, Gaps and a URL per claim; gapfill2_data/ holds replication scripts and results |
| audits/ | Research audits rounds 1 and 2; plan audits rounds 1 and 2; scoring template |
| reviews/ | Three independent reviews, each with an appended re-review of plan v4 |
| data/ | GitHub repo search snapshot (269 active repos) and the verification scripts and logs for the TSX data path, contribution backtest and repo status. Raw vendor downloads are gitignored because their terms bar redistribution |

Nothing here is personal financial advice. It is research the owner commissioned for their own portfolio.

## Weekly analysis system (added 2026-11-07)

`etf-monitor/weekly/` scores 200 ETFs on 100 pillars every week (90 computed in Python, 10 news pillars scored by one agent each) and turns them into hold, deposit and sell decisions using rules backed by a 2015-2026 switching backtest. Start with `etf-monitor/weekly/runs/2026-W45/REPORT.md`, then `DECISION_RULES.md`, `PILLARS.md` and `WEEKLY_RUN.md`. An independent review is in `runs/2026-W45/REVIEW.md`. A cloud scheduled task runs it every Saturday at 09:17 Dubai time.
