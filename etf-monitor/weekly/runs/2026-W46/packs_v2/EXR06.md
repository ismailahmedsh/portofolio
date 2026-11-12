# Pillar EXR06: Currency valuation
Definition: Exposure-weighted z-score of each non-USD currency's BIS real effective exchange rate (broad basket) against its expanding mean, needing at least 10 years of data, inverted so cheaper scores higher. Release-lagged.
Coverage rule: missing for an exposure unless REER covers at least 70% of its non-USD weight. Before 10 years of data exist (about 2004-01), it is missing for every exposure.
Currencies: every currency above 2% of any sleeve's weight, including TWD and KRW (EIMI is about 26% Taiwan and 18% Korea).
Currency weights: live from holdings. In REC04 they come from the ELG07 frozen region mix with its stated as-of date (earliest documented index weights), plus a disclosed sensitivity run on today's mix. BIS files are revised vintages, not point-in-time; this is disclosed.
Weight 0.4 of EXR (8% of X), inside the value-cluster cap.
Source: Primary: BIS WS_EER M.R.B.<cc> CSV (verified 2026-11-07: XM and TW to 2026-09; KR from 1994-01). Backup: FRED RB<cc>BIS via curl --http1.1 (RBXMBIS, RBJPBIS, RBGBBIS, RBCNBIS, RBINBIS, RBTWBIS, RBKRBIS; verified 1994-01 to 2026-07). Then the cached last good value with an age flag. Holdings currency weights. (verified). Better when: higher (more undervalued foreign currency). Informs: portfolio_mix.
Week 2026-W46.

## From this week's report
Pillar coverage this week

63 of 100 pillars have code that computes them this week (some as record or context with weight 0, as the spec defines) and 10 are scored by the event agents in the weekly workflow; the rest are listed below with the reason.

| Family | Built and computed | Agents | Not built yet | Unverified source |
|---|---|---|---|---|
| ELG | ELG01, ELG02, ELG03, ELG04, ELG05, ELG06, ELG07, ELG08, ELG09, ELG10 | - | - | - |
| CST | CST01, CST02, CST04, CST06, CST08, CST10 | - | CST03 | CST05, CST07, CST09 |
| TAX | TAX01, TAX03, TAX05 | - | - | TAX02, TAX04 |
| DUR | DUR01, DUR02, DUR04, DUR06 | - | - | DUR03, DUR05, DUR07, DUR08 |
| EXR | EXR02, EXR08 | - | EXR03, EXR04, EXR06, EXR11, EXR12 | EXR01, EXR05, EXR07, EXR09, EXR10 |
| FAC | FAC01, FAC02, FAC03, FAC04, FAC05 | - | - | - |
| RSK | RSK01, RSK02, RSK03, RSK04, RSK05, RSK06, RSK07, RSK08 | - | - | - |
| CON | CON04, CON05 | - | CON01, CON02, CON03 | - |
| FIT | FIT01, FIT02, FIT03, FIT04, FIT05, FIT06, FIT07, FIT10, FIT11 | - | FIT08, FIT09 | - |
| MOM | MOM01, MOM02, MOM03, MOM04, MOM05 | - | - | - |
| REC | REC01, REC02, REC03, REC04, REC07 | - | - | REC05, REC06 |
| MAC | MAC01, MAC02, MAC03, MAC04 | - | - | - |
| EVT | - | EVT01, EVT02, EVT03, EVT04, EVT05, EVT06, EVT07, EVT08, EVT09, EVT10 | - | - |

