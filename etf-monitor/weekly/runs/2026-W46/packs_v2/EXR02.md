# Pillar EXR02: Beta-consistent expected excess return in % a year (FIT04 input)
Definition: For equity exposures:
E[R_i - R_f] = beta_i x ERP_world + clip(sum_j b_j x (x_ij - x_VWRA,j), -2%, +2%) - (CST10_i - CST10_VWRA)/100.
- beta_i is the single FAC05 beta (univariate, 120 months, Ledoit-Wolf, on the ELG07 world reference). The same number is used in FIT04, RSK01 and RSK04. ERP_world = 4.0%.
- b_j are unestimated priors, labelled as such in every weekly output. EXR06: +0.5% per unit of REER z. EXR08: -0.01% per point of relative return. FAC01: +1.5% per unit of beta. FAC02: +1.5%. FAC03 (CMA orthogonalised to HML): +1.0%. FAC04: +1.0%. Because CMA is orthogonalised, value is not paid twice.
- REC04 also runs a pre-registered variant with all b_j = 0 (pure beta x ERP minus cost). This shows whether the priors or the data drive qualification.
Gold: beta x ERP plus an EXR11 percentile table (below 25th +1%, 25-50 +0.5%, 50-75 0%, above 75 -1%). Bonds: EXR10 minus the 3-month T-bill. Gold and bond values are context only.
The constants live in config/pillar_scales.yaml (to be created) under the frozen config hash. Weight 0 (derived).
Built-in check: with all tilts at 0 and equal costs, FIT04 = 0 for every equity exposure. With the single beta this holds identically, and the tolerance stays ±0.1%.
Source: EXR06, EXR08, FAC01-FAC05, CST10 (verified); EXR10 (unverified, context), EXR11 (verified); 3-month T-bill from FRED DTB3 via curl --http1.1 (verified to 2026-11-05), fallback the cached last good value with an age flag (verified). Better when: higher. Informs: portfolio_mix.
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

