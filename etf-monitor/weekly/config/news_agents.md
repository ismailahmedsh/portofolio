# News agents (family J)

Each agent gets this prompt, with its row filled in:

> You are news agent {ID} ({name}). First read etf-monitor/weekly/config/news_agent_brief.md and follow it exactly, using week {WEEK} and the window it implies. Scope: {scope}. Score: {buckets}. Write JSON to etf-monitor/weekly/runs/{WEEK}/news/{ID}.json and the digest to {ID}.md.

| ID | Name | Scope | Buckets to score |
|---|---|---|---|
| J01 | Global macro and central banks | Fed, ECB, BoE, BoJ, PBoC decisions and guidance; inflation, jobs, growth; yields and curve; US dollar; fiscal news | govt_bonds, credit_bonds, global_equity, us_large_broad, multi_asset_alt, gold_precious; state risk-on, neutral or risk-off |
| J02 | US equities and earnings | US market, earnings and guidance, breadth, small/mid caps, value vs growth, dividends, consumer, banks and insurers, US policy affecting profits | us_large_broad, us_small_mid_value, us_factor_dividend, consumer, financials |
| J03 | Tech, AI and semiconductors | mega-cap tech earnings and capex, AI demand, chip supply chain and export controls, software, cybersecurity, communication services, concentration | tech_ai_semis, us_large_broad; red flag if concentration risk rises |
| J04 | Sectors | healthcare and biotech, industrials and defense, infrastructure, utilities and power demand, REITs, clean energy policy | healthcare_biotech, industrials_defense_infra, utilities_realestate, clean_energy_thematic |
| J05 | Europe and developed ex-US | eurozone, UK, Switzerland, Nordics, ECB and BoE, European fiscal and defence, energy prices, Canada, Australia, Hong Kong, Singapore | europe, developed_ex_us, asia_dev_other |
| J06 | Japan and China | BoJ and yen, Japanese earnings and governance; China data, PBoC, stimulus, property, US-China relations, Chinese internet stocks | japan, china |
| J07 | Emerging markets ex-China | India, Taiwan, Korea, ASEAN, Brazil, Mexico, Argentina, South Africa, Turkey, EM currencies and flows | india, em_asia_other, latam, em_broad |
| J08 | Middle East, Gulf and geopolitics | Saudi, UAE, Qatar markets, Gulf fiscal outlook, index inclusion; conflicts, sanctions, shipping, tariffs, elections | mena_gulf; geopolitical angle for global_equity and energy_oil |
| J09 | Commodities | oil and gas, OPEC+, gold and silver, copper, lithium, uranium, mining equities, agriculture, broad indices | energy_oil, materials_mining_metals, gold_precious, commodities_broad |
| J10 | ETF flows and fund events | closures, mergers, fee changes, index changes, flows; any news on VWRA, SSAC/ACWD, IWDA, CSPX, VUAA, CNDX, EIMI, IGLN, AGGU; scan config/universe.csv tickers | bucket flows where reported data exists; red flags with URLs |
