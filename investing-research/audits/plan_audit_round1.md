# Plan audit, round 1

Date: 2026-11-03. Auditor: plan auditor (independent, no new research). Object: `plan/plan_v1.md`. Reference: `reports/ETF long term and AI research tools.md` (Canonical facts win), `00-framework.md` (B1-B15, P1-P15), `audits/audit_template.md`.

## Scores

| Pillar | Score | Evidence (plan section) | Gap (if < 3) |
|---|---|---|---|
| B1 Feasibility for one person | 2 | P14 MVP (stop after Phase 1 is valid); P13 3 h/month; P3 Rule 2 | Phase 2 "about 12 hours" covers seven adapters, engine extension, EODHD adapter, two cross-checks, look-ahead test, grounding check, skills: 25-40 h realistic. "Always-on machine" for local cron never confirmed |
| B2 Consistency with research | 2 | P2 primary table, P4, P5, P8, P10, P12 numbers match Canonical facts 1-9, Tables A-J | Five mismatches (list below); two sit in the portfolio part and the success metrics |
| B3 Specificity | 2 | Tickers, weights, bands, cron specs, `.mcp.json`, two SKILL.md, CLAUDE.md, headless command, allowlist, pins | `portfolio.yaml` and `accounts.yaml` contents absent; `ledger.csv` schema prose only; `uvx` entry points are assumptions |
| B4 Risk-adjusted | 3 | M1 band below past decade; P2 rejects tilts, leverage, overlays with costs; P5 overlay-as-flag, AQR 10-20% bound; P15 life-events-only changes | |
| B5 Cost-bounded | 3 | P1 M8, P13 Setup A $20, pre-authorised escalations, $50 hard ceiling, P15 kill at $50 for two months | |
| B6 Time-bounded | 3 | P14 five phases, dated windows, measurable exits | |
| B7 Dependency clarity | 2 | P14 dependency paragraph; P8 `--bare` divergence; P9 cadences | `total_cost_usd` is reported with `--bare` (API key), yet Phase 2 records it "on Pro"; `.mcp.json` loads in `-p` mode per the report but P13 says scheduled runs "load none" with no mechanism named |
| B8 Failure modes | 2 | yfinance ladder (P13); allowlist failure to local cron (P8/P14); Pro windows to API/Max; Egypt B adviser trigger (P4); DEGRADED on any source | No broker-change path (Questrade itself "pending confirmation"); no Google News 503 fallback; no mid-run API 429 retry policy |
| B9 Measurable outcomes | 3 | P1 M1-M10 with numeric targets and anchors; P12 hit-rate and whipsaw definitions; P15 kill thresholds | |
| B10 User fit | 3 | CAD core, TFSA > FHSA > RRSP > taxable, Scenario A/B table, days-in-Egypt counter, recurring buy, 3 h/month | |
| B11 Simplicity | 2 | One fund; optional monitor; flat files, no LangGraph | Five signal families, a daily note the plan itself questions (assumption 9), quantstats, skfolio pinned for a gate no rule enters, three interactive-only MCP servers. Cuts in GAP 10 |
| B12 Maintainability | 3 | P13 pinning, P15 re-scan with drop criteria, OpenBB excluded, manual-NAV end of the fallback ladder | |
| B13 Compliance and safety | 2 | P5 never-do list; CLAUDE.md bans; P8 network secrets; P9 licensing; P15 no-advice with 31-103CP verify note | `monthly-etf-review` grants `Bash(git *)` under `--permission-prompts none` (force-push, `git config`, credential helpers); `ledger.csv` and Yahoo cache committed and cloned to a cloud VM without a privacy/ToS weighing; `WebSearch` in the monthly run widens the injection surface P10 says is closed |
| B14 Traceability | 2 | Ten-claim sample: seven correct, three faulty | See sample table |
| B15 Completeness | 3 | All fifteen sections present; sub-table below | |

- TOTAL: 37 / 45
- VERDICT: **FAIL** (total below 38; every pillar >= 2)

### B14 sample (ten numeric claims)

| # | Plan claim | Cited | Check |
|---|---|---|---|
| 1 | XEQT MER 0.19%, fee 0.17% (P2) | Canonical facts 1-2 | OK |
| 2 | XEQT XIRR 15.6%, max DD -24.8% (P2) | Table C | OK |
| 3 | Lump sum beats drip 68%, cash 70% (P3) | R4 section | OK |
| 4 | SMA overlay costs 1.4-3.3 pts/yr (P2) | Canonical fact 6 | OK |
| 5 | TFSA $7,000, RRSP $33,810, FHSA $8,000/$40,000 (P4) | "Account placement" | OK |
| 6 | XEQT SMA10: 7 switches, 12.14% vs 14.25% (P12) | Table H | OK |
| 7 | API line $4.40, ceiling $10 (P13) | Canonical fact 7 | OK |
| 8 | "<0.5% of panickers improved" (P1 M5) | R4 section | Wrong: report says <0.5% of investors went to cash and >80% of those were worse off |
| 9 | DIY mix "about 0.12% MER" (P2) | Table A text | Report computes 0.12% at XEQT weights; the plan's 45/30/10/15 mix is about 0.13% |
| 10 | VEE wrap "worth ~2 bps of level-2 withholding" (P2) | "egypt KQ2" | Not in the report; cites a research note directly |

### B15 sub-table: planning pillars P1-P15

| Pillar | Score | Main hole |
|---|---|---|
| P1 Objective and metrics | 2 | M5 anchor misquoted; M7 assumes 25 trading days a month (TSX has about 21) |
| P2 Portfolio construction | 2 | DIY table headed "at XEQT weights" but holds 15% Canada / 10% EM against XEQT's 26% / 4.5%; MER figure borrowed from the XEQT-weight calculation |
| P3 Contribution and rebalancing | 3 | None material |
| P4 Account, tax, platform | 3 | RRSP switch threshold C$100,000 is a plan choice not marked "Assumption" |
| P5 Risk guardrails | 2 | "No selling in any account for the first 10 years" contradicts P3 Rule 3 (band sales) and P15 (DIY switch, "never hold both") |
| P6 Toolkit architecture | 3 | None |
| P7 Repo selection | 3 | None |
| P8 Claude Code workflow | 2 | `Bash(git *)`; `uvx` strings unconfirmed; no mechanism named for running `-p` with MCP disabled; `total_cost_usd` on subscription route unverified |
| P9 Data pipeline | 2 | CAPE depends on a monthly manual check; no fallback for Google News RSS 503 |
| P10 Signal methodology | 3 | None |
| P11 Reporting | 3 | None |
| P12 Validation | 3 | None |
| P13 Operations | 3 | Setup B wording (see mismatch 3) |
| P14 Roadmap | 2 | Phase 2 effort estimate ("about 12 hours") unrealistic for its milestone list |
| P15 Review, kill, update | 2 | No broker-change trigger; DIY switch at C$300,000 implies selling in a possibly taxable account with no ACB/tax note |

## Mismatches found (plan value vs report value)

1. P1 M5 anchor: plan "<0.5% of panickers improved"; report "fewer than 0.5% of Vanguard's self-directed investors went to cash... more than 80% of those who did were worse off" (R4 section).
2. P2 DIY heading and MER: plan "4-fund DIY at XEQT weights... about 0.12% MER"; report Table A text computes 0.12% at XEQT weights (45/26/24/4.5), while the plan's own weights are Table C's 45/30/10/15, giving about 0.13% (0.45x0.07 + 0.30x0.22 + 0.10x0.28 + 0.15x0.06).
3. P13 Setup B: plan "EODHD Historian $19.99 plus Pro, or API Sonnet 5.5 at about $4.40, total about $24.40 (B2)"; report Table J B2 is EODHD $19.99 plus API Sonnet $4.40 on the API route (no Pro); EODHD plus Pro would be about $39.99.
4. P1 M7: plan ">= 90%... (23 of 25 per month)"; the report's cron spec runs weekdays, about 21 TSX trading days a month, so 90% is about 19 of 21.
5. P2 and P3 Rule 5: "~2 bps of level-2 withholding" (VEE) and "yield ~1.58%" are not in the report or its canonical table; they cite `egypt KQ2` and the verify log directly, which breaks the plan's own rule that every number cites a report section or a `data/verify/` script (the yield is log output, not a script result).

All other checked figures (Canonical facts 1-9, Tables A-J, cron specs, allowlist hosts, library versions, drawdowns, forecasts, treaty articles, contribution limits) match.

## GAP LIST (ordered by impact on G0)

1. **[P2] BLOCKING.** Retitle the DIY table "Table C DIY mix (45/30/10/15)", restate its MER as about 0.13%, and either justify 15% Canada / 10% EM against the lifecycle (33% domestic) and Vanguard (30%) findings or move the mix to XEQT weights.
2. **[P1] BLOCKING.** Correct the M5 anchor to "fewer than 0.5% of investors went to cash in Feb-May 2020 and more than 80% of those were worse off by end of May (report R4 section)".
3. **[P8, P13] BLOCKING.** Replace `Bash(git *)` in `monthly-etf-review` with the daily skill's narrow set (`git add reports/*`, `git commit*`, `git push origin reports*`), and state how `ledger.csv` and the committed cache are protected in the cloud clone (e.g. a units-only redacted copy).
4. **[P5, P3, P15] MINOR.** Reword P5 behavioural guardrail (2) to "no discretionary selling; the only sales are P3 Rule 3 band repairs, P15 life events and the P15 DIY switch", and add an ACB/capital-gains line to the C$300,000 switch for a taxable account.
5. **[P15, P8] MINOR.** Add a broker-change trigger: if Wealthsimple ends $0 commissions, fractional or recurring buys, confirm Questrade from a primary page at the next re-scan and redirect new contributions only; name IBKR Canada as the third option with its cost per C$1,000 buy.
6. **[P8, P14] MINOR.** Change the Phase 2 milestone to "record `total_cost_usd` on one `--bare` API run and Pro-window use on one subscription run"; name the flag that runs `claude -p` without `.mcp.json`; make confirming the `uvx` entry points a Phase 2 task with removal as fallback.
7. **[P13] MINOR.** Rewrite Setup B to match Table J: B2 is EODHD $19.99 plus API Sonnet $4.40 (about $24.40, API route, no Pro); Pro plus EODHD is about $39.99.
8. **[P1] MINOR.** Change M7 to "about 19 of 21 TSX trading days" and align the kill threshold in P15 (70%) with the same denominator.
9. **[P14] MINOR.** Re-estimate Phase 2 at 25-40 hours or split it into 2a (data layer, `run_daily.py`, look-ahead test, first run) and 2b (backtest extension, cross-checks, EODHD adapter) in weeks 7-10.
10. **[P6, P9, P10, P11] MINOR.** Simplify: drop ABSMOM12 and CAPE (keep SMA10 and drawdown as flags, 2s10s and Sahm as context); remove `quantstats` and `skfolio` from the pins until a new rule is proposed; move `.mcp.json` out of Phase 2; make the daily note change-only by default, which also protects Pro's windows.
11. **[P9] MINOR.** Replace the CAPE manual check with a static series refreshed at the re-scan or drop CAPE (GAP 10); on Google News RSS failure write "n/a (source failed)" in the news section instead of DEGRADED.
12. **[P2, P3, P4] MINOR.** Mark the "~2 bps VEE level-2" and "yield ~1.58%" figures as note/log-level claims (or patch them into the report's canonical table), and mark the C$100,000 RRSP switch threshold as an Assumption.
