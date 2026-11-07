# Pillar audit (families A-I, 90 pillars), 2026-W45

**Verdict: NOT FIT.** The weekly decisions are sound, but that is because `DECISION_RULES.md` ignores the composite score. The pillar set does not measure what those decisions depend on. About 60% of the weight sits on cross-sectional price history of US-listed proxies, and the backtest already shows that has no edge. The things that matter for a UAE holder of an Irish UCITS line are barely measured or are measured on the wrong instrument: the line's TER, tracking difference, LSE spread, withholding drag, fund size and flows, overlap with the core, and long-horizon expected return. A rebuild along the lines below would make it fit.

Scope: families A-I as computed by `src/pillars.py`. The J news family is not in scope, but it is mentioned where it affects the weights.

## 1. Criteria

| # | Criterion | Score (0-3) | Evidence |
|---|---|---|---|
| 1 | Relevance to the four decisions | 1 | The composite cannot judge the core. S6 never triggered, VT ranks 51 of 200, and seven pillars are mechanically fixed for VT: B01-B04 = 0 excess, B09 = 0, C08 = 0 (correlation with itself), C09 = 100. Decisions 1 and 3 run on three hand-coded flags, of which only G01 (and that via the wrong fee) comes from a pillar. Decision 2 has satellite share at 0. Only G08-G10 bear directly on the owner's goal. |
| 2 | Evidence base at the horizon used | 1 | Supported: cost (Sharpe 1991; Morningstar fee studies) and 3-12 month momentum (Moskowitz-Ooi-Pedersen 2012), although the latter decayed after publication (McLean-Pontiff 2016) and failed this system's own gate (S3). Contrary-signed: 1-week and 1-month returns (short-term reversal, Jegadeesh 1990), 5-10 year CAGR (long-term reversal, De Bondt-Thaler 1985), "lower volatility is better" across asset classes (low-volatility evidence holds within equities, Frazzini-Pedersen 2014, while across asset classes lower volatility means lower expected return), and the Fed model I06 (Asness 2003). No support: OBV, Chaikin, volume spikes (Park-Irwin 2007 find the edge eroded) and the H-bucket sensitivity table (hand-set, untested). Persistence of past Sharpe ratios is weak (Carhart 1997). |
| 3 | Non-redundancy | 1 | 59 pairs have \|rho\| >= 0.85, leaving 52 independent signals out of 77 non-constant pillars, and 21 principal components explain 90% of variance. B01-B04 are **rank-identical** to A02-A05: excess over VT subtracts a constant, so the scores differ by exactly 0. G10 = 1 - G08 exactly. G03 and F06 have rho 0.95. Momentum enters through A (10 pillars), B (10), E01 (rho 0.87 with A05) and the 6-12 month parts of D, so roughly a quarter of the weight is one factor. |
| 4 | Coverage of what matters | 1 | Missing: TER, tracking difference and spread of the **UCITS line**; look-through withholding; fund size, flows and closure risk on the UCITS fund; overlap and active share vs VWRA; country and sector weights vs world capitalisation; currency exposure; factor loadings; marginal risk contribution; CMA or CAPE expected returns; index-methodology and issuer events; securities lending and replication; bond YTM. The core's named alternative (SPYY/ACWD) and FWRA are not in the universe. |
| 5 | Data quality and availability | 1 | Prices are fine for what they measure, but they are the wrong instrument. Only 29 of 200 ETFs map to a live UCITS line, and those 29 cover 18 distinct lines. The 18 `.L` price series are already cached and used only for a "has 250 rows" test. Mapping errors: USMV and ACWV both go to MVOL (MSCI World Min Vol); IOO (Global 100) and VT both go to VWRA, which gives VWRA two different scores (ranks 37 and 51); VTI and ITOT go to CSPX (S&P 500); IAGG and BNDX go to AGGU. G01 uses Yahoo's expense ratio, which plan v5 P9 calls unreliable, and it drives the core rule "ER > 0.30%". I05 duration is missing 88% of the time and wrong otherwise (TLT 3.6y, VXUS 4.5y). The I family is missing 14-23% and filled with 50. G04, G07 and F07 never vary. G06 averages a 0.85% "NAV gap", most likely from a stale NAV. |
| 6 | UAE/UCITS execution fit | 1 | G08-G10 encode domicile and estate tax, which is the right idea. But G09 applies 15% or 30% to the US proxy's yield, ignores level-1 withholding on non-US holdings and the bond interest exemption, and G10 duplicates G08. All of F measures NYSE liquidity, while the owner trades on the LSE USD line through IBKR. |
| 7 | Weighting vs backtest evidence | 1 | Price families A-E carry 55, F (volume) 5, H 5 and J 10. The backtest shows price-composite rotation lost 2-10 points a year (S1, S2, S4), momentum failed in 2015-2019 (S3), trend-selling the core cost 1-3 points (S8), and deposit-to-top (S5) had a deflated Sharpe probability of 0.84-0.86, below the 0.95 gate. The composite correlates -0.77 (Spearman) with 1-year volatility: 7 of the top 20 are T-bill or bond funds (SHY, SGOV, BIL, VGSH, FLOT, VCSH, IAGG), which a 100%-equity 15-year plan would never buy. J scores sentiment, which plan v5 P10 forbids ("Sentiment is never scored"). G at 20 is the one defensible weight. |
| | **Total** | **7 / 21** | |

## 2. Verdict on each current pillar

Counts: **KEEP 20, MERGE 24, REPLACE 20, DROP 26.** "→ new Xnn" points to the proposed set in section 3.

| ID | Pillar | Verdict | Reason |
|---|---|---|---|
| A01 | Return 1w | DROP | Noise; short-term reversal has the opposite sign |
| A02 | Return 1m | DROP | Short-term reversal; rank-identical to B01 |
| A03 | Return 3m | MERGE into A06 | One momentum measure is enough |
| A04 | Return 6m | MERGE into A06 | Same |
| A05 | Return 12m | MERGE into A06 | rho 0.85 with A06; rank-identical to B04 |
| A06 | Momentum 12-1 | KEEP → new H03 | The one evidence-backed momentum measure and the backtested S3 signal; rank it among UCITS lines |
| A07 | Price vs 50d | DROP | Cluster with A02 |
| A08 | Price vs 200d | MERGE into A09 | rho 0.84 |
| A09 | Faber 10-month | KEEP → new H01 | Plan v5's core trend flag; information only |
| A10 | 50d vs 200d | DROP | A third trend rule |
| B01 | Excess vs VT 1m | DROP | Identical rank to A02 |
| B02 | Excess vs VT 3m | MERGE into B04 | Identical rank to A03 |
| B03 | Excess vs VT 6m | MERGE into B04 | Identical rank to A04 |
| B04 | Excess vs VT 12m | KEEP → new H04 | Display only, measured against VWRA.L |
| B05 | Rank in bucket 3m | REPLACE → new B02 | Between funds on the same index, the return gap is tracking difference; measure that directly |
| B06 | Rank in bucket 12m | REPLACE → new B03 | Same |
| B07 | Excess vs bucket median 6m | DROP | A fourth version of 6-month momentum |
| B08 | RS slope 13w | MERGE into B04 | In the A03/B02 cluster |
| B09 | Weeks beating VT | DROP | Always 0 for the core; no evidence |
| B10 | Information ratio vs VT | KEEP → new H05 | Lengthen to 3 years, measure vs VWRA |
| C01 | Volatility 1m | DROP | In the 7-pillar volatility cluster |
| C02 | Volatility 3m | DROP | Same |
| C03 | Volatility 1y | KEEP → new G01 | Owner context; use 3 years of monthly data |
| C04 | Volatility of volatility | DROP | No decision use |
| C05 | Downside deviation | MERGE into C03 | Cluster |
| C06 | Volatility regime | DROP | Tactical, no evidence at 15 years |
| C07 | Beta to VT | REPLACE → new E08 | What matters is the risk added to the core, not lower beta |
| C08 | Correlation to VT | REPLACE → new E09 | Mechanically 0 for the core; use a diversification ratio |
| C09 | Idiosyncratic volatility | REPLACE → new E07 | Recast as tracking error vs the core (context) |
| C10 | ATR 14d | DROP | Cluster with volatility and F04 |
| D01 | Drawdown from 52w high | KEEP → new G05 | Drives the drawdown protocol |
| D02 | Max drawdown 1y | DROP | Cluster with C09/D05 |
| D03 | Max drawdown 3y | MERGE into D04 | Use the longest history |
| D04 | Max drawdown full history | KEEP → new G03 | Behavioural survivability (plan M3); splice index history |
| D05 | Ulcer 1y | DROP | Cluster |
| D06 | CVaR 95% | KEEP → new G07 | Tail measure; use monthly data over 10 years |
| D07 | Skewness 3y | DROP | Sampling noise, not persistent |
| D08 | Kurtosis 3y | DROP | Same |
| D09 | Days since high | MERGE → new G06 | Becomes time under water |
| D10 | Share of drawdown recovered | DROP | No evidence, no decision use |
| E01 | Sharpe 1y | DROP | rho 0.87 with 12-month return; momentum double count |
| E02 | Sharpe 3y | MERGE into E03 | Cluster with E04-E06 |
| E03 | Sharpe 5y | KEEP → new G08 | One risk-adjusted record, measured vs the core |
| E04 | Sortino 3y | MERGE into E03 | Cluster |
| E05 | Calmar 3y | MERGE into E03 | Cluster |
| E06 | Martin 3y | MERGE into E03 | Cluster |
| E07 | Positive months share | DROP | No evidence |
| E08 | Worst rolling 12m | KEEP → new G04 | Behavioural loss metric |
| E09 | CAGR 5y | REPLACE → new F01 | Long-term reversal: rewards past winners. Use forward CMAs |
| E10 | CAGR 10y | REPLACE → new F07 | Same; use fundamental growth |
| F01 | Dollar volume (US proxy) | REPLACE → new B06 | Measure the LSE line actually traded |
| F02 | Dollar-volume trend | REPLACE → new D03 | Fund flows are what predict closure |
| F03 | Amihud (US proxy) | REPLACE → new B05 | Use the LSE quoted spread |
| F04 | High-low range | DROP | In the volatility cluster |
| F05 | Volume spikes | DROP | No evidence |
| F06 | History length | MERGE → new D05 | rho 0.95 with G03 |
| F07 | Missing data share | REPLACE → new A01 | Constant today; becomes UCITS feed staleness |
| F08 | 4-sigma jumps | KEEP → new I10 | As a data-integrity check, not scored |
| F09 | OBV slope | DROP | Technical indicator, no support |
| F10 | Chaikin money flow | DROP | Same |
| G01 | Expense ratio (Yahoo, proxy) | REPLACE → new B01 | UCITS TER from the KID |
| G02 | AUM (proxy) | REPLACE → new D01/D02 | UCITS fund and share-class size |
| G03 | Fund age (proxy) | REPLACE → new D05 | UCITS share-class age |
| G04 | Closure flag | REPLACE → new D06 | Zero variation today; build a real closure-risk score |
| G05 | Tracking deviation vs bucket | REPLACE → new B02-B04 | Mostly volatility (rho 0.68) and penalises distinct funds |
| G06 | Price vs NAV | REPLACE → new A06 | Stale Yahoo NAV; use issuer NAV vs the LSE close |
| G07 | Distribution yield | MERGE → new C02/C03 | Constant as a score; it is an input to withholding drag |
| G08 | UCITS line on LSE | KEEP → new C01 | Eligibility gate |
| G09 | Withholding drag | REPLACE → new C02/C03 | Look-through by country, not proxy yield x 15/30% |
| G10 | US estate tax | MERGE → new C06 | Equals 1 - G08 exactly |
| H01 | Yield curve 10y-2y | MERGE into H02 | One curve measure |
| H02 | Yield curve 10y-3m | KEEP → new I01 | Context, unweighted, with its false-alarm note |
| H03 | Sahm rule | KEEP → new I02 | Context; 2024 false signal noted |
| H04 | HY spread trend | KEEP → new I03 | Context |
| H05 | Real yield trend | KEEP → new I04 | Context; also an input to expected return |
| H06 | USD trend | KEEP → new I06 | Context; exposure moves to E06 |
| H07 | Oil trend | DROP | Hand-set bucket mapping, no evidence |
| H08 | NFCI | MERGE into H04 | Financial-conditions overlap |
| H09 | VIX level | KEEP → new I05 | Context for the drawdown protocol |
| H10 | VIX term structure | MERGE into H09 | One volatility-market reading |
| I01 | P/E | KEEP → new F05 | Valuation yield composite |
| I02 | P/B | MERGE into I01 | Composite |
| I03 | P/S | MERGE into I01 | Composite |
| I04 | P/CF | MERGE into I01 | Composite |
| I05 | Bond duration (Yahoo) | REPLACE → new F10 | Wrong data; use the issuer's YTM and duration |
| I06 | Earnings yield minus 10y | DROP | Fed model, discredited (Asness 2003) |
| I07 | Top-10 weight | KEEP → new G10 | Plan's concentration line |
| I08 | Sector HHI | REPLACE → new E05 | Deviation from world sector weights is what matters |
| I09 | Largest holding | MERGE into I07 | Cluster |
| I10 | P/E vs bucket median | DROP | Arbitrary bucket benchmark; rho 0.64 with I01 |

## 3. Proposed 90 pillars

Families are reorganised around the decisions. Momentum shrinks from about 25 pillars to one scored pillar plus logged records.

**Sources:** YF = yfinance (including the `.L` USD lines already cached); ISS = issuer UCITS fact sheet, KID and holdings file (Vanguard UK, iShares UK, SPDR); JE = justETF; LSE = LSE instrument page and RNS; IBKR = IBKR quote and contract data; IDX = FTSE/MSCI index fact sheets; KF = Kenneth French data library; CMA = published capital market assumptions (Vanguard VCMM, BlackRock, J.P. Morgan LTCMA, Research Affiliates); RA = Research Affiliates Asset Allocation Interactive; SH = Shiller data; FRED; ECB; IMF; ENG = computed by the engine from its own logs; NEWS = news agents and RSS.

**Decisions:** 1 = keep or review the core, 2 = where the deposit goes, 3 = sell or switch, 4 = what to watch. "Flag" means a binary gate, not a score.

### A. Line integrity: structural flags on the UCITS line (core and alternatives)

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| A01 | Feed staleness | Days since the last LSE print on the USD line | YF .L | lower; flag > 7 | 1 |
| A02 | TER change | Change in KID TER since the last check | ISS, JE | lower; flag on any rise | 1,3 |
| A03 | Index change | Benchmark switch or methodology consultation affecting the fund | ISS, IDX notices | flag | 1,3 |
| A04 | Corporate action | Merger, closure, liquidation or share-class conversion notice | LSE RNS, ISS | flag | 1,3 |
| A05 | Trading disruption | LSE suspension or market-maker withdrawal | LSE RNS | flag | 1,3 |
| A06 | Premium/discount | 20-day mean of \|LSE close / issuer NAV - 1\| | ISS NAV, YF .L | lower | 1,2 |
| A07 | Holdings reconciliation | Regional weights vs the index fact sheet, in points | ISS holdings, IDX | lower; flag > 2 | 1 |
| A08 | Legal status | Still an Irish UCITS ICAV/plc; prospectus unchanged | ISS prospectus | flag | 1 |
| A09 | Distribution policy | Accumulating share class unchanged | ISS | flag | 1 |
| A10 | Orderability | IBKR contract live on the LSE USD line for this account entity | IBKR (quarterly, manual) | flag | 1,2 |

### B. Implementation cost on the line actually bought

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| B01 | TER | Ongoing charge of the UCITS share class | ISS KID, JE | lower | 1,2 |
| B02 | Tracking difference 1y | Fund NAV return minus index net return | ISS fact sheet | higher | 1,2 |
| B03 | Tracking difference 3y (annualised) | Same, over 3 years | ISS, JE | higher | 1,2 |
| B04 | Tracking error 1y | Standard deviation of NAV minus index returns | ISS | lower | 2 |
| B05 | LSE spread | Median quoted bid-ask on the USD line, in bps, at the owner's order time | IBKR snapshot, LSE | lower | 2 |
| B06 | LSE traded value | 3-month average daily value on the USD line | YF .L | higher | 2 |
| B07 | Ticket cost | IBKR commission plus FX per US$2,500, in bps | IBKR schedule | lower | 2 |
| B08 | Securities lending | Share of lending revenue returned to the fund, and % on loan | ISS annual report | higher share, lower % on loan | 2,4 |
| B09 | Replication | Full physical, optimised, or swap | ISS KID | full physical | 2 |
| B10 | Turnover | Portfolio turnover (reconstitution cost) | ISS annual report | lower | 2,4 |

### C. Tax, domicile and legal fit (Canadian non-resident living in the UAE)

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| C01 | Eligibility and domicile | Irish (or Luxembourg) UCITS with an LSE USD line | ISS, ISIN prefix | IE | 1,2 |
| C02 | US dividend withholding drag | US weight x US yield x fund-level rate (15% IE, 30% US-listed), in bps | ISS holdings, IDX yield | lower | 2 |
| C03 | Non-US level-1 drag | Country weights x yields x treaty rates, in bps | ISS, IDX, Irish treaty table | lower | 2 |
| C04 | Level-2 withholding | Withholding on distributions to a UAE holder (IE 0, US 30%, CA 25%) | Rules table | lower | 2 |
| C05 | Index gross-net gap | Realised withholding: index gross minus net total return | IDX | lower | 2 |
| C06 | US estate exposure | US-situs asset (binary) | Domicile | 0 | 1,2 |
| C07 | Accumulating | Accumulating vs distributing | ISS KID | Acc | 2 |
| C08 | Re-entry exposure | s.94.1 offshore-fund risk if Canadian residence resumes | Adviser note, manual | flag | 4 |
| C09 | KID availability | PRIIPs KID exists (orderable under any IBKR entity) | ISS | yes | 2 |
| C10 | Trading currency | A USD line exists (no FX conversion) | LSE | USD | 2 |

### D. Fund durability and issuer

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| D01 | Fund size | UCITS fund AUM in US$ | ISS, JE | higher | 1,2 |
| D02 | Share-class size | AUM of the share class bought | JE | higher | 2 |
| D03 | Flows 3m | Change in shares outstanding x NAV, as % of AUM | iShares UK daily shares; JE size history (weekly snapshots build the series) | higher | 1,4 |
| D04 | Flows 12m | Same, over 12 months | Same | higher | 1,4 |
| D05 | Share-class age | Years since inception | ISS, JE | higher | 2 |
| D06 | Closure risk | Size < US$100m, negative flows, age < 3y, issuer closure rate | D01-D08 | lower | 1,3,4 |
| D07 | Issuer scale | Issuer UCITS ETF AUM | Issuer reports | higher | 1,2 |
| D08 | Issuer closure record | Issuer ETF closures over 5 years | JE closed list, LSE RNS | lower | 1,4 |
| D09 | Substitutes | Count of LSE USD lines on the same or an equivalent index | JE | higher (switch-ready) | 1 |
| D10 | Benchmark licence events | Index-provider changes in the fund's history | ISS notices | lower | 4 |

### E. Exposure fit vs the core and the world market

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| E01 | Overlap with VWRA | Sum of min(weight) across holdings | ISS holdings (Vanguard UK, iShares UK CSV) | lower for satellites | 2,4 |
| E02 | Active share vs FTSE All-World | Half the sum of \|weight differences\| | ISS, IDX | context | 2,4 |
| E03 | Country deviation | Half the sum of \|country weight - world cap weight\| | ISS, IDX | lower for core alternatives | 1,2 |
| E04 | US weight | US share vs world cap | ISS, IDX | context | 4 |
| E05 | Sector deviation | Half the sum of \|sector weight - world weight\| | ISS, IDX | lower for core alternatives | 2,4 |
| E06 | Currency exposure | Non-USD asset share; hedged or not | ISS | context | 2,4 |
| E07 | Tracking error vs core | 3y monthly return gap vs VWRA.L | YF .L | context | 2,4 |
| E08 | Marginal risk | Change in portfolio volatility from adding 10% of the fund to the core | YF monthly, 5-10y | lower | 2 |
| E09 | Diversification ratio | Weighted volatility / portfolio volatility for 90/10 | YF | higher | 2 |
| E10 | Factor distance | Distance between loadings (MKT, SMB, HML, UMD, RMW) and the core's | KF regressions, 5y | context | 2,4 |

### F. Long-horizon expected return (10-15 year horizon)

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| F01 | CMA expected return | Mean 10y return for the fund's region or asset class across houses | CMA | higher | 2,4 |
| F02 | CMA dispersion | Max minus min across houses | CMA | lower (confidence) | 4 |
| F03 | Regional CAPE | Region-weighted CAPE | RA, SH (US) | lower | 2,4 |
| F04 | CAPE percentile | Versus the region's own 20-year range | RA, SH | lower | 4 |
| F05 | Valuation yield | Composite of E/P, B/P, CF/P of holdings | YF funds_data, ISS | higher | 2 |
| F06 | Shareholder yield | Dividend plus net buyback yield | IDX, ISS | higher | 2 |
| F07 | Fundamental growth | 10y real EPS and dividend growth of the index | IDX, SH | context | 4 |
| F08 | Value loading | HML beta, 5y | KF | higher | 2 |
| F09 | Profitability loading | RMW beta, 5y | KF | higher | 2 |
| F10 | Bond yield | YTM minus expected default loss; issuer duration (bond fallback sleeve) | ISS fact sheet | higher | 2 |

### G. Risk and drawdown (owner context and behavioural guardrail)

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| G01 | Volatility 3y | Annualised from monthly returns | YF | lower | 4 |
| G02 | Downside capture | Versus VWRA in down months, 5y | YF | lower | 2 |
| G03 | Max drawdown, long history | Drawdown with index history spliced in | YF, IDX | higher | 4 |
| G04 | Worst rolling 12m | Over the full history | YF | higher | 4 |
| G05 | Current drawdown | From the 52-week high; protocol at -20% | YF .L | context | 1,4 |
| G06 | Time under water | Longest recovery, in months | YF | lower | 4 |
| G07 | CVaR 95% monthly | 10-year tail | YF | higher | 4 |
| G08 | Sharpe 5y vs core | Difference vs VWRA | YF | higher | 4 |
| G09 | Stress returns | Returns in 2008, 2020 Q1 and 2022 | YF, IDX | higher | 4 |
| G10 | Top-10 concentration | Top-10 weight and largest holding | ISS holdings | lower | 1,4 |

### H. Trend and record (only H03 and H05 are scored; the rest are logged)

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| H01 | Core trend flag | VWRA month-end vs 10-month average | YF .L | info | 1,4 |
| H02 | Core absolute momentum | VWRA 12-1 month sign | YF .L | info | 1,4 |
| H03 | Momentum rank | 12-1 momentum ranked among eligible UCITS lines | YF .L | higher | 2,4 |
| H04 | Excess vs VWRA 12m | Display only | YF .L | context | 4 |
| H05 | Information ratio vs VWRA 3y | Consistency of the active return | YF .L | higher | 2,4 |
| H06 | Backtest composite | Exact 9-feature price composite from `backtest.py`, logged weekly | ENG | log | 2,4 |
| H07 | S5 pick record | Weekly top eligible pick with forward 4/13/52-week return vs VWRA | ENG | log | 2,4 |
| H08 | Live score IC | Rank correlation of the live composite with forward 13/52-week returns | ENG | log | 2,4 |
| H09 | Momentum-crash state | Market down over 24 months and now rebounding (Daniel-Moskowitz 2016) | YF | context | 4 |
| H10 | Flag record | Hit rate and whipsaws of H01 over 12 months (plan P10) | ENG | log | 4 |

### I. Context and events (weight 0; flags and context only)

| ID | Name | What it measures | Source | Better | Dec. |
|---|---|---|---|---|---|
| I01 | Yield curve 10y-3m | With its false-alarm note | FRED T10Y3M | context | 4 |
| I02 | Sahm rule | Real-time reading | FRED | context | 4 |
| I03 | High-yield spread | Level and 3-month change | FRED | context | 4 |
| I04 | Real 10y yield | Level | FRED DFII10 | context | 4 |
| I05 | VIX level and term structure | Two readings | YF | context | 4 |
| I06 | Dollar | Broad USD index and EUR/USD | FRED, ECB | context | 4 |
| I07 | World growth and inflation | WEO forecasts | IMF | context | 4 |
| I08 | Structural event flag | Closure, merger, fee or sanctions news on held or candidate lines | NEWS, LSE RNS | flag | 1,3 |
| I09 | Tax-rule watch | US estate tax, Ireland-US treaty, UAE personal tax, CRS, s.94.1 | NEWS, IRS, Revenue.ie | flag | 1,4 |
| I10 | Data integrity | Share of pillars missing or defaulted, 4-sigma jumps, stale feeds | ENG | lower; flag | all |

## 4. Weights (sum 100)

| Family | Current analogue | Old | New | Justification against the backtest |
|---|---|---|---|---|
| A Line integrity | parts of G | - | 10 | Flags act as gates outside the score. The weight applies to A06 and A07 |
| B Implementation cost | G01, G05, F | 25 (G+F, G shared with C, D) | 22 | Cost was the one effect that showed up in every strategy: about 4 points a year of turnover cost sank S1. TER and tracking difference are known-sign, measurable drags |
| C Tax and domicile | G08-G10 | (in G) | 15 | 15% vs 30% withholding plus estate exposure is worth about 30-40 bps a year (plan P2: 34-40 bps all-in vs 65-80 for VT): larger than any edge the backtest found |
| D Durability | G02-G04 | (in G) | 12 | Closure forces a taxable-event-free but costly switch; size and flows predict closure |
| E Exposure fit | C07-C09 | (in C) | 15 | The satellite question is what the fund adds to VWRA, not its stand-alone rank |
| F Expected return | I | 5 | 10 | Valuation has evidence at 10-year horizons (Campbell-Shiller 1998), is weak at one year and has no point-in-time history here, so the weight is moderate |
| G Risk | C, D, E | 35 | 11 | A cross-asset "lower volatility is better" score put T-bills in the top 20. Kept for context and to choose among alternatives |
| H Trend | A, B | 20 | 5 | S1, S2 and S4 lost money, S3 failed 2015-2019, S8 cost 1-3 points and S5 has a deflated Sharpe probability of 0.84-0.86. The weight is kept small and the record is logged, so that after 52 weeks H07 and H08 can test it |
| I Context | H | 5 | 0 | The hand-set macro-to-bucket mapping has no evidence; plan P10 makes macro context only |
| J News (out of scope) | J | 10 | 0 | Flags only; plan P10: "Sentiment is never scored" |

Scoring change: score candidates against VWRA (as a difference) or against absolute thresholds, within the eligible UCITS set only, not by percentile across 200 US proxies. A missing value is excluded from the family mean and counted in I10, not filled with 50.

## 5. What this changes in practice

- **Core decision.** The rule "ER > 0.30%" reads VWRA's KID TER (B01, A02), not VT's Yahoo field. Staleness (A01), corporate actions (A04), index changes (A03) and premium/discount (A06) are measured on VWRA.L itself. Expected outcome: still HOLD almost every week, but for verified reasons.
- **Core alternatives** (SPYY/ACWD, FWRA, SSAC, IWDA) are added to the universe and compared with VWRA on B, C and D. This is where the pillars can earn money: a few bps of TER and tracking difference compounded over 15 years.
- **Deposit candidates** shrink from 200 proxies to roughly 20-30 eligible LSE USD lines. Bond and cash funds score only in the 80/20 fallback. T-bills stop topping the table.
- **Fix the mappings** before anything else: USMV/ACWV to MVOL, IOO to VWRA, VTI/ITOT to CSPX, BNDX/IAGG to AGGU. Better still, compute directly from the 18 `.L` series already cached.
- **Momentum** counts once (H03) instead of in about 25 pillars. Running the backtest composite (H06) and the S5 pick (H07) alongside lets the 52-week record answer the S5 question without contaminating the other families.
- **New data chores:** monthly issuer fact sheets and holdings files (TER, tracking difference, size, holdings), quarterly CMAs and CAPE, and an IBKR spread snapshot at each monthly buy. All are free. Flows come from weekly snapshots of issuer fund size, because plan v5 P9 found no free flow feed.
