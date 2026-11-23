# NWS16 Options-income fund news, 2026-W47 (14-20 Nov), verified

**Status:** not saturated (2 rounds, 9 explorers). Every score is capped at |1| and every confidence at low.

| Group | Score | Conf |
|---|---|---|
| global_premium_income | 0 | low (was medium) |
| sp500_premium_income | 0 | low |
| ndx100_premium_income | 0 | low |

**Key points**
- The volatility spike into the 20 Nov monthly roll is confirmed against Cboe: VIX 35.89 (19.99 at the October roll), VIX/VIX3M about 1.16, and VXN 45.25 (27.13 in October). Call premiums are much richer, which supports December income, but the overlays cap a snapback. Net effect: neutral.
- The JEPG.L -4.59% / z -2.34 flag is a pipeline artifact. The W-FRI resample picks up Monday 23 Nov. True-window excess vs VT is about +5.3 pts. The JEGA ASX distribution revision to 30.8092c is confirmed, but it is about 0.6% of the unit price and belongs to a different fund.
- Nvidia CEO episode (resigned 12 Nov, NS/export committee formed 17 Nov, reinstated 23 Nov): severity 1 watch. Q3 verified.

**Severities:** NVIDIA 1; all others 0. None were 2 or higher.

**Verifier changes**
- The global confidence was lowered from medium to low because of the unsaturated cap. Nothing was at +/-2 or severity 2+.
- Confirmed: Cboe VIX/VIX3M/VXN, ASX 16 Nov PDF, two Nvidia releases.
- Unconfirmed: FRED (bot wall) and the CNBC 19 Nov page (HTTP 403). Both verified=false; no score relies on them.

**Open threads:** fix packs_v3 W-FRI truncation at 20 Nov; check stale LSE quotes; retrieve JEPI/JEPQ/QYLD November declarations and 19a-1 notices; run the UCITS structural sweep and the owner-mix null check; confirm the T2 cause of the spike.

Held at 0%: information only. No gate or the US$60k cap is affected.
