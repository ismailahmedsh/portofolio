# Decision rules

The weekly engine answers four questions. The rules come from the 2015-2026 backtest in `src/backtest.py` (results in `runs/backtest_latest.json`), not from opinion.

## 1. Keep holding the core fund (VWRA)?

**HOLD and keep depositing**, unless a structural problem appears. Structural means one of:
- a news agent reports closure, merger, liquidation, suspension, delisting, sanctions or a fee increase for the core fund;
- the core UCITS price feed has gone stale for more than 7 days;
- the expense ratio rises above 0.30%.

Any of these turns the answer into **REVIEW: possible switch of core fund**. You then check the source, and if it is confirmed, switch to the named alternative (SPYY/ACWD) per plan v5.

Price signals never trigger a sale of the core. Selling VT to T-bills on its own downtrend (strategy S8) cut the time-weighted return from 10.4% to 7.4% a year with same-week execution and to 9.5% with lagged execution, and did not avoid the 2020 crash.

## 2. Where does this month's deposit go?

To the core, unless `satellite_share` in `config/portfolio.yaml` is above zero. In that case that share goes to the top-ranked ETF that has a verified UCITS line on the LSE. The default is 0 because sending each deposit to the top-ranked fund (S5) has no robust edge: with same-week execution it trails holding time-weighted (10.0% vs 10.4%), with lagged execution it leads (11.1% vs 10.4%), and its deflated Sharpe probability is about 0.85, below the 0.95 bar. It is the strategy to watch. The cap is 20%.

## 3. Sell or switch anything else?

Only on a structural red flag, as in rule 1. Weekly switching into the top 5 (S1) returned 5.7% to 8.7% a year on your money, depending on execution timing, against 11.8% for holding. Monthly switching (S2) returned 8.7% to 9.2%. Top-1 switching (S4) returned about 3%. News-based selling cannot be backtested, so it is not used.

## 4. When would the rules change?

The first weekly run of each month re-runs the backtest. A rotation rule is proposed for use only if it passes the gate coded in `src/backtest.py` (`gate_pass`):
1. beats holding VT time-weighted in 2015-2019, in 2020-today and overall, after costs;
2. does so under both execution assumptions: trading at the signal's Friday close, and trading one week later (real LSE execution on Monday sits between);
3. has a deflated Sharpe probability above 0.95 under both, given every strategy tested (the count lives in `N_TRIALS`).

The live 100-pillar score cannot be rebuilt historically (fund facts, valuations and news have no point-in-time history), so the backtest uses a 9-feature price composite. Weekly reports from now on build that history, and after 52 weeks the live score can be tested on its own record.

Momentum (S3) returned 14.4% to 15.0% on your money, but lost 4% to 6% a year in 2015-2019, had a 50% drawdown and trails holding time-weighted. It fails the gate.

## What the flags mean

- **Trend flag on the core**: below its 200-day average with negative 12-month momentum. Information only.
- **Expense ratio check** uses the proxy fund's fee from the data feed. VWRA's own fee (0.14% since July 2026) is checked by hand at each quarterly re-scan.
- **Drawdown protocol**: when the core is more than 20% below its 52-week high, the report says so. The rule is unchanged: keep depositing.
- **Red flags** from news agents list issues to read, with sources. Only the structural kinds in rule 1 lead to action.
