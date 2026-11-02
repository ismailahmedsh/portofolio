# Research and planning framework

Date: 2026-11-02
Owner: Ahmed Shehata (ismailahmedsh/portofolio)
Branch: claude/upbeat-franklin-ov66yv

## Goal (G0)

Produce an evidence-backed, auditable plan with two parts:

1. **Portfolio part.** A long-term, monthly-contribution ETF portfolio for an investor
   based in Canada and Egypt that targets high long-run return while staying stable
   (bounded drawdown, broad diversification, low cost, simple to maintain).
2. **Toolkit part.** A Claude Code driven ETF research and monitoring toolkit, built
   from currently maintained open-source repositories (GitHub trending AI-finance repos,
   plus lessons reverse-engineered from trading-bot repos), that produces daily and
   monthly ETF watch reports using price, news, macro and strategy signals.

The plan must state explicitly why trading bots are not the vehicle for this goal,
and what from them is still worth reusing for a monitor rather than a trader.

Success condition for the whole pipeline: research audit passes its threshold, plan
audit passes its threshold, and three independent reviewers return a majority
APPROVE verdict with no blocking issue. Otherwise, the cycle re-runs.

## 15 research pillars (what we research)

| # | Pillar | Question it must answer |
|---|--------|------------------------|
| R1 | ETF universe and selection criteria | Which ETF categories and screening criteria (expense ratio, AUM, tracking error, liquidity, domicile) matter for a long-term core? |
| R2 | Return and stability history | What are CAGR, max drawdown, volatility, rolling 10-year returns for candidate ETFs and indices, with dates? |
| R3 | Long-term allocation strategies | What do 3-fund, core-satellite, all-weather, factor tilt, and trend/momentum overlays deliver, and what is the evidence? |
| R4 | Monthly contribution and rebalancing mechanics | DCA vs lump sum evidence, rebalancing cadence and thresholds, drift handling. |
| R5 | Costs, taxes, accounts for Canada and Egypt | TFSA/RRSP/FHSA, US vs Canadian vs UCITS domicile, withholding tax, FX drag, broker choice, Egypt access. |
| R6 | Trading bot landscape 2025-2026 | What are the most used and trending bot frameworks, what do they do, maintenance status? |
| R7 | Why bots break | Evidence on performance decay, overfitting, regime change, costs, and live vs backtest gaps. |
| R8 | AI and LLM finance repos trending on GitHub | What do FinRobot, TradingAgents, ai-hedge-fund, FinGPT, FinRL, OpenBB and similar actually do, and are they maintained? |
| R9 | Claude Code and MCP integrations for finance | Which MCP servers, skills and agent patterns exist for market data, news and ETF analysis in Claude Code? |
| R10 | Data sources and APIs for ETFs | Price, holdings, flows, news, macro: free vs paid tiers, reliability, licensing, rate limits. |
| R11 | News, sentiment and macro signals | Is there evidence that LLM or FinBERT sentiment or macro regime signals add value for ETF rotation or timing? |
| R12 | Backtesting and validation frameworks | vectorbt, backtrader, zipline-reloaded, bt, Lean: walk-forward, CPCV, deflated Sharpe, overfitting controls. |
| R13 | Reverse-engineering lessons from bot repos | Architecture patterns (signal, risk, execution), risk management, what to reuse for a monitor. |
| R14 | Monitoring and alerting pipelines | Scheduled runs (GitHub Actions cron, Claude Code scheduled tasks), report generation, notification channels. |
| R15 | Regulatory, security and operational risk | API key handling, scam bots, data licensing, survivorship bias, LLM hallucination in finance, no-advice posture. |

## 15 research audit pillars (how we judge the research)

Each scored 0 to 3. Threshold to pass: every pillar at 2 or more, and total at 38 or more out of 45.

| # | Audit pillar | 3 means |
|---|--------------|---------|
| A1 | Recency | Time-sensitive claims cite sources from the last 12 months; repo activity checked as of Nov 2026. |
| A2 | Source quality | Primary sources, official docs, peer-reviewed or well-known practitioner research. |
| A3 | Coverage vs R1-R15 | Every research pillar has substantive findings. |
| A4 | Quantitative backing | Key claims carry numbers with dates and units. |
| A5 | Contradiction handling | Conflicting evidence is surfaced and weighed, not hidden. |
| A6 | Repo verification | Each named repo has stars, last activity, license and maintenance status recorded. |
| A7 | Claude Code applicability | Findings say concretely how they plug into Claude Code. |
| A8 | User-context fit | Canada and Egypt, monthly contributions, long horizon are respected. |
| A9 | Risk disclosure | Drawdowns, failure modes and instability are stated plainly. |
| A10 | Bot skepticism grounded | The "bots break" thesis is supported by evidence, not assertion. |
| A11 | Actionability | Findings translate into decisions the plan can use. |
| A12 | Reproducibility | URLs or citations for every material claim. |
| A13 | Bias awareness | Survivorship, look-ahead, backfill and marketing bias called out. |
| A14 | Cost transparency | Tool, data and API costs are stated. |
| A15 | Gap register | Unknowns and unresolved questions are listed explicitly. |

## Agent plan

Research round 1 uses 5 research agents, each owning 3 research pillars:

| Agent | Pillars |
|-------|---------|
| ETF-core | R1, R2, R3 |
| ETF-mechanics | R4, R5, R15 |
| Bots | R6, R7, R13 |
| AI-tooling | R8, R9, R14 |
| Data-signals | R10, R11, R12 |

Then 1 research auditor scores A1 to A15. If the threshold is not met, a gap-fill round
spawns one agent per failing cluster. Maximum 3 research rounds.

Planning uses 1 planner, 1 plan auditor, and gap-fill planners as needed, maximum 3 rounds.

Final review uses 3 independent reviewers with different lenses: portfolio practitioner,
software and agent engineer, risk and compliance skeptic. Verdict is majority APPROVE
with no blocking issue, otherwise the pipeline re-runs from the failing stage.

## 15 planning pillars (what the plan must contain)

P1 Objective and success metrics. P2 Portfolio construction with tickers and rationale.
P3 Contribution and rebalancing rules. P4 Account, tax and platform setup.
P5 Risk guardrails and stability constraints. P6 Toolkit architecture.
P7 Repo selection and integration. P8 Claude Code workflow (skills, MCP, prompts, scheduled runs).
P9 Data pipeline and sources. P10 Signal and analysis methodology.
P11 Reporting cadence and report templates. P12 Validation of the monitor's outputs.
P13 Operations: security, costs, maintenance. P14 Phased roadmap with milestones.
P15 Review, kill and update criteria.

## 15 plan audit pillars (how we judge the plan)

Each scored 0 to 3. Threshold: every pillar at 2 or more, total at 38 or more.

B1 Feasibility for one person. B2 Consistency with research findings. B3 Specificity (tickers, numbers, commands).
B4 Risk-adjusted, not return-chasing. B5 Cost-bounded. B6 Time-bounded with milestones.
B7 Dependency clarity. B8 Failure modes and fallbacks. B9 Measurable outcomes.
B10 User fit (Canada and Egypt, monthly DCA). B11 Simplicity, not over-engineered.
B12 Maintainability over years. B13 Compliance and safety posture. B14 Evidence traceability to research.
B15 Completeness vs P1-P15.
