# Pillar REC07: Owner policy-mix test with exact live routing
Definition: src/rec07.py (to move from the scratchpad and build) writes runs/rec07_latest.json. It tests the owner's policy_targets (and 4 standard mixes) against the world alone, on adjusted total returns of US-listed proxies before investor-level withholding. This slightly favours the higher-yield world proxy and is disclosed.
It simulates the exact live routing:
- starting from the owner's current VWRA balance in positions, or both US$0 and US$20,000 while positions are missing;
- MONTHLY = 681, k-month batching, the US$2 FX minimum, US$1.70 commission and the 3(g) ladder cost;
- whole shares;
- the rolling-12 flow cap;
- largest-gap routing, the second-order rule and the 4-line limit;
- both timings.
Periods: 2003-07, 2008-14, 2015-19, 2020-26 and full, on the single ELG07 world reference. It reports money-weighted return, worst rolling 60-month gap and worst drawdown against the world, plus the deflated information ratio as in REC04. A policy routes money only if it beats the world in every period under both timings. Re-run quarterly and whenever policy_targets change.
Gate (post-audit): a policy routes money only if it beats a VWRA-only portfolio by at least 0.25 points a year money-weighted in every period under both timings, with a deflated information-ratio probability above 0.95 counting every policy version in REC07_TRIALS (added to N_TRIALS and logged in CHANGELOG.md).
Source: yfinance VT, SPY, QQQ, EFA, EEM, EWC monthly adjusted closes (verified); ^NDX splice; Ken French market series for the ELG07 world reference before VT (verified). Better when: higher, and positive in every period. Informs: portfolio_mix.
Week 2026-W46.

## From this week's report
Your mix against the alternatives (REC07, information)

2008-07 to 2026-11-11, deposits of US$678.74 a month routed to the sleeve furthest below target, US$1.70 commission and 10 bps spread per buy. Proxies: VT world, SPY S&P 500, QQQ Nasdaq-100 (US-listed, dividend-adjusted, before UAE withholding). Past leadership is not a forecast.

| Mix | Final value | Paid in | Return on your money | Time-weighted | Worst drop | Worst year | 2008-2014 | 2015-2019 | 2020-2026 |
|---|---|---|---|---|---|---|---|---|---|
| Your mix 70/20/10 | US$540,112 | US$150,000 | 12.6% | 10.4% | -41% | -31% | 7.6% | 10.1% | 13.4% |
| 100% world | US$460,508 | US$150,000 | 11.2% | 8.8% | -44% | -32% | 5.4% | 8.7% | 12.1% |
| 100% S&P 500 | US$654,719 | US$150,000 | 14.4% | 12.2% | -42% | -28% | 9.9% | 11.5% | 14.8% |
| 100% Nasdaq-100 | US$1,088,982 | US$150,000 | 18.9% | 16.8% | -41% | -35% | 14.5% | 16.6% | 19.2% |
| 80/10/10 | US$519,067 | US$150,000 | 12.2% | 9.8% | -44% | -32% | 6.3% | 9.7% | 13.2% |
| 60/25/15 | US$573,157 | US$150,000 | 13.2% | 10.8% | -43% | -33% | 7.8% | 10.6% | 13.9% |
| 50/30/20 | US$608,101 | US$150,000 | 13.7% | 11.5% | -42% | -31% | 8.6% | 11.1% | 14.4% |

## Pillar coverage this week

63 of 100 pillars are computed by code this week and 10 are scored by the event agents in the weekly workflow; the rest are listed below.

| Family | Built and computed | Agents | Not built yet | Unverified source |
|---|---|---|---|---|
| ELG | ELG01, ELG02, ELG03, ELG04, ELG05, ELG06, ELG07, ELG08, ELG09, ELG10 | - | - | - |
| CST | CST01, CST02, CST04, CST06, CST08, CST10 | - | CST03 | CST05, CST07, CST09 |
| TAX | TAX01, TAX03, TAX05 | - | - | TAX02, TAX04 |
| DUR | DUR01, DUR02, DUR04, DUR06 | - | - | DUR03, DUR05, DUR07, DUR08 |
| EXR | EXR02, EXR08 | - | EXR03, EXR04, EXR06, EXR11, EXR12 | EXR01, EXR05, EXR07, EXR09, EXR10 |
| FAC | FAC01, FAC02, FAC03, FAC04, FAC05 | - | - | - |
| RSK | RSK01, RSK02, RSK03, RSK04, RSK05, RSK06, RSK07, RSK08 | - | - | - |
| CON | CON04, CON05 | - | CON01, CON02, CON03 | - |
| FIT | FIT01, FIT02, FIT03, FIT04, FIT05, FIT06, FIT07, FIT10, FIT11 | - | FIT08, FIT09 | - |
| MOM | MOM01, MOM02, MOM03, MOM04, MOM05 | - | - | - |
| REC | REC01, REC02, REC03, REC04, REC07 | - | - | REC05, REC06 |
| MAC | MAC01, MAC02, MAC03, MAC04 | - | - | - |
| EVT | - | EVT01, EVT02, EVT03, EVT04, EVT05, EVT06, EVT07, EVT08, EVT09, EVT10 | - | - |

