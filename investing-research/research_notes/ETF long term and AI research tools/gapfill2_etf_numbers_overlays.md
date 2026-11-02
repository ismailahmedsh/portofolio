# Gap-fill round 2: consistent ETF performance table, Canadian building blocks, fee reconciliation, all-weather / core-satellite evidence, trend overlays on the actual candidates, and 2026 expected real returns (R1, R2, R3, R11)

Research date: 2026-11-02. Closes audit gaps 2, 3, 4 (strategy part), 10 and 12 (fee part) from `audits/research_audit_round1.md`. Round-1 notes (`etf_core_R1_R2_R3.md`, `data_signals_R10_R11_R12.md` R11) are not repeated; this file corrects them where a primary source disagrees.

Conventions: every figure carries an as-of date, currency and source. "Issuer" = fund sponsor fact sheet or page; "Index provider" = MSCI / FTSE Russell / Nasdaq / S&P via a Vanguard sheet; "Aggregator" = third-party site (flagged); "Own calc" = my replication on yfinance dividend-adjusted monthly closes downloaded 2026-11-02 (scripts, CSVs and the price file are in `gapfill2_data/` beside this note). Returns over 1 year are annualized unless marked "cum.".

Two corrections to round 1 found along the way: (a) XUU does **not** hold US stocks directly; its Sep 30, 2026 fact sheet shows ITOT 47.99% + IVV 46.39% + IJH 2.39% + IJR 0.96%, i.e. it wraps US-listed iShares ETFs; (b) VTI's benchmark was renamed from "CRSP US Total Market" to "Morningstar US Total Market Index" on July 29, 2026 after Morningstar bought CRSP (no change to objective or holdings).

---

## Q1. Consistent performance table (issuer / index-provider fact sheets dated 2026-09-30 where available)

### Takeaway
On one basis (issuer fact sheets as of Sep 30, 2026, total return, NAV), the broad candidates line up as: US total market 14.7%/yr over 10 years (VTI, USD) and 15.3% for XUU in CAD; S&P 500 15.3% (VOO); total world 12.3% (VT); ex-US 9.2% (VXUS); EAFE 9.1% and EM 9.1% (MSCI, USD); Canada 12.4% (XIC, CAD); Canadian aggregate bonds 1.2% (XBB). Three-year standard deviations cluster at 11.6–13.5% for broad equity (MSCI/iShares), 17.2% for EM, 20.5% for the Nasdaq-100 and 5.0–5.6% for aggregate bonds. Peak-to-trough losses in the GFC were -50.8% (US total market, monthly), -58% to -65% (ACWI / EAFE / EM, daily, MSCI) and the 2022 drawdown was -18% to -26% for equity funds and -11.8% (CAD) for Canadian bonds.

### Cited Findings

**Table 1a. US-listed ETFs and their indices (USD, total return, as of 2026-09-30 unless noted)**

| Fund / index | Ccy | 1y | 3y | 5y | 10y | Since incep. (date) | 3y std dev | Max drawdown (period) | CY2008 | CY2020 | CY2022 | CY2025 | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VTI (Vanguard Morningstar Total Stock Market ETF; ER 0.03%; $689,219M) NAV | USD | 15.33 | 22.32 | 12.56 | 14.70 | 9.44 (2001-05-24) | n/a on sheet; ITOT 3y SD 13.51% (Jun 30, 2026) | -50.8% (2007-11 to 2009-02, monthly, own calc) | -37.0 (own calc) | 21.1 (own calc) | -19.5 (own calc; ITOT NAV -19.51) | 17.1 (own calc; ITOT 17.02) | [Vanguard VTI fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS970R.pdf); [iShares ITOT fact sheet](https://www.ishares.com/us/literature/fact-sheet/itot-ishares-core-s-p-total-u-s-stock-market-etf-fund-fact-sheet-en-us.pdf); own calc |
| Morningstar (ex-CRSP) US Total Market Index | USD | fund tracks within 0.03 bps of index on sheet; index line not separately printed | | | | | | | | | | | [Vanguard VTI fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS970R.pdf) |
| VOO (Vanguard S&P 500; ER 0.03%; $1,032,260M) NAV | USD | 15.70 | 22.85 | 13.75 | 15.29 | 14.94 (2010-09-07) | IVV 3y SD 13.05% (Jun 30, 2026) | -50.8% (SPY monthly, own calc) | -36.55 (S&P 500 TR, Damodaran) | 18.02 | -18.04 (IVV NAV -18.13) | 17.78 (IVV 17.85) | [Vanguard VOO fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS968R.pdf); [iShares IVV fact sheet](https://www.ishares.com/us/literature/fact-sheet/ivv-ishares-core-s-p-500-etf-fund-fact-sheet-en-us.pdf); [Damodaran histretSP (updated Jan 5, 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html) |
| S&P 500 Index | USD | 15.74 | 22.89 | 13.79 | 15.33 | 14.98 (from 2010-09-07) | 13.05 (IVV proxy) | as above | -36.55 | 18.02 | -18.11 (IVV benchmark) | 17.88 (IVV benchmark) | [Vanguard VOO fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS968R.pdf); [SPY fact sheet Sep 30, 2026 (performance table did not extract)](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spy.pdf) |
| VT (Vanguard Total World; ER 0.06%; $81,752M) NAV | USD | 16.32 | 21.42 | 11.34 | 12.32 | 8.78 (2008-06-24) | ACWI ETF 3y SD 11.65% | -44.5% monthly own calc (2008-07 start; daily -50.3% per myplaniq, aggregator) | n/a (fund began Jun 2008; Jul–Dec 2008 alone -33.0%, own calc) | 16.6 (own calc) | -18.0 (own calc) | 22.4 (own calc) | [Vanguard VT fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS3141R.pdf); [Schwab research VT page (1y 16.3, 3y 21.4, 5y 11.3, SI 8.8 NAV, 9/30/2026)](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=vt) |
| FTSE Global All Cap Index | USD | 16.7 (12M) | 21.6 | 11.5 | n/a on sheet | – | vol: 1y 11.4, 3y 12.7, 5y 15.0 | 10y drawdown -34.3% | n/a on sheet | 16.8 | -17.9 | 22.6 | [FTSE Russell factsheet, 30 Sep 2026](https://research.ftserussell.com/Analytics/FactSheets/Home/DownloadSingleIssue?issueName=GEISLMS&isManual=false) |
| Spliced Total World Stock Index (VT's benchmark line) | USD | 16.57 | 21.48 | 11.39 | 12.40 | 8.84 | | | | | | | [Vanguard VT fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS3141R.pdf) |
| VXUS (Vanguard Total International; **ER 0.05%**; $163,231M) NAV | USD | 18.49 | 20.15 | 9.35 | 9.20 | 6.53 (2011-01-26) | IXUS 3y SD 12.45% | not on sheet | n/a (incep. 2011) | 11.5 (FTSE AW ex-US) | -15.2 (FTSE AW ex-US; IXUS NAV -16.35) | 32.6 (FTSE AW ex-US; IXUS 32.63) | [Vanguard VXUS fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS3369R.pdf); [iShares IXUS fact sheet](https://www.ishares.com/us/literature/fact-sheet/ixus-ishares-core-msci-total-international-stock-etf-fund-fact-sheet-en-us.pdf) |
| FTSE All-World ex US Index (large/mid; VXUS tracks the All Cap ex US variant) | USD | 20.0 (12M) | 20.8 | 10.0 | n/a | – | vol 1y 14.3, 3y 15.1, 5y 15.4 | n/a | n/a | 11.5 | -15.2 | 32.6 | [FTSE Russell factsheet, 30 Sep 2026](https://research.ftserussell.com/Analytics/FactSheets/Home/DownloadSingleIssue?issueName=AWXUSAS&isManual=false) |
| MSCI EAFE (net, USD) | USD | 15.69 | 18.40 | 9.32 | 9.07 | 5.61 (since 2000-12-29) | 13.02 (5y 15.56, 10y 15.04) | -60.41% (2007-10-31 to 2009-03-09) | n/a on sheet | 7.82 | -14.45 | 31.22 | [MSCI EAFE factsheet Sep 30, 2026](https://www.msci.com/documents/10199/822e3d18-16fb-4d23-9295-11bc9e07b8ba) |
| MSCI Emerging Markets (net, USD) | USD | 29.22 | 24.09 | 8.94 | 9.09 | 9.11 (since 2000-12-29) | 17.24 (5y 18.36, 10y 17.46) | -65.25% (2007-10-29 to 2008-10-27) | n/a on sheet | 18.31 | -20.09 | 33.57 | [MSCI EM factsheet Sep 30, 2026](https://www.msci.com/documents/10199/c0db0a48-01f2-4ba9-ad01-226fd5678111) |
| MSCI ACWI (net, USD) | USD | 16.75 | 21.73 | 11.57 | 12.38 | 7.41 | 12.02 (5y 14.92, 10y 14.73) | -58.38% (2007-10-31 to 2009-03-09) | n/a | 16.25 | -18.36 | 22.34 | same MSCI sheets |
| AVUV (Avantis US Small Cap Value; ER 0.25%) NAV | USD | 19.9 | 16.6 | 11.2 | n/a (incep. Sep 2019) | 14.8 (2019-09-24) | n/a; aggregator SD 27.8%, max DD -49.4% (Sep 2019–Oct 23, 2026, myplaniq) | see left | n/a | n/a (not on page) | n/a | n/a | [Schwab research AVUV (9/30/2026)](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=avuv); [Avantis AVUV page (ER, YTD 22.20% to 10/31/2026)](https://avantisinvestors.com/avantis-investments/avantis-us-small-cap-value-etf); [myplaniq AVUV (aggregator)](https://myplaniq.com/invest/quote/AVUV/); AUM $32.69B Nov 2, 2026 [stockanalysis (aggregator)](https://stockanalysis.com/etf/avuv/) |
| SCHD (Schwab US Dividend Equity; ER 0.06%) NAV | USD | 23.36 | 15.44 | 9.48 | not on page (round 1: 13.13% aggregator) | 13.11 (Oct 2011) | n/a | round 1: -33.4% (aggregator) | n/a | n/a | n/a | n/a | [Schwab research SCHD (9/30/2026)](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=schd); AUM $120.60B, yield 2.94% (Nov 2, 2026) [stockanalysis (aggregator)](https://stockanalysis.com/etf/schd/) |
| QQQ (Invesco; ER 0.18%; net assets $371.1B at Mar 31, 2026 per SEC filing) NAV | USD | 23.8 | 28.0 | 16.3 | not on page | 10.9 (Mar 1999) | see index | | | | | | [Schwab research QQQ (9/30/2026)](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=qqq); [Invesco QQQ performance page (ER 0.18%)](https://www.invesco.com/qqq-etf/en/performance.html); [SEC N-CSRS Mar 31, 2026](https://www.sec.gov/Archives/edgar/data/0001067839/000119312526250483/8deb6f921189c0e.htm) |
| Nasdaq-100 Index (TR) | USD | 23.21 | 27.37 | 15.66 | 20.09 | – | 20.54 (10y 22.78) | n/a on sheet | n/a | 47.58 | -32.97 | 20.17 | [Nasdaq NDX factsheet, 09/30/2026](https://indexes.nasdaqomx.com/docs/FS_NDX.pdf) |
| AGG (iShares US Aggregate Bond; ER 0.03%; $135,652M) NAV | USD | -1.87 | 4.05 | -0.64 | 1.11 | 2.95 | 5.57 | n/a | n/a | n/a | -13.06 | 7.19 | [iShares AGG fact sheet Sep 30, 2026](https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf) |

Notes on Table 1a: IVV and ITOT sheets are dated June 30, 2026 (their 1y/3y/5y/10y: IVV 22.29/20.58/13.37/15.47; ITOT 23.05/20.43/12.24/15.01) and are used only for the 3-year standard deviation and 2021–2025 calendar returns (IVV: 28.66, -18.13, 26.27, 24.98, 17.85; ITOT: 25.64, -19.51, 26.11, 23.82, 17.02) — [IVV](https://www.ishares.com/us/literature/fact-sheet/ivv-ishares-core-s-p-500-etf-fund-fact-sheet-en-us.pdf), [ITOT](https://www.ishares.com/us/literature/fact-sheet/itot-ishares-core-s-p-total-u-s-stock-market-etf-fund-fact-sheet-en-us.pdf). ACWI ETF (Sep 30, 2026): 1y 16.49, 3y 21.75, 5y 11.62, 10y 12.48, SI 8.49; CY 2022 -18.27, 2025 22.43 — [ACWI fact sheet](https://www.ishares.com/us/literature/fact-sheet/acwi-ishares-msci-acwi-etf-fund-fact-sheet-en-us.pdf). IXUS (Sep 30, 2026): 1y 18.72, 3y 20.38, 5y 9.36, 10y 9.27 — [IXUS](https://www.ishares.com/us/literature/fact-sheet/ixus-ishares-core-msci-total-international-stock-etf-fund-fact-sheet-en-us.pdf). Damodaran's S&P 500 series: 2024 24.88%, 2025 17.78%; 10-year Treasury 2022 -17.83%.

**Table 1b. Canada-listed ETFs and indices (CAD, total return, NAV, as of 2026-09-30)**

| Fund | 1y | 3y | 5y | 10y | Since incep. (launch) | Std dev | Max drawdown | CY2021 | CY2022 | CY2023 | CY2024 | CY2025 | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XEQT (100% equity) | 18.88 | 23.46 | 13.94 | n/a | 14.46 (2019-08-07) | own calc monthly vol 12.7% (2019-09 to 2026-10) | -17.6% monthly (2022-01 to 2022-09, own calc) | 19.57 | -10.93 | 17.05 | 24.67 | 20.45 | [BlackRock XEQT fact sheet Sep 30, 2026](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xeqt-ishares-core-equity-etf-portfolio-fund-fact-sheet-en-ca.pdf); own calc |
| VEQT (100% equity) | 18.99 | 23.52 | 13.96 | n/a | 14.24 (2019-01-29) | 9.46% (36-month, Vanguard), Sharpe 1.99 | -17.9% monthly (2022, own calc) | 19.66 | -10.92 | 16.95 | 24.87 | 20.45 | [Vanguard VEQT fact sheet (Sep 30, 2026 returns; CY to Dec 31, 2025)](https://fund-docs.vanguard.com/VEQT_All_Equity_ETF_Portfolio_9692_FS_EN_CA.pdf) |
| XAW (ACWI ex Canada) | 18.86 | 22.87 | 13.76 | 12.84 | (2015-02-10) | not on sheet | -18.5% monthly (2022, own calc) | 18.23 | -11.77 | 18.16 | 26.60 | 15.75 | [BlackRock XAW fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xaw-ishares-core-msci-all-country-world-ex-canada-index-etf-fund-fact-sheet-en-ca.pdf) |
| MSCI ACWI ex Canada IMI (XAW benchmark) | 18.95 | 23.21 | 13.57 | 12.96 | | | | 17.01 | -12.66 | 18.54 | 27.07 | 15.89 | same |
| XUU (S&P Total Market, wraps ITOT/IVV/IJH/IJR) | 17.37 | 23.96 | 15.21 | 15.27 | (2015-02-10) | not on sheet | n/a | 25.81 | -13.19 | 22.40 | 34.76 | 11.05 | [BlackRock XUU fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xuu-ishares-core-s-p-u-s-total-market-index-etf-fund-fact-sheet-en-ca.pdf) |
| S&P Total Market Index (CAD, XUU benchmark) | 17.22 | 23.87 | 14.69 | 15.02 | | | | 24.09 | -14.09 | 22.09 | 34.56 | 11.14 | same |
| VFV (S&P 500, wraps VOO) | not on page | | | | (2012-11-02) | 11.60% (36-month), beta 1.00, Sharpe 1.70 | n/a | | | | | | [Vanguard VFV page (Sep 30, 2026 risk stats)](https://www.vanguard.ca/en/investor/products/products-group/etfs/VFV); returns: round-1 Cboe aggregator only |
| XEF (MSCI EAFE IMI, direct holdings) | 17.72 | 20.32 | 11.31 | 9.73 | (2013-04-10) | not on sheet | n/a | 10.05 | -9.27 | 14.34 | 12.58 | 25.36 | [BlackRock XEF fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xef-ishares-core-msci-eafe-imi-index-etf-fund-fact-sheet-en-ca.pdf) |
| MSCI EAFE IMI (CAD, XEF benchmark) | 17.76 | 20.33 | 11.30 | 9.76 | | | | 10.13 | -9.39 | 14.35 | 12.94 | 25.17 | same |
| XEC (MSCI EM IMI, direct holdings) | 29.82 | 24.62 | 10.86 | 9.21 | (2013-04-10) | not on sheet | n/a | -2.03 | -14.56 | 7.73 | 16.43 | 25.34 | [BlackRock XEC fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xec-ishares-core-msci-emerging-markets-imi-index-etf-fund-fact-sheet-en-ca.pdf) |
| MSCI EM IMI (CAD, XEC benchmark) | 29.90 | 24.88 | 11.27 | 9.86 | | | | -1.13 | -14.01 | 8.68 | 16.81 | 25.21 | same |
| XIC (S&P/TSX Capped Composite) | 19.94 | 24.96 | 15.11 | 12.35 | (2001-02-16) | not on sheet | n/a | 25.06 | -5.85 | 11.67 | 21.53 | 31.59 | [BlackRock XIC fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xic-ishares-core-s-p-tsx-capped-composite-index-etf-fund-fact-sheet-en-ca.pdf) |
| S&P/TSX Capped Composite (XIC benchmark) | 20.02 | 25.06 | 15.18 | 12.37 | | | | 25.09 | -5.84 | 11.75 | 21.65 | 31.68 | same; RBC WM total returns 2023 11.8%, 2024 21.6%, 2025 31.7% [RBC](https://ca.rbcwealthmanagement.com/weatherill-wealth/blog/4717442-SPTSX-Composite-Index-Bearing-it-All) (via search snippet; page 404 on fetch) |
| S&P/TSX Composite price return (not total) 2008 / 2020 | | | | | | | | 2008 -35.0; 2020 +2.17 (price, aggregator) | | | | | [topforeignstocks (aggregator, Yahoo price data)](https://topforeignstocks.com/indices/the-sp-tsx-composite-index-returns-by-year/) |
| VGRO (80/20) | not on page | | | | (2018-01-25) | 8.25% (36-month) | n/a | | | | | | [Vanguard VGRO page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VGRO) |
| XGRO (80/20) | 14.64 | 19.59 | 11.18 | 10.15 | (2007-06-21; repurposed Dec 2018) | not on sheet | n/a | 15.17 | -11.00 | 14.92 | 20.47 | 16.96 | [BlackRock XGRO fact sheet Sep 30, 2026](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xgro-ishares-core-growth-etf-portfolio-fund-fact-sheet-en-ca.pdf) |
| XBB (FTSE Canada Universe Bond) | -1.19 | 4.66 | 0.21 | 1.18 | (2000-11-20) | not on sheet | n/a | -2.65 | -11.78 | 6.61 | 4.12 | 2.57 | [BlackRock XBB fact sheet Sep 30, 2026](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xbb-ishares-core-canadian-universe-bond-index-etf-fund-fact-sheet-en-ca.pdf) |
| FTSE Canada Universe Bond Index (XBB benchmark) | -1.10 | 4.75 | 0.30 | 1.29 | | | | -2.54 | -11.69 | 6.69 | 4.23 | 2.64 | same |
| ZAG (FTSE Canada Universe) | 10-yr compound 1.8%/yr to Dec 31, 2024 only (ETF Facts) | | | | (2010-01-19) | n/a | worst 3 months -7.1% (to Apr 30, 2022) | | | | | | [BMO ZAG ETF Facts](https://fundfacts.bmo.com/EtfEnglish/BMO_Aggregate_Bond_Index_ETF-EN-series_ETF_Units.pdf) |
| VAB (Bloomberg Global Agg CAD Float Adj) | not on page | | | | (2011-11-30) | 5.01% (36-month) | n/a | | | | | | [Vanguard VAB page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VAB) |

### Inferences
- The round-1 aggregator snapshots were broadly right but mixed bases; this table is all NAV total return from the sponsor. Where only the 3-year window is comparable across everything (Sep 30, 2026): US total market 22.3 (USD) / 24.0 (CAD, XUU); S&P 500 22.9; world 21.4; ex-US 20.2; EAFE 18.4 (USD) / 20.3 (CAD, XEF); EM 24.1 (USD) / 24.6 (CAD); Canada 25.0; XEQT 23.5; VEQT 23.5; Canadian bonds 4.7. The CAD figures for US/EAFE funds exceed the USD figures because CAD weakened over the window.
- Drawdown budget confirmed on primary data: -58% to -65% (MSCI daily, GFC) for global/EAFE/EM; -50.8% for US total market (monthly); XEQT/VEQT have only lived through -17.6%/-17.9% (2022, monthly), which is the live record, not the stress case.
- Volatility ranking (3y SD): aggregate bonds 5.0–5.6 < VEQT 9.5 / VFV 11.6 / VUN 12.0 (Vanguard 36-month) ≈ ACWI 11.7–12.0 < EAFE 13.0 < S&P 500 13.1 < US total 13.5 < EM 17.2 < Nasdaq-100 20.5 < AVUV ~27.8 (aggregator). Nasdaq-100's 2022 (-33.0%) and AVUV's -49% max drawdown are the price of their higher 10-year returns.

### Gaps
- S&P DJI factsheets (S&P 500, S&P/TSX Capped Composite) returned HTTP 403; S&P 500 index returns are taken from the Vanguard VOO sheet and TSX from the iShares XIC sheet. TSX **total** return for 2008 and 2020 was not located from a primary source (only price returns from an aggregator: -35.0%, +2.17%); XIC's sheet starts at 2021.
- Vanguard Canada product pages publish risk statistics but no returns; only VEQT's fact sheet PDF was located (fund-docs.vanguard.com). VFV, VUN, VIU, VEE, VCN, VAB, VGRO returns remain aggregator-only (round 1, Cboe).
- The SPY fact sheet (Sep 30, 2026) downloaded but its performance table did not extract; VOO's sheet carries the same S&P 500 index returns.
- No issuer standard deviation for the BlackRock Canada funds (not printed on their sheets); only Vanguard Canada prints 36-month SD.
- SCHD and QQQ 10-year returns are not on Schwab's research page; QQQ's index 10-year (20.09%) is primary, SCHD's 10-year (13.13%) is round-1 aggregator. Invesco's fact-sheet performance table did not render and Schwab's product page returned 403.
- AVUV calendar-year returns and 3-year SD from the issuer not found (Avantis page shows only YTD).
- VT's CY2008 is a partial year (fund began June 2008).

---

## Q2. Canadian building blocks: fee, MER, AUM, structure, yield; XEQT/VEQT MER reconciliation; VXUS fee

### Takeaway
The Canadian DIY set is now priced at 0.05–0.28% MER: XIC 0.06 / VCN 0.05 (Canada), XUU 0.07 / VUN 0.16 / VFV 0.08 / ZSP 0.09 (US), XEF 0.22 / VIU 0.21 / ZEA 0.22 (EAFE), XEC 0.28 / VEE 0.24 / ZEM 0.27 (EM), XBB 0.10 / VAB 0.08 / ZAG 0.09 (bonds). Of these, XEF, XEC, XIC, VCN, VIU, ZSP, ZEA, ZEM hold securities directly; XUU, VFV, VUN, VEE wrap US-listed ETFs (Level-II withholding applies in TFSA/RRSP). The XEQT MER is **0.19%** on the Sep 30, 2026 fact sheet (management fee 0.17% since Dec 18, 2025); VEQT's is **0.22%** as of Mar 31, 2026 (fee 0.17% since Nov 18, 2025, so the MER still mostly reflects the old 0.22% fee and should fall toward ~0.19% at the next fiscal year-end). VXUS's expense ratio is **0.05%** per Vanguard's Sep 30, 2026 fact sheet.

### Cited Findings

**Table 2. Canadian building blocks (CAD; as-of dates per source)**

| Ticker | Mgmt fee | MER | AUM | Structure | Distribution yield (12m trailing) | Inception | Source / date |
|---|---|---|---|---|---|---|---|
| XEF (iShares Core MSCI EAFE IMI) | 0.20% | 0.22% | C$24,329.62M (Sep 30, 2026) | Holds 2,466 securities directly; IEFA is 2.27% of assets | 3.04% (2.31%); semi-annual | 2013-04-10 | [BlackRock XEF fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xef-ishares-core-msci-eafe-imi-index-etf-fund-fact-sheet-en-ca.pdf) |
| XEC (iShares Core MSCI EM IMI) | 0.25% | 0.28% | C$4,945.61M (Sep 30, 2026) | Holds 2,918 securities directly; IEMG 2.58% | 1.52% (1.56%); semi-annual | 2013-04-10 | [BlackRock XEC fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xec-ishares-core-msci-emerging-markets-imi-index-etf-fund-fact-sheet-en-ca.pdf) |
| XIC (iShares Core S&P/TSX Capped Composite) | 0.05% | 0.06% | C$35,022.65M (Sep 30, 2026) | 217 Canadian stocks directly | 2.03% (2.01%) | 2001-02-16 | [BlackRock XIC fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xic-ishares-core-s-p-tsx-capped-composite-index-etf-fund-fact-sheet-en-ca.pdf) |
| XUU (iShares Core S&P US Total Market) | 0.07% | 0.07% | C$4,739.50M (Sep 30, 2026) | **Wrap**: ITOT 47.99%, IVV 46.39%, IJH 2.39%, IJR 0.96% (125 line items) | 0.86% (1.02%) | 2015-02-10 | [BlackRock XUU fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xuu-ishares-core-s-p-u-s-total-market-index-etf-fund-fact-sheet-en-ca.pdf) |
| XAW (iShares Core MSCI ACWI ex Canada) | 0.20% | 0.22% | C$4,674.44M (Sep 30, 2026) | Mixed wrap of 6 ETFs: IVV 51.50%, XEF 22.26%, XEC 12.90%, ITOT 8.27%, IJH 3.09%, IJR 1.81% | 1.31% (1.19%); semi-annual | 2015-02-10 | [BlackRock XAW fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xaw-ishares-core-msci-all-country-world-ex-canada-index-etf-fund-fact-sheet-en-ca.pdf) |
| XEQT (iShares Core Equity Portfolio) | 0.17% (0.18% before Dec 18, 2025) | **0.19%** | C$22,910.25M (Sep 30, 2026) | Mixed: ITOT 30.78%, XIC 24.89%, XEF 24.26%, IVV-type "Core S&P Total U.S." 14.99%, XEC 4.89% | 0.90% (1.58%); quarterly | 2019-08-07 | [BlackRock XEQT fact sheet Sep 30, 2026](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xeqt-ishares-core-equity-etf-portfolio-fund-fact-sheet-en-ca.pdf); [BlackRock Canada press release Dec 18, 2025](https://www.blackrock.com/ca/investors/en/literature/press-release/fee-cut-aa-1218-en.pdf) |
| XGRO (iShares Core Growth Portfolio) | 0.17% | 0.19% | C$5,213.97M (Sep 30, 2026) | Mixed: ITOT 36.88%, XEF 19.94%, XIC 19.55%, XEC 4.36%, plus bond ETFs; 8 holdings | 1.35%; quarterly | 2007-06-21 | [BlackRock XGRO fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xgro-ishares-core-growth-etf-portfolio-fund-fact-sheet-en-ca.pdf) |
| XBB (iShares Core Canadian Universe Bond) | 0.09% | 0.10% | C$10,842.53M (Sep 30, 2026) | 1,923 bonds directly; duration 6.65y; YTM 4.17% | 3.58% (3.55%); monthly | 2000-11-20 | [BlackRock XBB fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xbb-ishares-core-canadian-universe-bond-index-etf-fund-fact-sheet-en-ca.pdf) |
| VEQT (Vanguard All-Equity Portfolio) | 0.17% (0.22% before Nov 18, 2025) | **0.22% as of Mar 31, 2026** | C$17,528M (fact sheet, Sep 30, 2026) | Mixed: Morningstar US Total Market ETF 45.5%, FTSE Canada All Cap 29.65%, FTSE Dev ex-NA 17.6%, FTSE EM All Cap 7.2% (VUN/VCN/VIU/VEE, of which VUN and VEE wrap US ETFs) | 1.22% (12-month) | 2019-01-29 | [Vanguard VEQT fact sheet](https://fund-docs.vanguard.com/VEQT_All_Equity_ETF_Portfolio_9692_FS_EN_CA.pdf); [Vanguard Canada press release Nov 18, 2025](https://www.vanguard.ca/content/dam/intl/americas/canada/en/documents/PressRelease_Vanguard_PriceChanges_Final.pdf) |
| VGRO (Vanguard Growth Portfolio) | 0.17% | 0.22% (page; "as of most recent fund year end") | not shown on page | Mixed: VUN 37.21%, VCN 24.03%, VIU 14.71%, VAB 11.18%, VEE 5.72%, VBG 3.66%, VBU 3.45% | 1.97% (1.74%) | 2018-01-25 | [Vanguard VGRO page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VGRO) |
| VFV (Vanguard S&P 500) | 0.08% | 0.08% (page) | not shown (191,150,000 units Oct 31, 2026) | **Wrap**: "Invests primarily in the U.S.-domiciled Vanguard S&P 500 ETF" (VOO) | 0.84% (0.84%) | 2012-11-02 | [Vanguard VFV page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VFV) (round-1 Cboe showed 0.09% MER) |
| VUN (Vanguard US Total Market) | 0.15% | 0.16% (page) | not shown (142,351,100 units; ≈C$20.07B at Oct 30 NAV, own arithmetic) | **Wrap**: "Invests primarily in the U.S.-domiciled Vanguard Morningstar Total Stock Market ETF" (VTI) | 0.77% (0.77%) | 2013-08-02 | [Vanguard VUN page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VUN) |
| VIU (Vanguard FTSE Developed All Cap ex North America) | 0.20% | 0.21% (page) | not shown | Direct: full-replication, 3,689 holdings; page does not name a US-listed ETF (unlike VFV/VUN/VEE) | 1.61% (2.18%) | 2015-12-01 | [Vanguard VIU page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VIU) |
| VEE (Vanguard FTSE Emerging Markets All Cap) | 0.23% | 0.24% (page) | not shown (94,409,750 units) | **Wrap**: "Invests primarily in the U.S.-domiciled Vanguard FTSE Emerging Markets ETF" (VWO); 6,507 holdings | 0.42% (1.55%) | 2011-11-30 | [Vanguard VEE advisor page](https://www.vanguard.ca/en/advisor/products/products-group/etfs/VEE) |
| VCN (Vanguard FTSE Canada All Cap) | 0.05% | 0.05% (page) | not shown (248,740,600 units) | Direct: 221 Canadian stocks | 2.11% (2.05%) | 2013-08-02 | [Vanguard VCN page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VCN) |
| VAB (Vanguard Canadian Aggregate Bond) | 0.08% | 0.08% (page) | not shown (345,900,000 units) | Direct: 1,324 bonds; YTM 4.2%; duration 6.8y | 3.60% (3.48%); monthly | 2011-11-30 | [Vanguard VAB page](https://www.vanguard.ca/en/investor/products/products-group/etfs/VAB) |
| ZAG (BMO Aggregate Bond) | not on ETF Facts | 0.09% (TER 0.00%) | C$9.8B (Nov 30, 2024) | Direct: 1,638 bonds; monthly | n/a on ETF Facts | 2010-01-19 | [BMO ZAG ETF Facts](https://fundfacts.bmo.com/EtfEnglish/BMO_Aggregate_Bond_Index_ETF-EN-series_ETF_Units.pdf) |
| ZSP (BMO S&P 500) | not on ETF Facts | 0.09% (TER 0.00%) | C$22.0B (Nov 30, 2024); C$23.77B (Jul 17, 2026, Cboe aggregator) | Direct: 500 US stocks held directly ("Total number of investments: 500") | n/a on ETF Facts; quarterly | 2012-11-14 | [BMO ZSP ETF Facts](https://fundfacts.bmo.com/EtfEnglish/BMO_S%26P_500_Index_ETF-EN-series_ETF_Units.pdf) |
| ZEA (BMO MSCI EAFE) | not on ETF Facts | 0.22% (TER 0.04%, total 0.26%) | C$8.5B (Nov 30, 2024); C$13.81B (Oct 21, 2026, Cboe aggregator) | Direct: 718 securities | n/a; quarterly | 2014-02-10 | [BMO ZEA ETF Facts](https://fundfacts.bmo.com/EtfEnglish/BMO_MSCI_EAFE_Index_ETF-EN-series_ETF_Units.pdf) |
| ZEM (BMO MSCI Emerging Markets) | not on ETF Facts | 0.27% | C$1.0B (Nov 30, 2024); ~C$3.5B (May 26, 2026, P&I aggregator) | Direct: 773 securities | n/a; annual (December) | 2009-10-20 | [BMO ZEM ETF Facts](https://fundfacts.bmo.com/EtfEnglish/BMO_MSCI_Emerging_Markets_Index_ETF-EN-series_ETF_Units.pdf) |

**MER reconciliation (XEQT 0.17 vs 0.19 vs 0.20; VEQT 0.22 vs 0.24)**
- 0.17% is the *management fee* for both: BlackRock cut XEQT/XGRO/XBAL/XCNS/XINC from 0.18% to 0.17% effective Dec 18, 2025 ("exclusive of HST") — [BlackRock Canada press release](https://www.blackrock.com/ca/investors/en/literature/press-release/fee-cut-aa-1218-en.pdf); Vanguard cut VEQT/VGRO/VBAL/VCNS/VCIP from 0.22% to 0.17% effective Nov 18, 2025 — [Vanguard Canada press release](https://www.vanguard.ca/content/dam/intl/americas/canada/en/documents/PressRelease_Vanguard_PriceChanges_Final.pdf).
- 0.19% is XEQT's MER "as reported in the fund's most recent Semi-Annual or Annual Management Report of Fund Performance", printed on the Sep 30, 2026 fact sheet; the 0.20% figure in round 1 came from a blog (Tawcan) and is superseded — [BlackRock XEQT fact sheet](https://www.blackrock.com/ca/investors/en/literature/fact-sheet/xeqt-ishares-core-equity-etf-portfolio-fund-fact-sheet-en-ca.pdf).
- VEQT: 0.22% "is the MER as of March 31, 2026 ... The MER would have been 0.22% without any absorptions or waivers"; the pre-cut MER was 0.24% (advisor.ca, secondary) — [Vanguard VEQT fact sheet](https://fund-docs.vanguard.com/VEQT_All_Equity_ETF_Portfolio_9692_FS_EN_CA.pdf); [advisor.ca](https://advisor.ca/investments/products/vanguard-canada-makes-its-biggest-fee-cut-in-history/). The prospectus amendment is filed as [Amendment No. 2 to the prospectus](https://fund-docs.vanguard.com/Amend-2-Prospectus-EN.pdf) (not fetched).
- VXUS expense ratio: 0.05% on Vanguard's Sep 30, 2026 fact sheet (ChartRow's 0.07% in round 1 is stale) — [Vanguard VXUS fact sheet](https://workplace.vanguard.com/iippdf/pdfs/FS3369R.pdf).

### Inferences
- Structure matters as much as fee for a TFSA holder: the BlackRock direct-holding trio (XIC 0.06, XEF 0.22, XEC 0.28) plus XUU (0.07, wrap) averages ~0.12% MER at XEQT weights (25/25/5/45: 0.25×0.06 + 0.25×0.22 + 0.05×0.28 + 0.45×0.07), versus XEQT's 0.19%; the DIY saving is ~7 bps/yr, which is below the cost of a single mistimed rebalance. The withholding-tax drag is identical in structure (both route US exposure through US-listed iShares ETFs), so the DIY case rests on the 6 bps and on rebalancing with contributions, not on tax.
- VEQT's 0.22% MER will not show the full fee cut until the FY2026 MRFP; expect ~0.19% (0.17% + HST), i.e. parity with XEQT.
- BMO's ETF Facts (Nov 30, 2024 AUM) are stale relative to iShares/Vanguard Sep 30, 2026 data; use Cboe for current BMO AUM and flag it.

### Gaps
- BMO product pages are JavaScript-only; ETF Facts give MER and Nov 2024 AUM but no management fee, yield or Sep 2026 returns. ZEM's AUM conflict (C$1.0B ETF Facts vs ~C$3.5B P&I) is unresolved.
- Vanguard Canada pages show no total assets ("—"); only VEQT's AUM came from its fact sheet. VIU's direct-holding status is inferred from the absence of a "U.S.-domiciled" statement on its page.
- Prospectus amendment PDFs were not read; press releases are used as the dated primary record of the fee cuts.

---

## Q3. All-weather / risk parity / permanent-type portfolios and core-satellite evidence

### Takeaway
Across every source and my own replication, the defensive multi-asset portfolios (All Weather, Golden Butterfly, Permanent, RPAR) delivered roughly 5–8%/yr nominal with 8–10% volatility and 16–21% worst drawdowns since 2007, versus 10.6%/yr, 16% volatility and -50.8% for 100% US equity and 7.8%/yr, -32% for 60/40. Their advertised weakness is real: 2022 was their worst year (-13% to -19%; RPAR -22.8%) because long Treasuries fell with stocks, and over the RPAR live window (Dec 2019–Oct 2026) the live fund compounded at 3.4%/yr versus 14.6% for VTI. Practitioners (Morningstar) put the satellite sleeve at 5–20% of a portfolio with the explicit warning that it "is in no way a guarantee of outperformance"; no primary PWL or Bogleheads text on satellite caps was retrievable.

### Cited Findings

**Table 3a. Published long-horizon statistics (nominal unless stated; aggregator/backtest sites flagged)**

| Portfolio | CAGR | Std dev | Max drawdown | Worst recent drawdown | Source (as-of) |
|---|---|---|---|---|---|
| All Weather (30 VTI / 40 TLT / 15 IEI / 7.5 DBC / 7.5 GLD) | 10y 5.94%, 20y 6.60%, 30y 7.24%, since 1871 6.36% | 30y 7.52% | -37.02% (Sep 1929–May 1932; recovered Apr 1935) | -20.58% (Jan 2022–Sep 2022; recovered Jun 2025; 42 months) | [lazyportfolioetf (aggregator, Oct 31, 2026)](https://www.lazyportfolioetf.com/allocation/ray-dalio-all-weather/) |
| All Seasons (30 LCB / 40 LTT / 15 ITT / 8 gold / 7 commodities), real, 1970–2025 | avg real 5.3%, baseline 15-yr real 3.9% | 8.7% | deepest real drawdown 22%; longest 11 years | | [PortfolioCharts](https://portfoliocharts.com/portfolios/all-seasons-portfolio/) |
| Golden Butterfly (20 each VTI / IJS / TLT / SHY / GLD) | 10y 7.67%, 20y 7.48%, 30y 7.87%, since 1927 8.47% | 30y 8.00% | -48.31% (1929–1932) | not listed | [lazyportfolioetf (aggregator)](https://www.lazyportfolioetf.com/allocation/golden-butterfly/) |
| Golden Butterfly, real, 1970–2025 | avg real 6.3%, baseline 5.3% | 8.3% | deepest real drawdown 18%; longest 5 years | | [PortfolioCharts](https://portfoliocharts.com/portfolios/golden-butterfly-portfolio/) |
| Permanent (25 VTI / 25 TLT / 25 BIL / 25 GLD) | 10y 7.10%, 20y 6.91%, 30y 6.89%, max 5.38% | 30y 6.90% | -30.61% (1929–1932) | -15.92% (Jan–Sep 2022; recovered Mar 2024) | [lazyportfolioetf (aggregator)](http://www.lazyportfolioetf.com/allocation/harry-browne-permanent/) |
| 60/40 (VTI / BND) | 10y 9.61%, 20y 8.04%, 30y 8.08%, max 7.33% | 30y 9.73% | -62.03% (1929–1932) | -20.69% (2022, recovered Feb 2024); -30.55% (Nov 2007–Feb 2009) | [lazyportfolioetf (aggregator)](https://www.lazyportfolioetf.com/allocation/stocks-bonds-60-40/) |
| 100% US stocks (VTI) | 10y 14.87%, 20y 10.83%, 30y 10.17%, max 8.44% | 30y 15.72% | -84.60% (1929–1932; recovered Dec 1944) | -24.81% (2022); -50.84% (Nov 2007–Feb 2009, recovered Mar 2012) | [lazyportfolioetf (aggregator)](https://www.lazyportfolioetf.com/allocation/us-stocks/) |
| All Weather vs S&P 500, real, 1973–2024 | 4.6% vs 6.5% real; "two drawdowns greater than 20%" since 1973; GFC decline "less than half" of 60/40 | | | | [Of Dollars and Data, 2024 update](https://ofdollarsanddata.com/ray-dalio-all-weather-portfolio/) |
| All-Weather vs 60/40 vs 100% equities, 1934–2023 (UK-based blog) | 3.1% vs 4.0% vs 5.5% (basis not stated); vol 9.0 / 14.8 / 20.6 | | 1972–74: -28% vs -60% vs -72% | | [Monevator (secondary)](https://monevator.com/asset-allocation-for-all-weathers) |

**Table 3b. RPAR live record (issuer, USD)**

| | 1y | 3y | 5y | Since 2019-12-12 | CY2020 | 2021 | 2022 | 2023 | 2024 | 2025 | ER / AUM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RPAR NAV (as of 9/30/2026) | 2.65% | 9.34% | 0.42% | 3.40% | 19.35 | 7.78 | -22.81 | 6.32 | -0.11 | 18.28 | 0.52% net (0.50% ex-AFFE); $552.06M (10/30/2026) |

— [RPAR fund page](https://www.rparetf.com/rpar).

**Table 3c. Own replication on one data set (monthly, rebalanced monthly, yfinance adjusted closes; no fees beyond ETF ERs; "ETF era" = Jul 2007–Oct 2026, "live" = Dec 2019–Oct 2026)**

| Portfolio | Window | CAGR | Max DD | Vol | CY2008 | CY2020 | CY2022 | CY2025 | Worst calendar year |
|---|---|---|---|---|---|---|---|---|---|
| 100% US (VTI) | ETF era | 10.61% | -50.8% | 16.0% | -37.0 | 21.1 | -19.5 | 17.1 | -37.0 (2008) |
| 100% US (VTI) | live | 14.63% | -24.8% | 17.1% | – | 21.1 | -19.5 | 17.1 | -19.5 (2022) |
| 60/40 (VTI/BND) | ETF era | 7.82% | -32.2% | 10.2% | -21.5 | 16.4 | -16.7 | 13.2 | -21.5 (2008) |
| 60/40 (VTI/BND) | live | 9.13% | -20.7% | 11.7% | – | 16.4 | -16.7 | 13.2 | -16.7 (2022) |
| All Weather (30/40/15/7.5/7.5) | ETF era | 6.36% | -21.0% | 8.1% | -0.9 | 17.2 | -18.9 | 12.8 | -18.9 (2022) |
| All Weather | live | 5.15% | -21.0% | 9.9% | – | 17.2 | -18.9 | 12.8 | -18.9 (2022) |
| Golden Butterfly | ETF era | 7.40% | -18.0% | 8.7% | -6.1 | 15.8 | -13.4 | 18.1 | -13.4 (2022) |
| Golden Butterfly | live | 7.85% | -18.0% | 10.4% | – | 15.8 | -13.4 | 18.1 | -13.4 (2022) |
| Permanent (VTI/TLT/BIL/GLD) | ETF era | 6.70% | -16.4% | 7.5% | -1.0 | 17.0 | -13.0 | 20.7 | -13.0 (2022) |
| Permanent | live | 7.20% | -16.4% | 8.7% | – | 17.0 | -13.0 | 20.7 | -13.0 (2022) |
| 100% world (VT) | Jul 2008– | 8.68% | -44.5% | 16.6% | – | 16.6 | -18.0 | 22.4 | -18.0 (2022) |
| 100% world (VT) | live | 12.52% | -25.5% | 16.2% | – | 16.6 | -18.0 | 22.4 | -18.0 (2022) |
| RPAR actual | Jan 2020– | 3.56% | -28.6% | 13.4% | – | 19.4 | -22.8 | 17.9 | -22.8 (2022) |

— own calc; script `gapfill2_data/aw_gem.py`, results `gapfill2_data/allweather_results.csv`. ETF-era start is set by BIL (May 2007) and DBC (Feb 2006).

**Core-satellite (practitioner statements)**
- Morningstar Australia (Simonelle Mody, Jul 22, 2026): "conventional wisdom keeps satellites in the 5-20% range"; the structure gives "a controlled way to express a view without letting that view dominate the entire portfolio"; the model "is in no way a guarantee of outperformance"; cautions on overconfidence, boundary discipline and abandoning the sleeve after poor results — [Morningstar AU](https://www.morningstar.com.au/personal-finance/young-invested-can-this-investing-strategy-help-you-beat-market)
- Vanguard Australia's adviser survey (2026) found "average indexed exposure around 50%" in adviser core-satellite construction (a description of practice, not a recommendation) — [Financial Standard](https://www.financialstandard.com.au/news/core-satellite-models-can-only-be-effective-with-purpose-vanguard-179812344); Vanguard Canada frames active-passive combinations around manager-selection skill, without a percentage — [Vanguard Canada](https://www.vanguard.ca/en/investor/learn/featured-group/strategies/active-passive-combinations) (page fetch returned 503; description from search snippet)
- Other retail guidance: core 60–80% / satellites the remainder — [interactive investor](https://ii.co.uk/analysis-commentary/core-and-satellite-funds-ps100k-isa-portfolio-ii530728); Alpha Architect uses an 80/20 example — [Alpha Architect](https://alphaarchitect.com/how-to-use-active-etfs-in-a-diversified-portfolio/)
- Morningstar on tactical funds generally: "the average tactical asset-allocation fund has consistently underperformed more static asset-allocation funds" — [Morningstar, Why Tactical-Allocation Funds Failed—Again](https://www.morningstar.com/funds/why-tactical-allocation-funds-failedagain) (via search snippet)
- Wikipedia's entry defines the structure (passive index core plus alpha-seeking satellites) but states no percentages and carries a "needs more citations" banner — [Wikipedia](https://en.wikipedia.org/wiki/Core_%26_Satellite)

### Inferences
- For a 15+-year accumulator the defensive portfolios cost 3–4 pts/yr versus 100% equity over 2007–2026 (6.4–7.4% vs 10.6%) in exchange for halving the worst drawdown (-16% to -21% vs -51%). That is a reasonable *retirement-phase* trade, not an accumulation-phase one; the live RPAR record (3.4%/yr vs 14.6% for VTI over the same seven years) shows the cost can be far larger than the long-run average when rates rise from zero.
- 2022 exposed the shared failure mode: every bond-heavy design had its worst year since inception in 2022 (-13% to -23%), so "all-weather" did not protect against the one shock a Canadian equity investor most needs protection from (inflation plus rising rates). Gold and short bills were the only sleeves that helped (Permanent Portfolio -13.0% vs All Weather -18.9%).
- Core-satellite for this investor: a 5–10% satellite (e.g. AVUV or a gold sleeve) is within every practitioner range found and small enough that a 50% loss in the satellite costs 2.5–5% of the portfolio; the evidence does not support satellites above 20%.

### Gaps
- Bogleheads wiki (Core and satellite, Three-fund) is behind a Cloudflare challenge (HTTP 402 / "Just a moment"); its text could not be read. No PWL Capital document stating a satellite cap was found. Morningstar Canada's core/satellite articles redirect to the new global site.
- Curvo and Portfolio Visualizer pages were not fetched (not attempted after PV's round-1 block); lazyportfolioetf (aggregator) and PortfolioCharts supply the long-horizon numbers, which pre-ETF rely on simulated asset-class series.
- No published Bridgewater All Weather fund track record (the fund is private); RPAR is the only live risk-parity ETF record used.
- Calendar 2008 for the defensive portfolios comes only from my replication (ETF proxies), not an index-provider source.

---

## Q4. Trend overlay (10-month SMA / 200-day) and GEM on the actual candidates, including April 2025

### Takeaway
On dividend-adjusted monthly data to Oct 2026, a month-end 10-month SMA rule with 0.1% per switch cut the max drawdown of SPY/VTI from -50.8% to -18% to -26% and of VT/ACWI from -44% to -52% to -19% to -21%, but cost 1.4–3.2 pts/yr of CAGR (SPY 8.0–8.9% vs 11.0%; VT 7.2–8.1% vs 8.7%) with 27–33 switches in ~20 years; on XEQT/VEQT (2019–2026) it cost 2.1–3.3 pts/yr for a 2–8 pt drawdown improvement. In the April 2025 tariff crash the monthly rule did exactly what its critics predict: SPY and VT closed March 2025 below their SMA, the rule sat out April (roughly flat) and missed May's +6% rebound, re-entering in June; XEQT exited a month later still (end-April, after the trough) and missed May entirely. The daily 200-day rule whipsawed 4 times on SPY and 6 times on VT between March 10 and May 12, 2025. GEM (12-month dual momentum) held SPY through the crash, then rotated SPY→VEU→SPY→VEU→SPY between May and October 2025 (four switches, 13.1% for the year vs 17.7% for SPY), and from Dec 2014 to Oct 2026 compounded at 7.3%/yr vs 13.4% for SPY and 8.8% for 60/40 with a -21.7% max drawdown (vs -23.9% / -20.0%). For a DCA investor the overlay is a **report flag, not a trade rule**.

### Cited Findings

**Table 4a. Own replication: month-end 10-month SMA and 12-month absolute momentum (decide at month-end close, hold next month, 0.1% cost per switch; "BIL" = T-bill ETF, "CASH0" = 0%; yfinance adjusted closes to Oct 2026)**

| Equity sleeve | Rule → defensive | Start | CAGR | Max DD | Vol | Switches | Months out | CY2020 | CY2022 | CY2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | buy & hold | 2006-02 | 10.96% | -50.8% | 15.0% | – | – | 18.3 | -18.2 | 17.7 |
| SPY | SMA10 → CASH0 | 2006-02 | 7.73% | -23.4% | 10.5% | 33 | 58 | 14.3 | -21.3 | 11.5 |
| SPY | SMA10 → BIL | 2006-02 | 8.00% | -22.4% | 10.5% | 33 | 58 | 14.5 | -20.5 | 12.3 |
| SPY | SMA10 → AGG | 2006-02 | 8.93% | -25.9% | 10.8% | 33 | 58 | 16.4 | -25.9 | 11.3 |
| SPY | ABSMOM12 → BIL | 2007-02 | 9.25% | -19.6% | 12.0% | 14 | 42 | 0.0 | -11.7 | 17.7 |
| SPY | ABSMOM12 → AGG | 2007-02 | 9.58% | -19.7% | 12.3% | 14 | 42 | 2.4 | -17.0 | 17.7 |
| VTI | buy & hold | 2006-02 | 10.84% | -50.8% | 15.5% | – | – | 21.1 | -19.5 | 17.1 |
| VTI | SMA10 → BIL | 2006-02 | 8.66% | -17.6% | 10.5% | 31 | 60 | 17.9 | -13.0 | 11.6 |
| VTI | SMA10 → AGG | 2006-02 | 9.46% | -22.1% | 10.9% | 31 | 60 | 19.9 | -22.1 | 10.6 |
| VTI | ABSMOM12 → AGG | 2007-02 | 9.15% | -22.6% | 12.8% | 16 | 46 | 3.8 | -17.5 | 17.1 |
| VT | buy & hold | 2008-07 | 8.68% | -44.5% | 16.6% | – | – | 16.6 | -18.0 | 22.4 |
| VT | SMA10 → BIL | 2008-07 | 7.24% | -20.6% | 10.6% | 27 | 53 | 14.3 | -8.1 | 15.7 |
| VT | SMA10 → AGG | 2008-07 | 8.11% | -18.7% | 11.1% | 27 | 53 | 17.0 | -18.5 | 14.6 |
| VT | ABSMOM12 → AGG | 2009-07 | 7.58% | -23.5% | 12.2% | 17 | 51 | 2.6 | -16.7 | 22.4 |
| ACWI | buy & hold | 2008-04 | 8.39% | -51.7% | 16.5% | – | – | 16.3 | -18.4 | 22.4 |
| ACWI | SMA10 → AGG | 2008-04 | 7.89% | -19.1% | 10.9% | 27 | 56 | 15.7 | -18.6 | 14.8 |
| XEQT.TO (CAD) | buy & hold | 2019-09 | 14.25% | -17.6% | 12.7% | – | – | 11.9 | -11.0 | 20.6 |
| XEQT.TO | SMA10 → CASH0 | 2019-09 | 11.94% | -9.6% | 8.9% | 7 | 20 | 17.8 | -9.6 | 14.1 |
| XEQT.TO | SMA10 → ZAG | 2019-09 | 12.14% | -15.4% | 9.7% | 7 | 20 | 24.3 | -15.4 | 14.0 |
| XEQT.TO | ABSMOM12 → ZAG | 2020-09 | 13.50% | -12.8% | 10.2% | 2 | 11 | n/a | -11.7 | 20.6 |
| VEQT.TO (CAD) | buy & hold | 2019-03 | 13.38% | -17.9% | 12.4% | – | – | 11.4 | -10.8 | 20.4 |
| VEQT.TO | SMA10 → CASH0 | 2019-03 | 10.04% | -9.1% | 9.0% | 9 | 24 | 8.4 | -9.1 | 14.1 |
| VEQT.TO | SMA10 → ZAG | 2019-03 | 11.14% | -14.9% | 9.8% | 9 | 24 | 12.6 | -14.9 | 14.0 |
| VEQT.TO | ABSMOM12 → ZAG | 2020-03 | 12.72% | -12.2% | 11.1% | 4 | 13 | n/a | -11.1 | 20.4 |
| XAW.TO (CAD) | buy & hold | 2015-03 | 11.06% | -18.5% | 11.8% | – | – | 12.4 | -11.8 | 15.9 |
| XAW.TO | SMA10 → ZAG | 2015-03 | 8.81% | -16.2% | 9.4% | 15 | 32 | 11.7 | -16.2 | 9.9 |

— own calc; `gapfill2_data/overlay_bt.py`, `overlay_results.csv`, price file `monthly_adj_close_yfinance_2026-11-02.csv`. XEQT's 2020 figure for SMA rules covers only roughly Jun–Dec 2020 (the rule needs 10 months of history plus one month lag; the fund began Aug 2019), so the "17.8 / 24.3 vs 11.9" comparison is not like-for-like.

**Episode detail (month-end close vs 10-month SMA; "out" = holds the defensive asset the following month)**
- *April 2025 tariff crash* (SPY peak Feb 19 → trough Apr 8, 2025: -18.8% on closes; VT -16.5%): SPY closed Mar 31, 2025 at 550.26 vs SMA 561.99 → out for April; Apr 30 close 545.49 vs 563.51 → out for May; May 30 close 579.77 vs 567.81 → back in for June. April's month-to-month move was about -0.9% (545.49/550.26) and May's +6.3% (579.77/545.49), so the rule avoided nothing and forfeited the rebound; CY2025: SMA→BIL 12.3% vs buy-and-hold 17.7%. VT: identical pattern (out for April and May, in for June). XEQT (CAD): closed Mar 31 above its SMA (32.76 vs 31.99) and only fell below at Apr 30 (31.94 vs 32.25) → out for May (+5.4%) and back in June: a pure whipsaw after the trough; CY2025 14.1% vs 20.6% — own calc.
- *Daily 200-day rule, 2025*: SPY crossed below on Mar 10, above Mar 24, below Mar 26, above May 12 (4 crossings); VT crossed Mar 10 (below), Mar 14 (above), Mar 28 (below), Apr 2 (above), Apr 3 (below), May 1 (above) — 6 crossings in seven weeks — own calc on daily adjusted closes.
- *2020*: SPY closed Feb 28 below (269.38 vs 272.38) → out for March (avoided -12.5%), April (missed +12.7%) and May (missed +4.8%), back in June; net CY2020 14.5% (→BIL) vs 18.3%. VT stayed out one month longer (back in July). XEQT's SMA was undefined until May 2020 — own calc.
- *2022*: SPY: out after Feb, in after Mar (whipsaw), out after Apr through Oct, in after Nov, out after Dec, in after Jan 2023 → three round trips; with AGG as the defensive asset the SMA rule lost -25.9% vs -18.2% for buy-and-hold because AGG fell -13.06% (iShares) while the rule was "defensive"; with BIL it lost -20.5%. VT and XEQT exited after Jan 2022 and stayed out until Nov 2022 (one whipsaw in Nov–Dec), losing -8.1% (VT→BIL) / -9.6% (XEQT→cash) vs -18.0% / -11.0% — own calc.
- Published daily replication (round 1, not repeated): 48 switches 1987–2026, 2022 -26.6% with bonds as defensive — [algostrategylab](https://algostrategylab.github.io/sma-trend-filter/); the monthly Shiller replication's 2022 -5.2% used cash — [sp500-trend-filter-backtest](https://github.com/lotushansstudio-maker/sp500-trend-filter-backtest). My SPY→AGG (-25.9%) and →BIL (-20.5%) results bracket the two and confirm the defensive-asset choice explains most of the gap.

**GEM (Antonacci dual momentum) replication, SPY / VEU / AGG, 12-month lookback vs BIL, monthly, 0.1% per switch — own calc**

| Window | GEM CAGR | GEM max DD | Switches | SPY CAGR / DD | 60/40 SPY-AGG CAGR / DD |
|---|---|---|---|---|---|
| Apr 2008–Oct 2026 | 8.25% | -21.7% | 31 | 11.85% / -46.3% | 8.39% / -29.7% |
| Dec 2014–Oct 2026 (post-book) | 7.25% | -21.7% | 23 | 13.35% / -23.9% | 8.78% / -20.0% |

- GEM calendar returns (own calc): 2015 -6.8, 2016 6.7, 2017 20.8, 2018 -8.1, 2019 18.4, 2020 2.4, 2021 25.1, 2022 -17.0, 2023 6.5, 2024 24.9, 2025 13.1, 2026 YTD (Oct) 10.5.
- GEM positions: held SPY Dec 2024–Apr 2025 (through the crash), VEU May–Jul 2025, SPY Aug, VEU Sep, SPY Oct 2025; held SPY through the Feb–Mar 2020 crash, AGG for Apr–May 2020 (missing the rebound), SPY from June; SPY Jan–May 2022, AGG Jun 2022–Feb 2023 — own calc.
- Independent published results agree in direction: quant4free (Jul 31, 2026) out-of-sample since 2014 GEM 8.4%/-20% vs SPY 13.6%/-24% (round 1); Petit (SSRN 2026) GEM trailed the S&P 500 by ~4.8 pts/yr since 2010 (round 1). AllocateSmartly lists "Antonacci's Global Equities Momentum" in its strategy tables (20-year Keller ratio 7.07% aggressive) but has no public GEM page; its monthly member reports were not accessible — [AllocateSmartly Keller ratio article](https://allocatesmartly.com/the-keller-ratio-measuring-return-relative-to-drawdown/); [AllocateSmartly list of strategies](https://allocatesmartly.com/list-of-strategies/). Antonacci's own site returned HTTP 403.
- Contemporary accounts of the April 2025 signal: SPY "slipped below" its 200-day on March 10, 2025 — [Benzinga](https://www.benzinga.com/general/market-summary/25/03/44508042/sp-500-nasdaq-100-trackers-spy-and-qqq-below-200-day-average-as-tariff-concerns-continue-to-trouble-markets); S&P Global noted the break below the 200-day SMA and a "death cross" during the tariff selloff — [S&P Global Market Intelligence](https://spglobal.com/market-intelligence/en/news-insights/research/visualizing-market-reactions-to-us-tariff-policy); SentimenTrader on the May 2025 reclaim of the 200-day — [Yahoo Finance](https://finance.yahoo.com/news/the-sp-500-just-reclaimed-its-200-day-moving-average--but-history-says-it-may-not-be-a-good-thing-164718289.html); none published a rule-level P&L.

### Inferences
- **Verdict: report flag, not trade rule.** Over the actual candidates the monthly SMA rule gives up 1.4–3.3 pts/yr and still carries -18% to -26% drawdowns with bonds as the defensive asset; its two best episodes (2008, 2022 with cash) are offset by 2020 and 2025, where a V-shaped crash inside one or two months made the rule exit at or after the bottom. A DCA investor's monthly contribution already buys more units after a fall; adding a rule that sells after the fall works against that mechanism.
- The absolute-momentum gate (12-month) switches far less (14–17 times in ~19 years vs 27–33) and preserved more return (SPY 9.3–9.6% vs 8.0–8.9% for SMA), consistent with round 1's "prefer the gate over the relative leg"; GEM's relative leg added four switches in 2025 alone and cost ~4.6 pts versus SPY that year.
- If the toolkit shows these signals, show them as *context* with the rule's own 2020/2022/2025 record next to them (e.g. "SPY below 10-month SMA at month-end; the last three such signals in 2020, 2022 and 2025 netted +X/-X/-X vs holding"), so the human sees the base rate before acting.
- Defensive-asset choice matters more than the lookback: in 2022 cash beat aggregate bonds by 5–10 pts inside the overlay; for a Canadian, ZAG's -11.8% (2022) means an "XEQT→ZAG" switch would have deepened, not cushioned, that year's loss (-15.4% vs -11.0% buy-and-hold).

### Gaps
- No third-party (testfol.io, Portfolio Visualizer, Curvo, AllocateSmartly) rule-level result for April 2025 was found; the April 2025 figures above are my replication only. The method (month-end adjusted close vs 10-month SMA of month-end closes, trade at that close) is Faber's stated rule, but it ignores bid-ask spread and uses yfinance's dividend adjustment, which is unaudited.
- Monthly series from yfinance use month-start labels for month-end closes; one-day timing slippage at month ends is not modelled.
- GEM live (as opposed to replicated) results 2014–2026 from an independent tracker remain unavailable; AllocateSmartly's member-only pages and Antonacci's site were blocked.
- Switch cost of 0.1% is an assumption; for a Canadian trading XEQT/ZAG at Questrade/Wealthsimple the round-trip cost is near zero in commissions but 2–5 bps in spread.

---

## Q5. 10-year expected real returns per asset class (Vanguard VCMM, AQR, Research Affiliates, J.P. Morgan)

### Takeaway
On a real basis the four houses span roughly 1–4% for US large caps (RA 0.8%, Vanguard ~3.5% midpoint less inflation, AQR 3.9%, JPM ~4.3%), 4–5.3% for developed ex-US (AQR 5.3%, JPM ~5.0%, Vanguard ~4%), 1.3–5.1% for EM (Vanguard lowest, RA/JPM ~5%), and ~2–3% for aggregate bonds. Only AQR and RA publish real figures natively; Vanguard and JPM are nominal and are converted here with the inflation assumptions stated in the table, so those real figures are my arithmetic.

### Cited Findings

**Table 5. 10-year expected returns (annualized)**

| Asset class | Vanguard VCMM (run Sep 30, 2026; 10-yr nominal ranges, USD) | AQR 2026 CMA (as of Dec 31, 2025; 5–10-yr real, USD) | Research Affiliates (Morningstar 2026 compilation; 10-yr) | J.P. Morgan 2026 LTCMA (as of Sep 30, 2025; 10–15-yr nominal, USD) |
|---|---|---|---|---|
| US large cap / US equities | 4.8–6.8% nominal | 3.9% real | 0.8% real | 6.7% nominal (≈4.3% real at 2.4% inflation, own arithmetic) |
| Developed ex-US equities | 5.3–7.3% nominal | 5.3% real (cap-weighted Euro-5, Japan, UK, Australia, Canada) | 7.7% nominal (secondary) | EAFE 7.4% nominal (JPM Private Bank page); 7.5% in Morningstar compilation |
| Emerging-market equities | 3.7–5.7% nominal | not extracted | 5.1% real (secondary) | 7.7–7.8% nominal |
| Global / AC World equities | – | global 60/40 3.4% real | – | AC World 6.7% nominal (Private Bank page) vs "global equities 7.0%" (press release) — conflict |
| US aggregate bonds | 5.1–6.1% nominal | not extracted | 4.7% nominal (≈2.3% real, secondary) | intermediate Treasuries 4.0%, long Treasuries 4.9%, IG credit 5.2%, HY 6.1% nominal |
| Global ex-US bonds (hedged) | 5.2–6.2% nominal | – | – | – |
| US high yield | 5.4–6.4% nominal | – | – | 6.1% |
| 60/40 | – | 3.4% real (global) | – | 6.4% nominal (USD global 60/40) |
| Inflation assumption | not on page (CPI is the index; no forecast printed) | n/a (real) | n/a (real) | 2.4% US inflation (matrix row; column mapping uncertain, see gap) |
| Primary URL | [Vanguard VCMM return forecasts (Oct 21, 2026 page)](https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html) | [AQR 2026 CMAs](https://www.aqr.com/insights/research/alternative-thinking/2026-capital-market-assumptions-for-major-asset-classes); PDF via `?aqrPDF=1` (Exhibit 1 is an image) | [RA Asset Allocation Interactive](https://interactive.researchaffiliates.com/asset-allocation) (redirects to interactive.syzygyassetmanagement.com; membership required; no data extracted) | [JPM 2026 LTCMA press release](https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2026-long-term-capital-market-assumptions/); [JPM Private Bank, 2026 LTCMAs in focus (Oct 24, 2025)](https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/tmt/30-years-of-foresight-the-2026-ltcmas-in-focus); [USD assumption matrix PDF](https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/ltcma-2026-us-matrix_usd.pdf) (404 on fetch; row quoted via search index) |

- AQR's US 3.9% / non-US developed 5.3% / Eurozone 5.0% / UK 4.9% / Japan 4.9% real figures are taken from a blog that reproduces AQR's Exhibit 1 (Jan 31, 2026; updated May 4, 2026); AQR's page itself prints only the 3.4% global 60/40 figure in text — [philippdubach.com](https://philippdubach.com/posts/buying-the-haystack-might-not-work-this-year/); [AQR](https://www.aqr.com/insights/research/alternative-thinking/2026-capital-market-assumptions-for-major-asset-classes). AQR states the US CAPE sits at the "96th percentile since 1980" and that there is a ~50% chance realized returns miss by more than 3 pts/yr (same blog).
- Research Affiliates' figures (0.8% real US stocks, 5.1% real EM, 4.7% nominal US aggregate, 7.7% nominal developed ex-US) are from Wealthtender's reading of Morningstar's "Experts Forecast Stock and Bond Returns: 2026 Edition"; Morningstar's own page returns HTTP 403 — [Wealthtender](https://wealthtender.com/insights/analysis-of-2026-expert-market-predictions/); [Morningstar 2026 edition](https://www.morningstar.com/markets/experts-forecast-stock-bond-returns-2026-edition). Wealthtender's trimmed-average real 10-year expectations across firms: US stocks 2.9% (chart) / 2.6% (text), developed ex-US 4.5%, EM 4.3%, US bonds 2.1–2.2%, using 2.32% breakeven inflation.
- JPM has since published the 2027 edition (data as of September 2026): US large cap "up 80bps, to 7.5%", balanced global stock-bond portfolio "rises 60bps, to 7.0%", global aggregate bonds 5.3% — [JPM LTCMA page](https://am.jpmorgan.com/us/en/asset-management/adv/insights/portfolio-insights/ltcma/). The 2026 edition therefore implies 6.7% / 6.4%, consistent with the 2026 press release.
- Vanguard's page also lists EM sovereign bonds (hedged) 6.4–7.4% — [Vanguard VCMM](https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html).

### Inferences
- Taking each house's central figure, the forward real equity premium over bonds is only ~1–2 pts (Vanguard: equities 5.8% vs bonds 5.6% nominal midpoints; AQR: 3.9% real US stocks vs ~1.5–2% real bonds implied by RA/JPM). That is the strongest quantitative argument in this file for holding ex-US and EM at market weight or above (every house puts developed ex-US 1–2 pts above US) and for not expecting the 14.7%/yr of the last decade (Table 1a) to repeat.
- The dispersion across houses (US real 0.8–4.3%) is itself the finding: a 15-year plan should be stress-tested at ~1% real equity returns, where a C$1,000/month contributor accumulates roughly 15% less than at 3% real.

### Gaps
- Vanguard's VCMM page gives no inflation forecast, so its ranges are left nominal; AQR's and JPM's full asset-class tables (bonds, cash, EM for AQR; the inflation row for JPM) were not extractable from primary pages (AQR Exhibit 1 is an image in the PDF; JPM's matrix PDF returned 404 to the fetch tool and a 7-byte stub to curl). The JPM 2.4% inflation figure rests on a search-engine rendering of that matrix whose column order is ambiguous (2.50 / 2.52 / 1.77 / 2.40 / 1.00).
- Research Affiliates' Asset Allocation Interactive now redirects to a Syzygy Asset Management domain and requires membership; all RA numbers are second-hand (Morningstar via Wealthtender) and undated beyond "2026 edition".
- The JPM EAFE figure differs between its Private Bank page (7.4%) and the Morningstar compilation (7.5%), and AC World differs between the Private Bank page (6.7%) and the press release (7.0% "global equities"); the primary matrix would settle this.
