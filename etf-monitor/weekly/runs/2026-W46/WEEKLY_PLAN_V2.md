# Weekly plan, 2026-W46 (engine v2)

## 1. Decisions

| Item | Decision |
|---|---|
| This month's order | Buy **3 x VWRA.L** at about US$188.96, **US$568.58** including the US$1.70 commission. US$110.16 is left over. |
| Why this line | World is furthest below its 70% target (gap US$475.11 vs US$135.75 and US$67.87). VWRA.L is the world line. |
| Line switch | None. No structural event (S1) and no cost switch (S2: VWRA vs IWDA gap 7.7 bps, below 15 bps). |
| Sell anything | No. Nothing is held, and S0 forbids selling on scores, drawdown or news. |
| Timing | Normal LSE hours. Avoid US data minutes, 17-18 Nov (Nvidia) and 26-27 Nov. Execution only: do not push the deposit past the month. |

**What to watch**

| Watch | Trigger |
|---|---|
| Confirm one S&P 500 and one Nasdaq-100 line in IBKR, add them plus FWRA.L and ACWD.L to `orderable` | Before the December deposit (see the dissent below on which lines) |
| Log the fill in config/portfolio_v2.yaml (`fills` / `positions`) | Right after the order fills |
| Rebuild: re-anchor VWRA-as-yardstick wording and logic to the 70/20/10 mix | The rebuild you asked for, before any score moves money |
| Fix v2/packs_v2.py line 24 KeyError 'RSK01' | Next engine run |
| Data fixes (CSWG.L and IB01.L price jumps, RSK01 code, short-history exposures) | Part of the rebuild |
| VWRA fee correction 0.19% to 0.14% in the universe file | Next data update |
| FTSE review (21 Dec), Nasdaq-100 reconstitution (11-21 Dec), MSCI review (30 Nov), China export-control pause end (2027-01-10), UAE CRS 2.0 (2027-01-01) | Each date |
| Nvidia results and board decision, AI credit stress, VIX 25.6 inverted | Context only. Cannot move or sell money. |

## 2. Was the committee unanimous?

**No.** After 1 round, four of five members approved (rules, risk, macro, quant). The UAE execution and tax member dissented for three reasons:

1. **Residency gate.** Plan v5 (Milestone 1a) says the first buy waits until your residency facts (Branch A) are recorded in plan/changes.md with your accountant's written confirmation, plus the Phase 1 statement (horizon, no withdrawal within 5 years, emergency fund). No such record exists. This is your first buy.
2. **December routing is wrong.** World is still furthest below target in December (about US$382 vs US$271), so December goes to VWRA again. CSPX (US$819 a share) cannot fit one month's cash. Pick VUAA.L (US$146.92, cheaper) and XNAS.L (US$65.35, cheapest) instead of CSPX and CNDX.
3. **Leftover cash is not carried.** The engine reads it only from `extra_cash_usd`, missing from portfolio_v2.yaml. Set it to your IBKR USD balance after the fill.

**Because the vote was not unanimous, the default under DECISION_RULES_V2.md applies: the engine's v2_plan.json order (3 x VWRA.L, US$568.58) and no sells.** Point 1 is your call, not the engine's: if the Branch A confirmation is not on record yet, hold the USD at IBKR until it is.

## 3. Why

- **Rule 1:** one order to the sleeve furthest below target. On an empty portfolio that is world.
- **Rule 2:** scores stay display-only. **Backtest: the REC04 gate failed (deflated probability 0.001, info ratio about -0.2, tilts end near US$554k vs US$558.5k for your mix), so no tilt.**
- **Families:** cost says VWRA is the cheapest world line (fee now 0.14%); risk says all limits pass (drawdown -3.3% vs -20% trigger); events found nothing structural.

**Your question: why VWRA as the default and yardstick?** The wording you quoted comes from PILLARS_V2.md line 7 and the pillars_v2.json rationale, both written before your 2026-11-12 decision. That decision already made the 70/20/10 mix the default and yardstick in GOAL.md and CHANGELOG.md. VWRA got the role under a burden-of-proof rule: no rule had beaten simply holding the world after costs, so the world was the "no-edge" baseline. It was never about returns. Since 2003, 100% world ended lowest (US$729,598 vs US$886,835 for the mix), but that is hindsight.

**Should there be a default?** As a fallback line so a deposit is never skipped: yes, but it should be the cheapest line in the most underweight sleeve that passes every gate, with VWRA only as a last-resort backstop. As a yardstick: it should be your mix. The rebuild must change that wording plus X, MOM05, RSK08, FIT07, RSK01 and RSK06, which still anchor to the world. Each formula change is a new trial, re-tested against the mix.

## 4. Five key news facts

1. **5 Nov:** SOX fell 12.25%, 38.4% below its June record. ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/chip-stocks-just-had-second-140243882.html))
2. **8 Nov:** Nvidia's board opened an investigation into reports about its CEO. ([Nvidia IR](https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx))
3. **6 Nov:** CoreWeave 2032 notes yielded above 16%; CDS above about 1,289bp. ([CNBC](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html))
4. **11 Nov:** CoreWeave Q3 revenue +168%, backlog US$132.5bn, but debt up to US$46.9bn. ([Seoul Economic Daily](https://en.sedaily.com/world/2026/11/11/coreweave-beats-estimates-but-debt-costs-mount-as-bond))
5. **VWRA fee cut** from 0.19% to 0.14%, effective 2026-07-28. ([Vanguard](https://www.nl.vanguard/professional/insights/were-lowering-fees-on-one-of-our-most-popular-etfs))

## 5. Structural events (EVT01-EVT10)

| Pillar | Finding | Severity |
|---|---|---|
| EVT01 Corporate actions | Nothing found | 0 |
| EVT02 Fees and structure | VWRA fee cut (favourable, data fix needed) | 0 |
| EVT03 Satellite thesis | S&P 500 and Nasdaq-100 cases intact | 0 |
| EVT04 Index methodology | No rule changes | 0 |
| EVT05 Issuer health | DWS rebrand, no product change | 0 |
| EVT06 Tax and legal | No adverse change | 0 |
| EVT07 Sanctions and access | China export-control pause to 2027-01-10 | 0 |
| EVT08 Broker | No IBKR incident | 0 |
| EVT09 Calendar | Execution dates only | 0 |
| EVT10 Market assumptions | No new sets | 0 |

EVT01 and EVT05 mean "nothing found", not "confirmed clear".

## 6. What the agents did

2 pillar agents, 1 pillar investigation round, 1 news round with 2 explorers, 3 family judges and 1 committee round: **33 agents in total**.
