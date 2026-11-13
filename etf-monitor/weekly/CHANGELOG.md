# Changelog

## 2026-11-12: owner mix replaces VWRA as the default and the yardstick
- Owner decision: each month's deposit follows the owner's own strategic mix (config/portfolio_v2.yaml), starting at 70% world (VWRA), 20% S&P 500, 10% Nasdaq-100. The same mix is the yardstick that any score-driven rule must beat in the backtest gate before it can move money.
- This is an owner choice outside the evidence rule, as pillars v2 allows ("the owner may amend GOAL.md explicitly"). REC07 still runs every month and shows how the mix compares with 100% world, 100% S&P 500 and 100% Nasdaq-100, as information.
- The 15% tilt cap, per-sleeve maxima and the 2-of-12 deposit limit now apply to score-driven tilts away from the mix, not to the mix itself.
- DECISION_RULES.md rule 2 changes: the deposit goes to the sleeve furthest below its target in the owner mix (one order), not to "the top-ranked ETF".
- N_TRIALS: unchanged by this entry (the mix is not a tested rule). Each later edit to the mix is logged here.

## 2026-11-13: owner requirements for pillars v3 and a wider universe
- News is essential: news and event pillars become a main category (about 25 pillars) with expanding agent rounds, scored per sleeve with sources and logged weekly so they can be tested against the owner's mix.
- Pillar split target: news and events about 25, macro regime about 10, line choice and safety about 20, exposure/valuation/risk about 25, fit about 10, record and testing about 10 (100 in total).
- Universe adds about 150 US-listed ETFs as buy candidates, with the 30% US dividend withholding priced into their cost and a US$60,000 cap on total US-listed holdings (US estate-tax threshold for non-resident aliens), with a warning as it nears.
- New types: spot bitcoin ETFs in, labelled speculative, capped at 5% of the portfolio; options-income ETFs in (US-listed and UCITS), scored on upside given up. Leveraged and single-stock ETFs are shown for information only, never bought.
- Same-index lines count once in scoring.
- Unchanged: the owner mix sets deposits; structural events act at once; scores and news move deposit money only after passing the test against the mix.
