# Week pack EVT01: Fund corporate actions (week 2026-W47)

## Scope (pillars v3)
The agent scans held lines, shortlisted lines and same-index substitutes, in every wrapper, for:
- closure, merger, liquidation or trust termination;
- share-class conversion, delisting, ISIN or ticker change, share split;
- loss of the USD or primary-exchange line;
- a fund converting into a leveraged or single-stock product.
For US funds this includes SEC 497 supplements and N-14, N-8F and 8-K filings; for ETPs, issuer redemption notices.
Output 1, line severity: 0 none, 1 watch, 2 review (confirmed notice), 3 act. Two dated, cited sources are required, and a primary source for severity 2 or more. Penalty-only in the line view (50/40/25/0). Severity 2 or more blocks deposits at once and feeds S1.
Output 2, group score from -2 to +2, in news_log.csv. It comes from the severity of the group's held line, or its CST10-chosen line if none is held, through the map 0/1/2/3 to 0/-1/-2/-2. A group with an eligible substitute ready under DUR06 is scored one step less negative. A confirmed favourable action, such as a merger into a cheaper same-index line, scores +1.

Sources: Web search. Primary sources: issuer notices, investegate.co.uk RNS (daily NAV notices filtered out), SEC EDGAR 497, N-14, N-8F and 8-K filings, and ETP issuer notices.

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
