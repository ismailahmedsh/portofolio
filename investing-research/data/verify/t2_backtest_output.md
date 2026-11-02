# Contribution backtest output (2026-11-02 21:19:36 UTC)

Monthly CAD 1,000 on first trading day of each month; yfinance Adj Close (pre-tax, no FWT, no commissions); FX = FRED DEXCAUS ffill.

| Portfolio | Start | End | Months | Contributed CAD | Ending CAD | Gain CAD | XIRR (MWR) | TWR CAGR | MaxDD (TWR index) | MaxDD (account value) | Final weights |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A: 100% XEQT.TO (CAD) | 2019-09-03 | 2026-11-02 | 87 | 87,000 | 153,112 | 66,112 | 15.60% | 14.27% | -29.7% | -24.8% | {'XEQT.TO': np.float64(1.0)} |
| B: DIY 45/30/10/15 (CAD), XEQT window | 2019-09-03 | 2026-11-02 | 87 | 87,000 | 152,062 | 65,062 | 15.41% | 13.79% | -28.9% | -24.1% | {'XUU.TO': np.float64(0.45), 'XEF.TO': np.float64(0.299), 'XEC.TO': np.float64(0.097), 'XIC.TO': np.float64(0.153)} |
| C: 100% VT (USD->CAD at FRED DEXCAUS), XEQT window | 2019-09-03 | 2026-11-02 | 87 | 87,000 | 151,088 | 64,088 | 15.23% | 14.07% | -27.8% | -23.1% | {'VT': np.float64(1.0)} |
| B2: DIY 45/30/10/15 (CAD), from XUU inception | 2015-03-02 | 2026-11-02 | 141 | 141,000 | 313,487 | 172,487 | 13.02% | 11.03% | -28.9% | -27.9% | {'XUU.TO': np.float64(0.451), 'XEF.TO': np.float64(0.297), 'XEC.TO': np.float64(0.098), 'XIC.TO': np.float64(0.155)} |
| C2: 100% VT (USD->CAD), from 2015-02 | 2015-03-02 | 2026-11-02 | 141 | 141,000 | 317,530 | 176,530 | 13.22% | 11.42% | -27.8% | -26.8% | {'VT': np.float64(1.0)} |
| D2: 100% XIC.TO (CAD), from 2015-02 (reference) | 2015-03-02 | 2026-11-02 | 141 | 141,000 | 330,927 | 189,927 | 13.87% | 10.63% | -37.2% | -36.3% | {'XIC.TO': np.float64(1.0)} |

Data starts (Adj Close first date): XEQT.TO 2019-08-14; XUU.TO 2015-02-20; XEF.TO 2013-04-15; XEC.TO 2013-04-15; XIC.TO 2005-01-04; VT 2008-06-26; FX DEXCAUS 1971-01-04..2026-10-23
