# Final verdict

Date: 2026-11-03

## Rule applied

From 00-framework.md: the pipeline passes when the research audit passes its threshold, the plan audit passes its threshold, and three independent reviewers return a majority APPROVE with no blocking issue. Otherwise the failing stage re-runs.

## Record of cycles

| Stage | Round | Score | Result | Action taken |
|-------|-------|-------|--------|--------------|
| Research audit (A1-A15) | 1 | 38 / 45 | Marginal pass, 12 gaps | Gap-fill round with 3 agents |
| Research audit (A1-A15) | 2 | 44 / 45 | Pass, 10 contradictions | Resolved in report "Canonical facts" |
| Plan audit (B1-B15) | 1 | 37 / 45 | Fail, 3 blocking | Plan v2 |
| Plan audit (B1-B15) | 2 | 41 / 45 | Pass, 8 minor, 10 inconsistencies | Plan v3 |
| Independent review | 1 | 3 x approve with conditions, 3 blocking (engineering) | Fail on blocking rule | Plan v4 plus report correction |
| Independent review | 2 | 3 x APPROVE, 0 blocking | **PASS** | Pipeline complete |

## Reviewer verdicts on plan v4

| Reviewer | Lens | Verdict | Blocking |
|----------|------|---------|----------|
| 1 | Canadian fee-only portfolio practitioner | APPROVE | None |
| 2 | Production agent and data-pipeline engineer | APPROVE | None |
| 3 | Risk, compliance and research-integrity skeptic | APPROVE | None |

## What the approved package says, in brief

- Primary portfolio: 100 percent XEQT.TO, bought on receipt every month, FHSA first if eligible, then RRSP or TFSA by marginal-rate rule, then taxable. Gate before the first buy: emergency fund of 3 to 6 months, 15-plus year horizon, written drawdown tolerance; failing the gate makes XGRO the core.
- Alternative: a four-fund Canadian-listed DIY mix, explicitly labelled as a tilt, considered only above about C$300k.
- Trading bots are rejected on base-rate evidence (regulator and academic datasets, LLM-agent benchmarks); trend and momentum overlays are report flags only, never trade rules.
- Toolkit: Python computes, Claude narrates, a grounding check fails closed, no broker keys, no order placement, a committed deny list for the agent, one local scheduler, reports on the default branch. Cost setup A at about $20 per month with a $50 hard ceiling.
- Egypt: Scenario A (Canadian resident with Egyptian ties) handled; Scenario B (Egyptian residence) sends the owner to a cross-border adviser before any trigger event.

## Residual items the owner should know (non-blocking, recorded by reviewers)

1. Run cost was never measured live (sandbox had no Claude login); it is the first Phase 2a milestone.
2. FRED fetch from plain Python is unverified; macro stays context-only until it is.
3. Questrade pricing is from secondary sources; the plan defaults to Wealthsimple.
4. Egypt Scenario B tax specifics remain partly unverified; the adviser trigger covers this.
5. Plan v4 was reviewer-checked, not auditor-scored; reviewer 3 judged this acceptable at the review stage.

## Addendum 2026-11-03: owner is a Canadian citizen resident in the UAE

The owner disclosed after approval that they live in the UAE, invest through Interactive Brokers and are moving about US$2,500 per month from Sarwa. A third research round (gapfill3_uae_resident_canadian.md) and plan v5 followed.

| Stage | Result |
|-------|--------|
| Gap-fill research round 3 | Canada-UAE treaty residency is limited to UAE nationals, so Canadian status is purely factual; Part XIII withholding 25 percent with no treaty cut; Irish UCITS all-world fund via IBKR at 34-40 bps all-in drag versus 55-80 bps for XEQT via IBKR and about 75 bps for US-listed VT |
| Plan v5 | Two-branch residency gate; Branch A (factual non-resident, expected): VWRA on the LSE in USD, SPYY/ACWD alternative; Branch B (still resident): v4 stands with an adviser engaged immediately |
| Reviewer 1 (portfolio) on v5 | APPROVE WITH CONDITIONS, no blockers |
| Reviewer 3 (risk and compliance) on v5 | APPROVE WITH CONDITIONS, no blockers |
| Post-review patch | All conditions applied in plan_v5.md: departure-tax scope, past-departure filing check, Sarwa sale waits for written Branch A confirmation, s.94.1 on re-entry, will and residual cash, residency trigger for any country |

Reviewer 2 (engineering) was not re-run: the toolkit design did not change beyond tickers, currency and the cron time zone.

Current approved plan: plan/plan_v5.md.
