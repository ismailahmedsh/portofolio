# Research audit, round 1

Date: 2026-11-02. Scope: five note files in `research_notes/ETF long term and AI research tools/`, scored against A1-A15 (`00-framework.md`) per `audit_template.md`. Files abbreviated: core (R1-R3), mech (R4/R5/R15), bots (R6/R7/R13), ai (R8/R9/R14), data (R10-R12).

| Pillar | Score | Evidence (file and section) | Gap (if < 3) |
|--------|-------|-----------------------------|--------------|
| A1 Recency | 2 | All files dated 2026-11-02; fees/AUM Sep-Oct 2026 (core R1); PyPI versions observed 2026-11-02 (data R10/R12); Claude Code docs fetched 2026-11-02 (ai R9); seed TSV limited to pushes after 2026-05-01 (bots R6). | Load-bearing claims older than 12 months: Egypt FRA rules (2012-2014 news, mech R5), XEQT/VEQT withholding drag (2014-2016 PWL/CCP, core R1, mech R4), IBKR Egypt eligibility (undated third-party), Questrade/Wealthsimple USD-tier pricing (official pages 403). |
| A2 Source quality | 2 | Primary: Vanguard PDFs, CRA (mech R4/R5); BlackRock XEQT fact sheet (core R1/R2); FINRA/SEC/CSA (mech R15); SEBI, arXiv, JoF/RFS (bots R7); code.claude.com and vendor pricing pages (ai, data). | R2 return/drawdown history and concentration rest on aggregators and blogs (ChartRow, myplaniq, Motley Fool, KuCoin, cryptodaily) where S&P DJI, MSCI, Vanguard, Morningstar primaries exist; US ETF fees/AUM from comparison sites; Bogleheads unread. |
| A3 Coverage vs R1-R15 | 2 | All 15 pillars have takeaway, cited findings, inferences, gaps (sub-table below). | R2 lacks volatility and rolling 10-yr for candidates; R3 lacks all-weather/risk-parity and core-satellite; R1 omits XEF/XEC/XIC figures; R5 Egypt unresolved; R10 TSX coverage untested. |
| A4 Quantitative backing | 3 | Dated numbers with units throughout: returns/drawdowns (core R2), limits and FX tiers (mech R5), SEBI and StockBench figures (bots R7), API quotas and per-run cost (ai R14, data R10), trend replications (data R11). | |
| A5 Contradiction handling | 3 | VXUS 0.05 vs 0.07, stale Cboe fees (core R1); Vanguard 2022 vs 2024 rebalancing (mech R4); IBKR fee conflict (mech R5); monthly vs daily SMA replications on 2022 (data R11); StockBench abstract vs table (bots R7); Polygon tiers (data R10). | |
| A6 Repo verification | 2 | Stars/last push/license for ~40 repos from seed TSV (bots R6, ai R8/R9 tables); pages fetched for ai-hedge-fund, Lean, Vibe-Trading; maintenance status recorded (Qlib, backtrader, OpenBB wind-down). | GitHub API blocked: last-commit dates missing for FinRobot, FinGPT, FinRL, FinanceToolkit, quantstats, skfolio, PyPortfolioOpt, Riskfolio-Lib; NautilusTrader has no stars/push; TradingAgents stars unconfirmed; Lean ETF/IB support not re-verified; no source code read (bots R13 gaps). |
| A7 Claude Code applicability | 3 | ai R9: `claude mcp add` commands per server, `.mcp.json` scopes with `${VAR}`, SKILL.md fields, hook events/handlers, `claude -p --bare --max-budget-usd --permission-prompts none`; ai R14: cloud/desktop/session tasks and Actions with limits; R9 inference prescribes project `.mcp.json` + two skills + Stop hook; bots R13 maps bot stages to Data->Analyzer->Policy->Report. | (Open, not deducted: cloud-task network allowlist unverified; no worked config.) |
| A8 User-context fit | 2 | Canada: 2026 TFSA/RRSP/FHSA limits, FWT by account/structure, T1135, Norbert's Gambit, broker FX tiers, 30/70 home bias (mech R5, core R1); monthly contributions: lump-sum evidence, contribution-based rebalancing, fractional/recurring buys (mech R4/R5); 15+ yr horizon framed (core R2/R3). | Egypt is flagged, not resolved: IBKR eligibility third-party, FRA position 2012-2014, tax on foreign gains "needs an adviser", treaty articles unread, no EGP remittance/FX mechanics; the 183+-days-in-Egypt scenario is only an inference. |
| A9 Risk disclosure | 3 | Drawdown budget -50%/-25%/lost decade (core R2); TQQQ -81% (core R3); top-10 concentration 39-47% (core R2); trend whipsaw 2020/2022 (data R11); LLM error rates, scams (mech R15); agent fragility (bots R7). | |
| A10 Bot skepticism grounded | 3 | Overfitting (Bailey et al., Harvey-Liu-Zhu), decay (McLean-Pontiff, Falck et al.), retail base rates (SEBI 93%, Brazil, Taiwan, BIS 81%), LLM agents (StockBench, Alpha Arena, TradeTrap), bots' own disclaimers and zero-slippage backtests (bots R6/R7). | |
| A11 Actionability | 2 | Tickers and fees (core R1); account placement and broker choice (mech R5); rebalancing rules (mech R4); data stack and costs (data R10, ai R14); repo and MCP shortlist (ai R8/R9); validation checklist (data R12); monitor architecture (bots R13). | Planner cannot build the DIY multi-ETF alternative (no XEF/XEC/XIC/VIU/VEE data), cannot compare candidate portfolios on one return/volatility/drawdown basis, has no Egypt decision, and has no overlay results on the actual candidate ETFs. |
| A12 Reproducibility | 3 | URL on every material claim; "observed" vs "reported" labelled (data R10); seed TSV path cited; blocked fetches named in each gap register. | |
| A13 Bias awareness | 3 | Survivorship/backfill (RA 2017, Morningstar 2025 closures; mech R15); memorization/look-ahead in LLM forecasts (data R11); freqtrade look-ahead rules, planted-leak tests (bots R13); in-sample selection flagged; pre-1957 reconstruction, short live histories (core R2); vendor-linked GEM numbers flagged (data R11). | |
| A14 Cost transparency | 2 | MER/FWT drag (core R1, mech R4/R5); commissions and FX tiers (mech R5); 12 data vendors plus news/search APIs (data R10); Claude API prices and per-run arithmetic (ai R14); Portfolio Visualizer/OpenBB pricing. | No Claude subscription prices or usage caps although scheduled tasks bill the subscription; Financial Datasets, VectorBT PRO, QuantConnect tiers, testfol.io, Massive free tier unpriced; no summed monthly budget. |
| A15 Gap register | 3 | Every section ends with an explicit Gaps list naming blocked sources, unverified figures and open questions. | |

**A3 sub-table: coverage per research pillar**

| R | Score | Main hole |
|---|-------|-----------|
| R1 | 2 | No fee/MER/AUM/structure for XEF, XEC, XIC, VIU, VEE, VCN; VXUS fee unresolved. |
| R2 | 2 | No volatility; no consistent total-return CAGR/max-DD table; rolling 10-yr only S&P funds; 2025 TSX full year missing. |
| R3 | 2 | All-weather/risk-parity and core-satellite absent; Bogleheads unread; no live GEM record post-2014. |
| R4 | 3 | Daryanani full text and Vanguard 2022 PDF via summaries only. |
| R5 | 2 | Egypt access, FRA status, tax on foreign gains, treaty text; Questrade/Wealthsimple official pricing. |
| R6 | 3 | TradingAgents stars and Lean ETF/IB support unconfirmed. |
| R7 | 3 | No regulator statistic on retail bot outcomes; Alpha Arena official stats unread. |
| R8 | 3 | Last-commit dates for eight libraries; Financial Datasets pricing. |
| R9 | 3 | Alpha Vantage MCP page unrendered; OpenBB MCP ETF tools unverified. |
| R10 | 2 | yfinance/Alpha Vantage TSX ETF holdings untested; no free TSX holdings or flows source. |
| R11 | 3 | Trend rules in April 2025 not covered; no ETF-level sentiment study beyond days. |
| R12 | 3 | vectorbt `cash_deposits` and bt cash injection need code check. |
| R13 | 3 | Roles inferred from file names; no code read. |
| R14 | 3 | Cloud-task network allowlist not enumerated; token cost not measured. |
| R15 | 3 | NI 31-103 rule text; 2026 FinanceBench scores. |

- TOTAL: 38 / 45
- VERDICT: PASS (exactly at threshold: every pillar >= 2, total 38; marginal, so the gaps below should be filled before the plan relies on them)

## GAP LIST (ordered by impact on G0, max 12)

1. [R5, A8, A1] Egypt flagged, not answered. Instruction: from FRA decrees, IBKR's official country-eligibility page and the Canada-Egypt treaty text (Articles 4, 10, 13), determine whether an Egypt resident may buy foreign-listed ETFs, whether IBKR accepts Egyptian residents, and how foreign ETF dividends/gains are taxed; deliver a dated decision table for two scenarios (Canadian factual resident with Egypt ties; 183+ days in Egypt).
2. [R2, A2, A11] No consistent risk/return table. Instruction: from issuer fact sheets, MSCI/S&P DJI factsheets and testfol.io/Portfolio Visualizer, build one total-return table (10/20/30-yr CAGR, annual volatility, max drawdown, worst rolling 10-yr) for VTI, VXUS, VT, XEQT, VEQT, XAW, XUU, XEF, XEC, XIC, ZAG/VAB and their indices, with dates and currency; deliver CSV plus sources.
3. [R1, A11] Canadian DIY building blocks missing. Instruction: from BlackRock CA, Vanguard CA and BMO product pages, record fee, MER, AUM, structure (direct vs US-wrap), inception and yield for XEF, XEC, XIC, VIU, VEE, VCN, ZEA, ZEM; resolve VXUS's fee from Vanguard; deliver a dated table.
4. [R3, R5] Withholding drag and missing strategies. Instruction: apply the PWL/Vanguard FWT method with 2026 yields to quantify drag for XEQT/VEQT vs DIY XUU+XEF+XEC+XIC in TFSA, RRSP, taxable; add 2024-2026 primary evidence on all-weather/risk-parity ETFs and core-satellite; deliver bps/yr table and a verdict per strategy.
5. [R10, A11] TSX data path untested. Instruction: run yfinance 1.7 `history` and `funds_data` on XEQT.TO, XEF.TO, XIC.TO; test Alpha Vantage ETF_PROFILE and EODHD sandbox with Toronto symbols; find holdings CSV URL patterns on blackrock.com/ca, vanguard.ca, bmo.com; deliver working calls, outputs and failures.
6. [R14, R9, A7] Scheduler feasibility unverified. Instruction: from Claude Code cloud environment docs, list the default network allowlist and how to add query1.finance.yahoo.com, api.stlouisfed.org, bankofcanada.ca; write and run once a minimal project `.mcp.json` plus `daily-etf-watch` SKILL.md via `claude -p --output-format json`; deliver the files, `total_cost_usd`, and daily/monthly cron specs.
7. [R6, R8, A6] Repo verification holes. Instruction: via GitHub API or commits pages, record last commit, open issues, latest release and license for FinRobot, FinGPT, FinRL, FinanceToolkit, quantstats, skfolio, PyPortfolioOpt, Riskfolio-Lib, NautilusTrader, OctoBot, Superalgos; confirm TradingAgents stars and Lean equity/ETF/IB support from QuantConnect docs; deliver an updated table.
8. [R5, A1] Broker fees from primary pages. Instruction: fetch Questrade official pricing, Wealthsimple plan-tier USD/FX pricing, IBKR Canada activity-fee rule, TD and RBC Direct Investing schedules; deliver a dated fee/FX table for a C$500-2,000 monthly contributor.
9. [R14, R15, A14] Budget and compliance totals. Instruction: record Claude Pro/Max/Team prices and usage caps for scheduled tasks; price Financial Datasets, testfol.io, Massive free tier; sum a monthly budget for the recommended stack; quote NI 31-103 registration-trigger text; deliver a one-page budget table and compliance note.
10. [R11] Overlay evidence on actual candidates. Instruction: using monthly total returns for XEQT/VEQT/VT (2019-2026) and S&P 500 (2007-2026), compute 10-month SMA and 12-month absolute momentum including April 2025, with 0.1% switch cost and both cash and ZAG as defensive asset; deliver CAGR, max DD, switches and 2025 behaviour.
11. [R12] Contribution-aware backtesting. Instruction: check in code whether vectorbt 1.x `Portfolio.from_orders` supports `cash_deposits` and how `bt` injects cash; deliver a minimal monthly-contribution backtest (pandas or skfolio) converting CAD via Bank of Canada Valet, reporting IRR and TWR separately.
12. [R1, R4, R13] Reconciliation and code read. Instruction: reconcile XEQT MER 0.19% (fact sheet) vs 0.20% (Tawcan) and VEQT 0.24% vs 0.25% to one sourced figure; read TradingAgents `agents/risk_mgmt/`, `managers/portfolio_manager.py`, `reporting.py` to confirm roles and outputs for reuse; deliver corrected figures and a module map.
