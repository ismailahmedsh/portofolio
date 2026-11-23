# Week pack EVT09: Deposit-week calendar and market dislocations (week 2026-W47)

## Scope (pillars v3)
The agent lists the deposit-week events: FOMC, US CPI and payrolls, ECB, BoE and BoJ meetings, index rebalance days, option expiries, ex-dates of held distributing lines, and US, UK and UAE holidays. It adds any ETF dislocation, exchange outage, or bitcoin ETP gap after a large weekend move.
It recommends the order day and session (LSE 14:30-16:15 London; US 10:00-15:30 New York), given MAC03's state. It may delay an order by at most 1 week, and every delay is logged in REC05. It never skips a deposit or triggers a sale.
Per-group execution score on the -2..+2 scale, limited to -1 or 0: -1 when the group due an order this month has a conflict in its order window, otherwise 0. It is logged in news_log.csv but kept out of N and out of REC08's primary test, because it forecasts order-day friction, not 1-3 month returns. It is tested against realised entry cost in REC05.

Sources: Web search; central-bank, index-provider and exchange calendars; MAC03 readings.

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

Deposit window: the first LSE trading days of next month after the AED arrives; this month's planned order: [{"sleeve": "world", "ticker": "VWRA.L", "units": 3, "price_usd": 178.72, "cost_usd": 537.86, "gap_before_usd": 475.11}]

## Macro readings mapped to you
none mapped

All MAC readings: MAC01 10y-3m +0.60 pts; inverted 0 of last 6 months; Sahm 0.00 (ON); MAC02 HY spread 3.52% (3m +0.77); Baa-10y 1.56 (off); MAC03 VIX 29.2, VIX/VIX3M 1.11 (ON); MAC04 10y TIPS 2.88% (3m +0.53); core CPI 3m ann. 3.7% vs 12m 2.9% (ON); MAC05 broad dollar 3m +3.2%; AED/USD 3.6728 (peg 3.6725) (off); MAC06 1-year daily SPY/IEF correlation +0.17 (ON); MAC07 oil 92.9 USD, 3m -2.5% (off); MAC08 NFCI -0.48 (off); MAC09 world -8.3% from high (-8.3% from 52-week high); below 10-month average; 12-1 return +12.0%; equal-weight vs S&P 500 6m +6.5% (off); MAC10 3 of 9 flags on (policy-uncertainty flag off) (off)

## Last week
"no previous v3 run"

## Activity index A = 1 (explorer floor = 1 + A = 2, cap 6 per round)
