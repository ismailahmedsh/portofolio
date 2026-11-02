# Research audit, round 2

Date: 2026-11-02. Scope: five round-1 files plus three gap-fill files in `research_notes/ETF long term and AI research tools/` (`gapfill2_egypt_canada_accounts.md` = egypt, `gapfill2_etf_numbers_overlays.md` = numbers, `gapfill2_technical_verification.md` = tech), scored per `audit_template.md`. Scripts confirmed in `gapfill2_data/` and `data/verify/`. Round-1 abbreviations kept.

## Gap closure (round-1 GAP LIST)

| # | Round-1 gap | Status | Justification |
|---|---|---|---|
| 1 | Egypt (R5, A8) | CLOSED | egypt KQ1: IBKR official country list (Egypt present), FRA Decision 37/2014 checked for reversal, treaty Arts 4/10/13/22 read, Law 151/2026; dated two-scenario decision table. Residual: IBKR entity, Scenario B foreign dividends. |
| 2 | Consistent risk/return table (R2) | PARTIALLY CLOSED | numbers Q1 Tables 1a/1b: issuer/MSCI/FTSE NAV total return 1/3/5/10-yr, 3-yr SD, max DD, calendar years, CSV. Missing: 20/30-yr, worst rolling 10-yr for any candidate; VFV/VUN/VIU/VEE/VCN/VAB returns still aggregator-only. |
| 3 | Canadian DIY blocks (R1) | CLOSED | numbers Q2 Table 2: fee/MER/AUM/structure/yield/inception for XEF, XEC, XIC, XUU, VIU, VEE, VCN, ZEA, ZEM, bonds; VXUS 0.05% from Vanguard. Vanguard CA AUM blank, BMO AUM stale (flagged). |
| 4 | FWT drag, strategies (R3, R5) | CLOSED | egypt KQ2: bps-by-account table with stated assumptions and CPM cross-check; numbers Q3: RPAR live record, replication of four defensive portfolios, core-satellite 5-20%, verdict per strategy. |
| 5 | TSX data path (R10) | PARTIALLY CLOSED | tech Q1: yfinance batch, `info`, `funds_data` verified on XEQT.TO/XEF.TO; iShares CA holdings CSV pattern; BoC Valet and FRED CSV verified. Alpha Vantage ETF_PROFILE and EODHD untested (key needed); Vanguard/BMO CSV unprobed. |
| 6 | Scheduler feasibility (R14, R9, A7) | PARTIALLY CLOSED | tech Q5: 204-domain allowlist enumerated (no data hosts), network secrets, cron specs, write-back. `.mcp.json` + SKILL.md never written or run; `claude -p` auth failed, cost unmeasured. |
| 7 | Repo verification (R6, R8, A6) | CLOSED | tech Q3: 23 repos via `gh api` with stars, push, issues, license, release; TradingAgents 119,927 confirmed; Lean IB/US-ETF confirmed from QC docs. OctoBot/Superalgos not refreshed. |
| 8 | Broker fees (R5, A1) | PARTIALLY CLOSED | egypt KQ3: Wealthsimple, TD, RBC (ETF page), IBKR CA read 2026-11-02; contributor fee table delivered. Questrade still 403 (FX 1.5% secondary); RBC general page 404; TD FX and select-ETF lists unread. |
| 9 | Budget and compliance (R14, R15, A14) | PARTIALLY CLOSED | tech Q4: Pro/Max/Ultra prices, scheduled-task usage rules, three-setup summed budget; egypt KQ4: 31-103CP s.1.3 quoted. Financial Datasets, testfol.io, VectorBT PRO unpriced; CP from 2014 consolidation, not 2026. |
| 10 | Overlay on candidates (R11) | CLOSED | numbers Q4: SMA10 and ABSMOM12 on SPY/VTI/VT/ACWI/XEQT/VEQT/XAW with cash/BIL/AGG/ZAG, 0.1% switch, April 2025 and 2020/2022 episodes, GEM; verdict "report flag, not trade rule". |
| 11 | Contribution-aware backtest (R12) | CLOSED | tech Q2: `cash_deposits` absent in vectorbt 1.2.0 (grep, signature); `bt.algos.CapitalFlow` in source; pandas CAD 1,000/month backtest with FX conversion, XIRR and TWR separate. bt not executed. |
| 12 | Reconciliation, code read (R1, R4, R13) | CLOSED | numbers Q2: XEQT MER 0.19% supersedes 0.20%, VEQT 0.22%; tech Q3: TradingAgents manager, risk, rating, reporting modules read from raw source, 10-item module map. |

Count: 7 closed, 5 partially closed, 0 open.

## Scores (rounds 1 and 2 together)

| Pillar | Score | Evidence (file and section) | Gap (if < 3) |
|--------|-------|-----------------------------|--------------|
| A1 Recency | 3 | Issuer sheets Sep 30, 2026 (numbers Q1/Q2); IBKR list, treaty, Law 151/2026 (egypt KQ1); broker pages 2026-11-02 (egypt KQ3); repo metadata and Claude pricing 2026-11-02 (tech Q3/Q4); 2014 FRA rule checked for reversal. | |
| A2 Source quality | 3 | Aggregator history replaced by issuer/MSCI/FTSE/Nasdaq/Damodaran (numbers Q1); treaty text; official broker pages; 31-103CP; raw source code. Remaining secondary items (Questrade FX, Decision 37, EY snippet, RA/AQR) labelled with the blocked primary named. | |
| A3 Coverage | 3 | All pillars substantive; sub-table below. | |
| A4 Quantitative | 3 | Dated, unit-bearing tables throughout: numbers Tables 1a-5, egypt KQ2/KQ3 tables, tech backtest, repo and budget tables. | |
| A5 Contradictions | 2 | Weighed: XEQT 0.17/0.19/0.20, VEQT 0.22/0.24, VXUS (numbers Q2); IBKR inactivity fee (egypt KQ3); CPM 22 vs own 15 bps (egypt KQ2); SMA 2022 cash-vs-bonds bracket (numbers Q4); JPM 6.7 vs 7.0 (numbers Q5). Not weighed: cross-file inconsistencies introduced in round 2, e.g. tech Q1 says Yahoo's 0.20 "matches BlackRock's MER" against numbers Q2's 0.19. | Resolve the list below; the three round-2 agents did not see each other's files. |
| A6 Repo verification | 3 | tech Q3: 23 repos with stars, push, issues, license, created, release via `gh api`/PyPI; NautilusTrader and TradingAgents confirmed; PyPortfolioOpt relocation found. | |
| A7 Claude Code applicability | 3 | ai R9/R14 primitives plus tech Q5: allowlist contents, network secrets, `CRON_TZ=America/Toronto 7 17 * * 1-5`, host list, branch override; tech Q3 names reusable TradingAgents modules (`PortfolioContext`, `rating.py` REVIEW, `write_report_tree`). | (Worked config unwritten; gap 2.) |
| A8 User-context fit | 3 | egypt KQ1 decision table (Scenario A factual Canadian resident; Scenario B 183+ days); FWT by TFSA/RRSP/FHSA/taxable (egypt KQ2); C$500-2,000 contributor fee table (egypt KQ3); CAD contribution backtest (tech Q2); CAD candidate table (numbers 1b). | |
| A9 Risk disclosure | 3 | GFC -58% to -65% MSCI, XEQT live record "not the stress case" (numbers Q1); RPAR 3.4%/yr live, 2022 bond failure (Q3); SMA exits after the trough 2020/2025 (Q4); 1% real stress (Q5); round-1 R7/R15. | |
| A10 Bot skepticism | 3 | bots R7; tech Q3 adds TradingAgents' risk layer is prompt-only with no deterministic exposure logic and its backtest is not a portfolio simulator. | |
| A11 Actionability | 3 | All-in-one and DIY both buildable: reconciled MERs, structures, drag (numbers Q2, egypt KQ2), DIY-vs-XEQT within ~1 pp over 7 years (tech Q2), one-basis comparison (numbers 1b), Egypt decision table, overlay verdict, broker shortlist, keyless data path and cloud-task spec. | |
| A12 Reproducibility | 3 | URLs on every claim; own calcs tied to named scripts/CSVs; tech verification log with UTC timestamps and failures. | |
| A13 Bias awareness | 3 | In-sample and simulated-series flags (numbers Q3/Q4); yfinance adjustment "unaudited", back-loaded XIRR (tech Q2); vendor pre-publication numbers separated; round-1 R15/R11/R13. | |
| A14 Cost transparency | 3 | tech Q4: subscription tiers, API per-MTok, batch/cache/search rates, scheduled-task usage rules, three-setup summed budget ($20 / $24-120 / $99-238) with explicit token assumptions; vendor prices from data R10. | |
| A15 Gap register | 3 | Every round-2 section ends with Gaps naming blocked URLs, untested calls and assumptions. | |

**A3 sub-table**

| R | Score | Remaining hole |
|---|-------|----------------|
| R1 | 3 | Vanguard CA AUM; BMO fee/yield. |
| R2 | 2 | No worst rolling 10-yr or 20/30-yr for VT/ACWI/EAFE/EM/XIC despite monthly data on hand; Vanguard CA fund returns aggregator-only. |
| R3 | 3 | Bogleheads/PWL satellite-cap text unread; 2008 defensive figures own calc only. |
| R4 | 3 | Daryanani full text. |
| R5 | 3 | Questrade FX secondary; Scenario B foreign dividends, IBKR entity. |
| R6 | 3 | OctoBot/Superalgos from TSV only. |
| R7 | 3 | Alpha Arena official stats. |
| R8 | 3 | Release dates lack year; issue counts include PRs. |
| R9 | 3 | Worked config not run. |
| R10 | 3 | Keyed vendors untested with TSX; no free flows source. |
| R11 | 3 | April 2025 rule-level result own replication only. |
| R12 | 3 | bt not executed; no PV cross-check. |
| R13 | 3 | TradingAgents `graph/`, `dataflows/` unread. |
| R14 | 3 | Cost per run unmeasured; Pro window not in tokens. |
| R15 | 3 | 2026 31-103CP text unread. |

- TOTAL: 44 / 45
- VERDICT: PASS (every pillar >= 2; total >= 38)

## Contradictions to resolve (planner picks one value each)

1. XEQT MER: 0.19% (fact sheet, numbers Q2) vs 0.20% (mech R4 Tawcan; tech Q1 Yahoo `netExpenseRatio`, wrongly said to "match BlackRock's MER"). Use 0.19%; treat Yahoo MER fields as unreliable (XEF 0.22 vs 0.23 likewise).
2. XEQT management fee: tech Q1 cites 0.18%; numbers Q2 and core R1 give 0.17% from Dec 18, 2025. Use 0.17%.
3. XEQT sleeves: numbers Table 2 labels 30.78% "ITOT" and 14.99% "Core S&P Total U.S."; egypt KQ2 and tech Q1 (holdings CSV Oct 30, 2026) show XTOT 31.26% (TSX) and ITOT 14.32%. Use the CSV labelling.
4. XUU structure: core R1 and mech R5 say XUU holds US stocks directly; numbers Q2 shows it wraps ITOT/IVV/IJH/IJR. Round-1 "structurally cleaner" inferences are void; egypt KQ2 already uses the wrap.
5. VEQT MER: 0.22% (fact sheet Mar 31, 2026) vs 0.24%/0.25% (mech R4, Cboe). Use 0.22%, note expected ~0.19%.
6. Overlay return cost: data R11 "roughly zero-to-negative" vs numbers Q4 1.4-3.3 pts/yr on actual candidates. Use numbers Q4.
7. Claude run-cost assumptions: ai R14 (60k/5k tokens, ~$5-10/month Sonnet) vs tech Q4 (40k/4k, $4.40). Pick one; neither is measured.
8. Budget route: tech Q4 Setup B1 uses Max ($100) while its inference says Pro ($20) includes scheduled tasks. Decide Pro-first, Max as escalation.
9. ZEM AUM C$1.0B vs ~C$3.5B; XEQT AUM 22.91B vs 23.42B; ai-hedge-fund issues 61 vs 187; TradingAgents stars 119,922 vs 119,927: date or definition differences, cite the later/API figure.

## GAP LIST (ordered by impact on G0)

1. [R1, R4, A5] Resolve the ten contradictions above before P2/P4 are written. BLOCKING (values given; one pass over the plan's numbers).
2. [R14, R9, A7] No worked `.mcp.json` + `daily-etf-watch` SKILL.md and no measured run cost. Instruction: planner writes both under P8 and makes "first live run on Pro, record `total_cost_usd` and allowlist failures" a phase-1 milestone. ACCEPTABLE (inputs fully documented in tech Q5, ai R9).
3. [R2] Worst rolling 10-yr and 20-yr returns for VT/ACWI/EAFE/EM/XIC not computed. Instruction: derive from `gapfill2_data/monthly_adj_close_yfinance_2026-11-02.csv` plus MSCI/Shiller in P5. ACCEPTABLE (S&P 500 lost decade and MSCI GFC drawdowns bound the stress case).
4. [R5] Questrade pricing secondary-only; TD/RBC select-ETF lists and FX unread. Instruction: name Wealthsimple (primary-sourced) as default CAD broker, Questrade as alternative pending confirmation. ACCEPTABLE.
5. [R5, A8] Scenario B: "centre of activities" from an EY snippet, foreign-dividend tax unstated, IBKR entity and Canadian departure tax unresearched. Instruction: P4 encodes an "adviser before 183 days or an Egyptian home" trigger. ACCEPTABLE (Scenario A is the base case and answered).
6. [R10] Alpha Vantage/EODHD untested with TSX symbols; Vanguard/BMO CSV unprobed; yfinance 429 from cloud egress untested. Instruction: P9 keeps the keyless path primary, EODHD as a phase-1-tested fallback. ACCEPTABLE.
7. [R14, R15] Pro usage window not in tokens; Financial Datasets, testfol.io, VectorBT PRO unpriced; 2026 31-103CP unread. Instruction: P13 budgets Pro-first; quote the 2014 CP with a verify-against-2026 note. ACCEPTABLE.
8. [R12] bt not executed; backtest omits FWT, spreads, FX cost; yfinance adjustment unaudited. Instruction: P12 cross-checks pandas vs bt `CapitalFlow` and one Portfolio Visualizer run. ACCEPTABLE.
