# Week pack EVT06: Tax and legal regime for a UAE resident (week 2026-W46)

## Scope (pillars v3)
The agent sets severity only when a primary source confirms a change. It watches:
- US estate tax for non-resident aliens: the US$60,000 exemption equivalent (IRC 2102, US$13,000 credit) and situs rules (IRC 2104);
- US withholding: 30% under 871(a) and 1441, the 871(k) exemptions, 871(m), 1446(f), W-8BEN rules, and any surcharge on foreign holders;
- the Ireland-US treaty rate of 15%, and the Irish fund regime;
- the Canada-US treaty estate credit, which needs Canadian residence and so does not apply to the owner;
- Canadian residency and departure rules (s.128.1, s.94.1);
- UAE personal and corporate tax, CRS and the crypto reporting framework (CARF);
- Indian tax on foreign portfolio investors;
- PRIIPs/KID access rules.
Severity 2 or more freezes sales (S6), except S1 and S8 switches that reduce US-situs exposure, and re-runs TAX01, TAX03, CST10 and FIT12. A confirmed change to the estate threshold updates FIT12's constants after the owner confirms it.
Group or wrapper score from -2 to +2:
- an adverse change gives -1/-2/-2 by severity for the groups or wrapper sets it hits. Examples: a US surcharge on foreign holders is -2 for US-listed lines in every group; a rise in Indian FPI tax is -1 for india;
- a favourable change confirmed by T1 plus T2 sources (for example a higher estate exemption, or a US-UAE treaty) gives +1, or +2 if material.

Sources: Web search. Primary sources: IRS (the nonresident estate-tax page fetched and confirms US$60,000, data test 5), Treasury, Federal Register, Revenue.ie, UAE MoF and FTA, CRA, OECD, the European Commission, FCA.

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
