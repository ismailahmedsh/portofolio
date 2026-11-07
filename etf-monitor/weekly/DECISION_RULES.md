# Decision rules

The weekly engine answers four questions. The rules come from the 2015-2026 backtest in `src/backtest.py` (results in `runs/backtest_latest.json`), not from opinion.

## 1. Keep holding the core fund (VWRA)?

**HOLD and keep depositing**, unless a structural problem appears. Structural means one of:
- a news agent reports closure, merger, liquidation, suspension, delisting, sanctions or a fee increase for the core fund;
- the core UCITS price feed has gone stale for more than 7 days;
- the expense ratio rises above 0.30%.

Any of these turns the answer into **REVIEW: possible switch of core fund**. You then check the source, and if it is confirmed, switch to the named alternative (SPYY/ACWD) per plan v5.

Price signals never trigger a sale of the core. Selling VT to T-bills on its own downtrend (strategy S8) cut the return from 10.4% to 7.4% a year and did not avoid the 2020 crash.

## 2. Where does this month's deposit go?

To the core, unless `satellite_share` in `config/portfolio.yaml` is above zero. In that case that share goes to the top-ranked ETF that has a verified UCITS line on the LSE. The default is 0 because sending each deposit to the top-ranked fund (S5) roughly matched holding (12.2% vs 11.8% on your money, 10.0% vs 10.4% time-weighted) with more concentration. The cap is 20%.

## 3. Sell or switch anything else?

Only on a structural red flag, as in rule 1. Weekly switching into the top 5 (S1) returned 5.7% a year on your money against 11.8% for holding. Monthly switching (S2) returned 8.7%. Top-1 switching (S4) returned 2.8%.

## 4. When would the rules change?

The first weekly run of each month re-runs the backtest. A rotation rule is proposed for use only if it:
1. beats holding VT in both 2015-2019 and 2020-today, time-weighted, after costs;
2. has a deflated Sharpe probability above 0.95, given every strategy ever tested (the count lives in `N_TRIALS`);
3. still beats holding with a one-week execution delay.

Momentum (S3) is the one to watch. It returned 14.4% on your money, but lost 6% a year in 2015-2019, had a 50% drawdown and trails on a time-weighted basis. It fails tests 1 and 2.

## What the flags mean

- **Trend flag on the core**: below its 200-day average with negative 12-month momentum. Information only.
- **Drawdown protocol**: when the core is more than 20% below its 52-week high, the report says so. The rule is unchanged: keep depositing.
- **Red flags** from news agents list issues to read, with sources. Only the structural kinds in rule 1 lead to action.
