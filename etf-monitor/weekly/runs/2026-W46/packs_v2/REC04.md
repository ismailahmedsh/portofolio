# Pillar REC04: Exact-rule backtest and score-target gate
Definition: src/backtest.py re-runs the exact live exposure rule monthly: the X pillars and weights under the frozen config hash; X smoothed as the mean of the last 3 month-end values (the same definition live and in the backtest); the clip((X-55)/15) target, hysteresis, the satellite limits and the constraints.
Settings:
- MONTHLY = 681, the US$2 FX minimum, the US$1.70 commission, k-month batching per allocation 3(a), whole shares and the rolling-12 flow cap;
- both execution timings;
- expanding windows with Ken French and FRED release lags (revised vintages, disclosed), point-in-time stress windows, the single ELG07 world reference, the ^NDX splice and the dated frozen region mixes.
Periods: 2003-2014 (holdout; primary out-of-sample for EXUS and EIMI only, because REC07 already viewed it for the S&P 500 and Nasdaq-100), 2015-19, 2020-26 and full. A per-sleeve availability table sets each sleeve's start (series start + 60 months for FAC and EXR08, + 120 months for RSK). Sleeves without a passing splice are excluded and named.
Gate: a positive money-weighted excess over the world in every period under both timings, AND a deflated Sharpe probability above 0.95 computed on the monthly active return (strategy minus world reference, i.e. an information ratio), at N_TRIALS of 26 or more. The 26 are: 8 existing strategies, 4 design tilts, 4 REC04 variants, 5 REC07 mixes, 3 audit-round revisions informed by the 2015-2026 backtest, the b_j = 0 variant and the EIMI Emerging-factor sensitivity run; add 1 per further variant. dsr() in src/backtest.py must be patched to accept an excess-return series.
Until the gate passes, X sets no targets.
Source: Engine; Ken French; BIS/FRED with fallbacks; yfinance; runs/backtest_latest.json (current file uses MONTHLY = 2500 and absolute Sharpe; to be re-run) (verified). Better when: gate_pass true. Informs: record_for_testing.
Week 2026-W46.

## From this week's report
May scores move money yet? (REC04 gate)

Rule tested: Quarterly: a sleeve qualifies when its X (3-month average) is 55 or more at two consecutive quarter-ends and its expected alpha against your mix is positive; target = band max x clip((X - 55) / 15), 0 or at least 5%, changes of 2.5 to 5 points a quarter, total tilt at most 15%, at most 2 of any 12 deposits. Candidates: developed ex-US (EFA, band 10%), emerging markets (EEM, band 7.5%). Factor and small-cap sleeves excluded: no proxy passes the splice test. Period 2008-01 to 2026-11-11, against your mix, 26 trials counted. The deflated probability assumes the information ratios of the 26 trials spread by 0.25 a year; this is an assumption, not a measurement.

| Variant | Return on your money | 2008-2014 | 2015-2019 | 2020-2026 | Information ratio | Deflated probability | Beats your mix by 0.25+ points every period |
|---|---|---|---|---|---|---|---|
| Your mix (yardstick) | 12.4% | 12.2% | 10.4% | 13.7% | | | |
| Tilts, with priors, same month | 12.3% | 12.2% | 10.4% | 13.6% | -0.24 | 0.00 | no |
| Tilts, with priors, one month later | 12.4% | 12.2% | 10.4% | 13.6% | -0.21 | 0.00 | no |
| Tilts, priors = 0, same month | 12.4% | 12.2% | 10.4% | 13.7% | 0.00 | 0.00 | no |
| Tilts, priors = 0, one month later | 12.4% | 12.2% | 10.4% | 13.7% | 0.00 | 0.00 | no |

Latest smoothed X: exus 65.0, eimi 48.8.

**Gate: not passed, so scores stay display-only and every deposit follows your mix.** With priors set to 0, expected alpha against your mix is exactly zero, so the prior-free variants can never qualify and equal your mix: any qualification comes from the assumed priors, not from estimated returns. Only the with-priors variants decide the gate.

## Exposure view: equity groups against the world (X, world = 50)

X combines expected-return signals (20), rewarded factor tilts (40) and crash risk beyond market exposure (40, one-sided, cannot exceed 50). Display only until the REC04 gate passes. The factor priors are assumptions, not estimates.

| Line (group reference) | X | Expected return | Factors | Risk | Beta | Fit with your mix | Name |
|---|---|---|---|---|---|---|---|
| XDWS | 74 | 77 | 99 | 47 | 0.57 | 85 | Xtrackers MSCI World Consumer Staples UCITS ETF 1C |
| IUCS | 74 | 72 | 99 | 50 | 0.54 | 86 | iShares S&P 500 Consumer Staples Sector UCITS ETF USD (Acc) |
| GLRA | 74 | 80 | 94 | 50 | 1.05 | 78 | SPDR Dow Jones Global Real Estate UCITS ETF USD (Acc) |
| SXLP | 74 | 74 | 99 | 47 | 0.54 | 86 | State Street SPDR S&P U.S. Consumer Staples Select Sector UC |
| DPYA | 71 | 80 | 89 | 50 | 0.94 | 81 | iShares Developed Markets Property Yield UCITS ETF USD (Acc) |
| EPRA | 71 | 80 | 87 | 50 | 0.93 | 81 | Amundi FTSE EPRA NAREIT Global UCITS ETF Acc |
| IEFQ | 69 | 76 | 89 | 46 | 0.94 | 79 | iShares Edge MSCI Europe Quality Factor UCITS ETF EUR (Acc) |
| IUMS | 69 | 78 | 83 | 50 | 1.01 | 83 | iShares S&P 500 Materials Sector UCITS ETF USD (Acc) |
| SXLB | 69 | 78 | 83 | 50 | 1.00 | 82 | State Street SPDR S&P U.S. Materials Select Sector UCITS ETF |
| VERG | 69 | 66 | 88 | 50 | 1.03 | 78 | Vanguard FTSE Developed Europe ex UK UCITS ETF Accumulation |
| JPGL | 68 | 64 | 88 | 50 | 0.84 | 74 | JPM Global Equity Multi-Factor UCITS ETF USD Acc |
| VEUA | 68 | 61 | 90 | 50 | 1.00 | 78 | Vanguard FTSE Developed Europe UCITS ETF EUR Accumulation |
| IUUS | 68 | 44 | 97 | 50 | 0.53 | 87 | iShares S&P 500 Utilities Sector UCITS ETF USD (Acc) |
| GGRA | 67 | 65 | 86 | 50 | 0.90 | 68 | WisdomTree Global Quality Dividend Growth UCITS ETF - USD Ac |
| IEUX | 67 | 75 | 88 | 41 | 1.02 | 78 | iShares MSCI Europe ex-UK UCITS ETF EUR (Dist) |
| XLES | 26 | 23 | 36 | 16 | 1.09 | 79 | Invesco Energy S&P US Select Sector UCITS ETF |
| SXLE | 27 | 23 | 39 | 18 | 1.06 | 79 | State Street SPDR S&P U.S. Energy Select Sector UCITS ETF |
| IUES | 27 | 23 | 39 | 17 | 1.04 | 79 | iShares S&P 500 Energy Sector UCITS ETF USD (Acc) |
| WNRG | 29 | 26 | 41 | 19 | 0.92 | 83 | State Street SPDR MSCI World Energy UCITS ETF |
| WFIN | 32 | 34 | 36 | 26 | 1.02 | 67 | State Street SPDR MSCI World Financials UCITS ETF USD Acc |
| CNDX | 32 | 25 | 27 | 41 | 1.00 | 43 | iShares NASDAQ 100 UCITS ETF USD (Acc) |
| XLKS | 32 | 20 | 28 | 43 | 1.05 | 45 | Invesco Technology S&P US Select Sector UCITS ETF |
| XDWT | 33 | 20 | 31 | 42 | 1.08 | 44 | Xtrackers MSCI World Information Technology UCITS ETF 1C |

Your sleeves: world 50, S&P 500 40, Nasdaq-100 32. A low X for Nasdaq-100 reflects growth tilt (negative value loading) and deeper crashes than its beta implies, not a sell signal.

## Pillar coverage this week

63 of 100 pillars have code that computes them this week (some as record or context with weight 0, as the spec defines) and 10 are scored by the event agents in the weekly workflow; the rest are listed below with the reason.

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

