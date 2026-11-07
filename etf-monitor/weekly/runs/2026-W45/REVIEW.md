# Independent review, 2026-W45

**Verdict: SOUND WITH FIXES.** The accounting is correct: S0 matches to the dollar, and I found no look-ahead (signals use data up to Friday t; positions earn only week t+1). HOLD is supported. The problems are in the claims: headline numbers use fills that cannot be executed, the promotion gate is described but never coded, and the report overstates what was tested.

## BLOCKING

1. **Headline results use same-close fills that cannot be executed** (`backtest.py` `simulate`, lines 46-49, `delay=1`). The engine trades at the same Friday US close that makes the signal, but VWRA trades on the LSE, which closes earlier. Under the executable delay=2 run:
   - S1 money-weighted: 5.71% → 8.66%.
   - S8 time-weighted: 7.41% → 9.45% (S0 10.42%); money-weighted 10.02% → 11.21%. So "cut the return from 10.4% to 7.4%" (DECISION_RULES) and "cost 3 points a year" (`run_weekly.py` line 84) become about 1 point time-weighted, 0.6 on your money.
   - S5 time-weighted: 9.99% → 11.07%.

   Fix: make delay=2 the headline, keep delay=1 as a sensitivity, and store full stats for both.

2. **The promotion gate is not implemented, and S5 passes tests 1 and 3 under executable timing.** DECISION_RULES §4 and REPORT line 92 say "the engine ... will propose...", but no code evaluates tests 1-3. With delay=2, S5 beats S0:

   | | S5 | S0 |
   |---|---|---|
   | Time-weighted | 11.07% | 10.42% |
   | 2015-19 | 9.34% | 8.83% |
   | 2020-26 | 12.34% | 11.58% |
   | Money-weighted | 13.04% | 11.85% |

   The deflated Sharpe is computed only for the best Sharpe strategy (S0 itself). The edge is fragile: S5 time-weighted is 9.99/11.07/10.35% at 0/1/2-week lags against about 10.4%. So: "no robust edge". Fix: code a per-strategy pass/fail table, with deflated Sharpe on returns in excess of S0.

3. **The "Sell anything?" row misstates the evidence** (`run_weekly.py` line 83, "Selling on scores, news or trend lost money in every tested variant"):
   - No variant lost money; all money-weighted returns are positive.
   - News-based selling was never backtested.
   - S6 never sold. VT's composite never fell below 0.387, and its percentile never below 0.31, so S6 equals S0.
   - The live 100-pillar composite (G=20, H, I, J) was never tested, only a 9-feature price composite.

   Fix: "Selling VT on its own trend (S8) trailed holding by 0.6-1.8 points a year on your money; selling on the live composite or news is untested."

4. **"Why rotation trails" is contradicted by the data** (`run_weekly.py` line 91). The backtest composite's top-5 holdings, 2015-2026, were 19% tech_ai_semis and only 17% defensive buckets. S5's picks led with DXJ, IHI and ITA. Fix: delete the sentence or state the measured cause, and label the signal "price-only composite (9 features)".

## MINOR

- **S6 rule** (lines 117-121): compares the composite value to 0.30, not its percentile as described. Neither triggers, so S6 is a dead trial still counted in `N_TRIALS` and the deflated Sharpe.
- **State carry-over** (line 145): `state`/`st2` are not reset before the delay=2 runs. Harmless today, but latent.
- **Deflated Sharpe** uses absolute Sharpe (S0 scores 0.894), so it cannot test a rotation against holding. `N_TRIALS` omits delay variants, S7 and the S6→S8 iteration.
- **Costs**: 10 bps "incl. commission" plus US$1.70 double-counts commission. Conservative; 0.03 points on S0.
- **Dropped daily returns** (`pillars.compute_quant`): 69 London-only days since 2015 drop returns next to US holidays (VT: 244 instead of about 250 a year). Filter to rows where SPY is not NaN, as `backtest.py` does.
- **H07 sign is correct**: oil up gives XLE/XOP 100 and XLP 30. But WTI is from 2026-11-03, stale in a week oil fell about 15%. Show data age.
- **News weighting** (50 + 25 × score × {1, 0.75, 0.4}) is correct and bucket keys are valid. But uncovered J pillars sit at 50, so news weight scales with how many agents cover a bucket.
- **G pillars**: G09 applies 30% withholding to bond-ETF yields, though most of that interest is exempt for non-residents. G04 flags any fund with missing AUM.
- **Core checks** (`run_weekly.py`):
  - The expense-ratio rule reads VT's (0.06%), not VWRA's.
  - Keyword matching is substring-based ("merg" matches "emerging").
  - Target matching misses list and bucket-level flags.
  - The 20% satellite cap is not enforced.
  - IOO maps to VWRA, the core itself.
  - UCITS proxies mismatch: USMV→MVOL, VTI→CSPX, IAGG/BNDX→AGGU.
- **Missing caveat**: "No structural red flag" omits J10's note that its closure and fee scan was incomplete.
- **Overclaims**: DECISION_RULES says S3 "fails test 2", but its deflated Sharpe was never computed; the structural triggers were never backtested. "A broad world fund always ranks mid-pack" is opinion (VT ranks 53/200). "News effect fades within days" has no source.

## Independent S0 check

VT, US$2,500 each first Friday from 2015-01-09 (holiday Fridays filled at the prior trading day).

| Item | Independent | backtest.py |
|---|---|---|
| Deposits / contributed | 143 / US$357,500 | US$357,500 |
| Final value, no costs | US$748,002 | n/a |
| XIRR, no costs | 11.88% | n/a |
| Final value, 10 bps + US$1.70 per buy | US$746,745 | US$746,745 |
| XIRR, with costs | 11.85% | 11.85% |
| Time-weighted CAGR | 10.51% gross | 10.43% (net of deposit costs) |
| Max drawdown, weekly | -32.6% | -32.6% |

S8 sold on 2020-04-10 at 58.93 and bought back on 2020-06-05 at 68.25, so it did not avoid 2020.
