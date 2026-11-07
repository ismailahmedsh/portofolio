# Goal of the weekly system (v2, agreed 2026-11-07)

## In one sentence
Build and grow a portfolio of UCITS ETFs, bought through IBKR on the London Stock Exchange, from 2,500 AED (about US$680) added every month, aiming for the highest long-run return the owner can hold through crashes, by scoring 200+ funds every week on 100 audited pillars and deciding each month where the new money goes.

## Owner context
- Canadian citizen resident in the UAE, Branch A of plan v5: no UAE tax, Canadian non-resident, so Irish-domiciled UCITS funds are the default wrapper. US-listed funds cost 30% dividend withholding and US estate-tax exposure above US$60,000.
- Horizon 15+ years. Deposits arrive monthly in AED.
- Existing anchor: VWRA, which is one candidate, not a fixed answer. S&P 500 (CSPX, VUAA), Nasdaq-100 (CNDX, EQAC), regional, factor, sector, bond and gold UCITS funds are all candidates.

## What the system must answer
| Cadence | Question |
|---|---|
| Weekly | How is each holding doing, has anything structural changed, which candidates are rising or falling across the 100 pillars, what to watch |
| Monthly | Where this month's 2,500 AED goes: which fund or funds, how much each |
| Monthly | Does any holding need to be reduced or sold, and why |
| Quarterly | Is the portfolio's mix still right (regions, sectors, styles, concentration, overlap) |

## Constraints
- Cost per buy: IBKR LSE minimum US$1.70 per order, about 0.25% of a US$680 buy. Prefer one or two funds per month.
- Taxes: no capital-gains tax in the UAE, so selling has no tax cost while Branch A holds; costs are commission, spread and FX.
- Evidence: any rule that moves money must be backtested with monthly deposits and realistic costs, and beat holding the world market under both execution assumptions (see DECISION_RULES.md); the system records every pick so the rule can be re-tested on live data.

## Success measures
- Money-weighted return after all costs versus a VWRA-only portfolio with the same deposits.
- Worst drawdown versus the world market.
- No unforced sells in drawdowns.
- A few hours a month of the owner's time.
