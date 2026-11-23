# Week pack EVT02: Fees, structure, strategy and cheaper substitutes (week 2026-W47)

## Scope (pillars v3)
The agent detects and cites changes to:
- TER or sponsor fee, including the end of a bitcoin fee waiver;
- replication, securities lending, distribution policy, domicile and KID availability;
- options-income strategy (overwrite ratio, strike rule, ELN or listed options, payout frequency).
It also finds new same-index lines, such as a UCITS twin of a US-only product.
It seeds missing TERs from issuer KIDs: IB1T.L, BTCW.L, QYLD.L, QYLU.L and any other line with a blank ter column. This is required before the first order in their groups, and each probe is logged in CHANGELOG. Confirmed TER changes are appended to ter_history (CST01).
Output 1, line severity: an adverse confirmed change is 2. The cheaper-substitute trigger is computed by code: severity 1 when an eligible same-index substitute's CST10 is 10 bps or more lower, after US withholding and FIT12 headroom.
Output 2, group score from -2 to +2: adverse severity 1/2/3 gives -1/-2/-2 for the group. A confirmed fee cut, a cheaper same-index substitute or a new UCITS twin gives +1. Penalty-only in the line view.

Sources: Web search. Primary sources: issuer KIDs, prospectus supplements and notices, SEC 485 and 497 filings, justETF profiles (agent part verified by data test 1: iShares KID parsed, EDGAR J.P. Morgan ETF Trust filings listed, justETF profiles parsed). The code substitute trigger reads CST10 from v2_line_values.csv: verified for UCITS lines, unverified for US lines until those rows are added.

## Fund groups you score (-2..+2 for the next 1-3 months; NWS: against the world; premium-income groups: against their underlying)
global_equity, us_large_broad, tech_ai_semis

Owner mix: world 70% (VWRA.L), S&P 500 20%, Nasdaq-100 10%. Owner-mix groups: global_equity (world), us_large_broad (S&P 500), tech_ai_semis and us_large_broad (Nasdaq-100). Crypto excluded by the owner.

## Group moves against the world (proxy ETF; z on 52-week volatility; |z| > 2 = unexplained, seed a topic)
| group | proxy | 1w vs world % | z | 4w vs world % | z | unexplained |
|---|---|---|---|---|---|---|
| global_equity | VT | 0.0 | 0.0 | 0.0 | 0.0 |  |
| us_large_broad | SPY | 0.2 | 0.35 | 0.01 | 0.01 |  |
| tech_ai_semis | QQQ | 2.37 | 1.58 | -1.01 | -0.34 |  |

## Lines
Held: none yet (first deposit this month)
Shortlisted (orders, line-choice winners, owner-confirmed): SPXS.L, VWRA.L, XNAS.L
Same-index substitutes: world: VWRA.L, FWRA.L, ACWD.L, VT, ACWI; sp500: CSPX.L, VUAA.L, SPXS.L, SPY5.L, HSPD.L, XSPU.L, VOO, IVV, SPYM, SPY; ndx100: CNDX.L, EQQU.L, XNAS.L, QQQM, QQQ

## Macro readings mapped to you
none mapped

All MAC readings: MAC01 10y-3m +0.60 pts; inverted 0 of last 6 months; Sahm 0.00 (ON); MAC02 HY spread 3.52% (3m +0.77); Baa-10y 1.56 (off); MAC03 VIX 29.2, VIX/VIX3M 1.11 (ON); MAC04 10y TIPS 2.88% (3m +0.53); core CPI 3m ann. 3.7% vs 12m 2.9% (ON); MAC05 broad dollar 3m +3.2%; AED/USD 3.6728 (peg 3.6725) (off); MAC06 1-year daily SPY/IEF correlation +0.17 (ON); MAC07 oil 92.9 USD, 3m -2.5% (off); MAC08 NFCI -0.48 (off); MAC09 world -8.3% from high (-8.3% from 52-week high); below 10-month average; 12-1 return +12.0%; equal-weight vs S&P 500 6m +6.5% (off); MAC10 3 of 9 flags on (policy-uncertainty flag off) (off)

## Last week
"no previous v3 run"

## Activity index A = 1 (explorer floor = 1 + A = 2, cap 6 per round)
