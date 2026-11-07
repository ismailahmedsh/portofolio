# Pillars v2: draft candidate (not yet passed audit)

Status on 2026-11-07: four designers proposed sets, a synthesiser merged them, and five auditors scored the merged set in round 1. All five failed it (totals 21, 21, 23, 24 and 21 of 30; pass needs 25 with no criterion below 2). The synthesiser then revised it into the set below. The round-2 audit and the three reviewers did not run because the usage limit was hit. This is the latest candidate, not an approved set.

Pillars are scored on three separate scorecards, each out of 100: the **line** you buy (cost, tax, durability, events), the **exposure** it gives (expected return, factors, risk, concentration), and its **fit** with your current portfolio. Gate, record and context families carry no weight.

| Code | Family | Weight | Purpose |
|---|---|---|---|
| ELG | Eligibility, line integrity and data quality | 0 | Pass/fail gates and data checks on the exact LSE line: domicile and the physical-ETC branch, USD quote, product complexity, asset class, freshness, price integrity, proxy mapping and splice, IBKR orderability, coverage and source reconciliation. Gates decide what may receive money and are never averaged into a score. The core's designated line is never blocked by an owner-input or coverage gate. |
| CST | Implementation cost on the UCITS line | 53 | Line view (the line score sums to 100 within each sleeve). Known-sign drags on the line actually bought, compared like for like with the other lines in the same sleeve: TER, tracking difference beyond TER relative to the same-index reference line, its stability, price noise, traded value, whole-share residue and, later, realised fills. CST10 (15-year all-in cost, including half of the tax-rule-dependent saving) picks the line inside each sleeve. |
| TAX | Withholding, tax-rule fragility and distribution drag | 21 | Line view. Look-through US withholding, used only where 3 or more years of tracking difference are missing; the fragility of a cost advantage that rests on one tax rule; and distribution friction. Pillars with hand-kept, unverified rule tables are recorded, not scored. |
| DUR | Fund durability and switch readiness | 19 | Line view. The chance the line survives 15 years without a forced switch: size, age and ready substitutes are scored. Physical-ETC custody, flows, issuer record, counterparty exposure and benchmark history are recorded or used as gates until their sources are verified. Feeds the structural sell rules. |
| EXR | Long-horizon expected return | 40 | Exposure view (X sums to 100, VWRA = 50, scored on each sleeve's reference index and never on its best line). Only pillars REC04 can rebuild point-in-time are scored: currency value, currency carry and long-term reversal; bond and gold sleeves use their own pillars. CAPE, multi-ratio valuation, payout yield, capital-market assumptions, index drag and country risk premium are recorded until REC03 promotes them. EXR02 turns the scored pillars into an expected return in % a year for FIT04. |
| FAC | Rewarded factor exposure | 20 | Exposure view. Value, profitability, investment and quality-conditioned size loadings from Ken French regional regressions on expanding or rolling windows with a release lag, shrunk by their t-statistics. Beta and alpha are context only. EXR08 and FAC01 together are capped at 25% of X, so value is not counted several times. |
| RSK | Holdability (one-sided or scale-free against the world) | 30 | Exposure view. Penalises crash, recovery and tail risk beyond what the world and beta imply, never rewarding calm. Also holds the portfolio drawdown budget and risk-contribution constraints (weight 0), and the drawdown-protocol and regret display (context). |
| CON | Fund-level exposure hazards | 10 | Exposure view. Only the specialised-fund hype penalty is scored. Breadth is recorded (no history). Restricted-market exposure is a gate only (above 5% blocks deposits), so the hazard is counted once. Country, currency and sector mix are context; their limits sit in FIT as constraints. |
| FIT | Fit with the current portfolio (state-dependent) | 100 | Fit view, its own 100 points, current portfolio = 50. Expected alpha in % against the current portfolio (40%), down-market correlation, diversification return and ex-ante tracking error against VWRA are scored. Sleeve gap and months-to-cure drive routing and sells. Overlap is context. The US, sector, single-name and line-count limits are hard constraints with weight 0, so one purchase is not penalised five times. Until owner positions exist, the portfolio is taken as 100% core. |
| MOM | Trend (record only) | 0 | 12-1 and residual momentum are recorded and tested in REC04 as a pre-registered variant. A 3-12 month signal cannot survive quarterly targets with two-quarter confirmation, and this system's own momentum test (S3) failed the gate. The crash state, core trend flag and relative-performance display are information only. Trend is never a reason to sell. |
| EVT | News and structural events (agents) | 7 | Ten agents with cited, dated sources. Line events (EVT01, EVT02, EVT05) are penalty-only in the line score and gate deposits at severity 2 or more. Exposure events (EVT03, EVT04, EVT07) carry no weight in X because they cannot be backtested. EVT07 severity 3 is a hard gate, EVT03 only records, and EVT10 numbers are accepted only after code confirms the quoted text. Sentiment is never scored. |
| REC | Live record and rule testing | 0 | Judges the system on the owner's money and decides when anything may start moving money. Covers money-weighted return against a VWRA-only shadow, point-in-time snapshots of every pillar, live information coefficient by exposure, the exact-rule backtest gate (REC04), the funding and execution log, behaviour and attribution, and the owner policy-mix test (REC07). |
| MAC | Macro context | 0 | Context for the weekly note, the drawdown protocol, order-time caution and the owner's decision on the diversifier share D. Weight 0 because macro predictors fail out of sample (Welch and Goyal 2008). Logged at every deposit (REC02). |

## ELG: Eligibility, line integrity and data quality

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| ELG01 | Irish or Luxembourg UCITS domicile, non-US-situs, with a physical-ETC branch (gate) | verified | pass (IE preferred over LU) | monthly_allocation | Pass branch (a): the ISIN starts with IE or LU, the fund is UCITS, and it is not US-situs (IE is preferred over LU on the same index; the cost shows in TAX01). Pass branch (b), for the gold or silver sleeve only: an IE-issued, physically backed precious-metal ETC holding allocated, segregated LBMA b |
| ELG02 | USD LSE line and price-unit check (gate) | verified | pass | monthly_allocation | Pass if the line trades on the LSE in USD (yfinance currency == USD). A fund held through a GBp, GBP or EUR line is mapped to its USD sibling by ISIN (SSAC.L to ISAC.L, SPXP.L to SPXS.L). A non-USD line is eligible only if its sleeve has no affordable eligible USD line, and its FX cost is then charg |
| ELG03 | Product-complexity gate | verified | pass | monthly_allocation | Fails leveraged, inverse, daily-reset, option-overlay (covered-call, buffer) and single-stock products, identified from fund name, universe scope and issuer structure fields. |
| ELG04 | Asset-class and sleeve eligibility (gate) | verified | pass | monthly_allocation | Maps each line to one sleeve. Equity UCITS lines go to the core or an equity satellite. Physical gold ETCs that pass ELG01(b) go to the gold sleeve only. Investment-grade government or aggregate bond funds with duration of 5 years or more go to the owner-sized diversifier sleeve only. Money-market,  |
| ELG05 | Feed freshness | verified | lower | sell_or_reduce | LSE trading days since the last print with volume above 0 on the USD line. More than 5 days: not buyable. More than 7 days on a held line: structural review under S1, confirmed with the issuer or an Investegate notice. |
| ELG06 | Price integrity | verified | lower | weekly_review | Count over 252 sessions of daily .L returns beyond 6 robust sigmas that the sleeve reference line does not match on the same or next day (same sign, at least half the size), plus unit jumps and runs of repeated closes. Any unmatched event suspends the line's price-based pillars until explained. |
| ELG07 | Proxy mapping, approved equivalents and splice fidelity | verified | pass | weekly_review | (a) The line's benchmark must equal the history proxy's index or an entry in config/approved_equivalents.csv. That file is versioned, owned by the engine and changed only through CHANGELOG. Each row states its allowed use: price splice, holdings stand-in (CNDX holdings for XNAS and EQQU; CSPX for VU |
| ELG08 | IBKR orderability | unverified | pass | monthly_allocation | An owner-confirmed flag in config/portfolio.yaml: orderable: {LINE: {ok: true, checked_on: date}}. Renewed every 100 days and when a line first enters the shortlist; expired or absent = fail, except for the core's designated line, which is seeded as orderable from the owner's existing VWRA holding a |
| ELG09 | Coverage and source freshness | verified | higher | monthly_allocation | Share of the line's scored pillar weight, counting only pillars with verified sources, that has a live reading this week. Age limits: holdings 35 days (45 days for issuers that publish month-end, such as Vanguard), tracking difference 100 days, TER 120 days. Below 70% the line cannot receive money,  |
| ELG10 | Cross-source reconciliation | verified | lower disagreement | weekly_review | Compares issuer, Yahoo and justETF-profile figures for TER (2 bps tolerance), fund AUM (10%) and date-matched NAV (20 bps), and look-through region weights against the benchmark (2 points). A breach blocks the affected pillar until resolved and logs which source was used. |

## CST: Implementation cost on the UCITS line

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| CST01 | TER of the share class | verified | lower | monthly_allocation | Ongoing charge of the exact USD share class in bps a year, scored against the sleeve's median eligible line with k = 10 bps. Any rise opens a review (EVT02, S2). |
| CST02 | Tracking difference beyond TER, relative to the sleeve reference line | verified | higher | monthly_allocation | For every line: the annualised gap between its USD LSE total return and the same-index sleeve reference line's, over at least 3 years (5 where available), plus the TER difference, shrunk toward 0 by its standard error. Endpoint premium noise is reduced by using 20-day average prices at both ends. Th |
| CST03 | Tracking-difference stability | verified | lower | monthly_allocation | Standard deviation of the last 5 calendar-year gaps against the sleeve reference line (iShares lines: calendar-year tracking difference from the issuer table), in bps, with k = 15 bps. |
| CST04 | Price noise against the sleeve reference line | verified | lower | monthly_allocation | Annualised standard deviation of daily return differences against the sleeve reference line over 1 year, in bps. |
| CST05 | Quoted bid-ask spread (record until verified) | unverified | lower | record_for_testing | A separate weekday job takes one snapshot at 14:00 London, Tuesday to Thursday. A quote is kept only if regularMarketTime is within 25 minutes, bid < ask, both sizes are above 0, and the spread is under 200 bps. The pillar is the 20-snapshot median in bps. Recorded with weight 0 until 20 valid snaps |
| CST06 | LSE traded value and zero-volume days | verified | higher, capped | monthly_allocation | Log of the 63-session median daily traded value on the USD line (close x volume, US$), saturating at US$5m a day, minus a penalty for the share of zero-volume sessions (0% none, 20% or more maximum). |
| CST07 | Premium or discount to NAV (record until verified across issuers) | unverified | lower | record_for_testing | Mean /LSE close / issuer NAV - 1/ over 20 sessions, matched on NAV date, in bps. Computed for iShares lines from the daily product-page NAV. Recorded with weight 0 because the practical buy lines (VWRA, VUAA, SPXS, XNAS) have no verified NAV source. Yahoo navPrice is never used. |
| CST08 | Whole-share residue at deposit size | verified | lower | monthly_allocation | Expected uninvested share of an order for whole shares, averaged over orders of US$340-760: (order - commission - floor((order - commission) / price) x price) / order. A line priced above 0.9 x US$679 is flagged as not buyable in one month. Fractional shares are assumed unavailable until EVT08 confi |
| CST09 | Realised execution cost from owner fills | unverified | lower | monthly_allocation | Median over the line's last 6 owner fills of (fill - mid at order entry) / mid plus commission / order, in bps. Missing below 3 fills; from 3 fills it takes 0.10 of CST weight from CST06. |
| CST10 | 15-year all-in cost per deposited dollar (line choice) | verified | lower | monthly_allocation | Expected annual cost in bps: minus the CST02 relative tracking difference, plus 0.5 x TAX03 (half the saving that depends on one tax rule, the same logic as sell rule S2), plus one-off entry costs spread over 15 years (commission share, half the spread where CST05 or CST09 exist, and CST08 residue d |

## TAX: Withholding, tax-rule fragility and distribution drag

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| TAX01 | US dividend withholding drag | verified | lower | monthly_allocation | Look-through US weight x US dividend yield x fund-level rate (Irish physical 15%, Irish swap on a qualified index about 0%, Luxembourg physical 30%), in bps a year. Scored in the line view only when the line has less than 3 years of CST02; otherwise context, because CST02 already contains it. |
| TAX02 | Non-US level-1 withholding drag (record) | unverified | lower | record_for_testing | Sum over countries of fund weight x country dividend yield x unrecoverable rate for an Irish or Luxembourg fund, in bps a year. Recorded with weight 0 until the treaty table is verified; CST02 captures the realised effect meanwhile. |
| TAX03 | Tax-rule dependence of a cost advantage | verified | lower | monthly_allocation | Part of the line's all-in cost advantage over its physical same-index peer that depends on one tax rule (for example the section 871(m) qualified-index exemption for swap S&P 500 lines), in bps. One-sided: 0 bps scores 50, falling to the floor at 25 bps or more. Half of it is charged in CST10. |
| TAX04 | Bond-interest withholding (diversifier sleeve, record) | unverified | lower | record_for_testing | Share of a bond fund's income not exempt for an Irish fund x rate x yield, in bps a year. Recorded with weight 0 until the rules table is verified. |
| TAX05 | Distribution friction | verified | lower | monthly_allocation | 0 for an accumulating class. For a distributing class (for example EQQU): the cost of reinvesting each payment (US$1.70 / payment) or its cash drag, in bps a year. A distributing class is eligible only where its sleeve has no affordable accumulating USD line. |

## DUR: Fund durability and switch readiness

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| DUR01 | Fund and share-class size (merged) | verified | higher, capped | monthly_allocation | min(fund AUM, 5 x share-class AUM) where the share-class AUM is known, otherwise fund AUM, in US$, log-scaled from US$50m and saturating at US$5bn. |
| DUR02 | Physical-ETC structure and custody (gold sleeve gate) | unverified | pass | monthly_allocation | For ELG01 branch (b): the metal is allocated and segregated, LBMA good-delivery, held by a named custodian in a vault outside the US, with an independent trustee or security over the metal, and no unsecured counterparty beyond settlement. Pass or fail, confirmed from the product page or base prospec |
| DUR03 | Net flows, 12 months (one-sided, record until history exists) | unverified | higher up to 0 (outflows bad, inflows neutral) | sell_or_reduce | (Shares outstanding now - 12 months ago) x NAV / AUM 12 months ago, in %. Outflows penalised, inflows neutral. Missing until 52 weekly snapshots exist (from 2027-W45); the signed series is logged for REC03. |
| DUR04 | Share-class age | verified | higher, capped | monthly_allocation | Years since the USD line launched, saturating at 5. The universe or issuer first date is preferred over yfinance fundInceptionDate. |
| DUR05 | Issuer scale and closure record (record) | unverified | higher scale, fewer closures | record_for_testing | Mean of the issuer's European ETF AUM (log) and its UCITS closures and mergers over 5 years per average line count. Weight 0 until a closure list is verified. |
| DUR06 | Switch-ready substitutes | verified | higher | sell_or_reduce | Number of other eligible LSE USD lines on the same or an approved equivalent index with TER within 0.10% and CST02 within 0.15% of this line; a different issuer counts double. 0 scores worst, 2 or more saturates. |
| DUR07 | Counterparty and lending exposure (record) | unverified | lower | weekly_review | Physical fund: average % of NAV on loan over 1 year (iShares disclosure). Swap fund: replication and counterparties from the justETF profile as a flag; net swap exposure % when available. Weight 0 until swap exposure percentages are verified. |
| DUR08 | Benchmark-change history (record) | unverified | lower | weekly_review | Number of benchmark or provider changes, built from the engine's weekly snapshots of the benchmark field from now on, plus 1 for a pending consultation flagged by EVT04. Weight 0. |

## EXR: Long-horizon expected return

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| EXR01 | CAPE yield and CAPE against own history (record) | unverified | higher (recorded hypothesis) | record_for_testing | Records US 1/CAPE and the US CAPE z-score against its 20-year history weekly. Regional look-through 1/CAPE is recorded once config/cape.csv rows pass EVT10's code check. Weight 0, and missing for every exposure in scoring, including the US and VWRA, so data-rich exposures are not handicapped against |
| EXR02 | Expected excess return in % a year (FIT04 input) | verified | higher | portfolio_mix | E[R_i - R_f] = ERP_world + clip(sum_j b_j x (x_ij - x_VWRA,j), -2%, +2%) - (CST10_i - CST10_VWRA)/100. Inputs are in natural units. ERP_world = 4.0%. The b_j values are pre-registered:
- EXR06: +0.5% per unit of REER z;
- EXR07: +0.5 x carry %;
- EXR08: -0.01% per point of relative return;
- FAC01:  |
| EXR03 | Multi-ratio valuation yield (record) | verified | higher (recorded hypothesis) | record_for_testing | Mean robust z-score, against VWRA, of holdings' E/P, B/P, CF/P and S/P. yfinance returns these as yields even under P/E labels, and that is documented. Weight 0, recorded from now on (no history, so REC04 cannot test it). |
| EXR04 | Dividend yield after withholding (record) | verified | higher (recorded hypothesis) | record_for_testing | Trailing-12-month dividends of the same-index US proxy (accumulating UCITS lines report 0) / price, after fund-level withholding, in %. The buyback leg is dropped. INDA is flagged (no dividend in 23 months). Weight 0. |
| EXR05 | CMA consensus 10-year return (record) | unverified | higher (recorded hypothesis) | record_for_testing | Mean 10-year nominal USD expected return across at least 3 houses, shrunk toward VWRA's by 1 / (1 + range / 2 points). Rows in config/cma.csv must carry house, exposure, horizon, nominal_usd, url, quoted_text and published_on. Code fetches the URL and confirms the number before use, and rejects rows |
| EXR06 | Currency valuation | verified | higher (more undervalued foreign currency) | portfolio_mix | Exposure-weighted z-score of each non-USD currency's BIS real effective exchange rate against its 20-year mean, inverted so cheaper scores higher; computed point-in-time on expanding data with FRED release lags. USD-only exposures score 0, relative to VWRA's non-USD share. In X. |
| EXR07 | Currency carry | verified | higher | portfolio_mix | Sum over non-USD currencies of unhedged weight x (local 3-month rate - US 3-month rate), in %, point-in-time. A currency with no current rate is dropped for every exposure, VWRA included. In X at low weight. |
| EXR08 | Long-term reversal | verified | lower | portfolio_mix | USD total return of the sleeve's reference index (spliced under ELG07) from month -60 to month -13, minus VWRA's over the same window. Price-only, so it is rebuilt exactly in REC04. Together with FAC01 it is capped at 25% of X. |
| EXR09 | Index construction drag (record) | unverified | lower | record_for_testing | Index one-way turnover x asset-class trading cost, plus a front-running estimate for indices with predictable additions, in bps a year. Turnover comes from 12 months of iShares monthly holdings snapshots. Weight 0 until turnover exists for every sleeve's index. |
| EXR10 | Bond expected return (diversifier sleeve only) | verified | higher | portfolio_mix | Yield to worst minus expected default loss by rating (AAA-A 0.05%, BBB 0.2%, BB 1%, B and below 3%, x 0.6), minus TER, plus Treasury roll-down at the fund's duration, plus hedge carry for a hedged class, in %. Replaces the equity pillars for bond lines. |
| EXR11 | Gold real-price valuation (gold sleeve, record until history verified) | unverified | lower | portfolio_mix | Percentile of the USD gold price deflated by US CPI within its history from 1975 to today. Missing until a 1975+ gold series is verified, because a percentile inside 2000+ only is uninformative. Then it feeds EXR02's gold mapping. |
| EXR12 | Country risk premium (test only) | verified | higher (hypothesis under test) | record_for_testing | Look-through weighted Damodaran country risk premium, in %. Weight 0 until REC03 promotes it. |

## FAC: Rewarded factor exposure

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| FAC01 | Value loading | verified | higher | portfolio_mix | HML beta from a 60-month regression of the reference index's USD excess returns on the matching regional Ken French 5 factors plus momentum (Newey-West), estimated each month with only data released by then (1-month lag), shrunk by min(1, /t/ / 2). Shares a 25% cap of X with EXR08. |
| FAC02 | Profitability loading | verified | higher | portfolio_mix | RMW beta from the same point-in-time regression, shrunk by min(1, /t/ / 2). |
| FAC03 | Investment loading | verified | higher | portfolio_mix | CMA beta from the same point-in-time regression, shrunk by min(1, /t/ / 2). |
| FAC04 | Size loading, conditional on quality | verified | higher | portfolio_mix | SMB beta counts only if the RMW beta is 0 or above; otherwise 0. |
| FAC05 | Market beta and residual alpha (context) | verified | context only (not scored) | portfolio_mix | World-market beta and the annualised intercept with t-statistic from the same regression. Weight 0. Beta feeds RSK01, RSK04, FIT04 and FIT10. |

## RSK: Holdability (one-sided or scale-free against the world)

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| RSK01 | Excess drawdown beyond beta | verified | lower excess (one-sided) | portfolio_mix | Maximum drawdown of the reference index over an expanding window, at least 10 years and spliced under ELG07, monthly USD, minus beta x the world's drawdown over the same window. One-sided, k = 10 points: VWRA and anything calmer score 50. |
| RSK02 | Excess time under water | verified | lower excess (one-sided) | portfolio_mix | Longest peak-to-recovery spell in months minus the world's over the same expanding window; an unrecovered drawdown counts to date. One-sided, k = 24 months. |
| RSK03 | Downside-upside beta asymmetry | verified | lower | portfolio_mix | Beta to the world in down months minus beta in up months over 10 years, point-in-time. Scale-free. |
| RSK04 | Stress-window shortfall, beta-adjusted | verified | lower shortfall (one-sided) | portfolio_mix | Mean of (exposure return - beta x world return) over Oct 2007-Mar 2009, Feb-Mar 2020 and calendar 2022. The world reference before VT follows ELG07 (Ken French Developed market plus RF, then ACWI from 2008-03). Only shortfalls count (one-sided, k = 5 points); missing windows are excluded for every e |
| RSK05 | Tail fatness | verified | lower | portfolio_mix | Monthly 95% CVaR divided by monthly volatility over 10 years. Scale-free. Half the internal weight of RSK01-RSK04. |
| RSK06 | Portfolio drawdown budget (constraint) | verified | within budget | portfolio_mix | Replays the proposed target mix (owner policy or score targets) through 2008-09, 2011, 2020 Q1 and 2022, monthly and spliced. Worst loss minus the world's worst must be 5 points or less. Tilts are scaled down until it holds. Weight 0. |
| RSK07 | Risk-contribution ratio (constraint) | verified | 1.5 or lower | portfolio_mix | Each sleeve's share of portfolio variance (10-year Ledoit-Wolf monthly covariance) divided by its capital weight; 1.5 or less at target weights. Weight 0. |
| RSK08 | Drawdown protocol, volatility and regret display (context) | verified | context only (not scored) | weekly_review | Shows:
- the drawdown of the portfolio and of each holding from its 52-week and all-time highs, mapped to states 0, -10%, -20% and -30%;
- 3-year volatility;
- for each sleeve, the worst rolling 60-month money-weighted gap between a US$681-a-month plan into it and the same plan into VWRA (the former |

## CON: Fund-level exposure hazards

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| CON01 | Breadth of holdings (record) | verified | higher, capped | record_for_testing | Effective number of issuers, 1 / sum of squared look-through issuer weights (share classes merged), log-scaled and saturating at 500. Weight 0 in X because it has no history for REC04; recorded weekly. |
| CON02 | Country and currency mix (context) | verified | context only (not scored) | portfolio_mix | Largest country weight, half the sum of /country weight - world weight/, non-USD share and a hedged flag. Weight 0; portfolio limits sit in FIT07. |
| CON03 | Sector mix and index concentration (context) | verified | context only (not scored) | weekly_review | Half the sum of /GICS sector weight - world sector weight/, the top-10 weight, and its percentile in the index's own logged history. Weight 0; portfolio limits sit in FIT08 and FIT09. |
| CON04 | Restricted-market exposure (gate only) | verified | lower | monthly_allocation | Look-through weight in markets listed in config/restricted_markets.csv. Every row has a primary-source citation and a date, added by EVT07 and checked by code. Above 5%, the line cannot receive deposits. Weight 0, so the hazard is counted once. |
| CON05 | Specialised or thematic hype penalty | verified | lower | portfolio_mix | 1 for a narrow thematic, single-industry or single-frontier-country fund launched within 5 years, or after a top-quintile 36-month index return, or with 12-month inflows above 50% of AUM. 0.5 for other narrow sector or theme funds. 0 for broad funds. Point-in-time from launch dates and index history |

## FIT: Fit with the current portfolio (state-dependent)

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| FIT01 | Sleeve gap (routing input) | unverified | higher gap = higher deposit priority | monthly_allocation | For each sleeve: gap = target x (portfolio value + C) - sleeve value, in US$. Weight 0. If positions are missing or older than 35 days, the whole deposit goes to the core. |
| FIT02 | Months to cure drift with deposits | unverified | lower | sell_or_reduce | For each overweight sleeve: (sleeve value - band max x portfolio value) / monthly deposit, plus consecutive month-ends outside its band. Weight 0; used by S3. |
| FIT03 | Overlap with current holdings (context) | verified | lower | weekly_review | Sum over securities of min(fund weight, portfolio look-through weight), in %. Weight 0, shown to the owner. |
| FIT04 | Expected alpha against the current portfolio | verified | higher | portfolio_mix | alpha_i = E[R_i - R_f] - beta_i,P x E[R_P - R_f], in % a year. E comes from EXR02 and E[R_P - R_f] = sum of w_k x EXR02_k. Beta uses a 10-year Ledoit-Wolf monthly covariance. P is the core alone until positions exist. 40% of FIT. Cash scores 0 by construction. Required above 0 for a score-driven tar |
| FIT05 | Down-market correlation with the portfolio | verified | lower | portfolio_mix | Correlation of monthly returns with the current portfolio (core if positions are missing) in months when the world fell, over 10 years with at least 20 such months. Equity and gold lines only. |
| FIT06 | Diversification return | verified | higher | portfolio_mix | Change in 0.5 x (sum w_i sigma_i^2 - sigma_p^2), annualised in bps, moving from the current mix to 95% current + 5% this fund (10-year monthly). |
| FIT07 | US look-through weight (constraint) | verified | lower (limit world +10) | monthly_allocation | Portfolio US weight after the order (and at target) minus the world US weight. Hard limit +10 points. Weight 0. |
| FIT08 | Sector deviation and tech share (constraint) | verified | lower | monthly_allocation | Information Technology plus Communication Services at no more than world + 10 points, and total sector deviation at no more than 15 points, after the order and at target. Weight 0. |
| FIT09 | Single-name concentration (constraint) | verified | lower | monthly_allocation | Largest single-company look-through weight with share classes combined, 7% or less after the order and at target. Weight 0. |
| FIT10 | Ex-ante tracking error against VWRA | verified | lower (no penalty within 2%) | portfolio_mix | Forecast annual tracking error of the post-order portfolio against VWRA (10-year Ledoit-Wolf), in %. Scored one-sided with no penalty up to 2%; hard limit 3%. The only scored active-risk measure. |
| FIT11 | Line count and duplicate-exposure guard (gate) | verified | fewer duplicates; 4 lines or fewer | monthly_allocation | Blocks a candidate whose 3-year weekly correlation with a held line is 0.97 or more on the same index family, unless it is that line's designated replacement under S1 or S2. At most 4 lines in total, counting diversifier lines. Positions under 2% are flagged. Weight 0. |

## MOM: Trend (record only)

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| MOM01 | 12-1 momentum against VWRA (record) | verified | higher (recorded hypothesis) | record_for_testing | USD return from month -12 to -1 of the reference index minus VWRA's. Weight 0; logged by REC02 and tested in REC04 as one pre-registered variant. |
| MOM02 | Residual momentum against the world (record) | verified | higher (recorded hypothesis) | record_for_testing | Cumulative residual return over months -12 to -2 from a 36-month regression on world returns. Weight 0; logged and tested as part of the REC04 momentum variant. |
| MOM03 | Momentum-crash state (context) | verified | context only (not scored) | weekly_review | On when the world's 24-month return is below 0 and its 1-month return is above 0. Neutralises the recorded MOM01 and MOM02 values. |
| MOM04 | Core trend flag | verified | context only (not scored) | weekly_review | VWRA.L month-end close against its 10-month average and the sign of its 12-1 return. Information only. |
| MOM05 | Holdings and candidates against VWRA (weekly display) | verified | context only (not scored) | weekly_review | Excess USD return over VWRA.L for each holding and each sleeve's reference line over 1, 3 and 12 months, and the 3-year information ratio. Display only; this is the weekly 'how is each holding doing' answer. |

## EVT: News and structural events (agents)

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| EVT01 | Fund corporate actions | verified | lower severity | sell_or_reduce | Agent scans held and shortlisted lines for closure, merger, liquidation, share-class conversion, delisting, ISIN or ticker change, or loss of the USD line. Severity: 0 none, 1 watch, 2 review (confirmed notice), 3 act. Two dated, cited sources are required, and a primary source (issuer notice or an  |
| EVT02 | Fees, structure, KID and cheaper substitutes | verified | lower severity | monthly_allocation | Agent detects TER, replication, lending, distribution-policy and domicile changes and KID availability. It confirms non-iShares TERs monthly from the justETF profile and the issuer KID (feeding CST01 and ELG10). It also reports new LSE USD lines or fee cuts on any sleeve's index. Penalty-only in the |
| EVT03 | Satellite thesis log (record only) | verified | intact | record_for_testing | Quarterly, for each held or policy satellite, the agent records cited structural facts that bear on 10-year cash flows or investability, with base rates, and a verdict (intact, weakened or broken). Weight 0: it never changes a score or freezes a sleeve. Facts on the fixed list (sanctions, capital co |
| EVT04 | Index methodology, reclassification and mega-cap events | verified | lower severity | weekly_review | Agent tracks benchmark switches, provider consultations, capping-rule changes, special rebalances, country reclassifications and single-company events that move top-10 weights. Weight 0 in X (not backtestable). Recorded; it feeds DUR08 and triggers an immediate recompute of FIT and CON from fresh ho |
| EVT05 | Issuer, custodian and counterparty health | verified | lower severity | sell_or_reduce | Agent detects issuers exiting European ETFs, custodian or administrator changes (including ETC vault and custodian changes, which trigger a DUR02 re-check), lending or swap-counterparty incidents, and regulatory sanctions on an issuer or depositary. Applies to every line of that issuer. Penalty-only |
| EVT06 | Tax and legal regime for the owner | verified | no adverse change | sell_or_reduce | Agent watches the following, setting severity only on a primary-source change (IRS, Revenue.ie, UAE Ministry of Finance, CRA):
- US estate tax and situs rules;
- the Ireland-US treaty and section 871(m);
- the Irish fund regime and Irish CAT;
- UAE income tax and CRS;
- Canadian residency rules (s.1 |
| EVT07 | Sanctions, capital controls and market access (gate) | verified | lower severity | monthly_allocation | Agent detects sanctions, capital controls, exchange closures, investment bans and delisting risk affecting look-through holdings, estimates the affected weight per line, and proposes rows for config/restricted_markets.csv with a primary-source URL and quoted text, which code checks before CON04 uses |
| EVT08 | Broker, venue and funding channel | verified | no adverse change | monthly_allocation | Agent watches IBKR changes for UAE clients (US$1.70 minimum, FX terms and US$2 minimum, product access, KID), fractional LSE ETF shares, LSE outages, the CBUAE peg stance and UAE remittance fees. Weight 0. Confirmed changes update the allocator constants and the funding block. |
| EVT09 | Deposit-week calendar and market dislocations | verified | fewer conflicts | monthly_allocation | Agent lists deposit-week events (FOMC, US CPI and payrolls, ECB, BoE and BoJ, index rebalance days, US and UK holidays) and any ETF dislocation or LSE outage, and recommends the order day and hour. It may delay an order by at most 1 week and never skips a deposit or triggers a sale. Weight 0. |
| EVT10 | CMA and valuation data harvest (code-checked) | verified | fresh, code-confirmed inputs | record_for_testing | Each quarter the agent extracts numbers only, from CMA releases and regional CAPE readings. Each row is written to config/cma.csv or config/cape.csv with a URL, the quoted text span and a date. Code fetches the page and confirms the number appears in the span; failing rows are marked unverified and  |

## REC: Live record and rule testing

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| REC01 | Money-weighted return against a VWRA-only portfolio | unverified | higher | record_for_testing | Since start and rolling 12 months: the actual portfolio's money-weighted return after all costs against a shadow VWRA-only portfolio with identical deposits; also the money-weighted minus time-weighted gap and worst drawdown against the world. |
| REC02 | Point-in-time pick and pillar snapshot | unverified | higher (picks minus VWRA) | record_for_testing | Each month, runs/plan_log.csv (created by this revision) records:
- the actual orders;
- the S5 shadow pick;
- the top-X sleeve;
- the owner-policy order;
- the all-VWRA order;
- forward 1, 3, 12 and 36-month returns under same-week and next-week execution.
It also stores a snapshot of every pillar, |
| REC03 | Pre-launch redundancy check and live information coefficient by exposure | verified | higher | record_for_testing | Before week 1: a Spearman matrix of every scored pillar over the 318 unique lines and the sleeve reference indices; any pair with /rho/ of 0.85 or more is merged before launch, and EXR08 vs FAC01 must be below 0.7 or FAC01 is set to record-only. Live: rank IC of each family and each record-only pill |
| REC04 | Exact-rule backtest and score-target gate | verified | gate_pass true | record_for_testing | Monthly, src/backtest.py re-runs the exact live exposure rule (the X pillars and weights under the frozen config hash, the clip((X-55)/15) target, hysteresis, the satellite limits and the constraints). It uses:
- MONTHLY = 681 with the US$2 FX minimum, the US$1.70 commission and whole shares;
- both |
| REC05 | Execution and funding log | unverified | lower cost and no systematic drift | record_for_testing | For each order: the line's return minus VWRA's between the Friday signal close and the fill; fill minus mid at entry; and the funding cost (bank wire and correspondent fees, the IBKR AED/USD rate against 3.6725, and the FX minimum). Re-checks the batching choice (k months) each quarter. |
| REC06 | Behaviour, sell log and attribution | unverified | all deposits on schedule; zero non-structural sells; line regret near or above 0 | record_for_testing | Monthly: deposits on schedule, days from deposit to order, every sale with its rule and hold counterfactual, overrides, and a Brinson split of active return against VWRA into owner-policy sleeve choice, score-driven sleeve choice and line choice. Also line regret 12 months after each buy against the |
| REC07 | Owner policy-mix test against VWRA | verified | higher, and positive in every period | portfolio_mix | Price-only backtest of the owner's fixed policy mix (and the 4 standard mixes) against the world alone:
- US$681 monthly deposits, the US$2 FX minimum, US$1.70 commission and 10 bps cost;
- cash-flow rebalancing to the largest gap;
- both timings;
- periods 2003-07, 2008-14, 2015-19, 2020-26 and ful |

## MAC: Macro context

| ID | Pillar | Data | Better when | Decision | Definition |
|---|---|---|---|---|---|
| MAC01 | Recession indicators | verified | context only (not scored) | weekly_review | 10-year minus 3-month spread (level and months inverted in the last 24) and the real-time Sahm rule against 0.5, with false-alarm notes. Context. |
| MAC02 | Credit and financial stress | verified | context only (not scored) | weekly_review | US high-yield and EM corporate OAS (20-year percentile, 3-month change), the St. Louis Fed stress index, the Chicago NFCI, and EPU and GPR percentiles. Context for the drawdown note. |
| MAC03 | Volatility regime (execution caution) | verified | context only (not scored) | monthly_allocation | VIX, VIX/VIX3M and MOVE. When VIX is above 30 or VIX/VIX3M is above 1, the order uses a limit at mid and avoids the first and last 30 minutes. Never delays or skips the deposit. |
| MAC04 | Rates, inflation, dollar and stock-bond regime | verified | context only (not scored) | portfolio_mix | 10-year TIPS yield, 5y5y breakeven, US CPI, 12-month broad-dollar change, AED/USD against 3.6725, 36-month equity-bond correlation, and the US excess CAPE yield (Shiller). Context for the owner's decision on the diversifier share D. |

## Scoring method

1. Instrument. Line pillars are computed on the LSE USD UCITS line. Exposure pillars are computed on each sleeve's reference index: the reference line, spliced to an approved proxy only if ELG07 passes. They are never computed on the sleeve's best line, which removes the max-of-N bias for sleeves with many lines.

2. Gates first: ELG01-ELG05, ELG08, ELG09, DUR02 (ETCs), FIT11, CON04 above 5%, EVT01/02/05 at severity 2 or more, and EVT07 at severity 3. A failing line is still scored and reported but cannot receive money. Gates fail closed for buying and open for selling. The core's designated line is exempt from the owner-input gate (ELG08) and the coverage gate (ELG09).

3. Transform. s = 50 + 50 x tanh(d x (x - ref) / k), in natural units, never universe percentiles. The k scales are pre-registered in config/pillar_scales.yaml:
- costs: TER 10 bps, relative tracking difference 15, stability 15, noise 50, withholding 15, distribution 15, tax-rule dependence 25;
- residue 10%; traded value and size 1 log10 step; age 3 years; substitutes 1;
- currency z 1.0; carry 1%; reversal 20 points;
- factor betas 0.2;
- drawdown 10 points; time under water 24 months; asymmetry 0.2; stress 5 points; CVaR/vol 0.5;
- hype 1;
- alpha 1% a year; down-market correlation 0.2; diversification return 10 bps; tracking error 0.5%.
Record-only pillars are transformed the same way, so REC03 can test them. The config file, the thresholds (55/15, 2.5/5 hysteresis), the bands, the EXR02 coefficients and the weights below are frozen under a config hash before the first REC04 run. Any later change is a new trial (N_TRIALS + 1) logged in CHANGELOG.

4. Three references, three separate views. There is no cross-view composite and no 322-line ranking.
- Line view (CST 53, TAX 21, DUR 19, line EVT 7 = 100) is compared with the sleeve's median eligible line, and ranked only within the sleeve. Single-line sleeves use absolute anchors (TER 10 bps, AUM US$1bn).
- Exposure view X (EXR 40, FAC 20, RSK 30, CON 10 = 100) is compared with VWRA = 50.
- Fit view (FIT = 100) is compared with the current portfolio (core only until positions exist).

5. One-sided pillars score s = 50 - 50 x tanh(max(0, d x (x - threshold)) / k) and never exceed 50: RSK01, RSK02, RSK04, FIT10, TAX03, DUR03 and line EVT. Calm earns nothing. Bonds and gold compete only inside their sleeves (EXR10, EXR11).

6. Weights inside families.
- CST: CST01 0.25, CST02 0.30, CST03 0.10, CST04 0.05, CST06 0.15, CST08 0.15. CST09 takes 0.10 from CST06 after 3 fills. CST05 and CST07 are 0 until verified.
- TAX: TAX01 0.4 (only when CST02 is missing for the whole sleeve), TAX03 0.4, TAX05 0.2. TAX02 and TAX04 are 0 until verified.
- DUR: DUR01 0.4, DUR04 0.3, DUR06 0.3. DUR03, DUR05, DUR07 and DUR08 are 0 until verified.
- Line EVT: EVT01, EVT02 and EVT05 equal.
- EXR (equity X): EXR06 0.4, EXR07 0.2, EXR08 0.4. Bond sleeve: EXR10 1.0. Gold: EXR11 1.0, which is missing until verified.
- FAC: FAC01-FAC04 0.25 each.
- RSK: RSK01-RSK04 0.222 each, RSK05 0.111.
- CON: CON05 1.0.
- FIT: FIT04 0.40, FIT05 0.20, FIT06 0.20, FIT10 0.20.
Value cluster cap: EXR08 and FAC01 together are at most 25% of X (now 21%). Every X pillar can be rebuilt point-in-time in REC04, so the rule tested is the rule used.

Weight 0, as record, context, constraint, gate or derived:
- all ELG and DUR02;
- CST05, CST07, CST09 (below 3 fills), CST10;
- TAX02, TAX04;
- DUR03, DUR05, DUR07, DUR08;
- EXR01, EXR02 (derived), EXR03, EXR04, EXR05, EXR09, EXR12;
- FAC05; RSK06-RSK08; CON01-CON04;
- FIT01-FIT03, FIT07-FIT09, FIT11;
- all MOM, all REC, all MAC;
- EVT03, EVT04, EVT06-EVT10.

7. Verification rule. A pillar whose source is unverified has weight 0 and is recorded, never half-weighted into anything that moves money. It is promoted when its source passes a probe, and that change is logged in CHANGELOG. Paid sources are not used.

8. Missing data, applied the same way in every view.
- If the reference (VWRA, or any eligible line in the sleeve) lacks a pillar, that pillar is missing for every exposure or line compared with it.
- Otherwise a missing pillar drops out and the family score is 50 + c x (mean - 50), where c is the share of the family's weight that has data.
- Nothing is filled with 50 or with a worse quartile. ELG09 counts only verified pillars. Missing pillars are listed weekly.

9. Smoothing. Monthly line decisions use the median of the last 4 weekly readings. X uses the 13-week mean and two consecutive live qualifying quarters. One week's data or execution timing cannot flip a decision.

10. Built-in checks. The run fails loudly if any of these break:
- VWRA scores exactly 50 on every X family (no X pillar can penalise VWRA itself);
- every money-market, T-bill and ultra-short line fails ELG04;
- no low-volatility fund scores above 50 on a one-sided pillar;
- line scores are independent of US-proxy fund facts;
- the config hash matches the one REC04 tested.
Before launch, the REC03 Spearman matrix must show no scored pair with |rho| of 0.85 or more. Weights change only through CHANGELOG, backed by REC04 or a 36-month REC03 result.

## Allocation of the monthly deposit

Three layers: the pool and its limits are policy, targets come from the owner now (and from scores only after REC04 passes), and routing happens monthly. The weekly run never moves money.

1. THE POOL. Sleeve lines are verified on yfinance as USD LSE lines on 2026-11-07. The universe file is to be updated before launch: add EXUS, ACWD and SPYY, remove EQAC, remove the duplicate CUSS, R2US, WSML and XDEW rows, and fix the VWRA TER to 0.14.
- Core, world: VWRA (designated). Chain FWRA, then ACWD (US$314.84); SPYY is listed but thin. At least 80% of the portfolio while REC04 fails.
- S&P 500: SPXS (US$14.95), VUAA (US$143.90), CSPX (US$802). Band 0-15%.
- Nasdaq-100: XNAS (US$63.16), CNDX (US$1,563), EQQU (US$665, distributing). Band 0-10%.
- Developed ex-US: EXUS (Xtrackers MSCI World ex USA 1C, US$44.75, listed 2024-03). Band 0-15%.
- Emerging markets: EIMI. Band 0-10%.
- Factor and small-cap: IWVL, IWQU, WSML. Band 0-10%.
- Gold: IGLN, via ELG01(b) and DUR02 (SGLD only after Invesco data is verified). 0 or 5%.
- Diversifier bonds: AGGU or 5+ year government bonds. Share D set by the owner at 0-20%, default 0, never moved by scores.
- Limits: any satellite is 0% or at least 5%. At most 4 lines in total (FIT11). Satellites total at most 20% of the portfolio. Satellites receive at most satellite_share (0 to 0.20) of the dollars deposited over any rolling 12 months; this keeps the DECISION_RULES 20% deposit cap and still allows one order a month.

2. TARGETS.
(a) Before REC04 passes (now). X is computed, logged and reported but sets no targets. Targets come only from config/portfolio.yaml policy_targets, set by the owner, for example {SP500: 0.10, NDX: 0.05}. Every policy must pass:
- the hard constraints: US no more than world +10 (FIT07), IT plus Communication no more than world +10 (FIT08), single name 7% or less (FIT09), tracking error 3% or less (FIT10), drawdown budget world +5 (RSK06), and risk-contribution ratio 1.5 or less (RSK07);
- the REC07 test, re-run whenever the policy changes. The owner note labels the policy 'owner policy, not evidence-favoured', and also 'regime bet' if it lost in any REC07 period.
With satellite_share = 0 or no policy_targets, every deposit goes to the core (DECISION_RULES rule 2 default).
(b) After REC04 passes. The owner may set target_mode: score.
- X is the 13-week mean on the sleeve's reference index (never the best line).
- A sleeve qualifies when X is 55 or more at two consecutive live quarterly reviews (no backfilled quarters) and FIT04 alpha is above 0 at the proposed weight.
- Target = band max x clip((X - 55) / 15, 0, 1), rounded to 0 or at least 5%, then scaled down until every constraint holds.
- Hysteresis: a change of at least 2.5 points and at most 5 points per sleeve per quarter. The owner confirms each change.
- The 20% portfolio and rolling-12 deposit limits still apply. Going higher needs an owner CHANGELOG entry plus 36 months of REC03 live record.

3. MONTHLY DEPOSIT.
(a) Funding. The owner records in config/portfolio.yaml how the AED reaches IBKR: method, bank fee, correspondent fee, FX minimum and checked_on. Let F be the fixed USD cost per conversion. Convert every k months, where k in {1, 2, 3} minimises F/k + ((k-1)/2) x 680.74 x 0.4%. With only the US$2 FX minimum, k = 1; with F = US$10, k = 3. This month: 2,500 / 3.6725 = US$680.74, minus US$2 = US$678.74. C = that plus any residue (at most one month's deposit).
(b) Gaps. Gap g = target x (portfolio value + C) - sleeve value (FIT01). If positions are missing or stale, or no gap exceeds US$100, everything goes to the core.
(c) Routing. All of C goes in one order to the largest positive gap. A satellite may receive it only if the rolling-12-month satellite share of deposits stays at or below satellite_share; otherwise the core gets it. A second order to the next gap is placed only if both orders are at least US$340. Never more than 2 orders a month.
(d) Line choice. The line must pass:
- ELG01-ELG05, ELG08, ELG09 and FIT11;
- CON04 at 5% or less, and no EVT01, EVT02 or EVT05 event at severity 2 or more, and no EVT07 event at severity 3;
- a line score of 40 or more.
Among those, buy the lowest CST10. The new-money line changes only when a challenger is at least 5 bps a year cheaper at 2 consecutive monthly runs; the old line is kept, not sold.
(e) Whole shares: buy floor((order - 1.70) / price). If the cheapest line does not fit the order, use the next line within 10 bps a year all-in; otherwise route to the next gap.
(f) Fallback. If no line in the target sleeve passes, go to the next sleeve. If none passes, buy the core chain (VWRA, then FWRA, then ACWD), requiring only ELG01, ELG02, ELG05 and EVT01 below severity 2. Cash is never held for more than one month.
(g) Execution. Place the order on the EVT09 day, as a limit at mid plus half the spread, 14:30-16:15 London for US-heavy sleeves (MAC03 stress: a limit at mid). Log the fill for CST09, REC05 and REC06.
(h) In a drawdown nothing changes: new money fills whatever fell.

Worked example (illustrative). The owner holds VWRA US$20,000 and sets policy_targets S&P 500 10%, satellite_share 0.20. The previous 12 deposits all went to the core. C = US$678.74, so the portfolio after the deposit is US$20,678.74.
- Gaps: S&P 500 +US$2,067.87; core (90%) -US$1,389.13.
- Rolling-12 satellite share after this order is 678.74 / (12 x 678.74) = 8.3%, within 20%. Route to the S&P 500 sleeve.
- Line, by CST10: SPXS about -26.5 bps (3-year gap +19.3 bps over CSPX, minus the half TAX03 haircut of 9.7) against VUAA about -17 bps. SPXS is cheaper by about 9.5 bps, so it is chosen once it has led at 2 monthly runs.
- Order: 45 SPXS at US$14.95 = US$672.75 plus US$1.70 commission; residue US$4.29.
- Next month the S&P 500 sleeve can take a second deposit (16.7%). A third within 12 months would exceed 20%, so it goes to the core. The S&P 500 sleeve therefore gets at most 2 of every 12 deposits until it reaches 10%.

4. WEEKLY. All 318 unique lines are scored. The report shows three separate rankings and never one composite:
(i) line scores ranked within each sleeve;
(ii) exposure score X by sleeve against VWRA = 50, with its trend;
(iii) the fit view of each sleeve's best line against the current portfolio.
It also shows each holding against VWRA (MOM05), gates, events, coverage, missing pillars and the drawdown state.

5. RECORDS. REC02 logs every month. REC04 decides whether X may set targets. REC07 re-tests the owner's policy. Changes to DECISION_RULES rule 2 go through CHANGELOG: satellite_share now caps the rolling-12-month share of deposited dollars, and its destination is the policy-target gap rather than the top-ranked ETF.

config/portfolio.yaml additions:
- positions [{line, units, avg_cost_usd, as_of}];
- orderable {line: {ok, checked_on}}, seeded with VWRA.L;
- etc_checks {line: {custody_ok, checked_on}};
- fills [{date, line, qty, price, mid_at_entry, commission}];
- funding {method, bank_fee_aed, correspondent_fee_usd, fx_min_usd, checked_on};
- policy_targets {sleeve: weight};
- target_mode: policy | score (default policy);
- diversifier_share_D.
Statements go in inputs/ibkr/.

## Sell rules

Default: hold, and steer with new money. Deposits fix drift before any sale. Every sale is logged with its rule, sources, cost and the hold counterfactual (REC06).

S0. Never a reason to sell:
- price trend (MOM04), momentum, any score or rank, or X;
- drawdown depth (RSK08), volatility or any MAC reading;
- news sentiment, the EVT03 verdict, or EVT09 crisis status.
Evidence: trend-selling the core (S8) cost 1-3 points a year; score rotation (S1, S2 and S4 in the backtest) lost 2-10 points a year; the old composite never triggered a correct sell. Drawdown protocol at -20% on the core: report it and keep depositing.

S1. Structural exit of a line. Act within one month of primary-source confirmation. Triggers:
- EVT01 at severity 2 or more;
- a gate turning to fail: ELG01 including ETC custody (DUR02), ELG02-ELG04, or ELG08 confirmed by the owner;
- a feed stale for more than 7 trading days (ELG05), confirmed;
- a benchmark change that takes the line out of its sleeve (EVT04);
- EVT05 or EVT07 events impairing 5% or more of NAV.
Action: switch the whole position to the sleeve's best eligible substitute (DUR06, lowest CST10) in the same session, never into cash. If the fund trades more than 2% below NAV, stop deposits and wait until the discount is below 1%, or 60 days. A merger into a line that passes every gate may be accepted.

S2. Cost or durability switch. First stop buying and send new money to the substitute. Sell and switch only if all three hold:
- (a) the held line's CST10 exceeds the best eligible same-index line by 15 bps a year or more at 2 consecutive quarterly checks;
- (b) the annual saving x 10 years exceeds 3 times the round trip (2 x US$1.70, both half-spreads, any FX);
- (c) less than half of the saving depends on one tax rule (TAX03).
CST02 must rest on at least 3 years of same-index closes. Example under watch: FWRA beat VWRA by 20.4 bps a year over 3 years of LSE closes. A switch is considered only if this persists at 2 quarterly checks after 20-day endpoint averaging. Durability works the same way: a flag (fund AUM under US$100m with 12-month outflows once DUR03 exists, or EVT05 severity 1) stops buying, and a switch follows only if the flag holds for 2 monthly runs and a substitute exists.

S3. Band or constraint breach from drift. Applies when a sleeve is more than 5 points above its band max or its policy target plus 5, or actual weights breach FIT07-FIT10, RSK06 or RSK07. First stop buying the sleeve. Sell only if FIT02 shows more than 12 months of deposits are needed to cure it. Then sell down to the limit (not to target) in one order, at most once a quarter, and buy the most underweight sleeve in the same session.

S4. Satellite removal. Triggers: the owner sets its policy target to 0; or, in score mode, X below 50 for 2 quarters or FIT04 at 0 or below; or EVT07 severity 3 lasting more than a quarter. The sleeve is frozen: no new money and no sale, and it is diluted by deposits. It is sold only if still above 5% after 12 months, or under S1-S3. A frozen sleeve under 2% may be merged into the core at a quarterly review.

S5. Diversifier rebalance, only if D is above 0. Once a year, return to D if it is more than 5 points off. Selling equity to buy bonds is forbidden while the world is more than 20% below its 52-week high.

S6. Tax or legal change (EVT06 severity 2 or more): freeze all sales until an adviser review and a re-run of the TAX pillars.

Guardrails for S2-S5:
- a 30-day cooling-off and a re-run of the scores;
- no non-structural sale while the world is more than 15% below its 52-week high;
- missing or unverified data never triggers a sale: gates fail closed for buying and open for selling;
- the core's designated line is sold only under S1.

## Changes after round-1 audit

Revision after audit round 1 (all five audits: totals 21, 21, 24, 23 and 21). Still exactly 100 pillars: ELG 10, CST 10, TAX 5, DUR 8, EXR 12, FAC 5, RSK 8, CON 5, FIT 11, MOM 5, REC 7, MAC 4, EVT 10.

Blocking fixes:
1. Money moved before any test (all auditors). Score-driven targets are now off until REC04 passes. Before that, satellites come only from owner policy_targets, labelled 'owner policy, not evidence-favoured', and limited by:
- the existing DECISION_RULES cap, now applied as a rolling-12-month share of deposited dollars (at most 20%);
- satellites at most 20% of the portfolio;
- all hard constraints;
- the REC07 test.
This needs a CHANGELOG entry for DECISION_RULES rule 2. Removed: 'first targets from backfilled scores', and routing 100% of deposits to a satellite for months.
2. The tested rule differs from the live rule. X now holds only pillars REC04 can rebuild point-in-time: EXR06, EXR07, EXR08, FAC01-FAC04, RSK01-RSK05 and CON05. EXR01, EXR03, EXR04, EXR05, EXR09, CON01, MOM01, MOM02 and exposure EVT are record-only. 'US CAPE against the world' was removed from REC04, because no world-CAPE history exists. REC04 now:
- uses MONTHLY = 681, the US$2 FX minimum and whole shares;
- uses expanding windows with release lags;
- adds a 2003-2014 holdout;
- freezes a config hash and sets N_TRIALS to at least 21;
- reports the effective number of independent decisions and a survivorship note.
3. FIT04 had no units. The new EXR02 gives expected excess return in % a year: ERP_world 4.0% plus pre-registered coefficients on natural-unit X pillars, clipped at ±2%, minus the CST10 difference. Bonds use EXR10 minus T-bills; gold uses a percentile table. Withholding now enters once, through CST10.
4. Gold failed ELG01 (ETCs are not UCITS). ELG01 gains branch (b) for physical ETCs; new DUR02 checks custody (a gate); EVT05 re-checks custodian events; ELG04 is aligned.
5. The selection picked each sleeve's best line (max of N). Exposure is now scored on the reference index.
6. Value was counted about five times. EXR02 (old) was merged into EXR01, which is now record-only and missing for all exposures; EXR03 and EXR05 are record-only. EXR08 and FAC01 are capped at 25% of X, with a pre-launch rho test.
7. One purchase was penalised five times by FIT. FIT03 is context; FIT07, FIT08, FIT09 and FIT11 are constraints or gates with weight 0; FIT10 is the single scored active-risk pillar. DUR01 and DUR02 were merged into DUR01, which uses min(fund, 5 x class).
8. ELG08 and the positions had no schema, so day one would have blocked VWRA. Added a portfolio.yaml schema (positions, orderable seeded with VWRA.L, etc_checks, fills, funding, policy_targets, target_mode) and inputs/ibkr/. The core is exempt from ELG08 and ELG09, the core chain is VWRA, then FWRA, then ACWD, and missing positions mean core-only routing.
9. Source labels were wrong. Now unverified with weight 0: ELG08, CST05, CST07, CST09, TAX02, TAX04, DUR02, DUR03, DUR05, DUR07, DUR08, EXR01, EXR05, EXR09, EXR11, FIT01, FIT02, REC01, REC02, REC05 and REC06. The half-weight rule is replaced by 0 until verified. Other corrections:
- SSGA removed from CON01 and FIT09;
- EVT01 uses Investegate;
- EXR04 uses proxy ttm dividends and drops buybacks;
- EXR09's 7% turnover claim is withdrawn;
- Shiller is read only from shillerdata.com.
- CST02 is now the relative tracking difference from LSE closes against the same-index reference line, so it works for Vanguard, Xtrackers and Invesco lines. Measured 3-year gaps: SPXS +19.3, VUAA -0.1, XNAS +16.8, EQQU +4.2, FWRA +20.4, ACWD +19.8 bps a year.
10. Line choice contradicted the worked example. CST10 now adds 0.5 x TAX03. The example is redone: SPXS, 45 shares at US$14.95 = US$672.75, residue US$4.29, from C = US$678.74 (the earlier C of US$680 was corrected).
11. Sleeve lines were missing from the universe. Verified on yfinance today:
- EXUS.L: USD, US$44.75, from 2024-03, about US$8.2bn;
- ACWD.L: USD, US$314.84;
- SPYY.L: USD, thin.
EQAC.L returns 404 and is replaced by EQQU. SPXS.L (US$14.95, USD) and SPXP.L (1118.6 GBp) are the same fund's lines; the US$1,140 figure was a GBp misread. To apply in the universe CSVs before launch: add EXUS, ACWD and SPYY; remove the duplicate CUSS, R2US, WSML and XDEW rows (318 unique lines); move XDEW to us/equal_weight and settle its TER through ELG10; set VWRA's TER to 0.14; fill the missing VERG and VAPU ISINs; unify the GBX, GBp and GBP spellings.

Other fixes:
- The weekly composite is replaced by three separate views.
- The restricted-market hazard is counted once: CON04 is a gate only.
- EVT03 is record-only.
- EVT10 rows must pass a code check of URL and quoted text.
- MOM01 and MOM02 are record-only.
- Old RSK05 (in-sample regret, the opposite sign to EXR08) is now display only inside RSK08, and RSK06-RSK09 are renumbered RSK05-RSK08.
- REC03 now runs a pre-launch rho matrix, uses IC by exposure cluster with Newey-West errors, allows demotion only after 36 months (never on short-horizon IC for EXR or FAC), and tests CST within sleeves.
- CST05 uses one weekday snapshot gated on regularMarketTime.
- ELG09 allows 45 days for month-end publishers.
- The 2007-08 world reference is declared in ELG07.
- EXR11 is unverified before 2000.
- DUR03 reads missing until 2027-W45.
- A funding and batching rule (choice of k) is set up front.
- Gold is 0 or 5%; FIT11 counts diversifier lines.
- Ben-David et al. 2023 is cited to the Review of Financial Studies; the Boudoukh-Richardson-Whitelaw caveat is added to EXR01.

New pillars:
- EXR02: expected return in %.
- DUR02: ETC custody.
- REC07: owner policy-mix test. Run today, money-weighted, US$681 deposits: 10% S&P 500 plus 10% Nasdaq-100 gave 12.66% against 11.69% for the world in 2015-26 and 12.38% against 10.79% in 2008-14, but 14.07% against 14.94% in 2003-07.

Next steps:
1. Apply the universe and portfolio.yaml changes.
2. Write config/pillar_scales.yaml, approved_equivalents.csv and restricted_markets.csv, and freeze the hash.
3. Run the REC03 rho matrix.
4. Build REC04 with N_TRIALS of 21 or more.
5. The owner chooses satellite_share and policy_targets, or keeps 0 and 100% VWRA.
