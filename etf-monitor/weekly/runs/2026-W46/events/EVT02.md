# EVT02 Fees, structure and KID: week 2026-W46

**Result: no adverse event; one data correction (severity 0).**

## Line events
- **VWRA.L (severity 0, favourable).** Vanguard cut the ongoing charge on the FTSE All-World UCITS ETF from 0.19% to 0.14% a year, effective 2026-07-28 ([Vanguard notice, 2026-07-20](https://www.nl.vanguard/professional/insights/were-lowering-fees-on-one-of-our-most-popular-etfs)). The universe file still says 0.19. Append `2026-07-28, 0.14` to ter_history and refresh CST01. VWRA is now cheaper on TER than FWRA (0.15%).

## Checked, nothing found (2026-11-07 to 2026-11-12)
- No TER rise, replication or lending change, distribution-policy change, domicile change or KID issue was found for any world, S&P 500 or Nasdaq-100 line.
- No new LSE USD line or fee cut was announced on FTSE All-World, S&P 500 or Nasdaq-100.

## Context
- **Amundi LSE delisting.** Amundi delisted 26 share classes from the LSE, with the last trading day on 2026-11-06 and the delisting effective 2026-11-09 ([Investegate notice](https://www.investegate.co.uk/announcement/eqs/lyxor-international-asset-management--djel/amundi-asset-management-delisting-of-26-ucit-/9700859)). None of the 13 Amundi lines in the universe is on the ticker list, so no action is needed.
- **SPY5 fee.** SPY5's 0.03% fee (versus 0.07% for CSPX and VUAA) dates from 2023 and is not new. The cheaper-substitute test is computed by code (CST10). SPY5 distributes, so TAX and distribution drag apply.
- **Other 2026 fee cuts outside the sleeves.** Invesco cut its MSCI World fund to 0.05% (March), and DWS (March) and UBS (May) also cut fees. None of these funds tracks a sleeve index.
