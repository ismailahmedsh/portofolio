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

Rule tested: Quarterly: sleeves with X >= 55 at two consecutive quarter-ends get a tilt of up to 10% (X 55 -> 0, X 70 -> 10%), total tilt at most 15%, at most 2 of any 12 deposits; candidates EFA, EEM, IWD, IWM, IWN, QUAL, MTUM, USMV, VLUE, EWJ, VGK. Period 2011-12 to 2026-11-11, against your mix, 26 trials counted.

| Execution | Return on your money | Time-weighted | 2012-2016 | 2017-2021 | 2022-2026 | Information ratio | Deflated probability | Beats your mix everywhere |
|---|---|---|---|---|---|---|---|---|
| Your mix (yardstick) | 12.8% | 12.7% | 11.0% | 16.6% | 10.6% | | | |
| Tilts, same month | 12.8% | 12.7% | 11.0% | 16.6% | 10.6% | 0.08 | 0.05 | no |
| Tilts, lagged | 12.8% | 12.7% | 11.0% | 16.6% | 10.6% | 0.14 | 0.08 | no |

**Gate: not passed, so scores stay display-only and every deposit follows your mix.**

## Exposure view: equity groups against the world (X, world = 50)

X combines expected-return signals (20), rewarded factor tilts (40) and crash risk beyond market exposure (40, one-sided, cannot exceed 50). Display only until the REC04 gate passes. The factor priors are assumptions, not estimates.

| Line (group reference) | X | Expected return | Factors | Risk | Beta | Fit with your mix | Name |
|---|---|---|---|---|---|---|---|
| IUMS | 72 | 77 | 91 | 50 | 1.02 | 83 | iShares S&P 500 Materials Sector UCITS ETF USD (Acc) |
| XDWM | 72 | 74 | 96 | 46 | 1.07 | 84 | Xtrackers MSCI World Materials UCITS ETF 1C |
| SXLB | 72 | 77 | 91 | 49 | 1.01 | 83 | State Street SPDR S&P U.S. Materials Select Sector UCITS ETF |
| CPXJ | 70 | 76 | 89 | 47 | 0.99 | 83 | iShares VII PLC - iShares Core MSCI Pac ex-Jpn ETF USD Acc |
| XPXD | 68 | 78 | 96 | 34 | 1.00 | 86 | Xtrackers MSCI Pacific ex Japan Screened UCITS ETF 1C |
| XDWS | 67 | 76 | 93 | 36 | 0.69 | 81 | Xtrackers MSCI World Consumer Staples UCITS ETF 1C |
| IEFQ | 66 | 78 | 92 | 34 | 0.97 | 80 | iShares Edge MSCI Europe Quality Factor UCITS ETF EUR (Acc) |
| IDIN | 64 | 77 | 96 | 26 | 0.74 | 81 | iShares Global Infrastructure UCITS ETF USD (Dist) |
| GGRA | 64 | 71 | 84 | 40 | 0.97 | 68 | WisdomTree Global Quality Dividend Growth UCITS ETF - USD Ac |
| IAUS | 64 | 75 | 88 | 33 | 1.07 | 84 | iShares MSCI Australia UCITS ETF USD (Acc) |
| IEUX | 63 | 78 | 88 | 31 | 1.02 | 80 | iShares MSCI Europe ex-UK UCITS ETF EUR (Dist) |
| MVOL | 63 | 76 | 87 | 32 | 0.71 | 77 | iShares Edge MSCI World Minimum Volatility UCITS ETF USD (Ac |
| HMXJ | 63 | 80 | 85 | 32 | 0.97 | 83 | HSBC MSCI Pacific ex Japan UCITS ETF |
| UDVD | 63 | 71 | 94 | 27 | 0.86 | 81 | State Street SPDR S&P US Dividend Aristocrats UCITS ETF Dis |
| WHEA | 63 | 75 | 85 | 34 | 0.75 | 78 | State Street SPDR MSCI World Health Care UCITS ETF |
| SEMU | 19 | 20 | 2 | 36 | 1.34 | 59 | Amundi MSCI Semiconductors UCITS ETF Acc |
| XNGI | 20 | 21 | 1 | 39 | 1.09 | 49 | Xtrackers MSCI Next Generation Internet Innovation UCITS ETF |
| AIAI | 22 | 24 | 7 | 36 | 1.30 | 58 | L&G Artificial Intelligence UCITS ETF |
| EQQU | 22 | 26 | 3 | 39 | 1.08 | 42 | Invesco EQQQ NASDAQ-100 UCITS ETF |
| CNDX | 22 | 26 | 3 | 39 | 1.08 | 42 | iShares NASDAQ 100 UCITS ETF USD (Acc) |
| WTEC | 23 | 20 | 4 | 42 | 1.15 | 45 | State Street SPDR MSCI World Technology UCITS ETF USD Acc |
| XDWT | 23 | 20 | 5 | 42 | 1.14 | 45 | Xtrackers MSCI World Information Technology UCITS ETF 1C |
| XLKS | 23 | 20 | 4 | 44 | 1.12 | 45 | Invesco Technology S&P US Select Sector UCITS ETF |

Your sleeves: world 50, S&P 500 37, Nasdaq-100 22. A low X for Nasdaq-100 reflects growth tilt (negative value loading) and deeper crashes than its beta implies, not a sell signal.

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

