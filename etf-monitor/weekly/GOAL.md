# Goal of the weekly system (v2, agreed 2026-11-07)

## In one sentence
Build and grow a portfolio of UCITS ETFs, bought through IBKR on the London Stock Exchange, from 2,500 AED (about US$680) added every month, aiming for the highest long-run return the owner can hold through crashes, by scoring 200+ funds every week on 100 audited pillars and deciding each month where the new money goes.

## Owner context
- Canadian citizen resident in the UAE, Branch A of plan v5: no UAE tax, Canadian non-resident, so Irish-domiciled UCITS funds are the default wrapper. US-listed funds cost 30% dividend withholding and US estate-tax exposure above US$60,000.
- Horizon 15+ years. Deposits arrive monthly in AED.
- Starting mix and yardstick (owner decision, 2026-11-12): the owner's own strategic mix in config/portfolio_v2.yaml, initially 70% world (VWRA), 20% S&P 500, 10% Nasdaq-100. Every deposit goes to the sleeve furthest below its target; any score-driven rule must beat this mix in the backtest gate before it can move money. Results are also shown against 100% world, 100% S&P 500 and 100% Nasdaq-100. S&P 500 (CSPX, VUAA), Nasdaq-100 (CNDX, EQAC), regional, factor, sector, bond and gold UCITS funds are all candidates.

## What the system must answer
| Cadence | Question |
|---|---|
| Weekly | How is each holding doing, has anything structural changed, which candidates are rising or falling across the 100 pillars, what to watch |
| Monthly | Where this month's 2,500 AED goes: which fund or funds, how much each |
| Monthly | Does any holding need to be reduced or sold, and why |
| Quarterly | Is the portfolio's mix still right (regions, sectors, styles, concentration, overlap) |

## Owner requirements (2026-11-13)
- News is essential: a main pillar category with expanding agent research every week, logged so it can earn a vote.
- Candidates include US-listed ETFs (30% dividend withholding priced in; total US-listed holdings capped at US$60,000), spot bitcoin ETFs (speculative, at most 5% of the portfolio) and options-income ETFs. Leveraged and single-stock ETFs are information only.

## Constraints
- Cost per buy: IBKR LSE minimum US$1.70 per order, about 0.25% of a US$680 buy. Prefer one or two funds per month.
- Taxes: no capital-gains tax in the UAE, so selling has no tax cost while Branch A holds; costs are commission, spread and FX.
- Evidence: any rule that moves money must be backtested with monthly deposits and realistic costs, and beat holding the world market under both execution assumptions (see DECISION_RULES.md); the system records every pick so the rule can be re-tested on live data.

## Success measures
- Money-weighted return after all costs versus the owner's strategic mix with the same deposits (also shown against 100% world, S&P 500 and Nasdaq-100).
- Worst drawdown versus the world market.
- No unforced sells in drawdowns.
- A few hours a month of the owner's time.

## Owner decision (2026-11-13, later the same day)
Crypto is excluded for now; focus on the baseline mix (70% world, 20% S&P 500, 10% Nasdaq-100). Options-income is shown for information at 0%. Both can be revisited later.
