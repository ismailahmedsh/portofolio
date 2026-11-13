# Week pack EVT05: Issuer, custodian and counterparty health (week 2026-W46)

## Scope (pillars v3)
The agent detects:
- issuers leaving the ETF business;
- changes of custodian, administrator or vault, and incidents at a bitcoin custodian or prime broker (each triggers a DUR02 re-check);
- swap, securities-lending and ELN counterparty downgrades, defaults or incidents;
- credit events at an ETP issuer;
- regulatory sanctions on an issuer, depositary or trustee.
It also keeps each issuer's closure and merger record. A finding applies to every line of that issuer or custodian.
Output 1, severity: penalty-only. Severity 2 or more blocks deposits at once, and an impairment of 5% or more of NAV triggers S1.
Output 2, group score from -2 to +2: severity 1/2/3 gives -1/-2/-2 for each group whose held or chosen line is affected. A group in which the incident hits most lines, such as a shared bitcoin custodian, gets -2 at severity 2 or more. A confirmed improvement, such as a second custodian added or segregation strengthened, gives +1.

Sources: Web search. Primary sources: notices from the Central Bank of Ireland, CSSF, FCA, SEC, FINRA and Jersey FSC; issuer and custodian releases; rating-agency actions.

## Fund groups you score (-2..+2 for the next 1-3 months; NWS: against the world; premium-income groups: against their underlying)
global_equity, us_large_broad, tech_ai_semis

Owner mix: world 70% (VWRA.L), S&P 500 20%, Nasdaq-100 10%. Owner-mix groups: global_equity (world), us_large_broad (S&P 500), tech_ai_semis and us_large_broad (Nasdaq-100). Crypto excluded by the owner.

## Group moves against the world (proxy ETF; z on 52-week volatility; |z| > 2 = unexplained, seed a topic)
| group | proxy | 1w vs world % | z | 4w vs world % | z | unexplained |
|---|---|---|---|---|---|---|
| global_equity | VT | 0.0 | 0.0 | 0.0 | 0.0 |  |
| us_large_broad | SPY | 0.32 | 0.56 | -0.1 | -0.09 |  |
| tech_ai_semis | QQQ | 2.24 | 1.52 | -2.21 | -0.75 |  |

## Lines
Held: none yet (first deposit this month)
Shortlisted (orders, line-choice winners, owner-confirmed): SPXS.L, VWRA.L, XNAS.L
Same-index substitutes: world: VWRA.L, FWRA.L, ACWD.L, VT, ACWI; sp500: CSPX.L, VUAA.L, SPXS.L, SPY5.L, HSPD.L, XSPU.L, VOO, IVV, SPYM, SPY; ndx100: CNDX.L, EQQU.L, XNAS.L, QQQM, QQQ

## Macro readings mapped to you
none mapped

All MAC readings: MAC01 10y-3m +0.78 pts; inverted 0 of last 6 months; Sahm 0.00 (ON); MAC02 HY spread 3.30% (3m +0.59); Baa-10y 1.51 (off); MAC03 VIX 18.0, VIX/VIX3M 0.90 (off); MAC04 10y TIPS 2.78% (3m +0.35); core CPI 3m ann. 3.7% vs 12m 2.9% (off); MAC05 broad dollar 3m +2.4%; AED/USD 3.6726 (peg 3.6725) (off); MAC06 1-year daily SPY/IEF correlation +0.25 (ON); MAC07 oil 92.1 USD, 3m -0.4% (off); MAC08 NFCI -0.46 (off); MAC09 world -3.7% from high (-3.7% from 52-week high); above 10-month average; 12-1 return +12.0%; equal-weight vs S&P 500 6m +7.2% (off); MAC10 2 of 9 flags on (policy-uncertainty flag off) (off)

## Last week
"no previous v3 run"

## Activity index A = 1 (explorer floor = 1 + A = 2, cap 6 per round)
