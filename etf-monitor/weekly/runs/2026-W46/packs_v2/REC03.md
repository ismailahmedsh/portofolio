# Pillar REC03: Redundancy matrix and live information coefficient by exposure
Definition: Before launch, two redundancy checks:
- Exposure pillars, on the point-in-time panel REC04 reconstructs (sleeves x months, 2003-2026): the time-series average of monthly cross-sectional Spearman correlations (Fama-MacBeth style), with a block-bootstrap confidence interval using blocks of at least 24 months, reporting the effective number of sleeves. A pair whose |rho| is 0.85 or more at the lower confidence bound is merged. Mandatory pairs: EXR06/EXR08, EXR08/FAC01, FAC01/FAC03 (each must be below 0.7, or the lower-weighted pillar becomes record-only), RSK01/RSK03, RSK01/RSK05, RSK03/RSK05, FIT05/FIT06, FIT05/FIT10, FIT06/FIT10.
- Line pillars, the same test across lines within sleeves. Mandatory pairs: DUR01/CST06, CST03/CST04, CST02/TAX03.
Live: rank IC of each family and each record pillar against forward 13, 52 and 156-week returns versus VWRA, one row per exposure, with non-overlapping windows or Newey-West errors.
Low power is admitted (about 8 exposures, 4-5 effective clusters). So the main promotion route is reconstruction in REC04 as a pre-registered variant (N_TRIALS + 1). Live IC above 0 with t above 2 after 36 months is the secondary route. Demotion happens only after 36 months.
Source: REC04 panel; engine score history from 2026-W45; yfinance .L closes (verified). Better when: higher. Informs: record_for_testing.
Week 2026-W46.

## From this week's report
Portfolio limits and context

| Pillar | Reading | Status |
|---|---|---|
| RSK06 Drawdown budget (10 years) | Your mix -24.6% vs world -24.3% (budget -29.3%) | within |
| RSK07 Risk share, world | weight 70%, risk share 68%, ratio 0.98 | within 1.5 |
| RSK07 Risk share, sp500 | weight 20%, risk share 20%, ratio 1.0 | within 1.5 |
| RSK07 Risk share, ndx100 | weight 10%, risk share 12%, ratio 1.16 | within 1.5 |
| FIT07 US look-through weight | Your mix 69.4% vs world 59.9% (tilt limit 69.9%) | within |
| FIT11 Lines held or bought | VWRA | within 4 |
| RSK08 Drawdown now | Your mix -3.3% from its high, world -3.2% from its 52-week high | protocol at -20%: keep depositing |
| MOM04 Core trend flag | VWRA below 10-month average: no; 12-1 momentum +12.3% | off |
| MOM03 Momentum-crash state | world -3.2% from high, 1-month volatility 21.4% | normal |
| REC01 Live record | no fills recorded yet: the live record starts with your first logged buy | |
| REC03 Redundancy | 0 scored pairs with correlation 0.7 or more across groups | no pair at 0.85 or more |

**Your sleeves against the world (MOM05, display only)**

| Sleeve | 4 weeks | 13 weeks | 52 weeks |
|---|---|---|---|
| world | +0.0 pts | +0.0 pts | +0.0 pts |
| sp500 | -0.2 pts | +1.1 pts | +0.2 pts |
| ndx100 | -3.3 pts | -2.6 pts | +1.0 pts |

**Macro context (MAC01-04, never used for decisions)**

- MAC01 Recession indicators: 0.25 pts (2026-11-10); 0.68 pts (2026-11-10); 0.00 (2026-10-01)
- MAC02 Credit and financial stress: 3.34%, 3m change +0.64 (2026-11-09); -0.46 (2026-10-30)
- MAC03 Volatility regime: VIX 25.6; VIX/VIX3M 1.04
- MAC04 Rates, dollar and oil: 2.66%, 3m change +0.23; 121.9, 3m change +2.4%; US$99.6, 3m change +28.9% (2026-11-03)

**Crash windows: shortfall beyond what beta explains (RSK04, record), your sleeves**

| Sleeve | Covid crash | 2022 rate shock | Global financial crisis |
|---|---|---|---|
| world | +0.0 pts | +0.0 pts | +0.0 pts |
| sp500 | +1.0 pts | +1.8 pts | n/a |
| ndx100 | +9.4 pts | -4.8 pts | n/a |

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

