# Pillar CST07: Premium or discount to NAV, time-aligned (record)
Definition: Mean |aligned price / NAV - 1| over 20 sessions, in bps, where aligned price = LSE close(t) adjusted by the reference index or futures move between the NAV valuation point and 16:30 London. iShares lines use the daily Historical NAVs sheet. VWRA has only the vanguard.co.uk embedded navPrices JSON spot value (no history), so it has no 20-session value. Weight 0, because the main non-iShares buy lines (VWRA, VUAA, SPXS, XNAS) have no daily NAV history. Yahoo navPrice is never used. The same aligned method is used for the S1 discount check.
Source: iShares fund-document API 'Historical NAVs' sheet (verified: CSPX daily NAV 2010-05 to 2026-11-06); vanguard.co.uk embedded navPrices JSON (verified spot: USD 183.4672 on 2026-11-06, no history); other issuers unverified (unverified). Better when: lower. Informs: record_for_testing.
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

