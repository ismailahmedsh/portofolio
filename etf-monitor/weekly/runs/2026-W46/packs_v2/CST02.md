# Pillar CST02: Tracking beyond TER, relative to the sleeve reference line (fails closed)
Definition: First compute G_i, the annualised gap between line i's USD LSE total return and the same-index reference line's over at least 3 years (5 where available), using 20-day average prices at both ends. Restate it at current TERs: G_i = gap_raw_i + (TERbar_i - TERnow_i) - (TERbar_ref - TERnow_ref), where TERbar is the time-weighted TER actually charged, from ter_history.
Then CST02_i = G_i + (TERnow_i - TERnow_ref): the tracking edge beyond TER, so that TER itself is scored only in CST01. It is shrunk toward 0 by its standard error.
Fails closed: CST02 is missing for the whole sleeve unless ter_history has a dated, sourced seed entry for every line in the sleeve covering the whole window. Lines on different indices are never compared.
Source: yfinance .L daily closes (verified for all issuers); ter_history seeded from annual reports (CST01); iShares UK performance tables for the reference line's absolute tracking difference | STATUS: verified for iShares-only sleeves; unverified and fails closed for Vanguard, Invesco and Xtrackers lines until ter_history is seeded from another source (justETF snapshots from now on, or annual reports via the Central Bank of Ireland register) (unverified). Better when: higher. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                |   CST02_raw_gap_bps | buyable   |   line_score |
|:-------|:----------|:---------------------|--------------------:|:----------|-------------:|
| ISAC.L | ACWD.L    | global               |           -18.8238  | False     |        49.57 |
| VUAA.L | XSPU.L    | us                   |           -12.0101  | False     |        48.24 |
| HMEM.L | XMMD.L    | emerging             |           -11.4651  | False     |        50.55 |
| CSPX.L | XSPU.L    | us                   |            -9.91171 | False     |        52.34 |
| HSPD.L | XSPU.L    | us                   |            -7.45021 | False     |        47.04 |
| VHYA.L | VHYD.L    | dividend             |            -5.84042 | False     |        48.01 |
| SPY5.L | XSPU.L    | us                   |            -5.60689 | False     |        52.82 |
| XDWH.L | WHEA.L    | sector_health        |             2.73577 | False     |        55.44 |
| HMWD.L | IWDA.L    | global               |             3.48499 | False     |        50.13 |
| XDWC.L | WCOD.L    | sector_consumer_disc |             3.78869 | False     |        57.95 |
| XHYG.L | HIGH.L    | high-yield           |             4.68686 | False     |        51.8  |
| XDW0.L | WNRG.L    | sector_energy        |             5.39802 | False     |        55    |
| EQQU.L | CNDX.L    | us                   |             6.25532 | False     |        51.98 |
| XDWD.L | IWDA.L    | global               |             8.98801 | False     |        50.13 |
| SPXS.L | XSPU.L    | us                   |             9.72646 | False     |        56.04 |
|        | cluster   | scope                             |   CST02_raw_gap_bps | buyable   |   line_score |
|:-------|:----------|:----------------------------------|--------------------:|:----------|-------------:|
| IPRP.L | IPRP.L    | reit_europe                       |                 nan | False     |        39.51 |
| XDER.L | XDER.L    | reit_europe                       |                 nan | False     |        37.62 |
| IDAR.L | IDAR.L    | reit_asia                         |                 nan | False     |        35.09 |
| IUKP.L | IUKP.L    | reit_uk                           |                 nan | False     |        43.05 |
| IDIN.L | IDIN.L    | infrastructure_global             |                 nan | False     |        40.84 |
| XGID.L | XGID.L    | infrastructure_global             |                 nan | False     |        37.32 |
| GIN.L  | GIN.L     | infrastructure_global_multi_asset |                 nan | False     |        37.41 |
| PAVE.L | PAVE.L    | infrastructure_us                 |                 nan | False     |        38.56 |
| MAGG.L | MAGG.L    | multi_asset_growth                |                 nan | False     |        37.37 |
| MAMG.L | MAMG.L    | multi_asset_moderate              |                 nan | False     |        38.02 |
| MACG.L | MACG.L    | multi_asset_conservative          |                 nan | False     |        38.44 |
| NTSX.L | NTSX.L    | multi_asset_efficient_core        |                 nan | False     |        30.24 |
| ACWD.L | ACWD.L    | global                            |                 nan | False     |        56.16 |
| SPYY.L | SPYY.L    | global                            |                 nan | False     |        36.04 |
| EXUS.L | EXUS.L    | developed_ex_us                   |                 nan | False     |        48.48 |

## All lines (csv)
,cluster,scope,CST02_raw_gap_bps,buyable,line_score
IB01.L,IB01.L,government,,False,55.34
VDST.L,VDST.L,government,,False,56.33
IBTA.L,IBTA.L,government,,False,56.49
CBU3.L,CBU3.L,government,,False,49.56
XUT3.L,XUT3.L,government,,False,46.44
TRE3.L,TRE3.L,government,,False,48.81
US13.L,US13.L,government,,False,49.83
CBU7.L,CBU7.L,government,,False,55.46
CBU0.L,CBU0.L,government,,False,57.53
TREX.L,TREX.L,government,,False,50.59
US71.L,US71.L,government,,False,50.86
DTLA.L,DTLA.L,government,,False,56.46
US10.L,US10.L,government,,False,48.53
VDTA.L,VDTA.L,government,,False,54.89
XUTD.L,XUTD.L,government,,False,48.42
TRES.L,TRES.L,government,,False,49.65
TRSY.L,TRSY.L,government,,False,51.52
IGLA.L,IGLA.L,government,,False,43.86
XGGB.L,XGGB.L,government,,False,39.18
IGLT.L,IGLT.L,government,,False,55.37
IGLS.L,IGLS.L,government,,False,55.3
SEGA.L,SEGA.L,government,,False,51.69
XGLE.L,XGLE.L,government,,False,50.27
AGGU.L,AGGU.L,aggregate,,False,53.29
VAGU.L,VAGU.L,aggregate,,False,52.19
GLAD.L,GLAD.L,aggregate,,False,49.15
AGGG.L,AGGG.L,aggregate,,False,50.77
GAGU.L,GAGU.L,aggregate,,False,45.51
IUAA.L,IUAA.L,aggregate,,False,46.09
USAG.L,USAG.L,aggregate,,False,37.76
IDTP.L,IDTP.L,inflation-linked,,False,51.6
TIP5.L,TIP5.L,inflation-linked,,False,50.32
TIPU.L,TIPU.L,inflation-linked,,False,46.67
TIPS.L,TIPS.L,inflation-linked,,False,50.29
IGIL.L,IGIL.L,inflation-linked,,False,42.21
XG7U.L,XG7U.L,inflation-linked,,False,39.07
INXG.L,INXG.L,inflation-linked,,False,48.38
IBCI.L,IBCI.L,inflation-linked,,False,50.61
LQDA.L,LQDA.L,corporate,,False,47.08
VDPA.L,VDPA.L,corporate,,False,55.04
SDIA.L,SDIA.L,corporate,,False,47.71
VDCA.L,VDCA.L,corporate,,False,52.24
SUSU.L,SUSU.L,corporate,,False,44.72
ICBU.L,ICBU.L,corporate,,False,44.79
XDGU.L,XDGU.L,corporate,,False,45.21
CRPU.L,CRPU.L,corporate,,False,43.78
HLQD.L,HLQD.L,corporate,,False,38.11
FLOA.L,FLOA.L,corporate,,False,53.11
UCRP.L,UCRP.L,corporate,,False,40.12
IEAA.L,IEAA.L,corporate,,False,53.5
IHYA.L,IHYA.L,high-yield,,False,43.09
HYLA.L,HYLA.L,high-yield,,False,41.94
XUHY.L,XUHY.L,high-yield,,False,38.81
HYUS.L,HYUS.L,high-yield,,False,37.91
DHYA.L,DHYA.L,high-yield,,False,38.55
WIAU.L,WIAU.L,high-yield,,False,40.71
SJNK.L,SJNK.L,high-yield,,False,35.96
HIGH.L,HIGH.L,high-yield,,False,41.38
XHYG.L,HIGH.L,high-yield,4.686855770206222,False,51.8
JPEA.L,JPEA.L,em-debt,,False,44.92
VDEA.L,VDEA.L,em-debt,,False,42.08
EMSA.L,EMSA.L,em-debt,,False,39.48
EMCA.L,EMCA.L,em-debt,,False,43.87
EMGA.L,EMGA.L,em-debt,,False,43.83
EMDD.L,EMDD.L,em-debt,,False,39.95
EMLC.L,EMLC.L,em-debt,,False,36.44
EMLB.L,EMLB.L,em-debt,,False,36.59
ERNA.L,ERNA.L,money-market,,False,54.21
JPSA.L,JPSA.L,money-market,,False,41.89
ERNS.L,ERNS.L,money-market,,False,54.59
XSTR.L,XSTR.L,money-market,,False,47.73
ERNE.L,ERNE.L,money-market,,False,50.97
VWRA.L,VWRA.L,global,,True,52.93
ISAC.L,ACWD.L,global,-18.82381705738512,False,49.57
IWDA.L,IWDA.L,global,,False,51.14
XDWD.L,IWDA.L,global,8.988006103802793,False,50.13
SWRD.L,IWDA.L,global,14.36354577242005,False,51.37
HMWD.L,IWDA.L,global,3.484991085123124,False,50.13
FWRA.L,VWRA.L,global,12.55310419397082,False,48.74
VHVE.L,VHVE.L,global,,False,49.78
WSML.L,WDSC.L,global,21.635761846197088,False,57.19
CSPX.L,XSPU.L,us,-9.911706608460856,False,52.34
VUAA.L,XSPU.L,us,-12.010137462934445,False,48.24
SPXS.L,XSPU.L,us,9.726455304857051,False,56.04
SPY5.L,XSPU.L,us,-5.606892292318033,False,52.82
HSPD.L,XSPU.L,us,-7.450206073622567,False,47.04
XSPU.L,XSPU.L,us,,False,45.12
CNDX.L,CNDX.L,us,,False,56.06
EQQU.L,CNDX.L,us,6.25531929562495,False,51.98
XNAS.L,CNDX.L,us,15.314251892442066,False,52.88
XDEW.L,XDEW.L,us,,False,45.25
CSUS.L,CSUS.L,us,,False,55.65
VNRA.L,VNRA.L,us,,False,50.32
R2US.L,R2US.L,us,,False,41.95
SPY4.L,SPY4.L,us,,False,40.78
CUSS.L,CUSS.L,us,,False,41.01
VEUA.L,VEUA.L,europe,,False,53.64
VERG.L,VERG.L,europe,,False,53.18
SMEA.L,SMEA.L,europe,,False,53.99
IEUX.L,IEUX.L,europe,,False,42.26
CSX5.L,CSX5.L,europe,,False,54.36
XESC.L,XESC.L,europe,,False,52.88
XDAX.L,XDAX.L,single_country,,False,51.89
CACX.L,CACX.L,single_country,,False,43.14
CSWG.L,CSWG.L,single_country,,False,40.53
IAEX.L,IAEX.L,single_country,,False,40.2
CUKX.L,CUKX.L,uk,,False,56.68
VUKG.L,HUKX.L,uk,436.26995717104046,False,50.05
VMIG.L,MIDD.L,uk,456.2425465055253,False,50.69
MIDD.L,MIDD.L,uk,,False,41.43
HUKX.L,HUKX.L,uk,,False,50.86
CUKS.L,CUKS.L,uk,,False,34.47
IJPA.L,IJPA.L,japan,,False,49.67
CSJP.L,CSJP.L,japan,,False,40.3
VJPA.L,VJPA.L,japan,,False,46.36
XMJD.L,XMJD.L,japan,,False,58.22
HMJD.L,XMJD.L,japan,24.02388254167498,False,45.61
LCJP.L,LCJP.L,japan,,False,49.25
XDJP.L,XDJP.L,japan,,False,49.3
IDJP.L,IDJP.L,japan,,False,36.72
CPXJ.L,CPXJ.L,asia_pacific,,False,46.93
VAPU.L,VAPU.L,asia_pacific,,False,48.27
HMXJ.L,HMXJ.L,asia_pacific,,False,38.25
XPXD.L,XPXD.L,asia_pacific,,False,38.17
IFFF.L,IFFF.L,asia_pacific,,False,42.22
HMAD.L,HMAD.L,asia_pacific,,False,36.71
XMAD.L,XMAD.L,asia_pacific,,False,37.77
EIMI.L,EIMI.L,emerging,,False,50.71
VFEA.L,VFEA.L,emerging,,False,48.22
IEMA.L,IEMA.L,emerging,,False,50.65
XMME.L,XMMD.L,emerging,10.110205310771558,False,54.27
HMEM.L,XMMD.L,emerging,-11.465110747197471,False,50.55
EMXC.L,EMXC.L,emerging,,False,50.31
EMSD.L,EMSD.L,emerging,,False,35.56
XMMD.L,XMMD.L,emerging,,False,43.02
NDIA.L,XCS5.L,single_country,52.34529710810287,False,41.67
FLXI.L,FLXI.L,single_country,,False,43.0
XCS5.L,XCS5.L,single_country,,False,53.7
CNYA.L,CNYA.L,single_country,,False,44.98
XCS6.L,XCS6.L,single_country,,False,40.47
HMCD.L,XCS6.L,single_country,87.1829322584361,False,54.0
FXC.L,FXC.L,single_country,,False,40.02
KWEB.L,KWEB.L,single_country,,False,42.61
CSKR.L,CSKR.L,single_country,,False,42.54
ITWN.L,ITWN.L,single_country,,False,44.63
XMTD.L,ITWN.L,single_country,249.39772324378492,False,47.64
IBZL.L,IBZL.L,single_country,,False,40.27
XMBD.L,IBZL.L,single_country,472.2506983130059,False,53.91
CMXC.L,CMXC.L,single_country,,False,35.56
IKSA.L,IKSA.L,single_country,,False,37.6
IRSA.L,IRSA.L,single_country,,False,36.54
IDTK.L,IDTK.L,single_country,,False,34.39
IAUS.L,IAUS.L,single_country,,False,41.22
CCAU.L,CCAU.L,single_country,,False,41.63
IPOL.L,IPOL.L,single_country,,False,42.22
XVTD.L,XVTD.L,single_country,,False,36.69
HIDD.L,HIDD.L,single_country,,False,35.88
IWVL.L,IWVL.L,factor_value,,False,47.48
IWQU.L,IWQU.L,factor_quality,,False,44.24
IWMO.L,IWMO.L,factor_momentum,,False,44.06
MVOL.L,MVOL.L,factor_min_vol,,False,44.02
XDEV.L,XDEV.L,factor_value,,False,44.48
XDEQ.L,XDEQ.L,factor_quality,,False,40.36
XDEM.L,XDEM.L,factor_momentum,,False,40.51
XDEB.L,XDEB.L,factor_min_vol,,False,40.46
IUVL.L,IUVL.L,factor_value,,False,46.43
IUQA.L,IUQA.L,factor_quality,,False,44.79
IUMO.L,IUMO.L,factor_momentum,,False,43.29
SPMV.L,SPMV.L,factor_min_vol,,False,41.17
EMVL.L,EMVL.L,factor_value,,False,44.13
IEFV.L,IEFV.L,factor_value,,False,43.57
IEFQ.L,IEFQ.L,factor_quality,,False,40.42
IEFM.L,IEFM.L,factor_momentum,,False,41.08
JPGL.L,JPGL.L,factor_multi,,False,38.53
MOAT.L,MOAT.L,factor_quality,,False,36.86
WDSC.L,WDSC.L,size_small_cap,,False,45.53
USSC.L,USSC.L,size_small_cap_value,,False,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,,False,37.07
SPEQ.L,SPEQ.L,equal_weight,,False,42.26
VHYA.L,VHYD.L,dividend,-5.840420016618442,False,48.01
VHYD.L,VHYD.L,dividend,,False,50.34
FUSD.L,FUSD.L,dividend_quality,,False,38.09
FGQI.L,FGQI.L,dividend_quality,,False,37.29
GLDV.L,GLDV.L,dividend,,False,39.83
UDVD.L,UDVD.L,dividend,,False,41.58
WQDV.L,WQDV.L,dividend_quality,,False,41.46
QDIV.L,QDIV.L,dividend_quality,,False,37.32
TDIV.L,TDIV.L,dividend,,False,44.59
HDLV.L,HDLV.L,dividend_low_vol,,False,40.44
DGRA.L,DGRA.L,dividend_quality,,False,38.48
GGRA.L,GGRA.L,dividend_quality,,False,39.2
EUDV.L,EUDV.L,dividend,,False,40.49
IDVY.L,IDVY.L,dividend,,False,41.73
IUIT.L,IUIT.L,sector_tech,,False,49.92
SXLK.L,SXLK.L,sector_tech,,False,45.08
XLKS.L,XLKS.L,sector_tech,,False,45.96
XDWT.L,XDWT.L,sector_tech,,False,44.13
WTEC.L,WTEC.L,sector_tech,,False,38.34
IUHC.L,IUHC.L,sector_health,,False,49.63
SXLV.L,SXLV.L,sector_health,,False,45.91
XLVS.L,XLVS.L,sector_health,,False,44.01
XDWH.L,WHEA.L,sector_health,2.735768618022938,False,55.44
WHEA.L,WHEA.L,sector_health,,False,47.22
IUFS.L,IUFS.L,sector_financials,,False,47.69
SXLF.L,SXLF.L,sector_financials,,False,41.53
XLFS.L,XLFS.L,sector_financials,,False,40.07
XDWF.L,WFIN.L,sector_financials,15.350369437869826,False,55.81
WFIN.L,WFIN.L,sector_financials,,False,46.75
IUES.L,IUES.L,sector_energy,,False,48.23
SXLE.L,SXLE.L,sector_energy,,False,45.52
XLES.L,XLES.L,sector_energy,,False,41.55
XDW0.L,WNRG.L,sector_energy,5.398020082258981,False,55.0
WNRG.L,WNRG.L,sector_energy,,False,47.38
IOGP.L,IOGP.L,sector_energy,,False,36.17
IUCD.L,IUCD.L,sector_consumer_disc,,False,42.92
SXLY.L,SXLY.L,sector_consumer_disc,,False,36.23
XDWC.L,WCOD.L,sector_consumer_disc,3.78868901438123,False,57.95
WCOD.L,WCOD.L,sector_consumer_disc,,False,44.31
IUCS.L,IUCS.L,sector_consumer_staples,,False,46.39
SXLP.L,SXLP.L,sector_consumer_staples,,False,43.73
XDWS.L,XDWS.L,sector_consumer_staples,,False,41.16
IUIS.L,IUIS.L,sector_industrials,,False,45.18
SXLI.L,SXLI.L,sector_industrials,,False,45.18
XDWI.L,XDWI.L,sector_industrials,,False,41.14
IUUS.L,IUUS.L,sector_utilities,,False,48.81
SXLU.L,SXLU.L,sector_utilities,,False,42.66
XDWU.L,XDWU.L,sector_utilities,,False,40.73
IUMS.L,IUMS.L,sector_materials,,False,44.14
SXLB.L,SXLB.L,sector_materials,,False,39.26
XDWM.L,XDWM.L,sector_materials,,False,39.7
IUCM.L,IUCM.L,sector_communication,,False,45.41
SXLC.L,SXLC.L,sector_communication,,False,40.19
XWTS.L,XWTS.L,sector_communication,,False,35.61
SMH.L,SMH.L,theme_semiconductors,,False,45.19
SEMI.L,SEMI.L,theme_semiconductors,,False,45.1
SEMU.L,SEMU.L,theme_semiconductors,,False,39.52
AIAI.L,AIAI.L,theme_ai,,False,41.8
WTAI.L,WTAI.L,theme_ai,,False,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,,False,33.75
RBOT.L,RBOT.L,theme_ai_robotics,,False,43.84
ROBO.L,ROBO.L,theme_ai_robotics,,False,39.93
DGTL.L,DGTL.L,theme_digital_tech,,False,37.07
XNGI.L,XNGI.L,theme_digital_tech,,False,30.8
ITEK.L,ITEK.L,theme_digital_tech,,False,32.68
WCLD.L,WCLD.L,theme_cloud,,False,38.24
LOCK.L,LOCK.L,theme_cybersecurity,,False,41.54
USPY.L,USPY.L,theme_cybersecurity,,False,40.83
WCBR.L,WCBR.L,theme_cybersecurity,,False,36.33
HEAL.L,HEAL.L,theme_health_innovation,,False,42.54
BTEC.L,BTEC.L,theme_biotech,,False,43.97
SBIO.L,SBIO.L,theme_biotech,,False,41.16
INRG.L,INRG.L,theme_clean_energy,,False,41.88
RENW.L,RENW.L,theme_clean_energy,,False,36.63
HTWO.L,HTWO.L,theme_clean_energy,,False,35.08
ECAR.L,ECAR.L,theme_ev_battery,,False,37.63
BATT.L,BATT.L,theme_ev_battery,,False,37.85
IH2O.L,IH2O.L,theme_water,,False,41.27
WATU.L,WATU.L,theme_water,,False,38.39
GLUG.L,GLUG.L,theme_water,,False,39.87
NATO.L,NATO.L,theme_defence,,False,39.05
DFNS.L,DFNS.L,theme_defence,,False,42.49
IGLN.L,PHAU.L,gold_physical_etc,28.92208463552537,False,54.79
SGLD.L,PHAU.L,gold_physical_etc,29.78487853502409,False,54.36
XGDU.L,XGDU.L,gold_physical_etc,,False,48.98
WGLD.L,PHAU.L,gold_physical_etc,31.088194836452757,False,45.81
PHAU.L,PHAU.L,gold_physical_etc,,False,36.69
SGBX.L,SGBX.L,gold_physical_etc,,False,42.94
XGLD.L,PHAU.L,gold_physical_etc,20.443268370835543,False,34.54
RMAU.L,RMAU.L,gold_physical_etc,,False,41.74
GDX.L,GDX.L,gold_miners,,False,47.27
GDXJ.L,GDXJ.L,gold_miners,,False,43.98
IAUP.L,IAUP.L,gold_miners,,False,45.68
AUCO.L,AUCO.L,gold_miners,,False,41.04
ISLN.L,PHAG.L,silver_physical_etc,15.752877234214148,False,55.13
SSLV.L,PHAG.L,silver_physical_etc,23.606372892817085,False,53.25
PHAG.L,PHAG.L,silver_physical_etc,,False,37.57
SILV.L,SILV.L,silver_miners,,False,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,,False,38.29
IPLT.L,IPLT.L,platinum_physical_etc,,False,42.09
IPDM.L,IPDM.L,palladium_physical_etc,,False,41.44
CMOD.L,CMOD.L,commodities_broad,,False,43.98
ICOM.L,ICOM.L,commodities_broad,,False,45.76
BCOM.L,BCOM.L,commodities_broad,,False,38.59
COMF.L,COMF.L,commodities_broad,,False,36.88
ROLL.L,ROLL.L,commodities_broad,,False,39.95
WCOA.L,WCOA.L,commodities_broad,,False,38.51
ENCO.L,ENCO.L,commodities_broad,,False,36.22
AIGC.L,AIGC.L,commodities_broad_etc,,False,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,,False,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,,False,43.59
BRNT.L,BRNT.L,commodities_energy_etc,,False,42.51
CRUD.L,CRUD.L,commodities_energy_etc,,False,42.13
GDIG.L,GDIG.L,commodity_equity_mining,,False,43.0
COPX.L,COPX.L,commodity_equity_mining,,False,42.56
REMX.L,REMX.L,commodity_equity_mining,,False,41.2
URNU.L,URNU.L,commodity_equity_uranium,,False,37.49
URNM.L,URNM.L,commodity_equity_uranium,,False,36.43
SPAG.L,SPAG.L,commodity_equity_agri,,False,40.15
WOOD.L,WOOD.L,commodity_equity_timber,,False,34.99
DPYA.L,DPYA.L,reit_global,,False,40.49
GLRA.L,GLRA.L,reit_global,,False,36.71
HPRD.L,HPRD.L,reit_global,,False,40.52
EPRA.L,EPRA.L,reit_global,,False,39.75
TRET.L,TRET.L,reit_global,,False,36.78
IDUP.L,IDUP.L,reit_us,,False,39.63
XRES.L,XRES.L,reit_us,,False,44.93
IPRP.L,IPRP.L,reit_europe,,False,39.51
XDER.L,XDER.L,reit_europe,,False,37.62
IDAR.L,IDAR.L,reit_asia,,False,35.09
IUKP.L,IUKP.L,reit_uk,,False,43.05
IDIN.L,IDIN.L,infrastructure_global,,False,40.84
XGID.L,XGID.L,infrastructure_global,,False,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,,False,37.41
PAVE.L,PAVE.L,infrastructure_us,,False,38.56
MAGG.L,MAGG.L,multi_asset_growth,,False,37.37
MAMG.L,MAMG.L,multi_asset_moderate,,False,38.02
MACG.L,MACG.L,multi_asset_conservative,,False,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,,False,30.24
ACWD.L,ACWD.L,global,,False,56.16
SPYY.L,SPYY.L,global,,False,36.04
EXUS.L,EXUS.L,developed_ex_us,,False,48.48

