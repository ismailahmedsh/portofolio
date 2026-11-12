# Decision rules v2 (engine v2, pillars v2)

Replaces DECISION_RULES.md for engine v2. Source: the audited allocation method and sell rules in config/pillars_v2.json, amended by the owner's decision of 2026-11-12 (CHANGELOG.md).

## 1. Where each month's deposit goes
- Cash: 2,500 AED at 3.6725, minus the US$2 conversion minimum, about US$678.74, plus any left-over cash from last month.
- It goes to the sleeve of your strategic mix (config/portfolio_v2.yaml) that is furthest below its target, in one order. A second order only if the cash is at least US$680 more than one order needs (for example a lump sum).
- Line choice inside a sleeve: the lowest all-in cost (fee, US withholding, tax-rule risk, distribution friction) among lines that pass every gate. The world sleeve uses VWRA, with FWRA then ACWD as fallbacks.
- Gates that must pass: Irish or Luxembourg domicile, USD line, not leveraged or short, not money-market, price feed under 7 days old, no unexplained price jumps, confirmed buyable by you in IBKR (VWRA exempt), data coverage of 70% or more, no restricted-market exposure.
- If no line in the target sleeve passes, the money goes to the next sleeve, and finally to VWRA. The deposit is never skipped.
- Whole shares only. What is left over waits for next month.

## 2. When scores may move money
Scores (the exposure view X and the fit view) are display-only until the REC04 gate passes: a tilt rule must beat your mix by at least 0.25 points a year in every sub-period, under both execution timings, with a deflated probability above 0.95 counting every trial (N_TRIALS, now 26). Tilts are then limited to 10% per sleeve, 15% in total and 2 of any 12 deposits, and each change needs your confirmation.

## 3. When to sell (sell rules S0-S6, unchanged from the audit)
- S0 Never a reason to sell: trend, momentum, any score or rank, drawdown depth, volatility, macro readings, news sentiment.
- S1 Structural exit: fund closure or merger, a gate turning to fail, a feed stale for more than 7 trading days, a benchmark change that takes the line out of its sleeve, sanctions or issuer events impairing 5% or more. Switch the whole position to the best eligible same-index line, never into cash, after you confirm the primary source.
- S2 Cost or durability switch: stop buying first; sell only if the cost gap is 15 bps a year or more at 2 quarterly checks, ten years of saving exceed 3 times the round-trip cost, and less than half the saving rests on one tax rule.
- S3 Drift beyond limits: stop buying the sleeve; sell only if more than 12 months of deposits would be needed to cure it, and then only down to the limit.
- S4 Removing a sleeve from your mix: freeze it (no new money, no sale) and let deposits dilute it.
- S5 Bond share rebalance (only if you add one): once a year, never while the world is more than 20% below its high.
- S6 Tax or legal change for you: freeze all sales until an adviser review.
- Guardrails: 30-day cooling-off, no non-structural sale while the world is more than 15% below its high, missing data never triggers a sale.

## 4. What you maintain (about an hour a month)
- After each buy, add a row to `fills` (or update `positions`) in config/portfolio_v2.yaml.
- When you confirm a line can be bought in IBKR, add it to `orderable`. Start with one S&P 500 line and one Nasdaq-100 line from the cheapest in the weekly report, plus FWRA and ACWD as VWRA fallbacks.
- Change `strategic_mix` whenever you decide to; each change is logged in CHANGELOG.md.
