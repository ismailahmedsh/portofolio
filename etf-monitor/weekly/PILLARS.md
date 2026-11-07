# The 100 pillars

Each pillar becomes a 0-100 score (100 = best) by percentile rank across the 200 active ETFs. Missing values score 50. Families A-I (90 pillars) are computed by `src/pillars.py`; family J (10 pillars) is scored by one news agent each, using `config/news_agent_brief.md`. Family H readings are market-wide, so they are mapped to buckets with a fixed sensitivity table in `src/pillars.py`.

| Family | Weight | Data source |
|---|---|---|
| A. Trend and momentum | 12 | Daily adjusted close (yfinance) |
| B. Relative strength | 8 | Daily adjusted close vs VT and bucket peers |
| C. Volatility | 10 | Daily returns, high/low/close |
| D. Drawdown and tail risk | 10 | Daily and weekly adjusted close |
| E. Risk-adjusted return | 15 | Daily, weekly and monthly returns |
| F. Liquidity and trading | 5 | Daily volume, high, low, close |
| G. Cost, structure and UAE investability | 20 | Fund facts (yfinance info), UCITS line check on LSE |
| H. Macro regime (bucket-mapped) | 5 | FRED (T10Y2Y, T10Y3M, SAHMREALTIME, BAMLH0A0HYM2, DFII10, DTWEXBGS, DCOILWTICO, NFCI) and CBOE VIX/VIX3M |
| I. Valuation and holdings | 5 | Fund holdings data (yfinance funds_data), FRED DGS10 |
| J. News and events (agents) | 10 | 10 news agents, web search, cited headlines |

| ID | Family | Pillar | Better when |
|---|---|---|---|
| A01 | Trend and momentum | Return 1 week | higher |
| A02 | Trend and momentum | Return 1 month | higher |
| A03 | Trend and momentum | Return 3 months | higher |
| A04 | Trend and momentum | Return 6 months | higher |
| A05 | Trend and momentum | Return 12 months | higher |
| A06 | Trend and momentum | Momentum 12-1 months | higher |
| A07 | Trend and momentum | Price vs 50-day average | higher |
| A08 | Trend and momentum | Price vs 200-day average | higher |
| A09 | Trend and momentum | Above 10-month average (Faber) | higher |
| A10 | Trend and momentum | 50-day vs 200-day average | higher |
| B01 | Relative strength | Excess return vs VT 1m | higher |
| B02 | Relative strength | Excess return vs VT 3m | higher |
| B03 | Relative strength | Excess return vs VT 6m | higher |
| B04 | Relative strength | Excess return vs VT 12m | higher |
| B05 | Relative strength | Rank in bucket 3m | higher |
| B06 | Relative strength | Rank in bucket 12m | higher |
| B07 | Relative strength | Excess vs bucket median 6m | higher |
| B08 | Relative strength | Relative-strength slope vs VT 13w | higher |
| B09 | Relative strength | Share of weeks beating VT 26w | higher |
| B10 | Relative strength | Information ratio vs VT 1y | higher |
| C01 | Volatility | Volatility 1m | lower |
| C02 | Volatility | Volatility 3m | lower |
| C03 | Volatility | Volatility 1y | lower |
| C04 | Volatility | Volatility of volatility | lower |
| C05 | Volatility | Downside deviation 1y | lower |
| C06 | Volatility | Volatility regime 1m/1y | lower |
| C07 | Volatility | Beta to VT 1y | lower |
| C08 | Volatility | Correlation to VT 1y | lower |
| C09 | Volatility | Idiosyncratic volatility 1y | lower |
| C10 | Volatility | Average true range 14d % | lower |
| D01 | Drawdown and tail risk | Drawdown from 52-week high | higher |
| D02 | Drawdown and tail risk | Max drawdown 1y | higher |
| D03 | Drawdown and tail risk | Max drawdown 3y | higher |
| D04 | Drawdown and tail risk | Max drawdown full history | higher |
| D05 | Drawdown and tail risk | Ulcer index 1y | lower |
| D06 | Drawdown and tail risk | CVaR 95% weekly 3y | higher |
| D07 | Drawdown and tail risk | Skewness weekly 3y | higher |
| D08 | Drawdown and tail risk | Kurtosis weekly 3y | lower |
| D09 | Drawdown and tail risk | Days since all-time high | lower |
| D10 | Drawdown and tail risk | Share of 3y max drawdown recovered | higher |
| E01 | Risk-adjusted return | Sharpe 1y | higher |
| E02 | Risk-adjusted return | Sharpe 3y | higher |
| E03 | Risk-adjusted return | Sharpe 5y | higher |
| E04 | Risk-adjusted return | Sortino 3y | higher |
| E05 | Risk-adjusted return | Calmar 3y | higher |
| E06 | Risk-adjusted return | Martin ratio 3y | higher |
| E07 | Risk-adjusted return | Share of positive months 3y | higher |
| E08 | Risk-adjusted return | Worst rolling 12m return 5y | higher |
| E09 | Risk-adjusted return | CAGR 5y | higher |
| E10 | Risk-adjusted return | CAGR 10y | higher |
| F01 | Liquidity and trading | Average daily dollar volume 3m | higher |
| F02 | Liquidity and trading | Dollar volume trend 1m/6m | higher |
| F03 | Liquidity and trading | Amihud illiquidity | lower |
| F04 | Liquidity and trading | High-low range 20d | lower |
| F05 | Liquidity and trading | Volume spike frequency 3m | lower |
| F06 | Liquidity and trading | History length years | higher |
| F07 | Liquidity and trading | Missing data share | lower |
| F08 | Liquidity and trading | Price jumps over 4 sigma 1y | lower |
| F09 | Liquidity and trading | On-balance volume slope 3m | higher |
| F10 | Liquidity and trading | Chaikin money flow 20d | higher |
| G01 | Cost, structure and UAE investability | Expense ratio | lower |
| G02 | Cost, structure and UAE investability | Assets under management | higher |
| G03 | Cost, structure and UAE investability | Fund age years | higher |
| G04 | Cost, structure and UAE investability | Closure risk flag | lower |
| G05 | Cost, structure and UAE investability | Tracking deviation vs bucket 1y | lower |
| G06 | Cost, structure and UAE investability | Price vs NAV gap | lower |
| G07 | Cost, structure and UAE investability | Distribution yield (context) | context only (not scored) |
| G08 | Cost, structure and UAE investability | UCITS line available on LSE | higher |
| G09 | Cost, structure and UAE investability | UAE withholding drag bps | lower |
| G10 | Cost, structure and UAE investability | US estate-tax exposure | lower |
| H01 | Macro regime (bucket-mapped) | Yield curve 10y-2y | higher |
| H02 | Macro regime (bucket-mapped) | Yield curve 10y-3m | higher |
| H03 | Macro regime (bucket-mapped) | Sahm rule | higher |
| H04 | Macro regime (bucket-mapped) | High-yield spread trend | higher |
| H05 | Macro regime (bucket-mapped) | Real yield trend 10y | higher |
| H06 | Macro regime (bucket-mapped) | US dollar trend | higher |
| H07 | Macro regime (bucket-mapped) | Oil trend | higher |
| H08 | Macro regime (bucket-mapped) | Financial conditions (NFCI) | higher |
| H09 | Macro regime (bucket-mapped) | VIX level | higher |
| H10 | Macro regime (bucket-mapped) | VIX term structure | higher |
| I01 | Valuation and holdings | P/E | lower |
| I02 | Valuation and holdings | P/B | lower |
| I03 | Valuation and holdings | P/S | lower |
| I04 | Valuation and holdings | P/CF | lower |
| I05 | Valuation and holdings | Bond duration (bond funds) | lower |
| I06 | Valuation and holdings | Earnings yield minus 10y Treasury yield | higher |
| I07 | Valuation and holdings | Top-10 holdings weight | lower |
| I08 | Valuation and holdings | Sector concentration HHI | lower |
| I09 | Valuation and holdings | Largest holding weight | lower |
| I10 | Valuation and holdings | P/E vs bucket median | lower |
| J01 | News and events (agents) | Global macro and central banks | higher |
| J02 | News and events (agents) | US equities and earnings | higher |
| J03 | News and events (agents) | Tech, AI and semiconductors | higher |
| J04 | News and events (agents) | Sectors: health, industrials, utilities, clean energy | higher |
| J05 | News and events (agents) | Europe and developed ex-US | higher |
| J06 | News and events (agents) | Japan and China | higher |
| J07 | News and events (agents) | Emerging markets ex-China | higher |
| J08 | News and events (agents) | Middle East, Gulf and geopolitics | higher |
| J09 | News and events (agents) | Commodities | higher |
| J10 | News and events (agents) | ETF flows and fund events | higher |

Weights are pre-registered and change only with a written reason in `CHANGELOG.md` plus a fresh backtest. Bond duration (I05) from Yahoo is unreliable (TLT reads 3.6 years) and is kept only as a low-weight pillar until a better source is wired in.
