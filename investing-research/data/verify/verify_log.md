
## yfinance batched download (2026-11-02 21:07:32 UTC) yfinance=1.7.0
- call: yf.download(['XEQT.TO', 'XEF.TO', 'XIC.TO', 'VFV.TO', 'ZAG.TO', 'XUU.TO', 'VUN.TO', 'XEC.TO', 'VT', 'VTI', 'VXUS'], start=2005-01-01, auto_adjust=False, actions=True, group_by='ticker') elapsed 2.6s; shape=(5595, 96)
- XEQT.TO: rows=1812 first=2019-08-14 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- XEF.TO: rows=0 first=NaT last=NaT AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
- XIC.TO: rows=5481 first=2005-01-04 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- VFV.TO: rows=3508 first=2012-11-08 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- ZAG.TO: rows=4209 first=2010-01-25 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- XUU.TO: rows=2936 first=2015-02-20 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- VUN.TO: rows=3319 first=2013-08-12 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- XEC.TO: rows=3401 first=2013-04-15 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- VT: rows=4617 first=2008-06-26 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- VTI: rows=5493 first=2005-01-03 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
- VXUS: rows=3964 first=2011-01-28 last=2026-11-02 AdjClose=True cols=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']

## XEF.TO retry + info/funds_data (2026-11-02 21:07:54 UTC)
- XEF.TO single retry: rows=3401 first=2013-04-15 last=2026-11-02 cols=['Adj Close', 'Capital Gains', 'Close', 'Dividends', 'High', 'Low', 'Open', 'Stock Splits', 'Volume']
- Ticker('XEQT.TO').info: 92 keys; selected={"quoteType": "ETF", "longName": "iShares Core Equity ETF Portfolio", "currency": "CAD", "exchange": "TOR", "netExpenseRatio": 0.2, "totalAssets": 22910253056, "yield": 0.015800001, "dividendYield": 1.58, "fundInceptionDate": 1565136000, "navPrice": 44.62, "fundFamily": "BlackRock Asset Management Canada Ltd", "trailingAnnualDividendYield": 0.0, "ytdReturn": 15.54499, "threeYearAverageReturn": 0.2317234, "fiveYearAverageReturn": 0.1273794}
  - expense-like keys: ['netExpenseRatio', 'trailingPegRatio']
  - funds_data.description: str len=0: ''
  - funds_data.fund_overview: dict keys=['categoryName', 'family', 'legalType']
  - funds_data.fund_operations: DataFrame shape=(3, 2) cols=['XEQT.TO', 'Category Average'] idx=['Annual Report Expense Ratio', 'Annual Holdings Turnover', 'Total Net Assets']
  - funds_data.asset_classes: dict keys=['cashPosition', 'stockPosition', 'bondPosition', 'preferredPosition', 'convertiblePosition', 'otherPosition']
  - funds_data.top_holdings: DataFrame shape=(5, 2) cols=['Name', 'Holding Percent'] idx=['XTOT.TO', 'XIC.TO', 'XEF.TO', 'ITOT', 'XEC.TO']
  - funds_data.equity_holdings: DataFrame shape=(6, 2) cols=['XEQT.TO', 'Category Average'] idx=['Price/Earnings', 'Price/Book', 'Price/Sales', 'Price/Cashflow', 'Median Market Cap']
  - funds_data.bond_holdings: DataFrame shape=(3, 2) cols=['XEQT.TO', 'Category Average'] idx=['Duration', 'Maturity', 'Credit Quality']
  - funds_data.bond_ratings: dict keys=['bb', 'aa', 'aaa', 'a', 'other', 'b', 'bbb', 'below_b', 'us_government']
  - funds_data.sector_weightings: dict keys=['realestate', 'consumer_cyclical', 'basic_materials', 'consumer_defensive', 'technology', 'communication_services', 'financial_services', 'utilities', 'industrials', 'energy', 'healthcare']
  - fund_operations full: {'XEQT.TO': {'Annual Report Expense Ratio': 0.002, 'Annual Holdings Turnover': 0.136, 'Total Net Assets': 174598.9}, 'Category Average': {'Annual Report Expense Ratio': None, 'Annual Holdings Turnover': None, 'Total Net Assets': 174598.9}}
- Ticker('XEF.TO').info: 92 keys; selected={"quoteType": "ETF", "longName": "iShares Core MSCI EAFE IMI Index ETF", "currency": "CAD", "exchange": "TOR", "netExpenseRatio": 0.23, "totalAssets": 24329615360, "yield": 0.0231, "dividendYield": 2.31, "fundInceptionDate": 1365552000, "navPrice": 50.67, "fundFamily": "BlackRock Asset Management Canada Ltd", "ytdReturn": 14.49554, "threeYearAverageReturn": 0.19619079, "fiveYearAverageReturn": 0.1058731}
  - expense-like keys: ['netExpenseRatio', 'trailingPegRatio']
  - funds_data.description: str len=0: ''
  - funds_data.fund_overview: dict keys=['categoryName', 'family', 'legalType']
  - funds_data.fund_operations: DataFrame shape=(3, 2) cols=['XEF.TO', 'Category Average'] idx=['Annual Report Expense Ratio', 'Annual Holdings Turnover', 'Total Net Assets']
  - funds_data.asset_classes: dict keys=['cashPosition', 'stockPosition', 'bondPosition', 'preferredPosition', 'convertiblePosition', 'otherPosition']
  - funds_data.top_holdings: DataFrame shape=(10, 2) cols=['Name', 'Holding Percent'] idx=['ASML.AS', 'IEFA', 'HSBA.L', 'ROP.SW', 'SHEL.L']
  - funds_data.equity_holdings: DataFrame shape=(6, 2) cols=['XEF.TO', 'Category Average'] idx=['Price/Earnings', 'Price/Book', 'Price/Sales', 'Price/Cashflow', 'Median Market Cap']
  - funds_data.bond_holdings: DataFrame shape=(3, 2) cols=['XEF.TO', 'Category Average'] idx=['Duration', 'Maturity', 'Credit Quality']
  - funds_data.bond_ratings: dict keys=['bb', 'aa', 'aaa', 'a', 'other', 'b', 'bbb', 'below_b', 'us_government']
  - funds_data.sector_weightings: dict keys=['realestate', 'consumer_cyclical', 'basic_materials', 'consumer_defensive', 'technology', 'communication_services', 'financial_services', 'utilities', 'industrials', 'energy', 'healthcare']
  - fund_operations full: {'XEF.TO': {'Annual Report Expense Ratio': 0.0023, 'Annual Holdings Turnover': 0.3507, 'Total Net Assets': 70325.33}, 'Category Average': {'Annual Report Expense Ratio': None, 'Annual Holdings Turnover': None, 'Total Net Assets': 70325.33}}
- Ticker('VT').info: 98 keys; selected={"quoteType": "ETF", "longName": "Vanguard Total World Stock Index Fund ETF Shares", "currency": "USD", "exchange": "PCX", "netExpenseRatio": 0.06, "totalAssets": 101182521344, "yield": 0.0153, "dividendYield": 1.53, "fundInceptionDate": 1214265600, "navPrice": 155.16, "category": "Global Large-Stock Blend", "fundFamily": "Vanguard", "ytdReturn": 12.82577, "threeYearAverageReturn": 0.21995199, "fiveYearAverageReturn": 0.098834604}
  - expense-like keys: ['netExpenseRatio', 'trailingPegRatio']
  - funds_data.description: str len=316: 'The fund employs an indexing investment approach designed to track the performance of the FTSE Global All Cap Index. It '
  - funds_data.fund_overview: dict keys=['categoryName', 'family', 'legalType']
  - funds_data.fund_operations: DataFrame shape=(3, 2) cols=['VT', 'Category Average'] idx=['Annual Report Expense Ratio', 'Annual Holdings Turnover', 'Total Net Assets']
  - funds_data.asset_classes: dict keys=['cashPosition', 'stockPosition', 'bondPosition', 'preferredPosition', 'convertiblePosition', 'otherPosition']
  - funds_data.top_holdings: DataFrame shape=(10, 2) cols=['Name', 'Holding Percent'] idx=['NVDA', 'AAPL', 'MSFT', 'AMZN', 'GOOGL']
  - funds_data.equity_holdings: DataFrame shape=(6, 2) cols=['VT', 'Category Average'] idx=['Price/Earnings', 'Price/Book', 'Price/Sales', 'Price/Cashflow', 'Median Market Cap']
  - funds_data.bond_holdings: DataFrame shape=(3, 2) cols=['VT', 'Category Average'] idx=['Duration', 'Maturity', 'Credit Quality']
  - funds_data.bond_ratings: dict keys=['us_government']
  - funds_data.sector_weightings: dict keys=['realestate', 'consumer_cyclical', 'basic_materials', 'consumer_defensive', 'technology', 'communication_services', 'financial_services', 'utilities', 'industrials', 'energy', 'healthcare']
  - fund_operations full: {'VT': {'Annual Report Expense Ratio': 0.00059999997, 'Annual Holdings Turnover': 0.03, 'Total Net Assets': 179987.1}, 'Category Average': {'Annual Report Expense Ratio': 0.0093474, 'Annual Holdings Turnover': 0.4889, 'Total Net Assets': 179987.1}}

## Keyless endpoints (2026-11-02 21:08:20 UTC)
- BoC Valet FXUSDCAD json: HTTP 200 rc=0 bytes=299717 lines=14733 type=[JSON text data] url=https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?start_date=2010-01-01
  - head: {|    "terms": {|        "url": "https://www.bankofcanada.ca/terms/"|    },|    "seriesDetail": {|        "FXUSDCAD": {|            "label": "USD/CAD",|            "description": "Daily average exchange rate of the US dollar in Canadian dollars.",|            "dimension": {|                "key": "d
- BoC Valet FXUSDCAD csv: HTTP 200 rc=0 bytes=56650 lines=2461 type=[Unicode text, UTF-8 (with BOM) text, with CRLF line terminat] url=https://www.bankofcanada.ca/valet/observations/FXUSDCAD/csv?start_date=2010-01-01
  - head: ﻿"TERMS AND CONDITIONS"|"https://www.bankofcanada.ca/terms/"||"SERIES"|"id","label","description","date_format"|"FXUSDCAD","USD/CAD","Daily average exchange rate of the US dollar in Canadian dollars.","daily"||"OBSERVATIONS"|"date","FXUSDCAD"|"2017-01-03","1.3435"|"2017-01-04","1.3315"|
- BoC Valet group FX_RATES_DAILY json (recent_weeks=1): HTTP 200 rc=0 bytes=21913 lines=743 type=[JSON text data] url=https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/json?recent_weeks=1
  - head: {|    "terms": {|        "url": "https://www.bankofcanada.ca/terms/"|    },|    "groupDetail": {|        "label": "Daily exchange rates",|        "description": "Daily average exchange rates for various foreign currencies currently or historically published by the Bank of Canada, representing the va
- FRED fredgraph T10Y2Y: HTTP curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)
000 rc=92 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y
  - head: 
- FRED fredgraph DGS10: HTTP curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)
000 rc=92 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
  - head: 
- FRED fredgraph SAHMREALTIME: HTTP curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)
000 rc=92 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://fred.stlouisfed.org/graph/fredgraph.csv?id=SAHMREALTIME
  - head: 
- FRED fredgraph multi (DGS10,DGS2,UNRATE): HTTP curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)
000 rc=92 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10,DGS2,UNRATE
  - head: 
- FRED fredgraph DEXCAUS (USD/CAD): HTTP curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)
000 rc=92 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXCAUS
  - head: 
- Stooq XEQT.TO (symbol xeqt.ca?) daily: HTTP curl: (35) Recv failure: Connection reset by peer
000 rc=35 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://stooq.com/q/d/l/?s=xeqt.ca&i=d
  - head: 
- Stooq XEQT.TO literal: HTTP curl: (35) Recv failure: Connection reset by peer
000 rc=35 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://stooq.com/q/d/l/?s=xeqt.to&i=d
  - head: 
- Stooq SPY.US daily: HTTP curl: (35) Recv failure: Connection reset by peer
000 rc=35 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://stooq.com/q/d/l/?s=spy.us&i=d
  - head: 
- Stooq VT.US daily: HTTP curl: (35) Recv failure: Connection reset by peer
000 rc=35 bytes=0 lines=0 type=[cannot open `/home/user/portofolio/investing-research/data/v] url=https://stooq.com/q/d/l/?s=vt.us&i=d
  - head: 

## FRED retry over HTTP/1.1 + Stooq retry (2026-11-02 21:09:26 UTC)
- FRED T10Y2Y --http1.1: HTTP curl: (52) Empty reply from server
000 bytes= lines= head=[] tail=[]
- FRED DGS10 --http1.1: HTTP curl: (52) Empty reply from server
000 bytes= lines= head=[] tail=[]
- FRED SAHMREALTIME --http1.1: HTTP curl: (52) Empty reply from server
000 bytes= lines= head=[] tail=[]
- FRED DEXCAUS --http1.1: HTTP curl: (52) Empty reply from server
000 bytes= lines= head=[] tail=[]
- FRED DGS10,DGS2,UNRATE --http1.1: HTTP curl: (52) Empty reply from server
000 bytes= lines= head=[] tail=[]
- Stooq spy.us --http1.1 retry: HTTP curl: (35) Recv failure: Connection reset by peer
000 bytes=
- Stooq xeqt.ca --http1.1 retry: HTTP curl: (35) Recv failure: Connection reset by peer
000 bytes=
- FRED api.stlouisfed.org without api_key: HTTP 400 body={"error_code":400,"error_message":"Bad Request.  Variable api_key is not set.  Read https:\/\/fred.stlouisfed.org\/docs\/api\/api_key.html for more information."}

## GitHub repo metadata via gh api search (2026-11-02 21:13:07 UTC)
| repo | stars | pushed_at | open_issues | license | created | archived |
|---|---|---|---|---|---|---|
| TauricResearch/TradingAgents | 119927 | 2026-10-27T08:43:04Z | 110 | Apache-2.0 | 2024-12-28 | false |
| virattt/ai-hedge-fund | 64442 | 2026-11-02T19:25:36Z | 187 | MIT | 2024-11-29 | false |
| HKUDS/Vibe-Trading | 37469 | 2026-11-02T18:53:08Z | 28 | MIT | 2026-04-01 | false |
| OpenByteInc/QuantDinger | 13445 | 2026-11-02T18:17:50Z | 36 | Apache-2.0 | 2025-12-28 | false |
| ginlix-ai/LangAlpha | 2238 | 2026-11-02T20:32:22Z | 38 | Apache-2.0 | 2026-01-18 | false |
| JerBouma/FinanceDatabase | 9577 | 2026-11-01T12:06:46Z | 3 | MIT | 2021-01-28 | false |
| JerBouma/FinanceToolkit | 5489 | 2026-11-01T15:13:45Z | 2 | MIT | 2019-04-08 | false |
| QuantConnect/Lean | 22350 | 2026-11-02T15:27:34Z | 284 | Apache-2.0 | 2014-11-28 | false |
| nautechsystems/nautilus_trader | 31169 | 2026-11-02T14:15:13Z | 141 | LGPL-3.0 | 2018-06-25 | false |
| polakowo/vectorbt | 9646 | 2026-10-28T19:18:42Z | 135 | NOASSERTION | 2017-11-14 | false |
| skfolio/skfolio | 2579 | 2026-10-29T18:45:08Z | 37 | BSD-3-Clause | 2023-12-14 | false |
| ranaroussi/yfinance | 25798 | 2026-11-02T14:01:33Z | 114 | Apache-2.0 | 2017-05-21 | false |
| anthropics/financial-services | 40996 | 2026-10-28T17:23:24Z | 235 | Apache-2.0 | 2026-02-23 | false |
| AI4Finance-Foundation/FinRobot | 8358 | 2026-10-24T13:58:26Z | 79 | Apache-2.0 | 2024-02-27 | false |
| AI4Finance-Foundation/FinGPT | 21514 | 2026-10-25T13:49:15Z | 53 | MIT | 2023-02-11 | false |
| microsoft/qlib | 49941 | 2026-10-30T05:12:38Z | 512 | MIT | 2020-08-14 | false |
| Jakeschincariol/day-trader-skill | 4554 | 2026-10-20T14:18:00Z | 46 | MIT | 2026-10-20 | false |
| quant-sentiment-ai/claude-equity-research | 752 | 2026-11-02T12:32:26Z | 0 | MIT | 2025-09-09 | false |
| pmorissette/bt | 3015 | 2026-11-01T23:01:28Z | 15 | MIT | 2014-06-19 | false |
| AI4Finance-Foundation/FinRL | 16962 | 2026-10-25T13:49:47Z | 312 | MIT | 2020-07-26 | false |
| ranaroussi/quantstats | 7780 | 2026-11-02T14:00:34Z | 32 | Apache-2.0 | 2019-05-01 | false |
{"message":"Validation Failed","errors":[{"message":"The listed users and repositories cannot be searched either because the resources do not exist or you do not have permission to view them.","resource":"Search","field":"q","code":"invalid"}],"documentation_url":"https://docs.github.com/v3/search/","status":"422"}gh: Validation Failed (HTTP 422)
| dcajasn/Riskfolio-Lib | 4583 | 2026-10-30T16:05:31Z | 11 | BSD-3-Clause | 2020-03-02 | false |
## pip install vectorbt bt (2026-11-02 21:13:54 UTC)
Name: vectorbt
Version: 1.2.0
License: 
Location: /usr/local/lib/python3.13/site-packages
Name: bt
Version: 1.4.1
License: MIT
Location: /usr/local/lib/python3.13/site-packages
FRED T10Y2Y via WebFetch rows 13154 first ['1976-06-01', np.float64(0.68)] last ['2026-10-30', np.float64(0.38)] cols ['observation_date', 'T10Y2Y']
--- vectorbt cash_deposits grep:
(count in base.py: 0)
257:...     init_cash='autoalign', fees=0.001, slippage=0.001)
348:...     init_cash='autoalign', fees=0.001, slippage=0.001,
428:...     init_cash='autoalign', fees=0.001, slippage=0.001, log=True)
534:...     init_cash='autoalign', fees=0.001, slippage=0.001, freq='d')
568:...     init_cash=pf_baseline.init_cash
584:The only drawback of this approach is that you cannot use `init_cash='auto'` or `init_cash='autoalign'`
595:...     init_cash='autoalign', fees=0.001, slippage=0.001, freq='d')
1515:        init_cash (InitCashMode, float or array_like of float): Initial capital.
1542:        init_cash: tp.ArrayLike,
1555:            init_cash=init_cash,
1581:        self._init_cash = init_cash
1603:        if isinstance(self._init_cash, int):
--- bt cash flow grep:
/usr/local/lib/python3.13/site-packages/bt/algos.py:1722:class CapitalFlow(Algo):
/usr/local/lib/python3.13/site-packages/bt/algos.py:1742:    def __init__(self, amount):
/usr/local/lib/python3.13/site-packages/bt/algos.py:2603:    ``additional_data`` argument on :class:`Backtest <bt.backtest.Backtest>` must
/usr/local/lib/python3.13/site-packages/bt/algos.py:2613:          The name must coincide with the keys of the dictionary passed to additional_data as the
/usr/local/lib/python3.13/site-packages/bt/core.py:321:    def adjust(self, amount, update=True, flow=True):
/usr/local/lib/python3.13/site-packages/bt/core.py:513:    def flows(self):
/usr/local/lib/python3.13/site-packages/bt/core.py:928:    def adjust(self, amount, update=True, flow=True, fee=0.0):
/usr/local/lib/python3.13/site-packages/bt/backtest.py:92:    additional_data: dict[str, object] = backtest.additional_data
/usr/local/lib/python3.13/site-packages/bt/backtest.py:106:            additional_data=deepcopy(additional_data),
/usr/local/lib/python3.13/site-packages/bt/backtest.py:159:        * additional_data (dict): Additional kwargs passed to StrategyBase.setup, after preprocessing
/usr/local/lib/python3.13/site-packages/bt/backtest.py:192:        * additional_data (dict): Additional data passed at construction
/usr/local/lib/python3.13/site-packages/bt/backtest.py:205:        additional_data=None,
/usr/local/lib/python3.13/site-packages/bt/backtest.py:222:        self._process_data(data, additional_data)
/usr/local/lib/python3.13/site-packages/bt/backtest.py:377:    def _process_data(self, data, additional_data):
/usr/local/lib/python3.13/site-packages/bt/backtest.py:399:        self.additional_data = (additional_data or {}).copy()
/usr/local/lib/python3.13/site-packages/bt/backtest.py:403:        for k in self.additional_data:
/usr/local/lib/python3.13/site-packages/bt/backtest.py:404:            old = self.additional_data[k]
/usr/local/lib/python3.13/site-packages/bt/backtest.py:406:                self.additional_data[k] = self._prepend_missing_row(old)
/usr/local/lib/python3.13/site-packages/bt/backtest.py:419:        self.strategy.setup(self.data, **self.additional_data)
--- bt.algos.CapitalFlow docstring:
Used to model capital flows. Flows can either be inflows or outflows.

This Algo can be used to model capital flows. For example, a pension
fund might have inflows every month or year due to contributions. This
Algo will affect the capital of the target node without affecting returns
for the node.

Since this is modeled as an adjustment, the capital will remain in the
strategy until a re-allocation/rebalancement is made.

The amount must be finite. Nonfinite amounts raise ValueError when the
Algo runs, before the target's accounting state changes.

Args:
    * amount (float): Amount of adjustment
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "/usr/local/lib/python3.13/inspect.py", line 1274, in getsource
    lines, lnum = getsourcelines(object)
                  ~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1256, in getsourcelines
    lines, lnum = findsource(object)
                  ~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1071, in findsource
    file = getsourcefile(object)
  File "/usr/local/lib/python3.13/inspect.py", line 974, in getsourcefile
    filename = getfile(object)
  File "/usr/local/lib/python3.13/inspect.py", line 954, in getfile
    raise TypeError('module, class, method, function, traceback, frame, or '
                    'code object was expected, got {}'.format(
                    type(object).__name__))
TypeError: module, class, method, function, traceback, frame, or code object was expected, got cython_function_or_method
--- vectorbt from_orders cash_deposits doc snippet:
NOT IN from_orders doc
from_holding mentions cash_deposits: False
vectorbt 1.2.0

## TradingAgents raw source fetch (2026-11-02 21:16:18 UTC)
- tradingagents/portfolio.py: HTTP 200 bytes=3779 lines=81
- tradingagents/reporting.py: HTTP 200 bytes=6453 lines=136
- tradingagents/report_html.py: HTTP 200 bytes=14821 lines=305
- tradingagents/agents/managers/risk_manager.py: HTTP 404 bytes=14 lines=0
- tradingagents/agents/managers/research_manager.py: HTTP 200 bytes=3080 lines=74
- tradingagents/agents/risk_mgmt/aggresive_debator.py: HTTP 404 bytes=14 lines=0
- tradingagents/agents/risk_mgmt/conservative_debator.py: HTTP 200 bytes=4218 lines=70
- tradingagents/agents/risk_mgmt/neutral_debator.py: HTTP 200 bytes=4075 lines=68
- tradingagents/agents/trader/trader.py: HTTP 200 bytes=4336 lines=98
- tradingagents/backtest.py: HTTP 200 bytes=10152 lines=236
| PyPortfolio/PyPortfolioOpt | 6142 | 2026-07-07T21:18:14Z | 116 | MIT | 2018-05-29 | false |

## BlackRock CA XEQT product page + holdings CSV probe (2026-11-02 21:16:22 UTC)
- product page guess (309469): HTTP 404 bytes=57604
/ca/investors/en/products/309469/ishares-core-equity-etf-portfolio
<title>BlackRock
- product-list page: HTTP 200 bytes=170049
/ca/investors/en/products/309480/ishares-core-equity-etf-portfolio
/ca/investors/en/products/272102/ishares-core-msci-eafe-imi-index
/ca/investors/en/products/310468/ishares-core-msci-eafe-imi-index-etf

## BlackRock CA XEQT page 309480 + CSV (2026-11-02 21:17:39 UTC)
- product page 309480: HTTP 200 bytes=656775
/ca/investors/en/products/309480/fund/1464253357814.ajax?fileType=csv&fileName=XEQT_holdings&dataType=fund
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=average
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=chart
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=chart&subtab=total-returns&thumbnail=Y
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=cumulative
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=distributions&fileType=json
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=distributions&fileType=json&subtab=all.chart
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=distributions&fileType=json&subtab=all.table
/ca/investors/en/products/309480/fund/1464253357804.ajax?tab=distributions&fileType=json&subtab=calendar-year.chart
- holdings CSV https://www.blackrock.com/ca/investors/en/products/309480/fund/1464253357814.ajax?fileType=csv&fileName=XEQT_holdings&dataType=fund : HTTP 200 bytes=1962621 lines=8353
﻿Fund Holdings as of,"Oct 30, 2026"
 
Ticker,Name,Sector,Asset Class,Market Value,Weight (%),Notional Value,Shares,Par Value,Price,Location,Exchange,Currency,Duration,YTM (%),FX Rate,Maturity,Coupon
"XTOT","ISHARES CORE S&P TOTAL U.S. COM","Other","Equity","7,326,556,646.70","31.26","7,326,556,646.70","140,759,974.00","140,759,974.00","52.05","Canada","Toro
"XIC","ISHARES S&P/TSX CAPPED COMPOSITE","Financials","Equity","6,027,618,268.62","25.72","6,027,618,268.62","105,952,158.00","105,952,158.00","56.89","Canada",
"XEF","ISHARES MSCI EAFE IMI INDEX","Other","Equity","5,657,628,642.33","24.14","5,657,628,642.33","111,744,591.00","111,744,591.00","50.63","Canada","Toronto S
"ITOT","ISHARES CORE S&P TOTAL U.S. STOCK","Financials","Equity","3,356,294,328.35","14.32","3,356,294,328.35","14,578,795.00","14,578,795.00","230.22","United 
"XEC","ISHARES MSCI EMERGING MARKET","Financials","Equity","1,049,180,155.24","4.48","1,049,180,155.24","25,931,294.00","25,931,294.00","40.46","Canada","Toront
"CAD","CAD CASH","Cash and/or Derivatives","Cash","15,005,065.23","0.06","15,005,065.23","15,005,065.00","15,005,065.00","100.00","Canada","-","CAD","0.00","3.5
"USD","USD CASH","Cash and/or Derivatives","Cash","5,327,934.30","0.02","5,327,934.30","3,816,982.00","3,816,982.00","139.58","United States","-","CAD","0.00","
 
Fund Holdings as of,"Oct 30, 2026"
 
Ticker,Name,Sector,Asset Class,Market Value,Weight (%),Notional Value,Shares,Par Value,Price,Location,Exchange,Currency,Duration,YTM (%),FX Rate,Maturity,Coupon
"AAPL","APPLE","Information Technology","Equity","731,721,871.70","3.12","731,721,871.70","18,989,821.00","18,989,821.00","-","United States","NASDAQ","CAD","0.
- XEF page 310468: HTTP 200; csv links: /ca/investors/en/products/310468/fund/1464253357814.ajax?fileType=csv&fileName=XEFU_holdings&dataType=fund
FRED DEXCAUS via WebFetch rows 14560 first ['1971-01-04', np.float64(1.0109)] last ['2026-10-23', np.float64(1.3993)]
--- claude CLI present?
/opt/node22/bin/claude
2.1.316 (Claude Code)

## TradingAgents remaining files (2026-11-02 21:19:36 UTC)
- tradingagents/agents/managers/portfolio_manager.py: HTTP 200 lines=106
- tradingagents/agents/risk_mgmt/aggressive_debator.py: HTTP 200 lines=68
- tradingagents/agents/rating.py: HTTP 200 lines=117
- tradingagents/agents/schemas.py: HTTP 200 lines=379

## Latest releases: GitHub releases/latest redirect + PyPI (2026-11-02 21:19:37 UTC)
| repo | latest release tag (GitHub redirect) | release date (page) | PyPI pkg | PyPI version | PyPI upload |
|---|---|---|---|---|---|
| TauricResearch/TradingAgents | ? | ? | tradingagents | ? |
| virattt/ai-hedge-fund | ? | ? | n/a | ? |
| HKUDS/Vibe-Trading | ? | ? | n/a | ? |
| OpenByteInc/QuantDinger | ? | ? | n/a | ? |
| ginlix-ai/LangAlpha | ? | ? | n/a | ? |
| JerBouma/FinanceDatabase | ? | ? | financedatabase | 2.5.1 2026-10-12T07:33:34  |
| JerBouma/FinanceToolkit | ? | ? | financetoolkit | 2.3.0 2026-10-25T19:39:06  |
| QuantConnect/Lean | ? | ? | lean | 1.0.233 2026-10-27T19:57:56  |
| nautechsystems/nautilus_trader | ? | ? | nautilus_trader | 1.231.0 2026-08-02T18:51:05  |
| polakowo/vectorbt | ? | ? | vectorbt | 1.2.0 2026-10-19T13:19:06  |
| skfolio/skfolio | ? | ? | skfolio | 1.12.5 2026-10-29T18:45:36  |
| ranaroussi/yfinance | ? | ? | yfinance | 1.7.0 2026-08-26T17:25:08  |
| anthropics/financial-services | ? | ? | n/a | ? |
| AI4Finance-Foundation/FinRobot | ? | ? | n/a | ? |
| AI4Finance-Foundation/FinGPT | ? | ? | n/a | ? |
| microsoft/qlib | ? | ? | pyqlib | 0.9.7 2025-08-15T10:03:41  |
| Jakeschincariol/day-trader-skill | ? | ? | n/a | ? |
| quant-sentiment-ai/claude-equity-research | ? | ? | n/a | ? |
| pmorissette/bt | ? | ? | bt | 1.4.1 2026-10-10T15:58:21  |
| AI4Finance-Foundation/FinRL | ? | ? | finrl | 0.3.7 2024-04-12T02:42:14  |
| ranaroussi/quantstats | ? | ? | quantstats | 0.0.86 2026-09-27T19:41:43  |
| PyPortfolio/PyPortfolioOpt | ? | ? | pyportfolioopt | 1.6.0 2026-02-26T23:29:41  |
| dcajasn/Riskfolio-Lib | ? | ? | riskfolio-lib | 7.4.0 2026-10-04T05:08:50  |

## claude -p headless cost probe (2026-11-02 21:19:45 UTC)
- cmd: timeout 120 claude -p 'Reply with exactly the word OK.' --bare --model haiku --output-format json --max-budget-usd 0.05 --permission-prompts none
{
 "type": "result",
 "subtype": "success",
 "is_error": true,
 "result": "Authentication error \u00b7 This may be a temporary network issue, please try again",
 "total_cost_usd": 0,
 "duration_ms": 77,
 "num_turns": 1,
 "usage": {
  "output_tokens_details": {
   "thinking_tokens": 0
  },
  "input_tokens": 0,
  "cache_creation_input_tokens": 0,
  "cache_read_input_tokens": 0,
  "output_tokens": 0,
  "server_tool_use": {
   "web_search_requests": 0,
   "web_fetch_requests": 0
  },
  "service_tier": "standard",
  "cache_creation": {
   "ephemeral_1h_input_tokens": 0,
   "ephemeral_5m_input_tokens": 0
  },
  "inference_geo": "",
  "iterations": [],
  "speed": "standard",
  "fallback_credit": null
 },
 "modelUsage": {}
}

## yfinance rate-limit probe (2026-11-02 21:20:57 UTC)
- 25 tickers x (history(1y) + fast_info.last_price) sequential, no sleep: ok=25 errors=0 elapsed=10.3s (0.41s/ticker)
--- BoC Valet legacy pre-2017 USD/CAD (IEXE0101, noon rate) + series list check (21:21:36 UTC)
- IEXE0101 csv: HTTP 200 lines=1767 first-obs="2010-01-04","1.0378" last="2017-01-10","1.3208"
- FXUSDCAD json obs: 2452 first {'d': '2017-01-03', 'FXUSDCAD': {'v': '1.3435'}} last {'d': '2026-10-30', 'FXUSDCAD': {'v': '1.3960'}}
- BoC terms URL in payload: https://www.bankofcanada.ca/terms/
