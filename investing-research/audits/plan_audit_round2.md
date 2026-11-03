# Plan audit, round 2

Date: 2026-11-03. Auditor: plan auditor (independent, no new research). Object: `plan/plan_v2.md`. References: the report (Canonical facts win), `00-framework.md`, `audits/audit_template.md`, `audits/plan_audit_round1.md`.

## Closure of round-1 findings

| Item | Status | v2 pointer |
|---|---|---|
| Mismatch 1 (M5 anchor) | CLOSED | P1 M5, P3 Rule 4 quote R4 exactly |
| Mismatch 2 (DIY heading/MER) | CLOSED | P2 "Table C DIY mix (45/30/10/15)", 0.1345 -> 0.13%, 6 bps; XEQT-weight variant 0.12% |
| Mismatch 3 (Setup B) | CLOSED | P13 "Cost setups": B2 $24.40 API route, B1 ~$120, Pro+EODHD $39.99 off-table |
| Mismatch 4 (M7 denominator) | CLOSED | P1 M7 "about 19 of 21"; P15 kill "fewer than about 15 of 21"; Phase 3 ">= 9 of 10" |
| Mismatch 5 (note-level figures) | CLOSED | P2 (2 bps) and P3 Rule 5 (1.58%) marked note-level Assumptions; P15 Assumption 15 |
| Gap 1 [P2] | CLOSED | P2 weight justification; Assumption 13 |
| Gap 2 [P1] | CLOSED | P1 M5 |
| Gap 3 [P8, P13] | CLOSED | Both SKILL.md `allowed-tools` are `Bash(python run_*.py*), Read, Write(reports/*/*)`; no git, WebSearch or MCP; ledger and cache gitignored; monthly review local-only; wrapper pushes outside the model |
| Gap 4 [P5, P3, P15] | CLOSED | P5 guardrail (2); P15 "ACB and capital gains" (taxable switch by redirecting contributions) |
| Gap 5 [P15, P8] | CLOSED | P15 "Broker-change trigger"; IBKR C$1.00 minimum = 10 bps per C$1,000 (Table D) |
| Gap 6 [P8, P14] | CLOSED | Phase 2a: `--bare` cost run + Pro-window run; `--strict-mcp-config` as Assumption 17 with fallback; `uvx` check |
| Gap 7 [P13] | CLOSED | P13 "Cost setups" |
| Gap 8 [P1] | CLOSED | P1 M7, P15 kill |
| Gap 9 [P14] | CLOSED | Phases 2a (15-20 h), 2b (10-15 h); always-on machine Assumption 12 with M7 waiver |
| Gap 10 [P6, P9, P10, P11] | CLOSED | ABSMOM12 and computed CAPE dropped; `quantstats`/`skfolio` unpinned; `.mcp.json` Phase 3; change-only daily note |
| Gap 11 [P9] | PARTIALLY CLOSED | News failure -> "n/a (source failed)" done; CAPE remains a monthly manual chore (45-day staleness rule) rather than the static series or drop asked for |
| Gap 12 [P2, P3, P4] | CLOSED | Note-level marks; C$100,000 and C$300,000 thresholds as Assumption 14 |

Closure count: 5 of 5 mismatches CLOSED; 11 of 12 gaps CLOSED, 1 PARTIALLY CLOSED, 0 OPEN. Round-1 B3 config holes closed in P6.

## Scores

| Pillar | Score | Evidence (plan section) | Gap (if < 3) |
|---|---|---|---|
| B1 Feasibility | 3 | P14 MVP after Phase 1; 2a/2b hours; P13 3 h/month; Assumption 12 fallback | |
| B2 Consistency with research | 3 | Five mismatches corrected; Canonical facts, Tables A-J, section figures re-checked (sample below) | |
| B3 Specificity | 3 | P6 YAML/CSV contents; P3 bands; P8 SKILL.md, CLAUDE.md, command, cron, allowlist; P13 pins | |
| B4 Risk-adjusted | 3 | M1 below past decade; P2 rejections with costs; P5 overlay-as-flag, AQR 10-20% bound; P15 life-events-only | |
| B5 Cost-bounded | 2 | M8, P13 Setup A $20, escalations, $50 hard ceiling, P15 kill | P13/Assumption 7 name Max ($100; B1 ~$120) as an escalation although the year-1 hard ceiling is $50 and the kill fires above $50 for two months; P8 per-run caps (~21 x $1 + $3 = ~$24) exceed M8's $10 API line |
| B6 Time-bounded | 3 | P14 six dated phases with measurable exits | |
| B7 Dependency clarity | 2 | P14 dependency paragraph; P8 `--bare` vs subscription divergence; MCP exclusion named | Whether `--bare` still loads project skills and CLAUDE.md is unverified and not on the Phase 2a list; Phase 4 (months 4-5) requires "three months of committed reports" that Phase 3 (weeks 9-12) cannot have produced; wrapper `git push origin HEAD:reports` has no fetch/rebase against cloud pushes |
| B8 Failure modes | 3 | P13 yfinance ladder; P9 news fail; P8 API retry; P14 cloud -> local -> interactive; P15 broker-change | |
| B9 Measurable outcomes | 3 | M1-M10 numeric; P12 hit-rate/whipsaw definitions; P15 thresholds on one denominator | |
| B10 User fit | 3 | CAD core, account order, Scenario A/B table, Egypt-days counter, recurring buy | |
| B11 Simplicity | 3 | One fund; two flags, three context lines; optional monitor; flat files; MCP interactive-only | |
| B12 Maintainability | 3 | P13 pins and byte-for-byte dry run; P15 re-scan with drop criteria; OpenBB excluded | |
| B13 Compliance and safety | 2 | P5 never-do list; CLAUDE.md; skills without git/network tools; network secrets; P9 licensing; P15 no-advice | P11 monthly template commits an "Account (value, contributed, drawdown)" table to branch `reports`, which the cloud clone holds (P8), so P13's "past reports show... not balances" is false; `Bash(python run_daily.py*)` is a prefix wildcard where exact strings would do |
| B14 Traceability | 2 | Ten-claim sample: eight correct, two uncited (below) | P9 "3,401 on retry" is a verify-log printout cited directly, unmarked note-level against the plan's own rule; P3 Rule 5 "quarterly distributions" has no report source |
| B15 Completeness | 3 | All fifteen sections substantive; sub-table below | |

- TOTAL: 41 / 45
- VERDICT: **PASS** (every pillar >= 2; total >= 38)

### B14 sample (ten numeric claims, new where possible)

| # | Plan claim | Cited | Check |
|---|---|---|---|
| 1 | XEQT sleeves XTOT 31.26 / XIC 25.72 / XEF 24.14 / ITOT 14.32 / XEC 4.48 (P2) | Canonical fact 3 | OK |
| 2 | DIY tracked XEQT within C$1,050 on C$87,000 (P2) | Table C rows 1-2 | OK (153,112 - 152,062) |
| 3 | Trend footnote "7 switches, cost 2.1 pts/yr" (P10) | Table H | OK (14.25 - 12.14) |
| 4 | Setup C about $98.60 (P13) | Table J | OK (59.99 + 8.60 + 30) |
| 5 | IBKR CAD 0.01/share min CAD 1.00, FX 0.20 bp min US$2, USD 0 minimum/inactivity (P4, P15) | Table D, corrections | OK |
| 6 | SEBI 93% of 10 million F&O traders, FY22-24; 8 of 14 frameworks crypto-only (P2) | R7, R6 sections | OK |
| 7 | RPAR 3.40%/yr; XBB -11.8% in 2022 (P2) | R3 text, Table B | OK |
| 8 | C$300,000 x 6-7 bps = C$180-210/yr (P15) | arithmetic on Table A | OK |
| 9 | XEF.TO 0 rows in batch, 3,401 on retry (P9) | "verify log" | Not in report; verify-log printout, unmarked |
| 10 | XEQT distributions quarterly (P3 Rule 5) | none | Not in report |

### B15 sub-table: planning pillars P1-P15

| Pillar | Score | Main hole |
|---|---|---|
| P1 | 3 | None |
| P2 | 3 | None |
| P3 | 3 | Rule 4 "bring forward 3 months of deposits" is a mild, unsourced timing lever |
| P4 | 3 | None |
| P5 | 3 | None |
| P6 | 2 | Tree omits `templates/daily.md`, `templates/monthly.md` (P8, P11), `requirements.txt`, `.python-version` (P13), `logs/` (P8 command, `.gitignore`) |
| P7 | 3 | "Used" table is broken by the quantstats paragraph; `financial-services` row orphaned (format only) |
| P8 | 2 | `--bare` skill-loading unverified; `scripts/cron_daily.sh` named as the monthly committer though the tree defines it as the daily wrapper |
| P9 | 2 | CAPE manual chore retained (gap 11); verify-log figure cited directly |
| P10 | 3 | None |
| P11 | 2 | Account-balance table committed to `reports` (see B13) |
| P12 | 3 | None |
| P13 | 2 | "No balances in past reports" statement false for monthly reviews; Max escalation vs $50 ceiling |
| P14 | 2 | Phase 4 dependency on three months of reports unreachable by month 4; Phase 5 re-scan months vs P15 |
| P15 | 3 | None |

## New inconsistencies introduced in v2

1. P11 monthly template carries account balances; P8 commits it to `reports` and says the cloud VM holds past reports; P13 claims reports hold no balances.
2. P13 and Assumption 7 treat Max ($100, ~$120 with EODHD) as an escalation; P13/P15 set a $50 hard ceiling and kill trigger.
3. P8 per-run `--max-budget-usd 1` daily and `3` monthly allow ~$24/month against M8's $10 API ceiling.
4. P14 Phase 4 dependency ("three months of committed reports") vs Phase 3 timing and the "flag log >= 2 months" milestone.
5. P14 Phase 5 vs P15 quarterly re-scan months.
6. P6 tree vs files named in P8, P11, P13 (`templates/`, `requirements.txt`, `.python-version`, `logs/`).
7. `scripts/cron_daily.sh` doubles as the monthly committer with no monthly wrapper defined.
8. Wrapper pushes `HEAD:reports` from whatever branch is checked out, with no fetch/rebase against cloud pushes to the same branch.
9. P7 "Used" table broken.
10. P9 "3,401 rows" cites the verify log directly despite the v2 header rule on note-level marking.

Phase labels, the 21-day denominator, the $20 base ceiling and the Canonical-fact figures are consistent across sections.

## GAP LIST

1. **[P11, P13, P8] MINOR.** Write the Account table to a gitignored `reports/monthly/YYYY-MM.account.md` (or print percentages only) and correct the P13 sentence accordingly.
2. **[P13, P15, P1] MINOR.** State that Max is outside the year-1 $50 ceiling and needs a written P15 decision, not an escalation; set the daily cap to `--max-budget-usd 0.30` or state that the $10 line is enforced by the monthly tally.
3. **[P8, P14] MINOR.** Add to Phase 2a: confirm `--bare` still loads project skills and CLAUDE.md (fallback: logged-in non-bare `-p`); tighten `allowed-tools` to `Bash(python run_daily.py --date today)` and `Bash(python run_daily.py --check)` (same for monthly).
4. **[P14, P6] MINOR.** Change the Phase 4 dependency to "one month of committed daily notes and flags"; make Phase 5 read "months 3, 6, 9, 12"; add `templates/daily.md`, `templates/monthly.md`, `requirements.txt`, `.python-version`, `logs/` to the P6 tree.
5. **[P8, P11] MINOR.** Define `scripts/cron_monthly.sh` (or one parametrised wrapper) with the full monthly command; both wrappers fetch and rebase on `origin/reports` (or push from a `reports` worktree) before pushing.
6. **[P9, P3] MINOR.** Mark "3,401 on retry" note-level or use the report's wording (single-ticker retry fixed the sqlite lock); source "quarterly distributions" from the issuer sheet or mark it an Assumption.
7. **[P9, P11] MINOR.** Round-1 gap 11 partial: move the CAPE lookup to the quarterly re-scan (staleness 100 days) or drop it; it is the only non-automated data input left.
8. **[P7] MINOR.** Move the quantstats paragraph below the "Used" table so the `financial-services` row renders.
