# Pillar CON04: Restricted-market exposure (gate only)
Definition: Look-through weight in markets listed in config/restricted_markets.csv (to be created). Every row carries a primary-source citation and date, added by EVT07 and checked by code. Above 5%, the line cannot receive deposits. Weight 0.
Source: Holdings Location column (verified); config/restricted_markets.csv (verified). Better when: lower. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                   | CON04   | buyable   |   line_score |
|:-------|:----------|:------------------------|:--------|:----------|-------------:|
| IB01.L | IB01.L    | government              | False   | False     |        55.34 |
| WCOD.L | WCOD.L    | sector_consumer_disc    | False   | False     |        44.31 |
| XDWC.L | WCOD.L    | sector_consumer_disc    | False   | False     |        57.95 |
| SXLY.L | SXLY.L    | sector_consumer_disc    | False   | False     |        36.23 |
| IUCD.L | IUCD.L    | sector_consumer_disc    | False   | False     |        42.92 |
| IOGP.L | IOGP.L    | sector_energy           | False   | False     |        36.17 |
| WNRG.L | WNRG.L    | sector_energy           | False   | False     |        47.38 |
| XDW0.L | WNRG.L    | sector_energy           | False   | False     |        55    |
| IUCS.L | IUCS.L    | sector_consumer_staples | False   | False     |        46.39 |
| XLES.L | XLES.L    | sector_energy           | False   | False     |        41.55 |
| IUES.L | IUES.L    | sector_energy           | False   | False     |        48.23 |
| WFIN.L | WFIN.L    | sector_financials       | False   | False     |        46.75 |
| XDWF.L | WFIN.L    | sector_financials       | False   | False     |        55.81 |
| XLFS.L | XLFS.L    | sector_financials       | False   | False     |        40.07 |
| SXLF.L | SXLF.L    | sector_financials       | False   | False     |        41.53 |
|        | cluster   | scope          | CON04   | buyable   |   line_score |
|:-------|:----------|:---------------|:--------|:----------|-------------:|
| VUKG.L | HUKX.L    | uk             | False   | False     |        50.05 |
| CUKX.L | CUKX.L    | uk             | False   | False     |        56.68 |
| VERG.L | VERG.L    | europe         | False   | False     |        53.18 |
| IAEX.L | IAEX.L    | single_country | False   | False     |        40.2  |
| CACX.L | CACX.L    | single_country | False   | False     |        43.14 |
| XDAX.L | XDAX.L    | single_country | False   | False     |        51.89 |
| XESC.L | XESC.L    | europe         | False   | False     |        52.88 |
| CSX5.L | CSX5.L    | europe         | False   | False     |        54.36 |
| IEUX.L | IEUX.L    | europe         | False   | False     |        42.26 |
| CSWG.L | CSWG.L    | single_country | False   | False     |        40.53 |
| KWEB.L | KWEB.L    | single_country | True    | False     |        42.61 |
| FXC.L  | FXC.L     | single_country | True    | False     |        40.02 |
| HMCD.L | XCS6.L    | single_country | True    | False     |        54    |
| XCS6.L | XCS6.L    | single_country | True    | False     |        40.47 |
| CNYA.L | CNYA.L    | single_country | True    | False     |        44.98 |

## All lines (csv)
,cluster,scope,CON04,buyable,line_score
IB01.L,IB01.L,government,False,False,55.34
VDST.L,VDST.L,government,False,False,56.33
IBTA.L,IBTA.L,government,False,False,56.49
CBU3.L,CBU3.L,government,False,False,49.56
XUT3.L,XUT3.L,government,False,False,46.44
TRE3.L,TRE3.L,government,False,False,48.81
US13.L,US13.L,government,False,False,49.83
CBU7.L,CBU7.L,government,False,False,55.46
CBU0.L,CBU0.L,government,False,False,57.53
TREX.L,TREX.L,government,False,False,50.59
US71.L,US71.L,government,False,False,50.86
DTLA.L,DTLA.L,government,False,False,56.46
US10.L,US10.L,government,False,False,48.53
VDTA.L,VDTA.L,government,False,False,54.89
XUTD.L,XUTD.L,government,False,False,48.42
TRES.L,TRES.L,government,False,False,49.65
TRSY.L,TRSY.L,government,False,False,51.52
IGLA.L,IGLA.L,government,False,False,43.86
XGGB.L,XGGB.L,government,False,False,39.18
IGLT.L,IGLT.L,government,False,False,55.37
IGLS.L,IGLS.L,government,False,False,55.3
SEGA.L,SEGA.L,government,False,False,51.69
XGLE.L,XGLE.L,government,False,False,50.27
AGGU.L,AGGU.L,aggregate,False,False,53.29
VAGU.L,VAGU.L,aggregate,False,False,52.19
GLAD.L,GLAD.L,aggregate,False,False,49.15
AGGG.L,AGGG.L,aggregate,False,False,50.77
GAGU.L,GAGU.L,aggregate,False,False,45.51
IUAA.L,IUAA.L,aggregate,False,False,46.09
USAG.L,USAG.L,aggregate,False,False,37.76
IDTP.L,IDTP.L,inflation-linked,False,False,51.6
TIP5.L,TIP5.L,inflation-linked,False,False,50.32
TIPU.L,TIPU.L,inflation-linked,False,False,46.67
TIPS.L,TIPS.L,inflation-linked,False,False,50.29
IGIL.L,IGIL.L,inflation-linked,False,False,42.21
XG7U.L,XG7U.L,inflation-linked,False,False,39.07
INXG.L,INXG.L,inflation-linked,False,False,48.38
IBCI.L,IBCI.L,inflation-linked,False,False,50.61
LQDA.L,LQDA.L,corporate,False,False,47.08
VDPA.L,VDPA.L,corporate,False,False,55.04
SDIA.L,SDIA.L,corporate,False,False,47.71
VDCA.L,VDCA.L,corporate,False,False,52.24
SUSU.L,SUSU.L,corporate,False,False,44.72
ICBU.L,ICBU.L,corporate,False,False,44.79
XDGU.L,XDGU.L,corporate,False,False,45.21
CRPU.L,CRPU.L,corporate,False,False,43.78
HLQD.L,HLQD.L,corporate,False,False,38.11
FLOA.L,FLOA.L,corporate,False,False,53.11
UCRP.L,UCRP.L,corporate,False,False,42.57
IEAA.L,IEAA.L,corporate,False,False,53.5
IHYA.L,IHYA.L,high-yield,False,False,43.09
HYLA.L,HYLA.L,high-yield,False,False,41.94
XUHY.L,XUHY.L,high-yield,False,False,38.81
HYUS.L,HYUS.L,high-yield,False,False,37.91
DHYA.L,DHYA.L,high-yield,False,False,38.55
WIAU.L,WIAU.L,high-yield,False,False,40.71
SJNK.L,SJNK.L,high-yield,False,False,35.96
HIGH.L,HIGH.L,high-yield,False,False,41.38
XHYG.L,HIGH.L,high-yield,False,False,51.8
JPEA.L,JPEA.L,em-debt,False,False,44.92
VDEA.L,VDEA.L,em-debt,False,False,42.08
EMSA.L,EMSA.L,em-debt,False,False,39.48
EMCA.L,EMCA.L,em-debt,False,False,43.87
EMGA.L,EMGA.L,em-debt,False,False,43.83
EMDD.L,EMDD.L,em-debt,False,False,39.95
EMLC.L,EMLC.L,em-debt,False,False,36.44
EMLB.L,EMLB.L,em-debt,False,False,36.59
ERNA.L,ERNA.L,money-market,False,False,54.21
JPSA.L,JPSA.L,money-market,False,False,41.89
ERNS.L,ERNS.L,money-market,False,False,54.59
XSTR.L,XSTR.L,money-market,False,False,47.73
ERNE.L,ERNE.L,money-market,False,False,50.97
VWRA.L,VWRA.L,global,False,True,52.93
ISAC.L,ISAC.L,global,False,False,44.55
IWDA.L,IWDA.L,global,False,False,51.14
XDWD.L,IWDA.L,global,False,False,50.13
SWRD.L,IWDA.L,global,False,False,51.37
HMWD.L,IWDA.L,global,False,False,50.13
FWRA.L,VWRA.L,global,False,False,48.74
VHVE.L,VHVE.L,global,False,False,49.78
WSML.L,WDSC.L,global,False,False,57.19
CSPX.L,XSPU.L,us,False,False,52.34
VUAA.L,XSPU.L,us,False,False,48.24
SPXS.L,XSPU.L,us,False,False,56.04
SPY5.L,XSPU.L,us,False,False,52.82
HSPD.L,XSPU.L,us,False,False,47.04
XSPU.L,XSPU.L,us,False,False,45.12
CNDX.L,CNDX.L,us,False,False,52.49
EQQU.L,EQQU.L,us,False,False,41.39
XNAS.L,CNDX.L,us,False,False,50.96
XDEW.L,XDEW.L,us,False,False,45.25
CSUS.L,CSUS.L,us,False,False,55.65
VNRA.L,VNRA.L,us,False,False,50.32
R2US.L,R2US.L,us,False,False,41.95
SPY4.L,SPY4.L,us,False,False,40.78
CUSS.L,CUSS.L,us,False,False,41.01
VEUA.L,VEUA.L,europe,False,False,53.64
VERG.L,VERG.L,europe,False,False,53.18
SMEA.L,SMEA.L,europe,False,False,53.99
IEUX.L,IEUX.L,europe,False,False,42.26
CSX5.L,CSX5.L,europe,False,False,54.36
XESC.L,XESC.L,europe,False,False,52.88
XDAX.L,XDAX.L,single_country,False,False,51.89
CACX.L,CACX.L,single_country,False,False,43.14
CSWG.L,CSWG.L,single_country,False,False,40.53
IAEX.L,IAEX.L,single_country,False,False,40.2
CUKX.L,CUKX.L,uk,False,False,56.68
VUKG.L,HUKX.L,uk,False,False,50.05
VMIG.L,MIDD.L,uk,False,False,50.69
MIDD.L,MIDD.L,uk,False,False,41.43
HUKX.L,HUKX.L,uk,False,False,50.86
CUKS.L,CUKS.L,uk,False,False,34.47
IJPA.L,IJPA.L,japan,False,False,49.67
CSJP.L,CSJP.L,japan,False,False,40.3
VJPA.L,VJPA.L,japan,False,False,46.36
XMJD.L,XMJD.L,japan,False,False,58.22
HMJD.L,XMJD.L,japan,False,False,45.61
LCJP.L,LCJP.L,japan,False,False,49.25
XDJP.L,XDJP.L,japan,False,False,50.4
IDJP.L,IDJP.L,japan,False,False,36.72
CPXJ.L,CPXJ.L,asia_pacific,False,False,46.93
VAPU.L,VAPU.L,asia_pacific,False,False,48.27
HMXJ.L,HMXJ.L,asia_pacific,False,False,38.25
XPXD.L,XPXD.L,asia_pacific,False,False,38.17
IFFF.L,IFFF.L,asia_pacific,False,False,42.22
HMAD.L,HMAD.L,asia_pacific,False,False,36.71
XMAD.L,XMAD.L,asia_pacific,False,False,37.77
EIMI.L,EIMI.L,emerging,False,False,50.71
VFEA.L,VFEA.L,emerging,False,False,48.22
IEMA.L,IEMA.L,emerging,False,False,50.65
XMME.L,XMMD.L,emerging,False,False,54.27
HMEM.L,XMMD.L,emerging,False,False,50.55
EMXC.L,EMXC.L,emerging,False,False,50.31
EMSD.L,EMSD.L,emerging,False,False,35.56
XMMD.L,XMMD.L,emerging,False,False,43.02
NDIA.L,XCS5.L,single_country,False,False,41.67
FLXI.L,FLXI.L,single_country,False,False,43.0
XCS5.L,XCS5.L,single_country,False,False,53.7
CNYA.L,CNYA.L,single_country,True,False,44.98
XCS6.L,XCS6.L,single_country,True,False,40.47
HMCD.L,XCS6.L,single_country,True,False,54.0
FXC.L,FXC.L,single_country,True,False,40.02
KWEB.L,KWEB.L,single_country,True,False,42.61
CSKR.L,CSKR.L,single_country,False,False,42.54
ITWN.L,ITWN.L,single_country,False,False,44.63
XMTD.L,ITWN.L,single_country,False,False,47.64
IBZL.L,IBZL.L,single_country,False,False,40.27
XMBD.L,IBZL.L,single_country,False,False,53.91
CMXC.L,CMXC.L,single_country,False,False,35.56
IKSA.L,IKSA.L,single_country,False,False,37.6
IRSA.L,IRSA.L,single_country,False,False,36.54
IDTK.L,IDTK.L,single_country,False,False,34.39
IAUS.L,IAUS.L,single_country,False,False,41.22
CCAU.L,CCAU.L,single_country,False,False,41.63
IPOL.L,IPOL.L,single_country,False,False,42.22
XVTD.L,XVTD.L,single_country,False,False,36.69
HIDD.L,HIDD.L,single_country,False,False,35.88
IWVL.L,IWVL.L,factor_value,False,False,47.48
IWQU.L,IWQU.L,factor_quality,False,False,44.24
IWMO.L,IWMO.L,factor_momentum,False,False,44.06
MVOL.L,MVOL.L,factor_min_vol,False,False,44.02
XDEV.L,XDEV.L,factor_value,False,False,44.48
XDEQ.L,XDEQ.L,factor_quality,False,False,40.36
XDEM.L,XDEM.L,factor_momentum,False,False,40.51
XDEB.L,XDEB.L,factor_min_vol,False,False,40.46
IUVL.L,IUVL.L,factor_value,False,False,46.43
IUQA.L,IUQA.L,factor_quality,False,False,44.79
IUMO.L,IUMO.L,factor_momentum,False,False,43.29
SPMV.L,SPMV.L,factor_min_vol,False,False,41.17
EMVL.L,EMVL.L,factor_value,False,False,44.13
IEFV.L,IEFV.L,factor_value,False,False,43.57
IEFQ.L,IEFQ.L,factor_quality,False,False,40.42
IEFM.L,IEFM.L,factor_momentum,False,False,41.08
JPGL.L,JPGL.L,factor_multi,False,False,38.53
MOAT.L,MOAT.L,factor_quality,False,False,36.86
WDSC.L,WDSC.L,size_small_cap,False,False,45.53
USSC.L,USSC.L,size_small_cap_value,False,False,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,False,False,37.07
SPEQ.L,SPEQ.L,equal_weight,False,False,42.26
VHYA.L,VHYD.L,dividend,False,False,48.01
VHYD.L,VHYD.L,dividend,False,False,50.34
FUSD.L,FUSD.L,dividend_quality,False,False,38.09
FGQI.L,FGQI.L,dividend_quality,False,False,37.29
GLDV.L,GLDV.L,dividend,False,False,39.83
UDVD.L,UDVD.L,dividend,False,False,41.58
WQDV.L,WQDV.L,dividend_quality,False,False,41.46
QDIV.L,QDIV.L,dividend_quality,False,False,37.32
TDIV.L,TDIV.L,dividend,False,False,44.59
HDLV.L,HDLV.L,dividend_low_vol,False,False,40.44
DGRA.L,DGRA.L,dividend_quality,False,False,38.48
GGRA.L,GGRA.L,dividend_quality,False,False,39.2
EUDV.L,EUDV.L,dividend,False,False,40.49
IDVY.L,IDVY.L,dividend,False,False,41.73
IUIT.L,IUIT.L,sector_tech,False,False,49.92
SXLK.L,SXLK.L,sector_tech,False,False,45.08
XLKS.L,XLKS.L,sector_tech,False,False,45.96
XDWT.L,XDWT.L,sector_tech,False,False,44.13
WTEC.L,WTEC.L,sector_tech,False,False,38.34
IUHC.L,IUHC.L,sector_health,False,False,49.63
SXLV.L,SXLV.L,sector_health,False,False,45.91
XLVS.L,XLVS.L,sector_health,False,False,44.01
XDWH.L,WHEA.L,sector_health,False,False,55.44
WHEA.L,WHEA.L,sector_health,False,False,47.22
IUFS.L,IUFS.L,sector_financials,False,False,47.69
SXLF.L,SXLF.L,sector_financials,False,False,41.53
XLFS.L,XLFS.L,sector_financials,False,False,40.07
XDWF.L,WFIN.L,sector_financials,False,False,55.81
WFIN.L,WFIN.L,sector_financials,False,False,46.75
IUES.L,IUES.L,sector_energy,False,False,48.23
SXLE.L,SXLE.L,sector_energy,False,False,45.52
XLES.L,XLES.L,sector_energy,False,False,41.55
XDW0.L,WNRG.L,sector_energy,False,False,55.0
WNRG.L,WNRG.L,sector_energy,False,False,47.38
IOGP.L,IOGP.L,sector_energy,False,False,36.17
IUCD.L,IUCD.L,sector_consumer_disc,False,False,42.92
SXLY.L,SXLY.L,sector_consumer_disc,False,False,36.23
XDWC.L,WCOD.L,sector_consumer_disc,False,False,57.95
WCOD.L,WCOD.L,sector_consumer_disc,False,False,44.31
IUCS.L,IUCS.L,sector_consumer_staples,False,False,46.39
SXLP.L,SXLP.L,sector_consumer_staples,False,False,43.73
XDWS.L,XDWS.L,sector_consumer_staples,False,False,41.16
IUIS.L,IUIS.L,sector_industrials,False,False,45.18
SXLI.L,SXLI.L,sector_industrials,False,False,45.18
XDWI.L,XDWI.L,sector_industrials,False,False,41.14
IUUS.L,IUUS.L,sector_utilities,False,False,48.81
SXLU.L,SXLU.L,sector_utilities,False,False,42.66
XDWU.L,XDWU.L,sector_utilities,False,False,40.73
IUMS.L,IUMS.L,sector_materials,False,False,44.14
SXLB.L,SXLB.L,sector_materials,False,False,39.26
XDWM.L,XDWM.L,sector_materials,False,False,39.7
IUCM.L,IUCM.L,sector_communication,False,False,45.41
SXLC.L,SXLC.L,sector_communication,False,False,40.19
XWTS.L,XWTS.L,sector_communication,False,False,35.61
SMH.L,SMH.L,theme_semiconductors,False,False,45.19
SEMI.L,SEMI.L,theme_semiconductors,False,False,45.1
SEMU.L,SEMU.L,theme_semiconductors,False,False,39.52
AIAI.L,AIAI.L,theme_ai,False,False,41.8
WTAI.L,WTAI.L,theme_ai,False,False,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,False,False,33.75
RBOT.L,RBOT.L,theme_ai_robotics,False,False,43.84
ROBO.L,ROBO.L,theme_ai_robotics,False,False,39.93
DGTL.L,DGTL.L,theme_digital_tech,False,False,37.07
XNGI.L,XNGI.L,theme_digital_tech,False,False,30.8
ITEK.L,ITEK.L,theme_digital_tech,False,False,32.68
WCLD.L,WCLD.L,theme_cloud,False,False,38.24
LOCK.L,LOCK.L,theme_cybersecurity,False,False,41.54
USPY.L,USPY.L,theme_cybersecurity,False,False,40.83
WCBR.L,WCBR.L,theme_cybersecurity,False,False,36.33
HEAL.L,HEAL.L,theme_health_innovation,False,False,42.54
BTEC.L,BTEC.L,theme_biotech,False,False,43.97
SBIO.L,SBIO.L,theme_biotech,False,False,41.16
INRG.L,INRG.L,theme_clean_energy,False,False,41.88
RENW.L,RENW.L,theme_clean_energy,False,False,36.63
HTWO.L,HTWO.L,theme_clean_energy,False,False,35.08
ECAR.L,ECAR.L,theme_ev_battery,False,False,37.63
BATT.L,BATT.L,theme_ev_battery,False,False,37.85
IH2O.L,IH2O.L,theme_water,False,False,41.27
WATU.L,WATU.L,theme_water,False,False,38.39
GLUG.L,GLUG.L,theme_water,False,False,39.87
NATO.L,NATO.L,theme_defence,False,False,39.05
DFNS.L,DFNS.L,theme_defence,False,False,42.49
IGLN.L,PHAU.L,gold_physical_etc,False,False,54.79
SGLD.L,PHAU.L,gold_physical_etc,False,False,54.36
XGDU.L,XGDU.L,gold_physical_etc,False,False,48.98
WGLD.L,PHAU.L,gold_physical_etc,False,False,45.81
PHAU.L,PHAU.L,gold_physical_etc,False,False,36.69
SGBX.L,SGBX.L,gold_physical_etc,False,False,42.94
XGLD.L,PHAU.L,gold_physical_etc,False,False,34.54
RMAU.L,RMAU.L,gold_physical_etc,False,False,41.74
GDX.L,GDX.L,gold_miners,False,False,47.27
GDXJ.L,GDXJ.L,gold_miners,False,False,43.98
IAUP.L,IAUP.L,gold_miners,False,False,45.68
AUCO.L,AUCO.L,gold_miners,False,False,41.04
ISLN.L,PHAG.L,silver_physical_etc,False,False,55.13
SSLV.L,PHAG.L,silver_physical_etc,False,False,53.25
PHAG.L,PHAG.L,silver_physical_etc,False,False,37.57
SILV.L,SILV.L,silver_miners,False,False,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,False,False,38.29
IPLT.L,IPLT.L,platinum_physical_etc,False,False,42.09
IPDM.L,IPDM.L,palladium_physical_etc,False,False,41.44
CMOD.L,CMOD.L,commodities_broad,False,False,43.98
ICOM.L,ICOM.L,commodities_broad,False,False,45.76
BCOM.L,BCOM.L,commodities_broad,False,False,38.59
COMF.L,COMF.L,commodities_broad,False,False,36.88
ROLL.L,ROLL.L,commodities_broad,False,False,39.95
WCOA.L,WCOA.L,commodities_broad,False,False,38.51
ENCO.L,ENCO.L,commodities_broad,False,False,36.22
AIGC.L,AIGC.L,commodities_broad_etc,False,False,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,False,False,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,False,False,43.59
BRNT.L,BRNT.L,commodities_energy_etc,False,False,42.51
CRUD.L,CRUD.L,commodities_energy_etc,False,False,42.13
GDIG.L,GDIG.L,commodity_equity_mining,False,False,43.0
COPX.L,COPX.L,commodity_equity_mining,False,False,42.56
REMX.L,REMX.L,commodity_equity_mining,False,False,41.2
URNU.L,URNU.L,commodity_equity_uranium,False,False,37.49
URNM.L,URNM.L,commodity_equity_uranium,False,False,36.43
SPAG.L,SPAG.L,commodity_equity_agri,False,False,40.15
WOOD.L,WOOD.L,commodity_equity_timber,False,False,34.99
DPYA.L,DPYA.L,reit_global,False,False,40.49
GLRA.L,GLRA.L,reit_global,False,False,36.71
HPRD.L,HPRD.L,reit_global,False,False,40.52
EPRA.L,EPRA.L,reit_global,False,False,39.75
TRET.L,TRET.L,reit_global,False,False,36.78
IDUP.L,IDUP.L,reit_us,False,False,39.63
XRES.L,XRES.L,reit_us,False,False,44.93
IPRP.L,IPRP.L,reit_europe,False,False,39.51
XDER.L,XDER.L,reit_europe,False,False,37.62
IDAR.L,IDAR.L,reit_asia,False,False,35.09
IUKP.L,IUKP.L,reit_uk,False,False,43.05
IDIN.L,IDIN.L,infrastructure_global,False,False,40.84
XGID.L,XGID.L,infrastructure_global,False,False,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,False,False,37.41
PAVE.L,PAVE.L,infrastructure_us,False,False,38.56
MAGG.L,MAGG.L,multi_asset_growth,False,False,37.37
MAMG.L,MAMG.L,multi_asset_moderate,False,False,38.02
MACG.L,MACG.L,multi_asset_conservative,False,False,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,False,False,30.24
ACWD.L,ACWD.L,global,False,False,49.72
SPYY.L,SPYY.L,global,False,False,36.04
EXUS.L,EXUS.L,developed_ex_us,False,False,48.48

