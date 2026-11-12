# Pillar TAX01: US dividend withholding drag
Definition: Look-through US weight x US dividend yield x fund-level rate (Irish physical 15%, Irish swap on a qualified index about 0%, Luxembourg physical 30%), in bps a year. The US yield is the sum of the proxy's dividends with ex-dates in the 12 months ending today (not ending at the last payment). Scored only when CST02 is missing for the sleeve; otherwise it is inactive by design and TAX03/TAX05 are renormalised.
Source: iShares holdings CSV Location column (latest-holdings.csv by productId); vanguard.co.uk month-end region weights for Vanguard lines; yfinance Ticker.dividends of the US proxy, window anchored to today (verified). Better when: lower. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope            |   TAX01 | buyable   |   TAX01_score |   line_score |
|:-------|:----------|:-----------------|--------:|:----------|--------------:|-------------:|
| IB01.L | IB01.L    | government       |       0 | False     |            50 |        55.34 |
| TIPS.L | TIPS.L    | inflation-linked |       0 | False     |            50 |        50.29 |
| IGIL.L | IGIL.L    | inflation-linked |       0 | False     |            50 |        42.21 |
| XG7U.L | XG7U.L    | inflation-linked |       0 | False     |            50 |        39.07 |
| INXG.L | INXG.L    | inflation-linked |       0 | False     |            50 |        48.38 |
| IBCI.L | IBCI.L    | inflation-linked |       0 | False     |            50 |        50.61 |
| LQDA.L | LQDA.L    | corporate        |       0 | False     |            50 |        47.08 |
| VDPA.L | VDPA.L    | corporate        |       0 | False     |            50 |        55.04 |
| SDIA.L | SDIA.L    | corporate        |       0 | False     |            50 |        47.71 |
| VDCA.L | VDCA.L    | corporate        |       0 | False     |            50 |        52.24 |
| SUSU.L | SUSU.L    | corporate        |       0 | False     |            50 |        44.72 |
| ICBU.L | ICBU.L    | corporate        |       0 | False     |            50 |        44.79 |
| XDGU.L | XDGU.L    | corporate        |       0 | False     |            50 |        45.21 |
| CRPU.L | CRPU.L    | corporate        |       0 | False     |            50 |        43.78 |
| IEAA.L | IEAA.L    | corporate        |       0 | False     |            50 |        53.5  |
|        | cluster   | scope                  |   TAX01 | buyable   |   TAX01_score |   line_score |
|:-------|:----------|:-----------------------|--------:|:----------|--------------:|-------------:|
| VNRA.L | VNRA.L    | us                     | 14.839  | False     |         12.15 |        50.32 |
| IUCD.L | IUCD.L    | sector_consumer_disc   | 14.9337 | False     |         12.01 |        42.92 |
| USPY.L | USPY.L    | theme_cybersecurity    | 14.9702 | False     |         11.96 |        40.83 |
| WCBR.L | WCBR.L    | theme_cybersecurity    | 14.9702 | False     |         11.96 |        36.33 |
| CSUS.L | CSUS.L    | us                     | 14.9702 | False     |         11.96 |        55.65 |
| BRNT.L | BRNT.L    | commodities_energy_etc | 14.9702 | False     |         11.96 |        42.51 |
| SXLY.L | SXLY.L    | sector_consumer_disc   | 14.9702 | False     |         11.96 |        36.23 |
| CRUD.L | CRUD.L    | commodities_energy_etc | 14.9702 | False     |         11.96 |        42.13 |
| WCLD.L | WCLD.L    | theme_cloud            | 14.9702 | False     |         11.96 |        38.24 |
| LOCK.L | LOCK.L    | theme_cybersecurity    | 14.9702 | False     |         11.96 |        41.54 |
| AIGC.L | AIGC.L    | commodities_broad_etc  | 14.9702 | False     |         11.96 |        35.25 |
| CMOD.L | CMOD.L    | commodities_broad      | 14.9702 | False     |         11.96 |        43.98 |
| WCOA.L | WCOA.L    | commodities_broad      | 14.9702 | False     |         11.96 |        38.51 |
| ENCO.L | ENCO.L    | commodities_broad      | 14.9702 | False     |         11.96 |        36.22 |
| BCOM.L | BCOM.L    | commodities_broad      | 14.9702 | False     |         11.96 |        38.59 |

## All lines (csv)
,cluster,scope,TAX01,buyable,TAX01_score,line_score
IB01.L,IB01.L,government,0.0,False,50.0,55.34
VDST.L,VDST.L,government,0.0,False,50.0,56.33
IBTA.L,IBTA.L,government,0.0,False,50.0,56.49
CBU3.L,CBU3.L,government,0.0,False,50.0,49.56
XUT3.L,XUT3.L,government,0.0,False,50.0,46.44
TRE3.L,TRE3.L,government,0.0,False,50.0,48.81
US13.L,US13.L,government,0.0,False,50.0,49.83
CBU7.L,CBU7.L,government,0.0,False,50.0,55.46
CBU0.L,CBU0.L,government,0.0,False,50.0,57.53
TREX.L,TREX.L,government,0.0,False,50.0,50.59
US71.L,US71.L,government,0.0,False,50.0,50.86
DTLA.L,DTLA.L,government,0.0,False,50.0,56.46
US10.L,US10.L,government,0.0,False,50.0,48.53
VDTA.L,VDTA.L,government,0.0,False,50.0,54.89
XUTD.L,XUTD.L,government,0.0,False,50.0,48.42
TRES.L,TRES.L,government,0.0,False,50.0,49.65
TRSY.L,TRSY.L,government,0.0,False,50.0,51.52
IGLA.L,IGLA.L,government,0.0,False,50.0,43.86
XGGB.L,XGGB.L,government,0.0,False,50.0,39.18
IGLT.L,IGLT.L,government,0.0,False,50.0,55.37
IGLS.L,IGLS.L,government,0.0,False,50.0,55.3
SEGA.L,SEGA.L,government,0.0,False,50.0,51.69
XGLE.L,XGLE.L,government,0.0,False,50.0,50.27
AGGU.L,AGGU.L,aggregate,0.0,False,50.0,53.29
VAGU.L,VAGU.L,aggregate,0.0,False,50.0,52.19
GLAD.L,GLAD.L,aggregate,0.0,False,50.0,49.15
AGGG.L,AGGG.L,aggregate,0.0,False,50.0,50.77
GAGU.L,GAGU.L,aggregate,0.0,False,50.0,45.51
IUAA.L,IUAA.L,aggregate,0.0,False,50.0,46.09
USAG.L,USAG.L,aggregate,0.0,False,50.0,37.76
IDTP.L,IDTP.L,inflation-linked,0.0,False,50.0,51.6
TIP5.L,TIP5.L,inflation-linked,0.0,False,50.0,50.32
TIPU.L,TIPU.L,inflation-linked,0.0,False,50.0,46.67
TIPS.L,TIPS.L,inflation-linked,0.0,False,50.0,50.29
IGIL.L,IGIL.L,inflation-linked,0.0,False,50.0,42.21
XG7U.L,XG7U.L,inflation-linked,0.0,False,50.0,39.07
INXG.L,INXG.L,inflation-linked,0.0,False,50.0,48.38
IBCI.L,IBCI.L,inflation-linked,0.0,False,50.0,50.61
LQDA.L,LQDA.L,corporate,0.0,False,50.0,47.08
VDPA.L,VDPA.L,corporate,0.0,False,50.0,55.04
SDIA.L,SDIA.L,corporate,0.0,False,50.0,47.71
VDCA.L,VDCA.L,corporate,0.0,False,50.0,52.24
SUSU.L,SUSU.L,corporate,0.0,False,50.0,44.72
ICBU.L,ICBU.L,corporate,0.0,False,50.0,44.79
XDGU.L,XDGU.L,corporate,0.0,False,50.0,45.21
CRPU.L,CRPU.L,corporate,0.0,False,50.0,43.78
HLQD.L,HLQD.L,corporate,8.186083163062452,False,25.13,38.11
FLOA.L,FLOA.L,corporate,1.8323632531995888,False,43.92,53.11
UCRP.L,UCRP.L,corporate,10.00649430416374,False,20.85,40.12
IEAA.L,IEAA.L,corporate,0.0,False,50.0,53.5
IHYA.L,IHYA.L,high-yield,5.990400181758239,False,31.03,43.09
HYLA.L,HYLA.L,high-yield,0.0,False,50.0,41.94
XUHY.L,XUHY.L,high-yield,7.063278677843103,False,28.05,38.81
HYUS.L,HYUS.L,high-yield,6.351163783096117,False,30.01,37.91
DHYA.L,DHYA.L,high-yield,5.1613910206605365,False,33.44,38.55
WIAU.L,WIAU.L,high-yield,0.0,False,50.0,40.71
SJNK.L,SJNK.L,high-yield,9.114731179080849,False,22.88,35.96
HIGH.L,HIGH.L,high-yield,0.0,False,50.0,41.38
XHYG.L,HIGH.L,high-yield,0.0,False,50.0,51.8
JPEA.L,JPEA.L,em-debt,0.0,False,50.0,44.92
VDEA.L,VDEA.L,em-debt,0.0,False,50.0,42.08
EMSA.L,EMSA.L,em-debt,0.0,False,50.0,39.48
EMCA.L,EMCA.L,em-debt,0.0,False,50.0,43.87
EMGA.L,EMGA.L,em-debt,0.0,False,50.0,43.83
EMDD.L,EMDD.L,em-debt,0.0,False,50.0,39.95
EMLC.L,EMLC.L,em-debt,0.0,False,50.0,36.44
EMLB.L,EMLB.L,em-debt,0.0,False,50.0,36.59
ERNA.L,ERNA.L,money-market,0.0,False,50.0,54.21
JPSA.L,JPSA.L,money-market,0.0,False,50.0,41.89
ERNS.L,ERNS.L,money-market,0.0,False,50.0,54.59
XSTR.L,XSTR.L,money-market,0.0,False,50.0,47.73
ERNE.L,ERNE.L,money-market,0.0,False,50.0,50.97
VWRA.L,VWRA.L,global,8.968965395375186,True,49.99,52.93
ISAC.L,ACWD.L,global,9.249191707643464,False,50.09,49.57
IWDA.L,IWDA.L,global,10.58240739440274,False,50.06,51.14
XDWD.L,IWDA.L,global,10.472611809449743,False,50.42,50.13
SWRD.L,IWDA.L,global,10.617007817680683,False,49.94,51.37
HMWD.L,IWDA.L,global,10.666574761683892,False,49.78,50.13
FWRA.L,VWRA.L,global,8.961146310621094,False,50.01,48.74
VHVE.L,VHVE.L,global,9.675322456635136,False,21.58,49.78
WSML.L,WDSC.L,global,6.216431264666957,False,50.22,57.19
CSPX.L,XSPU.L,us,14.791225496064351,False,49.51,52.34
VUAA.L,XSPU.L,us,14.58836897263572,False,50.18,48.24
SPXS.L,XSPU.L,us,0.0,False,87.57,56.04
SPY5.L,XSPU.L,us,14.698931826816974,False,49.82,52.82
HSPD.L,XSPU.L,us,14.733122723030377,False,49.7,47.04
XSPU.L,XSPU.L,us,0.0,False,87.57,45.12
CNDX.L,CNDX.L,us,11.708856127614476,False,50.0,56.06
EQQU.L,CNDX.L,us,11.836729757273964,False,49.57,51.98
XNAS.L,CNDX.L,us,11.69260122414346,False,50.05,52.88
XDEW.L,XDEW.L,us,6.668303735414384,False,29.13,45.25
CSUS.L,CSUS.L,us,14.97018996400194,False,11.96,55.65
VNRA.L,VNRA.L,us,14.838955815884107,False,12.15,50.32
R2US.L,R2US.L,us,10.336787955589118,False,20.13,41.95
SPY4.L,SPY4.L,us,9.764578898792358,False,21.38,40.78
CUSS.L,CUSS.L,us,10.378006542927135,False,20.04,41.01
VEUA.L,VEUA.L,europe,0.0,False,50.0,53.64
VERG.L,VERG.L,europe,0.0,False,50.0,53.18
SMEA.L,SMEA.L,europe,0.0,False,50.0,53.99
IEUX.L,IEUX.L,europe,0.0,False,50.0,42.26
CSX5.L,CSX5.L,europe,0.0,False,50.0,54.36
XESC.L,XESC.L,europe,0.0,False,50.0,52.88
XDAX.L,XDAX.L,single_country,0.0,False,50.0,51.89
CACX.L,CACX.L,single_country,0.0,False,50.0,43.14
CSWG.L,CSWG.L,single_country,0.0,False,50.0,40.53
IAEX.L,IAEX.L,single_country,0.0,False,50.0,40.2
CUKX.L,CUKX.L,uk,0.0,False,50.0,56.68
VUKG.L,HUKX.L,uk,0.0,False,50.0,50.05
VMIG.L,MIDD.L,uk,2.524907154566249,False,50.37,50.69
MIDD.L,MIDD.L,uk,2.744890694990493,False,49.63,41.43
HUKX.L,HUKX.L,uk,0.0,False,50.0,50.86
CUKS.L,CUKS.L,uk,1.4798494229841028,False,45.08,34.47
IJPA.L,IJPA.L,japan,0.0,False,50.0,49.67
CSJP.L,CSJP.L,japan,0.3126469844742695,False,48.96,40.3
VJPA.L,VJPA.L,japan,0.0,False,50.0,46.36
XMJD.L,XMJD.L,japan,0.0,False,50.0,58.22
HMJD.L,XMJD.L,japan,0.0,False,50.0,45.61
LCJP.L,LCJP.L,japan,0.1944981772393899,False,49.35,49.25
XDJP.L,XDJP.L,japan,6.857508625398594,False,28.61,49.3
IDJP.L,IDJP.L,japan,0.0,False,50.0,36.72
CPXJ.L,CPXJ.L,asia_pacific,0.7618054357410761,False,47.46,46.93
VAPU.L,VAPU.L,asia_pacific,0.0,False,50.0,48.27
HMXJ.L,HMXJ.L,asia_pacific,3.4806754701414424,False,38.6,38.25
XPXD.L,XPXD.L,asia_pacific,4.080324305281876,False,36.72,38.17
IFFF.L,IFFF.L,asia_pacific,0.6149512546240269,False,47.95,42.22
HMAD.L,HMAD.L,asia_pacific,0.4069983385820694,False,48.64,36.71
XMAD.L,XMAD.L,asia_pacific,0.0,False,50.0,37.77
EIMI.L,EIMI.L,emerging,0.0,False,50.0,50.71
VFEA.L,VFEA.L,emerging,0.3181352027412716,False,48.94,48.22
IEMA.L,IEMA.L,emerging,0.0,False,50.0,50.65
XMME.L,XMMD.L,emerging,0.0,False,50.0,54.27
HMEM.L,XMMD.L,emerging,0.0,False,50.0,50.55
EMXC.L,EMXC.L,emerging,0.0,False,50.0,50.31
EMSD.L,EMSD.L,emerging,2.473080431524236,False,41.83,35.56
XMMD.L,XMMD.L,emerging,0.0,False,50.0,43.02
NDIA.L,XCS5.L,single_country,0.0,False,50.0,41.67
FLXI.L,FLXI.L,single_country,0.0,False,50.0,43.0
XCS5.L,XCS5.L,single_country,0.0,False,50.0,53.7
CNYA.L,CNYA.L,single_country,0.9791935016614212,False,46.74,44.98
XCS6.L,XCS6.L,single_country,0.0,False,50.0,40.47
HMCD.L,XCS6.L,single_country,0.0,False,50.0,54.0
FXC.L,FXC.L,single_country,0.0,False,50.0,40.02
KWEB.L,KWEB.L,single_country,0.2931405170242029,False,49.02,42.61
CSKR.L,CSKR.L,single_country,0.0,False,50.0,42.54
ITWN.L,ITWN.L,single_country,5.153248359413516,False,49.45,44.63
XMTD.L,ITWN.L,single_country,4.820871580371967,False,50.55,47.64
IBZL.L,IBZL.L,single_country,0.0,False,50.0,40.27
XMBD.L,IBZL.L,single_country,0.0,False,50.0,53.91
CMXC.L,CMXC.L,single_country,0.0,False,50.0,35.56
IKSA.L,IKSA.L,single_country,3.9931010957128823,False,37.0,37.6
IRSA.L,IRSA.L,single_country,0.0,False,50.0,36.54
IDTK.L,IDTK.L,single_country,0.0,False,50.0,34.39
IAUS.L,IAUS.L,single_country,1.7176279596338149,False,44.3,41.22
CCAU.L,CCAU.L,single_country,4.652045674612178,False,34.97,41.63
IPOL.L,IPOL.L,single_country,0.0,False,50.0,42.22
XVTD.L,XVTD.L,single_country,0.0,False,50.0,36.69
HIDD.L,HIDD.L,single_country,0.0,False,50.0,35.88
IWVL.L,IWVL.L,factor_value,1.4139838305378545,False,45.3,47.48
IWQU.L,IWQU.L,factor_quality,8.864304768554447,False,23.47,44.24
IWMO.L,IWMO.L,factor_momentum,9.356684428775424,False,22.31,44.06
MVOL.L,MVOL.L,factor_min_vol,0.0,False,50.0,44.02
XDEV.L,XDEV.L,factor_value,3.807719478012055,False,37.57,44.48
XDEQ.L,XDEQ.L,factor_quality,10.844041554302,False,19.06,40.36
XDEM.L,XDEM.L,factor_momentum,10.197610358635364,False,20.43,40.51
XDEB.L,XDEB.L,factor_min_vol,3.116201872420456,False,39.76,40.46
IUVL.L,IUVL.L,factor_value,7.923276374006442,False,25.8,46.43
IUQA.L,IUQA.L,factor_quality,11.92554456914916,False,16.94,44.79
IUMO.L,IUMO.L,factor_momentum,9.481892453484267,False,22.02,43.29
SPMV.L,SPMV.L,factor_min_vol,9.386701777412448,False,22.24,41.17
EMVL.L,EMVL.L,factor_value,0.0,False,50.0,44.13
IEFV.L,IEFV.L,factor_value,0.0,False,50.0,43.57
IEFQ.L,IEFQ.L,factor_quality,0.0,False,50.0,40.42
IEFM.L,IEFM.L,factor_momentum,0.0,False,50.0,41.08
JPGL.L,JPGL.L,factor_multi,1.80641035125628,False,44.01,38.53
MOAT.L,MOAT.L,factor_quality,6.973297237679962,False,28.3,36.86
WDSC.L,WDSC.L,size_small_cap,6.345769672189535,False,49.78,45.53
USSC.L,USSC.L,size_small_cap_value,7.4175198935408035,False,27.11,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,3.7057327650175216,False,37.89,37.07
SPEQ.L,SPEQ.L,equal_weight,7.620304662304237,False,26.58,42.26
VHYA.L,VHYD.L,dividend,0.1997122626778252,False,50.08,48.01
VHYD.L,VHYD.L,dividend,0.2500351972087151,False,49.92,50.34
FUSD.L,FUSD.L,dividend_quality,10.903844355107308,False,18.94,38.09
FGQI.L,FGQI.L,dividend_quality,7.482362268477337,False,26.94,37.29
GLDV.L,GLDV.L,dividend,0.0,False,50.0,39.83
UDVD.L,UDVD.L,dividend,0.1416143998525854,False,49.53,41.58
WQDV.L,WQDV.L,dividend_quality,3.69899274518595,False,37.91,41.46
QDIV.L,QDIV.L,dividend_quality,10.686474401674998,False,19.39,37.32
TDIV.L,TDIV.L,dividend,0.0,False,50.0,44.59
HDLV.L,HDLV.L,dividend_low_vol,0.0,False,50.0,40.44
DGRA.L,DGRA.L,dividend_quality,10.279165807193806,False,20.25,38.48
GGRA.L,GGRA.L,dividend_quality,4.774632618358986,False,34.6,39.2
EUDV.L,EUDV.L,dividend,0.0,False,50.0,40.49
IDVY.L,IDVY.L,dividend,0.0,False,50.0,41.73
IUIT.L,IUIT.L,sector_tech,11.801916277016176,False,17.17,49.92
SXLK.L,SXLK.L,sector_tech,11.86424718833753,False,17.05,45.08
XLKS.L,XLKS.L,sector_tech,11.835592913859896,False,17.11,45.96
XDWT.L,XDWT.L,sector_tech,11.66707049944422,False,17.43,44.13
WTEC.L,WTEC.L,sector_tech,11.740350111518984,False,17.29,38.34
IUHC.L,IUHC.L,sector_health,0.0,False,50.0,49.63
SXLV.L,SXLV.L,sector_health,0.0,False,50.0,45.91
XLVS.L,XLVS.L,sector_health,0.0,False,50.0,44.01
XDWH.L,WHEA.L,sector_health,0.0,False,50.0,55.44
WHEA.L,WHEA.L,sector_health,0.0,False,50.0,47.22
IUFS.L,IUFS.L,sector_financials,9.777918770987146,False,21.35,47.69
SXLF.L,SXLF.L,sector_financials,9.749452609377965,False,21.42,41.53
XLFS.L,XLFS.L,sector_financials,9.822205095119427,False,21.25,40.07
XDWF.L,WFIN.L,sector_financials,5.943035175629659,False,49.96,55.81
WFIN.L,WFIN.L,sector_financials,5.916738485256471,False,50.04,46.75
IUES.L,IUES.L,sector_energy,9.792280974217068,False,21.32,48.23
SXLE.L,SXLE.L,sector_energy,9.999535695721992,False,20.86,45.52
XLES.L,XLES.L,sector_energy,11.03152493446405,False,18.68,41.55
XDW0.L,WNRG.L,sector_energy,7.401049786100801,False,50.58,55.0
WNRG.L,WNRG.L,sector_energy,7.751580769746135,False,49.42,47.38
IOGP.L,IOGP.L,sector_energy,14.043046813703302,False,13.33,36.17
IUCD.L,IUCD.L,sector_consumer_disc,14.933675409986568,False,12.01,42.92
SXLY.L,SXLY.L,sector_consumer_disc,14.97018996400194,False,11.96,36.23
XDWC.L,WCOD.L,sector_consumer_disc,11.640913653697526,False,50.03,57.95
WCOD.L,WCOD.L,sector_consumer_disc,11.661667802519691,False,49.97,44.31
IUCS.L,IUCS.L,sector_consumer_staples,0.0,False,50.0,46.39
SXLP.L,SXLP.L,sector_consumer_staples,0.0,False,50.0,43.73
XDWS.L,XDWS.L,sector_consumer_staples,0.0,False,50.0,41.16
IUIS.L,IUIS.L,sector_industrials,8.621858076591566,False,24.06,45.18
SXLI.L,SXLI.L,sector_industrials,8.461163382951362,False,24.45,45.18
XDWI.L,XDWI.L,sector_industrials,4.304623141058552,False,36.03,41.14
IUUS.L,IUUS.L,sector_utilities,0.0,False,50.0,48.81
SXLU.L,SXLU.L,sector_utilities,0.0,False,50.0,42.66
XDWU.L,XDWU.L,sector_utilities,0.0,False,50.0,40.73
IUMS.L,IUMS.L,sector_materials,0.048493934092702,False,49.84,44.14
SXLB.L,SXLB.L,sector_materials,0.1113806028001257,False,49.63,39.26
XDWM.L,XDWM.L,sector_materials,0.0,False,50.0,39.7
IUCM.L,IUCM.L,sector_communication,14.704369989138732,False,12.34,45.41
SXLC.L,SXLC.L,sector_communication,14.2815232944694,False,12.96,40.19
XWTS.L,XWTS.L,sector_communication,14.336188886108452,False,12.88,35.61
SMH.L,SMH.L,theme_semiconductors,7.743274247271863,False,26.26,45.19
SEMI.L,SEMI.L,theme_semiconductors,6.696854003848256,False,29.05,45.1
SEMU.L,SEMU.L,theme_semiconductors,8.454339960886424,False,24.47,39.52
AIAI.L,AIAI.L,theme_ai,11.248119473822756,False,18.25,41.8
WTAI.L,WTAI.L,theme_ai,9.718499846570102,False,21.49,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,10.440163263060748,False,19.91,33.75
RBOT.L,RBOT.L,theme_ai_robotics,9.208352440344376,False,22.66,43.84
ROBO.L,ROBO.L,theme_ai_robotics,8.835452503923984,False,23.54,39.93
DGTL.L,DGTL.L,theme_digital_tech,14.722383843658257,False,12.31,37.07
XNGI.L,XNGI.L,theme_digital_tech,11.374172861815165,False,18.0,30.8
ITEK.L,ITEK.L,theme_digital_tech,11.219696867652928,False,18.3,32.68
WCLD.L,WCLD.L,theme_cloud,14.97018996400194,False,11.96,38.24
LOCK.L,LOCK.L,theme_cybersecurity,14.97018996400194,False,11.96,41.54
USPY.L,USPY.L,theme_cybersecurity,14.97018996400194,False,11.96,40.83
WCBR.L,WCBR.L,theme_cybersecurity,14.97018996400194,False,11.96,36.33
HEAL.L,HEAL.L,theme_health_innovation,1.8758055881612656,False,43.78,42.54
BTEC.L,BTEC.L,theme_biotech,0.7334429610389558,False,47.56,43.97
SBIO.L,SBIO.L,theme_biotech,0.2376731760638514,False,49.21,41.16
INRG.L,INRG.L,theme_clean_energy,9.195199764842878,False,22.69,41.88
RENW.L,RENW.L,theme_clean_energy,6.821492241937939,False,28.71,36.63
HTWO.L,HTWO.L,theme_clean_energy,3.7686336511747993,False,37.7,35.08
ECAR.L,ECAR.L,theme_ev_battery,6.206544025214663,False,30.42,37.63
BATT.L,BATT.L,theme_ev_battery,4.234043945160985,False,36.25,37.85
IH2O.L,IH2O.L,theme_water,0.0,False,50.0,41.27
WATU.L,WATU.L,theme_water,0.0,False,50.0,38.39
GLUG.L,GLUG.L,theme_water,0.5835232217731426,False,48.06,39.87
NATO.L,NATO.L,theme_defence,7.649830221601702,False,26.5,39.05
DFNS.L,DFNS.L,theme_defence,4.661992495712211,False,34.94,42.49
IGLN.L,PHAU.L,gold_physical_etc,0.0,False,50.0,54.79
SGLD.L,PHAU.L,gold_physical_etc,0.0,False,50.0,54.36
XGDU.L,XGDU.L,gold_physical_etc,0.0,False,50.0,48.98
WGLD.L,PHAU.L,gold_physical_etc,0.0,False,50.0,45.81
PHAU.L,PHAU.L,gold_physical_etc,0.0,False,50.0,36.69
SGBX.L,SGBX.L,gold_physical_etc,0.0,False,50.0,42.94
XGLD.L,PHAU.L,gold_physical_etc,0.0,False,50.0,34.54
RMAU.L,RMAU.L,gold_physical_etc,0.0,False,50.0,41.74
GDX.L,GDX.L,gold_miners,0.0,False,50.0,47.27
GDXJ.L,GDXJ.L,gold_miners,0.0,False,50.0,43.98
IAUP.L,IAUP.L,gold_miners,0.0,False,50.0,45.68
AUCO.L,AUCO.L,gold_miners,0.0,False,50.0,41.04
ISLN.L,PHAG.L,silver_physical_etc,0.0,False,50.0,55.13
SSLV.L,PHAG.L,silver_physical_etc,0.0,False,50.0,53.25
PHAG.L,PHAG.L,silver_physical_etc,0.0,False,50.0,37.57
SILV.L,SILV.L,silver_miners,0.0,False,50.0,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,0.0,False,50.0,38.29
IPLT.L,IPLT.L,platinum_physical_etc,0.0,False,50.0,42.09
IPDM.L,IPDM.L,palladium_physical_etc,0.0,False,50.0,41.44
CMOD.L,CMOD.L,commodities_broad,14.97018996400194,False,11.96,43.98
ICOM.L,ICOM.L,commodities_broad,0.0,False,50.0,45.76
BCOM.L,BCOM.L,commodities_broad,14.97018996400194,False,11.96,38.59
COMF.L,COMF.L,commodities_broad,9.301498721589237,False,22.44,36.88
ROLL.L,ROLL.L,commodities_broad,0.0,False,50.0,39.95
WCOA.L,WCOA.L,commodities_broad,14.97018996400194,False,11.96,38.51
ENCO.L,ENCO.L,commodities_broad,14.97018996400194,False,11.96,36.22
AIGC.L,AIGC.L,commodities_broad_etc,14.97018996400194,False,11.96,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,2.7548250144791555,False,40.92,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,0.0,False,50.0,43.59
BRNT.L,BRNT.L,commodities_energy_etc,14.97018996400194,False,11.96,42.51
CRUD.L,CRUD.L,commodities_energy_etc,14.97018996400194,False,11.96,42.13
GDIG.L,GDIG.L,commodity_equity_mining,0.0,False,50.0,43.0
COPX.L,COPX.L,commodity_equity_mining,0.0,False,50.0,42.56
REMX.L,REMX.L,commodity_equity_mining,0.5553614782633929,False,48.15,41.2
URNU.L,URNU.L,commodity_equity_uranium,8.080438742905395,False,25.4,37.49
URNM.L,URNM.L,commodity_equity_uranium,6.619403593621035,False,29.26,36.43
SPAG.L,SPAG.L,commodity_equity_agri,0.0,False,50.0,40.15
WOOD.L,WOOD.L,commodity_equity_timber,0.0,False,50.0,34.99
DPYA.L,DPYA.L,reit_global,0.0,False,50.0,40.49
GLRA.L,GLRA.L,reit_global,0.0,False,50.0,36.71
HPRD.L,HPRD.L,reit_global,0.0,False,50.0,40.52
EPRA.L,EPRA.L,reit_global,0.4862669865677745,False,48.38,39.75
TRET.L,TRET.L,reit_global,0.0,False,50.0,36.78
IDUP.L,IDUP.L,reit_us,0.1896334841245044,False,49.37,39.63
XRES.L,XRES.L,reit_us,0.0,False,50.0,44.93
IPRP.L,IPRP.L,reit_europe,0.0,False,50.0,39.51
XDER.L,XDER.L,reit_europe,0.0,False,50.0,37.62
IDAR.L,IDAR.L,reit_asia,0.0,False,50.0,35.09
IUKP.L,IUKP.L,reit_uk,0.0,False,50.0,43.05
IDIN.L,IDIN.L,infrastructure_global,0.0,False,50.0,40.84
XGID.L,XGID.L,infrastructure_global,0.0,False,50.0,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,0.0,False,50.0,37.41
PAVE.L,PAVE.L,infrastructure_us,8.476871682784092,False,24.41,38.56
MAGG.L,MAGG.L,multi_asset_growth,8.46118280781459,False,24.45,37.37
MAMG.L,MAMG.L,multi_asset_moderate,5.091636156198163,False,33.65,38.02
MACG.L,MACG.L,multi_asset_conservative,0.0,False,50.0,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,13.774933992410643,False,13.74,30.24
ACWD.L,ACWD.L,global,9.303728516981977,False,49.91,56.16
SPYY.L,SPYY.L,global,14.694546251037146,False,12.35,36.04
EXUS.L,EXUS.L,developed_ex_us,0.0,False,50.0,48.48

