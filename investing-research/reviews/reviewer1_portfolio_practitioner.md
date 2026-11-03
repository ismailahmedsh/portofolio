# Reviewer 1: portfolio practitioner (Canadian fee-only, evidence-based lens)

Date: 2026-11-03. Documents read: `00-framework.md`, the research report, `plan/plan_v3.md`, `audits/research_audit_round2.md`, `audits/plan_audit_round2.md`. No new research; judgments from the documents and my own practice knowledge.

## Verdict: APPROVE WITH CONDITIONS

The portfolio part is what I would put in front of a client with this profile: one all-equity, Canadian-listed, internally rebalanced fund, bought on receipt, TFSA-sheltered, left alone. The conditions below are account-order and tax-record details that cost money if left as written, not errors in the core.

## Blocking issues

None.

## Material concerns (non-blocking)

1. **P4 account order puts FHSA after TFSA and RRSP after both, with no marginal-rate test.** For an eligible first-time buyer the FHSA dominates: deductible going in, tax-free coming out for a home, and it rolls into the RRSP without using RRSP room if no home is bought. Room accrues only from the year the account is opened (max $8,000 carry-forward), so delay is lost room. The RRSP-vs-TFSA question depends on marginal rate now versus in retirement; above roughly the second federal bracket RRSP-first is often better. Fix: "FHSA first if eligible; then TFSA or RRSP by marginal rate, TFSA when in doubt."
2. **P3 Rule 5 and P4 step 5: the taxable-account ACB ledger omits reinvested (phantom) distributions.** XEQT and the sleeve ETFs regularly pay non-cash reinvested capital-gains distributions that raise ACB. A ledger that records only buys and DRIP will understate ACB and overstate gains on sale. Fix: add a yearly row from the T3/issuer tax breakdown per taxable holding.
3. **P2 DIY alternative (45/30/10/15) is presented as co-equal when its evidence is weaker and its US weight is a tilt.** Normalised ex-Canada it is 53% US / 35% EAFE / 12% EM against a market of roughly 64/26/10. The plan calls it an owner diversification choice while citing forecasters' ex-US edge; that is a forecast-driven tilt by another name. Either use XEQT or VEQT weights, or state plainly that it is a deliberate ex-US overweight.
4. **P4 step 4 RRSP switch to VTI/VXUS at C$100,000 is not worth the plumbing.** Roughly 20 bps on C$100,000 is C$200 a year for a USD account, FX conversions, a second ledger, and US-situs estate-tax exposure the plan never mentions. Wealthsimple Core cannot do Norbert's Gambit cleanly (no free USD account, journaling by request). I would move this to C$250,000 or more and only at IBKR.
5. **Cost framing is inconsistent.** The plan rejects a DIY mix for 6-7 bps (about C$60-70 a year on C$100,000) and then budgets $20/month, about 24 bps on the same balance, for a monitor the plan itself says adds no investment value. If the owner already pays for Claude Pro the marginal cost is zero; say so, otherwise the monitor fails its own cost logic until assets are several hundred thousand.
6. **M3 (-50% to -65% tolerated) is asserted, not tested.** No owner has a known tolerance until they have lived a drawdown. Assumption 2 and the XGRO fallback exist, but the plan should require a written answer to "what did you do in 2020 and 2022" before choosing 100% equity, and should default to XGRO if the answer is "sold" or "never invested".
7. **Rule 4's "bring forward up to 3 months of deposits" at -20% is a timing rule** in a plan that forbids timing rules. The evidence it cites (lump sum beats waiting) argues for investing cash you have, not for scheduling extra buys on a drawdown signal. Strike it or cap it at money already idle.
8. **The FWT drag is quoted at 15 bps with 22 bps as the alternative; I would plan at 20-25.** The independent calculator the report cites gives 22; the 15 is an own calculation. Nothing in the plan changes at either figure, but M4's ceiling should use the higher number.

## Three things the work gets right that most DIY investors get wrong

1. **Invest the deposit the day it lands.** The Vanguard 68%/70% lump-sum evidence is applied as a rule, with a recurring buy as the mechanism, so there is no decision to get wrong.
2. **Account placement and withholding tax are priced in basis points next to the MER, and the DIY-vs-all-in-one choice is settled by that arithmetic plus behaviour, not by fee-shopping.** The XUU-wraps-ITOT correction in round 2 is exactly the kind of structural fact retail investors get backwards.
3. **Trend and sentiment overlays are backtested on the actual candidates, charged for switches, and shown losing (1.4-3.3 points a year, April 2025 whipsaw costing 6.5 points), then demoted to a report flag.** Unhedged foreign equity as the Canadian's shock absorber (2022: XEQT -10.9% vs S&P -18%) is also correctly identified.

## Portfolio-specific judgment

**100% XEQT as primary:** yes, for a 15+ year horizon with no withdrawals inside five years and a demonstrated ability to hold through a loss. The lifecycle evidence and the 30/70 home-bias work both land on this product. My deviation is procedural (concern 6): make the drawdown-tolerance answer a gate, not an assumption. XEQT over VEQT is a coin flip; the MER edge is real today and the direct EM sleeve is a small plus.

**DIY alternative:** sensible as a concept, badly specified in weight (concern 3). I would delete it from the plan until the C$300,000 trigger and, when it fires, use XEQT's own weights so the fund remains the benchmark.

**FWT placements:** the structural claims are right (Canadian-listed wrap and direct are identical in registered accounts; US-listed in RRSP is the only saving; taxable is near-zero after the foreign tax credit). The XIC-to-taxable-first rule in the DIY case is correct. Account order is the problem (concern 1), and the RRSP switch threshold is too low (concern 4).

**Egypt handling:** adequate and appropriately humble. Scenario A is correctly identified as "nothing changes"; the 150-day adviser trigger with a buffer is the right design; the plan correctly refuses to route anything through an Egyptian broker. I would add one line: stop TFSA contributions the day Canadian residence is in doubt (1%/month penalty for non-residents), since that is the one self-inflicted wound an adviser cannot undo.

**Contribution and rebalancing rules:** Rules 1, 2, 3, 5, 6 and 7 are sound; the 20% relative bands with contribution-only repair are what I use. Rule 4 needs the edit in concern 7.

**Monitor:** as a skeptic of AI tooling, I accept it only because the plan makes it optional, read-only, deterministic on numbers, change-only by default, and killable the moment it tempts a timing decision. I would run the monthly review only and drop the daily note; the plan permits this (Assumption 9) and should make it the default.

## Process judgment

The research-audit-plan-audit cycle earned its keep on structure and consistency. **Caught:** the round-1 claim that XUU holds US stocks directly, which would have made the DIY case look structurally better than XEQT in registered accounts; also the v2 leak of account balances into a cloud-cloned `reports` branch. **Missed:** the entire account-ordering question (FHSA first, RRSP-vs-TFSA by marginal rate) and phantom-distribution ACB, because both audits scored the plan against the research rather than against Canadian planning practice; a consistency audit cannot find what the research never asked. The 15 research pillars had no pillar for "which registered account first", so three rounds of auditing could not surface it.

## Summary for the owner

1. Buy XEQT every month on payday with a recurring order; the research and plan support this, and nothing else in the documents beats it.
2. Open the FHSA first if you could ever buy a first home, then TFSA or RRSP by your tax bracket; the plan's TFSA-RRSP-FHSA order should be reversed in that respect.
3. Ignore the DIY mix and the RRSP US-listed switch until you have well over C$250,000; both save less than they cost in attention.
4. Keep a tax ledger in any taxable account that includes reinvested distributions, not only your buys.
5. Treat the monitor as a journal, not an adviser; monthly only, and shut it off the first time it makes you want to change a contribution.

## Re-review of plan v4 (2026-11-03)

Read the "Changes from v3 (post-review)" table and verified each item in P1, P2, P3, P4 and P14 of `plan/plan_v4.md`.

| My concern | Status | Pointer |
|---|---|---|
| 1. Account order, marginal-rate test | CLOSED | P4 step 2 (FHSA first, room accrues only once opened), step 3 (RRSP first when current marginal rate exceeds expected retirement rate, TFSA when in doubt, recorded in `plan/changes.md`); P2 primary table; P3 Rule 2 step 1; `accounts.yaml` `account_order` |
| 2. Phantom distributions in ACB ledger | CLOSED | P3 Rule 2 step 3 and Rule 5 (`kind=phantom` row per taxable holding per year from T3); P4 step 5 |
| 3. DIY mix presented as neutral | CLOSED | P2 heading and intro now say "deliberate US-underweight, EAFE/EM-overweight tilt", 53/35/12 vs 64/26/10 stated, forecaster citation removed, XEQT-weight variant is the default; Assumption 13 |
| 4. RRSP US-listed switch at C$100k | CLOSED | P4 step 4: C$250,000, IBKR only, estate-tax exposure and Wealthsimple's Norbert's Gambit limitation named; Assumption 14 |
| 5. Cost framing | CLOSED | P13 Cost setups: marginal cost $0 if Pro already paid, else ~24 bps on C$100,000, monitor paid for as a journal, never as an input |
| 6. Drawdown tolerance asserted | CLOSED | P14 Phase 1 milestone 1: written gate (emergency fund figure, horizon, 2020/2022 answer) before any account is funded; failure makes XGRO the core from the first buy; P1 M3; Assumption 2 |
| 7. Rule 4 bring-forward lever | CLOSED | P3 Rule 4: struck, invest-on-receipt only |
| 8. FWT 15 vs 22 bps | CLOSED (no change needed) | P1 M4 already computed at 22 bps (41 bps all-in, 45 ceiling); I accept that |

Two residual notes, neither a condition: the marginal-rate rule of thumb ("second federal bracket") is a reasonable shortcut but should be revisited once the owner knows whether a pension adjustment or OAS clawback applies in retirement; and the P2 DIY weights are still carried, which is fine now that they are labelled a tilt and the XEQT-weight variant is the default. The reviewer-2 restructuring (single local scheduler, settings-level deny list, assembly step outside the model) also reduces the one monitor risk I cared about, which is the model nudging a contribution decision.

**Final verdict: APPROVE.**

Blocking issues: None.
