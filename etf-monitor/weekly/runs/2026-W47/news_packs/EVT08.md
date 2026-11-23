# Week pack EVT08: Broker, venue, product access and funding channel (week 2026-W47)

## Scope (pillars v3)
The agent watches IBKR changes for UAE clients:
- which IBKR entity holds the account, which also decides where USD cash sits for FIT12;
- LSE commission (US$1.70 minimum) and the US tiered or fixed plan;
- FX terms and the US$2 minimum;
- fractional shares for LSE and US lines;
- access to US ETFs under PRIIPs/KID rules, crypto-ETP permissions for LSE bitcoin ETNs, and W-8BEN renewal.
It also watches LSE and US exchange outages, the CBUAE peg stance, and UAE remittance and USD-wire fees. Confirmed changes update the allocator constants, ELG08 and the funding block.
Per-sleeve score from -2 to +2, mapped to the sleeves and venues each change affects: LSE UCITS lines, US-listed lines, the bitcoin sleeve (ETP or US ETF route) and the options-income sleeve.
- Adverse severity 1/2/3 gives -1/-2/-2. Examples: loss of US-ETF access is -2 for US-listed lines; withdrawal of crypto-ETP permission is -2 for the bitcoin ETP route; a higher US commission is -1 for US-listed lines.
- A confirmed improvement gives +1, for example cheaper commission, fractional LSE shares or new ETP access.

Sources: Web search. Primary sources: IBKR pricing pages and notices; LSE, NYSE and Nasdaq notices; CBUAE releases. IBKR account facts themselves come only from the owner (ELG08).

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
{
 "MAC05": {
  "name": "Dollar and AED peg",
  "reading": "broad dollar 3m +3.2%; AED/USD 3.6728 (peg 3.6725)",
  "flag": false
 }
}

All MAC readings: MAC01 10y-3m +0.60 pts; inverted 0 of last 6 months; Sahm 0.00 (ON); MAC02 HY spread 3.52% (3m +0.77); Baa-10y 1.56 (off); MAC03 VIX 29.2, VIX/VIX3M 1.11 (ON); MAC04 10y TIPS 2.88% (3m +0.53); core CPI 3m ann. 3.7% vs 12m 2.9% (ON); MAC05 broad dollar 3m +3.2%; AED/USD 3.6728 (peg 3.6725) (off); MAC06 1-year daily SPY/IEF correlation +0.17 (ON); MAC07 oil 92.9 USD, 3m -2.5% (off); MAC08 NFCI -0.48 (off); MAC09 world -8.3% from high (-8.3% from 52-week high); below 10-month average; 12-1 return +12.0%; equal-weight vs S&P 500 6m +6.5% (off); MAC10 3 of 9 flags on (policy-uncertainty flag off) (off)

## Last week
"no previous v3 run"

## Activity index A = 1 (explorer floor = 1 + A = 2, cap 6 per round)
