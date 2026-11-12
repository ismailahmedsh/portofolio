# Pillar ELG07: Proxy mapping, approved equivalents and splice fidelity
Definition: (a) The line's benchmark must equal the history proxy's index or match a row in config/approved_equivalents.csv (to be created; versioned, changed only through CHANGELOG). Each row states its allowed use:
- price splice;
- holdings stand-in for constraints only, never for tracking difference: CNDX for XNAS and EQQU; CSPX for VUAA and SPXS; SSAC/ISAC (MSCI ACWI) for VWRA and FWRA, reconciled by ELG10; SWDA minus its US rows, renormalised, for EXUS;
- the single declared world reference used in REC04, REC07, FAC05, RSK01 and RSK04: Ken French Developed market + RF until 2008-02, then ACWI to 2008-05, then VT (before 2008 it excludes EM; disclosed);
- exposure history: Ken French Developed ex US market + RF for EXUS; Ken French Emerging market + RF for EIMI before EEM; ^NDX price plus an estimated dividend (trailing QQQ yield, or 0.5% a year before 1999) for the Nasdaq-100 before QQQ (1999-03), so that RSK01 sees the 2000-02 crash;
- the frozen per-sleeve region mix for EXR06 currency weights in REC04, with its as-of date and citation (the earliest documented index weights, entered by hand; today's holdings mix is used only as a disclosed sensitivity run).
(b) Splice test: at least 24 months of overlap, monthly correlation of 0.98 or more and an annualised gap of 50 bps or less. If it fails, nothing from the proxy is used, pillars that need longer history read missing for that exposure, and a sleeve with no passing splice (likely IWVL, IWQU, WSML) is excluded from score mode and named in the REC04 report. EXUS has about 30 months of overlap, which is enough but only barely.
Source: iShares UK 'Benchmark Index' field; justETF profiles; yfinance monthly closes, including ^NDX (verified 2026-11-07: 1985-10 to 2026-11, 494 rows); iShares holdings CSV (SSAC productId 251850 verified: 1,738 rows, US 63.88%; SWDA verified); Ken French Developed, Developed ex US and Emerging files (verified to 2026-09) (verified). Better when: pass. Informs: weekly_review.
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

## Data notes

- Splice tests (ELG07: 24+ months overlap, correlation 0.98+, gap 50 bps or less): CNDX not used (correlation 0.973, gap -3 bps); EIMI not used (correlation 0.983, gap 58 bps); XSPU not used (correlation 0.971, gap -16 bps). Where a splice fails, the exposure view uses the line's own London history.
- Prices: Yahoo Finance via yfinance, LSE lines converted to USD; unofficial and for personal use.
- Fund size is missing from Yahoo for 126 lines (for example CSPX, CNDX); it is listed as missing, not held against them.
- Tracking difference (CST02) fails closed until fee history is collected, so line choice uses current fee plus US withholding.
- Same-index groups come from the index named in each fund's name, confirmed by return correlation.

