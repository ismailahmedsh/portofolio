# Reviewer 3: risk, compliance and research-integrity review

Date: 2026-11-03. Lens: regulator-minded skeptic and overfitting hunter. Read: framework, report, `plan/plan_v3.md`, four audits, three gap-fill notes and the CSV/verify outputs they cite. No new web research.

## Verdict: APPROVE WITH CONDITIONS

The portfolio part is conservative and well sourced; the toolkit is read-only by construction with a correct compliance posture (personal use, no advice, no broker access). The conditions correct accuracy and trigger wording, not direction.

## Blocking issues

None.

## Material concerns (conditions 1-4; observations 5-8)

1. **Canonical fact 6 misstates its own data (condition).** The report and plan (P2, P10, P12) say the 10-month SMA overlay "costs 1.4-3.3 pts/yr". `gapfill2_data/overlay_results.csv` shows VT SMA10-to-AGG 8.11% vs 8.68% (0.57 pts), ACWI 7.89% vs 8.39% (0.50 pts) and XEQT ABSMOM12-to-ZAG 13.50% vs 14.25% (0.75 pts, 2 switches, drawdown -12.8% vs -17.6%). The honest range is 0.5-3.3 pts, and the best-looking variant (ABSMOM12) was dropped "for simplicity" rather than reported. "Flag, not rule" still stands on DCA mechanics, whipsaw and decay evidence, but a canonical table must not round away the cases that cut against the thesis. Fix: restate fact 6 as "0.5-3.3 pts/yr" and keep ABSMOM12's numbers in the Table H footnote.
2. **Egypt trigger (b) is too narrow (condition).** The "permanent home" test turns on a dwelling being *available* for continuous use, not owned; a family apartment the owner can use at will may satisfy it. Fix: trigger (b) should read "before acquiring, inheriting, or having continuous use of a dwelling in Egypt". Add to the Scenario B row that TFSA contributions while non-resident of Canada attract the 1%/month penalty and that departure tax applies to non-registered holdings; the owner-facing table names neither.
3. **Horizon and emergency fund are assumptions, not Phase 1 checks (condition).** A 100% equity core with a -50% to -65% stress case is only safe if Assumptions 1-2 (15+ year horizon, no withdrawal in 5 years, emergency fund outside the plan) hold, and Phase 1 never asks the owner to confirm them. Fix: make "emergency fund confirmed, horizon written in `plan/changes.md`" the first Phase 1 milestone; if either fails, XGRO applies before the first buy.
4. **The Yahoo path is tolerated, not licensed (condition).** Yahoo's terms bar collection "using any automated means"; a daily scheduled yfinance run is exactly that, personal use or not. Fix: P9 should say the keyless baseline is an unofficial API in a contractual grey zone, EODHD is the licensed route, and a block is expected. The exposure is operational, not legal.
5. **P3 Rule 4 "bring forward up to 3 months of deposits" is a timing rule in a plan that forbids timing.** The round-2 auditor called it "a mild, unsourced timing lever" and still scored P3 at 3. After a -20% leg a further -30% is the historical pattern. Strike it or restrict it to cash already earmarked for the portfolio.
6. **"85-93% of active retail traders lose in every large administrative dataset" is broader than its sources.** SEBI covers derivatives traders, Brazil and Taiwan cover day traders, and the 85% end has no cited source. The thesis does not need the overreach; its three mechanisms are each well cited.
7. **Validation design is sound but honor-system at the edges.** The new-rule gate (frozen publication split, CPCV with embargo, DSR fed the variant count, t > 3, delay stress, live-only evidence) is effectively a "never" gate, which is right for this goal. Weak points: the DSR variant count is self-reported; the flag log is a CSV the owner can rewrite; after 12 months it will hold two to seven changes, so "hit rate" is noise and should be labelled so; the kill trigger "owner notices flags influencing a decision" is self-diagnosis. The recurring auto-buy is the real safeguard.
8. **Plan v3 is unaudited.** Round 2 passed v2 at 41/45 while listing ten new inconsistencies; v3 self-reports closing all. I spot-checked seven (gitignored account file, `--max-budget-usd 0.30`, exact `allowed-tools`, `cron_monthly.sh`, Phase 4 dependency, Phase 5 months, P6 tree); all closed, no new contradictions found.

## Overclaim check

| # | Claim | Source cited | Rating |
|---|---|---|---|
| 1 | SMA overlay costs 1.4-3.3 pts/yr (Canonical fact 6; plan P2/P10) | `overlay_results.csv`, numbers Q4 | **Overstated**: own CSV shows 0.5-0.75 pts for VT/ACWI-to-AGG and XEQT ABSMOM12 |
| 2 | 85-93% of active retail traders lose in every large administrative dataset | SEBI PR 22/2024; Chague et al.; Barber et al. | **Overstated**: populations are derivatives and day traders; 85% uncited |
| 3 | Keyless data path "verified end to end" | `verify_log.md`, tech Q1 | **Overstated in headline**: FRED CSV failed on one of two routes, Stooq dead, cloud egress untested; body states all three |
| 4 | XEQT MER 0.19%, fee 0.17% | BlackRock fact sheet Sep 30, 2026; press release Dec 18, 2025 | Supported |
| 5 | DIY mix tracked XEQT within ~C$1,000 on C$87,000 | `t2_backtest_output.md` | Supported (pre-fee, pre-FWT; weights differ, so a portfolio comparison, not tracking error) |
| 6 | Four of six models lost real money in Alpha Arena | Forklog (secondary) | Fact supported; **overstated as evidence** (17 days, crypto perps, n=6, "exploratory") yet in the bottom line |
| 7 | LLM error rates ~36-40% on expert finance tasks | benchlm.ai, the-decoder (secondary) | Supported, secondary-sourced |
| 8 | Scenario A: Canadian-held ETFs outside Egyptian tax scope | Deloitte Highlights 2025; PwC Aug 2026 | Supported |
| 9 | 31-103CP business trigger not met by own-account research | 2014 CP consolidation | Supported; 2026 text unread and flagged |
| 10 | Monitor runs for $20/month on Pro | claude.com/pricing | **Unsupported as an outcome**: Pro-window sufficiency unmeasured; plan gates it on Phase 2a |

## Audit-integrity judgment

Strict, not rubber-stamped: round 1 of each audit failed or barely passed, research round 2 *lowered* A5 to 2 with a BLOCKING item, and plan round 2 held B5, B7, B13 and B14 at 2 while finding ten new inconsistencies. Increases were mostly earned, with caveats.

- **Justified: A6 repo verification 2 to 3.** Round 1 had eight repos without commit dates from a seed TSV; tech Q3 records stars, push, issues, licence and release for 23 repos via `gh api` with timestamps. The evidence improved where the gap said.
- **Generous: A8 user-context fit 2 to 3.** The Scenario A/B table arrived, but four Scenario B items (centre-of-activities from an EY snippet, foreign dividends, IBKR entity, departure tax) stayed open as gap 5; Egypt is resolved for the base case only, so 2 with a note was the honest score. Likewise B1 feasibility 2 to 3 came from the planner adopting the auditor's own hour estimate: closure by agreement, not evidence.

## Residual risk register

| # | Risk | Likelihood | Impact | Plan mitigation |
|---|---|---|---|---|
| 1 | A -40% to -65% drawdown and the owner sells or stops contributing | High over 15 years | High | M3, stress line, recurring auto-buy; **gap**: emergency fund and horizon unconfirmed before Phase 1 (concern 3) |
| 2 | Residence drifts toward Egypt without the adviser consult | Low to moderate | High: worldwide-income exposure, TFSA penalties, departure tax | 150-day trigger, 120-day flag; **gap**: "home available" and TFSA penalty unstated (concern 2) |
| 3 | Yahoo blocks or breaks the keyless path | Moderate | Low (portfolio unaffected; monitor DEGRADED) | yfinance ladder, EODHD adapter built in Phase 2b, manual NAV last resort |
| 4 | Monitor becomes a timing input (Rule 4, flag "hit rates") | Low to moderate | Moderate: forfeited rebounds, as April 2025 showed | Overlay-as-flag rule, P12 gate, kill trigger; honor-system at the edges (concerns 5, 7) |
| 5 | Forward returns of 1-4% real make M1's 4-12% band and the owner's expectations miss | Moderate | Moderate (disappointment, not loss) | Stress case at 1% real, M1 reviewed only annually; no action rule, which is correct |

## Summary for the owner

1. Buy XEQT every month in the TFSA first, automatically, and never let the monitor or a headline change that; nothing I found undermines this.
2. Before the first buy, write down that your horizon is 15+ years and that a 3-6 month emergency fund sits outside this plan; a 100% equity core is only safe if both are true.
3. Book a cross-border tax consult before you have a home in Egypt available to you (owned or not) or approach 150 days there in any 12 months; the plan's trigger is slightly too narrow today.
4. The report's "trend overlay costs 1.4-3.3 pts/yr" is really 0.5-3.3; the conclusion (show it, never trade on it) holds, but the number should be corrected.
5. The monitor is legally and operationally safe as designed (no broker, no advice, no sharing); its data path is tolerated rather than licensed, so treat a Yahoo outage as expected and keep the EODHD fallback ready.

## Re-review of plan v4 (2026-11-03)

Read: `plan/plan_v4.md` (change table, then P2-P5, P9, P12, P14) and the report's revision line, Bottom line and fact 6.

| # | Item | Status | Pointer |
|---|---|---|---|
| 1 | Canonical fact 6 overlay cost | **CLOSED** | Report fact 6 now "0.5-3.3 pts/yr" citing all SMA10 and ABSMOM12 rows of `overlay_results.csv`; R11 coverage row, plan P2 and P5 agree; XEQT ABSMOM12 (0.75 pts) stays visible |
| 2 | Egypt trigger (b); Scenario B omissions | **CLOSED** | P4 trigger (b) "acquiring, inheriting, or having continuous use of a dwelling", availability named as the treaty test; Scenario B names departure tax (non-registered only) and the 1%/month TFSA penalty; action "stop TFSA and FHSA contributions the day Canadian residence is in doubt" |
| 3 | Horizon and emergency fund gate | **CLOSED** | P14 milestone 1 is a written gate in `plan/changes.md` (3-6 months of expenses, 15+ years, no withdrawal inside 5 years, the 2020/2022 answer) with XGRO on failure; mirrored in P1 M3, P2, P3 |
| 4 | Yahoo path tolerated, not licensed | **CLOSED** | P9 "Licensing posture: tolerated, not licensed" states the ToS conflict, its operational nature and EODHD as the licensed route |
| 5 | Rule 4 bring-forward lever | **CLOSED** | P3 Rule 4 struck; emergency fund never drawn into the portfolio |
| 6 | "85-93%" sentence | **CLOSED** | Report Bottom line and plan P2 quote SEBI 93%, Brazil 1.1%, Taiwan under 1% with their populations; no "85-93" remains outside the change log |
| 7 | Validation honor-system edges | **CLOSED** (note) | P12: hash-chained append-only `flags.csv` verified each run and committed; `experiments/variants.jsonl` logged by the harness; hit rate labelled "not a statistic" below 30 changes. The chain stops careless edits, not a determined owner; git history is the real second record, adequate for a personal tool |
| 8 | v3 unaudited | PARTIALLY CLOSED | v4 is reviewer-checked, not auditor-scored; acceptable at the review stage |

v4 adds no compliance exposure: no broker access, no sharing, no advice language, private reports; one scheduler on the default branch removes the two-writer conflict. Pausing TFSA/FHSA contributions on residence doubt is the right default; RRSP contributions remain permitted for a non-resident with room.

**Final verdict: APPROVE.** Blocking issues: none. Residual risks 1-5 stand; mitigations are now stronger on 1, 2 and 4.

## Review of plan v5, UAE resident (2026-11-03)

Read: `gapfill3_uae_resident_canadian.md` and `plan/plan_v5.md` (change table, P2, P4, P5, P13, P15, Assumptions, Phase 1).

**Source check.** The Article 4(1)(b)(i) reading (UAE-resident individuals are UAE nationals, so no tie-breaker and no s.250(5) route for a Canadian citizen) matches the Justice Laws text quoted and the CRA Folio; "status is factual-only" follows. Part XIII at 25% on XEQT income distributions with no treaty cut is supported; the 36 bps rests on an assumed 90/10 income split and says so. Departure-tax, TFSA 1%/month and RRSP 25% rules are quoted from CRA primary pages. The drag table's inputs are labelled assumptions and Assumption 23 rightly says the ranking is robust, the point estimates not. Two overclaims:

1. **"Canada has no notional-distribution rule for foreign accumulating ETFs" (Q6; P4 step 7a).** Section 94.1 (offshore investment fund property) can impute income at the prescribed rate plus 2% on a non-resident fund interest where a main reason for holding it is to defer Canadian tax; an accumulating UCITS in a taxable account after re-entry is the textbook case. Option (a) "keep VWRA in taxable, no annual inclusion" asserts an outcome the source cannot support. Re-entry is adviser-gated, so not blocking; replace with "s.94.1 exposure to be assessed; VWRD or a Canadian-listed fund may be preferred in taxable on return".
2. **Departure-tax scope (P4 step 2)** says the deemed disposition "covers the Sarwa holdings"; it covers only property owned on the departure date, not positions bought after leaving.

**Residency gate.** Safe in direction: a wrong "resident" answer costs efficiency (Branch B); a wrong "non-resident" answer is the harmful one, and Branch B sends the owner to an adviser at once. Two gaps:

3. **Timing.** Milestone 1a needs the accountant *booked*, not confirmed, before money moves, yet step 5 liquidates Sarwa Invest in the same fortnight; if the facts land in Branch B that is a Canadian taxable disposition. Condition: Sarwa liquidation and the first VWRA buy wait for written confirmation of Branch A; cancelling registered-account buys proceeds immediately.
4. **The departure is probably in the past.** If the departure-year return, T1161 or T1243 was never filed, or TFSA contributions were made since, penalties accrue now (T1161 C$25/day to C$2,500; TFSA 1%/month retroactively). Condition: step 1 adds "state the departure year; if its forms were not filed or any TFSA/FHSA contribution was made since, remediation (Voluntary Disclosures Program if applicable) precedes any new investing".

**New unknowns.** IBKR entity (read from the agreement; product unaffected), UCITS recurring eligibility (whole-share fallback), FHSA on emigration (contributions stopped, on the accountant's list) and AGGU/VAGU (verified only if the gate fails) each have a safe default. Egypt triggers carry over intact, with the correct note that Branch A has no second residence to tie-break against.

**Hidden risk.** A move to a third country re-opens every question here; the P5 residency-change trigger should name "any change of country of residence", not only Canada and Egypt.

**Verdict: APPROVE WITH CONDITIONS.** Blocking issues: none. Conditions: items 1-4.
