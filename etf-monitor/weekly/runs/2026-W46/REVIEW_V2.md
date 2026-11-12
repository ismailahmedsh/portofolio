# Independent review: engine v2, week 2026-W46

## Verdict: SOUND WITH FIXES

The part that moves money is correct: the deposit plan, gap routing, whole shares, fallbacks and line choice by CST10. The exposure view X, the fit view and the REC04 gate depart from the approved spec. They are display-only and the gate fails, so nothing wrong is bought today.

## BLOCKING

**B1. X is not the approved X.** `engine_v2.py` `run.expo`, mirrored in `run_v2.py` `x_point_in_time`.
- RSK01 is the beta-scaled drawdown (`dd_i - FAC05*dd_w`). The spec's round-3 fix requires the mean of raw excess max drawdown (k 10), RSK02 (k 24) and RSK04 (k 5). RSK02 is computed but never scored.
- The factor regression uses 120 months, without the Developed WML factor (downloaded, unused) and without min(1, |t|/2) shrinkage. The spec says 60 months with Newey-West errors.
- FAC04 uses an RMW threshold of -0.1 and keeps negative SMB; the spec gives 0 unless RMW ≥ 0.
- EXR08 compounds the last 60 months; the spec window is months -60 to -13.
- FAC05 is a Blume-adjusted beta on raw returns; the spec says Ledoit-Wolf on excess returns.

**B2. FIT04 has phantom alpha.** `engine_v2.py` `run`, `exp_ret` and the `FIT04` line.
- The code computes `E_i - Σw·E_k`; the spec computes `E_i - (β_i/β_P)·E_P`.
- At zero tilts CNDX still gets +0.30%/yr, so the spec's built-in check (FIT04 = 0 ± 0.1) would fail. This is the error round 3 called blocking.
- The only built-in check coded (world X = 50) can never fail, because VWRA is compared with itself.
- Fix: apply the β_i/β_P scaling and add the scoring rule 13 checks.

**B3. REC04 does not test the live rule.** `run_v2.py` `rec04` and `sim_mix`.
- No 3-month X mean, no FIT04 > 0 condition, no hysteresis.
- A flat 10% band replaces the per-sleeve bands (Nasdaq-100 and EIMI 7.5%, factor and small-cap 5%).
- Sub-periods are judged on time-weighted returns; the spec says money-weighted.
- CMA_perp is fitted on the full sample (slope 0.555, against 0.604 on data to 2011), which is look-ahead.
- "same_month" is really a 1-month lag and "lagged" a 2-month lag.
- Periods are 2012-26, not 2003-14 / 2015-19 / 2020-26.
- The deflated-probability formula is correct, but the trial spread (0.25 annual IR) is an undisclosed hard-coded assumption. It sets the hurdle at 0.50 annual IR.
- "Not passed" is safe; a future pass would not be.

## MINOR

1. **Plan** (`run_v2.plan`):
   - It allows up to 3 orders; the spec allows 2.
   - The "no gap above US$100 → core" rule is missing.
   - An unaffordable cheapest line skips the whole sleeve instead of trying the next line within 10 bps (shown with CSPX US$819 and CNDX US$1,617).
   - Residue is not carried forward automatically (`extra_cash_usd` is not in the yaml).
   - ELG08 reads `E2.CFG`, not the `cfg` argument.
   - The final fallback can produce a 0-unit order.
   - There is no switch hysteresis and no CON05 or FIT11 gate.
2. **`clean_units`:**
   - It multiplies by the raw jump ratio, not the nearest power of 100. This sets that day's return to 0 and shifts all earlier history.
     - XDJP (204.7x spike): history raised 2.6%, a real +2.6% move erased.
     - UCRP: a 0.9% move erased.
   - Switches between 5x and 50x are missed (CSWG 0.025 / 29.7), and so are the alternating ±33% moves in IEMA and IJPA in 2009-10.
   - The simplified ELG06 lets CSWG through: FIT06 = 37,870 bps, FIT10 = 92%, X = 46.
   - Sleeve lines are not affected.
3. **Grouping:**
   - S&P 500 (CSPX, VUAA, SPXS, SPY5, HSPD, XSPU) and FTSE All-World (VWRA, FWRA) are correct, with no wrong members.
   - EQQU is missing from Nasdaq-100 (its key is "eqqq nasdaq 100").
   - ACWD is split from ISAC (its name adds "line").
4. **World splice:**
   - VT is dividend-adjusted.
   - The VT-VWRA overlap correlation is 0.977, which fails the spec's ELG07 test (0.98 or more); the splice is used untested.
   - The engine uses VWRA+VT while REC04 and REC07 use VT alone, so there is not one world reference.
5. **Line view:**
   - TAX03 and DUR06 have unverified sources but carry weight (rule 9).
   - DUR01 is dropped from coverage. Without that, CSPX coverage would be 0.686, failing ELG09; the spec's verified-only count gives about 0.81.
   - Luxembourg physical lines are taxed at 15%, not 30%.
   - `us_yield` is fetched live, with a silent 1.2% fallback, so runs cannot be reproduced.
   - CST10 leaves out the residue × r_forgone cost.
6. **REC07:**
   - It starts in 2008-07, dropping the spec's 2003-07 period (where the mix lost in the preliminary run) and the Nasdaq-100 crash of 2000-02.
   - There is no US$20,000 starting case and no whole-share simulation.
7. **Report:**
   - "63 of 100 pillars computed by code" overstates it: REC02 is not computed, and ELG06, ELG07 and CST02 are not built as defined.
   - "before UAE withholding" should read "before US dividend withholding".
   - The timing labels are wrong (see B3).
   - The REC07 table does not disclose the missing 2003-07 period.

## Independent checks

| Check | Result |
|---|---|
| Cash | 2,500/3.6725 - 2 = 678.74; 3 VWRA × 188.96 + 1.70 = 568.58; residue 110.16. All match. |
| Fake positions: 100 VWRA, world over target | 44 SPXS, cost 673.67 |
| + 400 SPXS | 10 XNAS |
| + 8 CSPX instead | counted as the S&P 500 sleeve; order goes to XNAS |
| World below target | VWRA |
| Lump sum 3,678.74 | one order of 240 SPXS |
| Only CSPX and CNDX orderable | falls back to VWRA; the deposit is never skipped |

**100% world REC07 row, re-derived in a separate loop.** 221 months, US$150,000 paid in, final US$460,508. Money-weighted 11.15%, time-weighted 8.78% (VT CAGR 8.90%). Worst drop -43.8%, worst year -31.8%. Sub-periods 5.40 / 8.66 / 12.10. All match exactly.

**REC04 re-run.** It reproduces the JSON: IR 0.08 / 0.14, deflated probability 0.049 / 0.077.

## Re-review after fixes (2026-11-12)

Commit 4daabeb; engine, REC04 and REC07 re-run from scratch.

**B1 (X not the approved X): PARTIALLY CLOSED.**
- Now matching the spec:
  - The factor regression is 60-month Newey-West with WML and t-shrinkage.
  - CMA is orthogonalised point-in-time.
  - FAC04 counts only when RMW ≥ 0.
  - FAC05 is a 120-month excess-return beta.
  - RSK01 is the mean of raw excess drawdown, RSK02 and RSK04.
  - EXR08 covers months -60 to -13.
  - The world reference runs Ken French, then ACWI, then VT. The splice tests run and fail (XSPU 0.971, CNDX 0.973).
- Still open: when a group has under 120 months of history, the RSK family is missing, and `exposure.score` re-weights X over EXR and FAC only. Rule 10 makes a family with no data score 50 (c = 0).
  - Live effect: the six highest X values all have no risk family (IUCS 89.9, GLRA 89.4, DPYA 85.7, EPRA 84.5, IUMS 81.6, VERG 80.8).
  - REC04 effect: EFA scores X 58-66 in 2008-12, but its RSK family first exists in 2013-03.
- Fix: score a family with no data as 50, or start each sleeve only once RSK is available.

**B2 (FIT04 phantom alpha): CLOSED.**
- `fit04` uses β_i/β_P.
- On live data with priors at 0 and equal costs, max |FIT04| = 4e-16 across 169 groups.
- `self_check()` runs in `engine_v2.run`.

**B3 (REC04 does not test the live rule): CLOSED.**
- In place: the 3-month X mean, two consecutive quarters, FIT04 > 0, per-sleeve bands, hysteresis, the 2-of-12 cap, money-weighted sub-periods, lag 0 and lag 1, point-in-time CMA, and a disclosed trial spread.
- Re-run with priors: information ratio -0.76 / -0.75, deflated probability 0.00, gate not passed.
- Residues (minor):
  1. "Priors = 0" can never tilt: without priors FIT04 is identically 0, so FIT04 > 0 never holds. It equals the mix exactly (US$558,589), so the report's claim that it "separates what the data say" is unsupported.
  2. The gate requires an excess above 0, while DECISION_RULES_V2.md requires at least 0.25 points.

**Minor fixes verified:**
- At most 2 orders.
- `clean_units` rescales by exactly 100.
- Groups with corrupt history are dropped (max FIT06 now 72 bps).
- EQQU is in the Nasdaq-100 group.
- REC07 starts in 2003, and the mix loses there: 14.79% against 16.39% for the world.

**New minor:** the 2008-03 world return is NaN (the first ACWI month) and the simulations treat it as 0%; fall back to Ken French for that month. ACWD still forms its own group.

**Independent check:** I re-derived the new 100% world REC07 row in a separate loop: 286 months, final US$732,457, money-weighted 9.93%. Both match.

**Final verdict: SOUND WITH FIXES.** The money path is sound, and B2 and B3 are closed. One blocking item remains: X drops a missing risk family instead of scoring it 50. It is a one-line fix in `exposure.score`, needed before any X ranking or REC04 result is relied on.
