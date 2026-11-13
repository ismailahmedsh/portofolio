# Decision rules v3 (engine v3, pillars v3)

Replaces DECISION_RULES_V2.md for engine v3. Source: the audited allocation method and sell rules in config/pillars_v3.json, with the owner's decisions of 2026-11-12 and 2026-11-13 (CHANGELOG.md): crypto excluded for now, options-income at 0%, mix 70/20/10. Sections 1-4 are the v2 rules, kept; section 5 adds the v3 rules.

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

## 5. Added in v3
- US-listed lines (VOO, QQQM, VT and others) are compared with the London line on the same index after a 30% tax on their dividends (no US-UAE treaty). A US line is bought only if it is 10 bps a year cheaper after that tax (20 bps once US holdings pass US$45,000), you have recorded your IBKR entity and W-8BEN date in config/portfolio_v2.yaml, and you have added it to `orderable`.
- US$60,000 cap on US-situs holdings (US estate tax). No US order may take them above US$54,000; above US$60,000 at a month-end, the excess is moved to the London twin (S8).
- Minimum order US$340, so the US$1.70 commission stays at or below 0.5%. A sleeve whose order would be smaller waits and its gap carries.
- Options-income funds are scored for information only. No money goes to them until you set a target, an underlying and the sleeve it comes from.
- Crypto is excluded by your decision. The bitcoin pillar (BTC01, FIT13, S7) is switched off and returns only if you turn it on.
- News: 24 news pillars, each with its own lead agent, are scored and logged every week (runs/news_log.csv). Structural events (EVT severity 2 or more, confirmed by a primary source) block buying a line at once. Other news is shown only and moves no money until the forward test REC08 passes (104 weeks of log, about late 2028).
- Macro flags (MAC01-MAC10) are context only. They never delay or skip a deposit and never trigger a sale.
- If the weekly committee is not unanimous, the engine's order stands and nothing is sold.
