# Changelog

## 2026-11-12: owner mix replaces VWRA as the default and the yardstick
- Owner decision: each month's deposit follows the owner's own strategic mix (config/portfolio_v2.yaml), starting at 70% world (VWRA), 20% S&P 500, 10% Nasdaq-100. The same mix is the yardstick that any score-driven rule must beat in the backtest gate before it can move money.
- This is an owner choice outside the evidence rule, as pillars v2 allows ("the owner may amend GOAL.md explicitly"). REC07 still runs every month and shows how the mix compares with 100% world, 100% S&P 500 and 100% Nasdaq-100, as information.
- The 15% tilt cap, per-sleeve maxima and the 2-of-12 deposit limit now apply to score-driven tilts away from the mix, not to the mix itself.
- DECISION_RULES.md rule 2 changes: the deposit goes to the sleeve furthest below its target in the owner mix (one order), not to "the top-ranked ETF".
- N_TRIALS: unchanged by this entry (the mix is not a tested rule). Each later edit to the mix is logged here.
