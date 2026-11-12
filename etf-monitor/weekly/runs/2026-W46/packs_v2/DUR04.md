# Pillar DUR04: Share-class age
Definition: Years since the USD line launched, saturating at 5. The universe or issuer first date is preferred over yfinance fundInceptionDate.
Source: universe_ucits_*.csv first_date; iShares inception date; justETF profile inception (verified). Better when: higher, capped. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                      |   DUR04 | buyable   |   DUR04_score |   line_score |
|:-------|:----------|:---------------------------|--------:|:----------|--------------:|-------------:|
| SPYY.L | SPYY.L    | global                     | 2.19302 | False     |         36.87 |        36.04 |
| EXUS.L | EXUS.L    | developed_ex_us            | 2.68583 | False     |         44.78 |        48.48 |
| NTSX.L | NTSX.L    | multi_asset_efficient_core | 3.09103 | False     |         51.52 |        30.24 |
| NATO.L | NATO.L    | theme_defence              | 3.36208 | False     |         56.01 |        39.05 |
| FWRA.L | VWRA.L    | global                     | 3.38125 | False     |         21.27 |        48.74 |
| DFNS.L | DFNS.L    | theme_defence              | 3.61944 | False     |         60.18 |        42.49 |
| XNGI.L | XNGI.L    | theme_digital_tech         | 4.33676 | False     |         70.91 |        30.8  |
| SILV.L | SILV.L    | silver_miners              | 4.52019 | False     |         73.37 |        41.74 |
| URNM.L | URNM.L    | commodity_equity_uranium   | 4.52841 | False     |         73.48 |        36.43 |
| URNU.L | URNU.L    | commodity_equity_uranium   | 4.55852 | False     |         73.87 |        37.49 |
| HYUS.L | HYUS.L    | high-yield                 | 4.60507 | False     |         74.46 |        37.91 |
| COPX.L | COPX.L    | commodity_equity_mining    | 4.97194 | False     |         78.83 |        42.56 |
| BOTZ.L | BOTZ.L    | theme_ai_robotics          | 4.98836 | False     |         79.01 |        33.75 |
| PAVE.L | PAVE.L    | infrastructure_us          | 5.02669 | False     |         79.43 |        38.56 |
| REMX.L | REMX.L    | commodity_equity_mining    | 5.13347 | False     |         80.57 |        41.2  |
|        | cluster   | scope                             |   DUR04 | buyable   |   DUR04_score |   line_score |
|:-------|:----------|:----------------------------------|--------:|:----------|--------------:|-------------:|
| COPA.L | COPA.L    | commodities_industrial_metals_etc | 18.8611 | False     |         99.97 |        43.59 |
| IDTK.L | IDTK.L    | single_country                    | 18.8611 | False     |         99.97 |        34.39 |
| WFIN.L | WFIN.L    | sector_financials                 | 18.8611 | False     |         50    |        46.75 |
| XMJD.L | XMJD.L    | japan                             | 18.8611 | False     |         50    |        58.22 |
| IGLT.L | IGLT.L    | government                        | 18.8611 | False     |         99.97 |        55.37 |
| CRUD.L | CRUD.L    | commodities_energy_etc            | 18.8611 | False     |         99.97 |        42.13 |
| IDIN.L | IDIN.L    | infrastructure_global             | 18.8611 | False     |         99.97 |        40.84 |
| IDAR.L | IDAR.L    | reit_asia                         | 18.8611 | False     |         99.97 |        35.09 |
| AIGC.L | AIGC.L    | commodities_broad_etc             | 18.8611 | False     |         99.97 |        35.25 |
| PHAG.L | PHAG.L    | silver_physical_etc               | 18.8611 | False     |         50    |        37.57 |
| PHAU.L | PHAU.L    | gold_physical_etc                 | 18.8611 | False     |         50    |        36.69 |
| PHPM.L | PHPM.L    | precious_metals_basket_etc        | 18.8611 | False     |         99.97 |        38.29 |
| AIGI.L | AIGI.L    | commodities_industrial_metals_etc | 18.8611 | False     |         99.97 |        40.34 |
| INXG.L | INXG.L    | inflation-linked                  | 18.8611 | False     |         99.97 |        48.38 |
| IBCI.L | IBCI.L    | inflation-linked                  | 18.8611 | False     |         99.97 |        50.61 |

## All lines (csv)
,cluster,scope,DUR04,buyable,DUR04_score,line_score
IB01.L,IB01.L,government,7.72621492128679,False,95.89,55.34
VDST.L,VDST.L,government,6.193018480492813,False,89.37,56.33
IBTA.L,IBTA.L,government,9.582477754962357,False,98.77,56.49
CBU3.L,CBU3.L,government,16.0684462696783,False,99.97,49.56
XUT3.L,XUT3.L,government,17.349760438056126,False,99.97,46.44
TRE3.L,TRE3.L,government,7.835728952772074,False,96.17,48.81
US13.L,US13.L,government,15.94798083504449,False,99.97,49.83
CBU7.L,CBU7.L,government,16.019164955509925,False,99.97,55.46
CBU0.L,CBU0.L,government,15.682409308692677,False,99.97,57.53
TREX.L,TREX.L,government,7.835728952772074,False,96.17,50.59
US71.L,US71.L,government,10.48870636550308,False,99.33,50.86
DTLA.L,DTLA.L,government,8.509240246406572,False,97.52,56.46
US10.L,US10.L,government,8.046543463381246,False,96.66,48.53
VDTA.L,VDTA.L,government,7.728952772073922,False,95.9,54.89
XUTD.L,XUTD.L,government,17.349760438056126,False,99.97,48.42
TRES.L,TRES.L,government,7.835728952772074,False,96.17,49.65
TRSY.L,TRSY.L,government,15.444216290212184,False,99.97,51.52
IGLA.L,IGLA.L,government,9.065023956194388,False,98.28,43.86
XGGB.L,XGGB.L,government,13.245722108145106,False,99.89,39.18
IGLT.L,IGLT.L,government,18.86105407255305,False,99.97,55.37
IGLS.L,IGLS.L,government,17.571526351813826,False,99.97,55.3
SEGA.L,SEGA.L,government,17.571526351813826,False,99.97,51.69
XGLE.L,XGLE.L,government,17.248459958932237,False,99.97,50.27
AGGU.L,AGGU.L,aggregate,8.974674880219029,False,98.17,53.29
VAGU.L,VAGU.L,aggregate,7.403148528405202,False,94.96,52.19
GLAD.L,GLAD.L,aggregate,7.08829568788501,False,93.85,49.15
AGGG.L,AGGG.L,aggregate,8.974674880219029,False,98.17,50.77
GAGU.L,GAGU.L,aggregate,5.774127310061601,False,86.41,45.51
IUAA.L,IUAA.L,aggregate,9.582477754962357,False,98.77,46.09
USAG.L,USAG.L,aggregate,15.444216290212184,False,99.97,37.76
IDTP.L,IDTP.L,inflation-linked,18.86105407255305,False,99.97,51.6
TIP5.L,TIP5.L,inflation-linked,9.56331279945243,False,98.76,50.32
TIPU.L,TIPU.L,inflation-linked,10.288843258042435,False,99.23,46.67
TIPS.L,TIPS.L,inflation-linked,10.94592744695414,False,99.5,50.29
IGIL.L,IGIL.L,inflation-linked,18.272416153319643,False,99.97,42.21
XG7U.L,XG7U.L,inflation-linked,13.763175906913071,False,99.92,39.07
INXG.L,INXG.L,inflation-linked,18.86105407255305,False,99.97,48.38
IBCI.L,IBCI.L,inflation-linked,18.86105407255305,False,99.97,50.61
LQDA.L,LQDA.L,corporate,9.582477754962357,False,98.77,47.08
VDPA.L,VDPA.L,corporate,7.728952772073922,False,95.9,55.04
SDIA.L,SDIA.L,corporate,9.582477754962357,False,98.77,47.71
VDCA.L,VDCA.L,corporate,7.728952772073922,False,95.9,52.24
SUSU.L,SUSU.L,corporate,7.917864476386037,False,96.37,44.72
ICBU.L,ICBU.L,corporate,9.54962354551677,False,98.75,44.79
XDGU.L,XDGU.L,corporate,11.118412046543463,False,99.56,45.21
CRPU.L,CRPU.L,corporate,9.259411362080767,False,98.48,43.78
HLQD.L,HLQD.L,corporate,8.372347707049967,False,97.29,38.11
FLOA.L,FLOA.L,corporate,8.646132785763175,False,97.73,53.11
UCRP.L,UCRP.L,corporate,8.49555099247091,False,97.5,40.12
IEAA.L,IEAA.L,corporate,9.141683778234086,False,98.36,53.5
IHYA.L,IHYA.L,high-yield,9.582477754962357,False,98.77,43.09
HYLA.L,HYLA.L,high-yield,9.065023956194388,False,98.28,41.94
XUHY.L,XUHY.L,high-yield,8.763860369609857,False,97.9,38.81
HYUS.L,HYUS.L,high-yield,4.605065023956194,False,74.46,37.91
DHYA.L,DHYA.L,high-yield,6.992470910335387,False,93.47,38.55
WIAU.L,WIAU.L,high-yield,8.591375770020534,False,97.65,40.71
SJNK.L,SJNK.L,high-yield,13.14715947980835,False,99.88,35.96
HIGH.L,HIGH.L,high-yield,9.141683778234086,False,51.28,41.38
XHYG.L,HIGH.L,high-yield,8.988364134154688,False,48.72,51.8
JPEA.L,JPEA.L,em-debt,9.582477754962357,False,98.77,44.92
VDEA.L,VDEA.L,em-debt,7.728952772073922,False,95.9,42.08
EMSA.L,EMSA.L,em-debt,8.134154688569472,False,96.84,39.48
EMCA.L,EMCA.L,em-debt,8.451745379876797,False,97.43,43.87
EMGA.L,EMGA.L,em-debt,8.451745379876797,False,97.43,43.83
EMDD.L,EMDD.L,em-debt,15.49349760438056,False,99.97,39.95
EMLC.L,EMLC.L,em-debt,9.598904859685147,False,98.79,36.44
EMLB.L,EMLB.L,em-debt,15.148528405201915,False,99.97,36.59
ERNA.L,ERNA.L,money-market,8.372347707049967,False,97.29,54.21
JPSA.L,JPSA.L,money-market,7.611225188227242,False,95.58,41.89
ERNS.L,ERNS.L,money-market,13.073237508555785,False,99.88,54.59
XSTR.L,XSTR.L,money-market,17.859000684462696,False,99.97,47.73
ERNE.L,ERNE.L,money-market,13.073237508555785,False,99.88,50.97
VWRA.L,VWRA.L,global,7.307323750855578,True,78.73,52.93
ISAC.L,ACWD.L,global,15.06091718001369,False,50.0,49.57
IWDA.L,IWDA.L,global,17.130732375085557,False,64.29,51.14
XDWD.L,IWDA.L,global,12.309377138945928,False,23.05,50.13
SWRD.L,IWDA.L,global,7.709787816563997,False,1.38,51.37
HMWD.L,IWDA.L,global,15.926078028747432,False,64.29,50.13
FWRA.L,VWRA.L,global,3.381245722108145,False,21.27,48.74
VHVE.L,VHVE.L,global,7.134839151266256,False,94.03,49.78
WSML.L,WDSC.L,global,8.629705681040383,False,19.08,57.19
CSPX.L,XSPU.L,us,16.15879534565366,False,50.0,52.34
VUAA.L,XSPU.L,us,7.498973305954825,False,0.67,48.24
SPXS.L,XSPU.L,us,16.468172484599588,False,50.0,56.04
SPY5.L,XSPU.L,us,14.650239561943874,False,44.2,52.82
HSPD.L,XSPU.L,us,16.49828884325804,False,50.0,47.04
XSPU.L,XSPU.L,us,16.632443531827516,False,50.0,45.12
CNDX.L,CNDX.L,us,16.15879534565366,False,90.42,56.06
EQQU.L,CNDX.L,us,11.633127994524298,False,50.0,51.98
XNAS.L,CNDX.L,us,5.806981519507187,False,2.02,52.88
XDEW.L,XDEW.L,us,12.424366872005477,False,99.81,45.25
CSUS.L,CSUS.L,us,16.15879534565366,False,99.97,55.65
VNRA.L,VNRA.L,us,7.307323750855578,False,94.64,50.32
R2US.L,R2US.L,us,12.369609856262834,False,99.81,41.95
SPY4.L,SPY4.L,us,14.784394250513348,False,99.96,40.78
CUSS.L,CUSS.L,us,16.15879534565366,False,99.97,41.01
VEUA.L,VEUA.L,europe,7.307323750855578,False,94.64,53.64
VERG.L,VERG.L,europe,7.307323750855578,False,94.64,53.18
SMEA.L,SMEA.L,europe,17.130732375085557,False,99.97,53.99
IEUX.L,IEUX.L,europe,17.859000684462696,False,99.97,42.26
CSX5.L,CSX5.L,europe,16.15879534565366,False,99.97,54.36
XESC.L,XESC.L,europe,17.859000684462696,False,99.97,52.88
XDAX.L,XDAX.L,single_country,17.859000684462696,False,99.97,51.89
CACX.L,CACX.L,single_country,17.859000684462696,False,99.97,43.14
CSWG.L,CSWG.L,single_country,16.40520191649555,False,99.97,40.53
IAEX.L,IAEX.L,single_country,17.859000684462696,False,99.97,40.2
CUKX.L,CUKX.L,uk,16.15605749486653,False,99.97,56.68
VUKG.L,HUKX.L,uk,7.498973305954825,False,3.77,50.05
VMIG.L,MIDD.L,uk,7.498973305954825,False,3.07,50.69
MIDD.L,MIDD.L,uk,17.859000684462696,False,82.45,41.43
HUKX.L,HUKX.L,uk,17.218343600273784,False,85.33,50.86
CUKS.L,CUKS.L,uk,16.139630390143736,False,99.97,34.47
IJPA.L,IJPA.L,japan,17.130732375085557,False,99.97,49.67
CSJP.L,CSJP.L,japan,16.83504449007529,False,99.97,40.3
VJPA.L,VJPA.L,japan,7.134839151266256,False,94.03,46.36
XMJD.L,XMJD.L,japan,18.86105407255305,False,50.0,58.22
HMJD.L,XMJD.L,japan,15.926078028747432,False,50.0,45.61
LCJP.L,LCJP.L,japan,8.70362765229295,False,97.82,49.25
XDJP.L,XDJP.L,japan,13.796030116358658,False,99.93,49.3
IDJP.L,IDJP.L,japan,18.510609171800137,False,99.97,36.72
CPXJ.L,CPXJ.L,asia_pacific,16.123203285420946,False,99.97,46.93
VAPU.L,VAPU.L,asia_pacific,7.134839151266256,False,94.03,48.27
HMXJ.L,HMXJ.L,asia_pacific,16.18069815195072,False,99.97,38.25
XPXD.L,XPXD.L,asia_pacific,17.809719370294317,False,99.97,38.17
IFFF.L,IFFF.L,asia_pacific,17.859000684462696,False,99.97,42.22
HMAD.L,HMAD.L,asia_pacific,13.127994524298426,False,99.88,36.71
XMAD.L,XMAD.L,asia_pacific,17.859000684462696,False,99.97,37.77
EIMI.L,EIMI.L,emerging,12.454483230663929,False,99.82,50.71
VFEA.L,VFEA.L,emerging,7.134839151266256,False,94.03,48.22
IEMA.L,IEMA.L,emerging,17.130732375085557,False,99.97,50.65
XMME.L,XMMD.L,emerging,9.39356605065024,False,2.33,54.27
HMEM.L,XMMD.L,emerging,15.181382614647502,False,50.0,50.55
EMXC.L,EMXC.L,emerging,7.397672826830938,False,94.94,50.31
EMSD.L,EMSD.L,emerging,15.49349760438056,False,99.97,35.56
XMMD.L,XMMD.L,emerging,17.859000684462696,False,50.0,43.02
NDIA.L,XCS5.L,single_country,8.457221081451062,False,6.64,41.67
FLXI.L,FLXI.L,single_country,7.383983572895278,False,94.9,43.0
XCS5.L,XCS5.L,single_country,16.386036960985628,False,84.8,53.7
CNYA.L,CNYA.L,single_country,11.597535934291582,False,99.68,44.98
XCS6.L,XCS6.L,single_country,15.983572895277208,False,50.0,40.47
HMCD.L,XCS6.L,single_country,15.789185489390828,False,50.0,54.0
FXC.L,FXC.L,single_country,17.859000684462696,False,99.97,40.02
KWEB.L,KWEB.L,single_country,7.978097193702943,False,96.51,42.61
CSKR.L,CSKR.L,single_country,16.1533196440794,False,99.97,42.54
ITWN.L,ITWN.L,single_country,17.859000684462696,False,50.0,44.63
XMTD.L,ITWN.L,single_country,17.859000684462696,False,50.0,47.64
IBZL.L,IBZL.L,single_country,17.859000684462696,False,50.0,40.27
XMBD.L,IBZL.L,single_country,17.859000684462696,False,50.0,53.91
CMXC.L,CMXC.L,single_country,16.11772758384668,False,99.97,35.56
IKSA.L,IKSA.L,single_country,7.592060232717317,False,95.53,37.6
IRSA.L,IRSA.L,single_country,16.804928131416837,False,99.97,36.54
IDTK.L,IDTK.L,single_country,18.86105407255305,False,99.97,34.39
IAUS.L,IAUS.L,single_country,16.804928131416837,False,99.97,41.22
CCAU.L,CCAU.L,single_country,16.829568788501028,False,99.97,41.63
IPOL.L,IPOL.L,single_country,15.808350444900752,False,99.97,42.22
XVTD.L,XVTD.L,single_country,18.82546201232033,False,99.97,36.69
HIDD.L,HIDD.L,single_country,15.62217659137577,False,99.97,35.88
IWVL.L,IWVL.L,factor_value,12.101300479123887,False,99.77,47.48
IWQU.L,IWQU.L,factor_quality,12.101300479123887,False,99.77,44.24
IWMO.L,IWMO.L,factor_momentum,12.101300479123887,False,99.77,44.06
MVOL.L,MVOL.L,factor_min_vol,13.949349760438055,False,99.93,44.02
XDEV.L,XDEV.L,factor_value,12.16974674880219,False,99.78,44.48
XDEQ.L,XDEQ.L,factor_quality,12.16974674880219,False,99.78,40.36
XDEM.L,XDEM.L,factor_momentum,12.186173853524982,False,99.78,40.51
XDEB.L,XDEB.L,factor_min_vol,12.186173853524982,False,99.78,40.46
IUVL.L,IUVL.L,factor_value,10.080766598220396,False,99.12,46.43
IUQA.L,IUQA.L,factor_quality,10.080766598220396,False,99.12,44.79
IUMO.L,IUMO.L,factor_momentum,10.080766598220396,False,99.12,43.29
SPMV.L,SPMV.L,factor_min_vol,13.949349760438055,False,99.93,41.17
EMVL.L,EMVL.L,factor_value,7.934291581108829,False,96.41,44.13
IEFV.L,IEFV.L,factor_value,11.813826146475018,False,99.72,43.57
IEFQ.L,IEFQ.L,factor_quality,11.813826146475018,False,99.72,40.42
IEFM.L,IEFM.L,factor_momentum,11.813826146475018,False,99.72,41.08
JPGL.L,JPGL.L,factor_multi,7.345653661875428,False,94.77,38.53
MOAT.L,MOAT.L,factor_quality,11.07460643394935,False,99.54,36.86
WDSC.L,WDSC.L,size_small_cap,12.9637234770705,False,80.92,45.53
USSC.L,USSC.L,size_small_cap_value,11.731690622861054,False,99.7,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,12.101300479123887,False,99.77,37.07
SPEQ.L,SPEQ.L,equal_weight,5.601642710472279,False,85.0,42.26
VHYA.L,VHYD.L,dividend,7.134839151266256,False,10.77,48.01
VHYD.L,VHYD.L,dividend,13.478439425051334,False,89.23,50.34
FUSD.L,FUSD.L,dividend_quality,9.6290212183436,False,98.81,38.09
FGQI.L,FGQI.L,dividend_quality,9.6290212183436,False,98.81,37.29
GLDV.L,GLDV.L,dividend,13.49760438056126,False,99.91,39.83
UDVD.L,UDVD.L,dividend,15.080082135523616,False,99.97,41.58
WQDV.L,WQDV.L,dividend_quality,9.418206707734427,False,98.63,41.46
QDIV.L,QDIV.L,dividend_quality,12.435318275154003,False,99.81,37.32
TDIV.L,TDIV.L,dividend,10.472279260780288,False,99.32,44.59
HDLV.L,HDLV.L,dividend_low_vol,11.507186858316222,False,99.66,40.44
DGRA.L,DGRA.L,dividend_quality,10.442162902121837,False,99.3,38.48
GGRA.L,GGRA.L,dividend_quality,10.442162902121837,False,99.3,39.2
EUDV.L,EUDV.L,dividend,14.702258726899384,False,99.96,40.49
IDVY.L,IDVY.L,dividend,17.859000684462696,False,99.97,41.73
IUIT.L,IUIT.L,sector_tech,10.978781656399724,False,99.51,49.92
SXLK.L,SXLK.L,sector_tech,11.351129363449692,False,99.62,45.08
XLKS.L,XLKS.L,sector_tech,16.906228610540726,False,99.97,45.96
XDWT.L,XDWT.L,sector_tech,15.97262149212868,False,99.97,44.13
WTEC.L,WTEC.L,sector_tech,17.744010951403148,False,99.97,38.34
IUHC.L,IUHC.L,sector_health,10.978781656399724,False,99.51,49.63
SXLV.L,SXLV.L,sector_health,11.351129363449692,False,99.62,45.91
XLVS.L,XLVS.L,sector_health,16.906228610540726,False,99.97,44.01
XDWH.L,WHEA.L,sector_health,15.97262149212868,False,50.0,55.44
WHEA.L,WHEA.L,sector_health,17.713894592744694,False,50.0,47.22
IUFS.L,IUFS.L,sector_financials,10.978781656399724,False,99.51,47.69
SXLF.L,SXLF.L,sector_financials,11.351129363449692,False,99.62,41.53
XLFS.L,XLFS.L,sector_financials,16.906228610540726,False,99.97,40.07
XDWF.L,WFIN.L,sector_financials,15.97262149212868,False,50.0,55.81
WFIN.L,WFIN.L,sector_financials,18.86105407255305,False,50.0,46.75
IUES.L,IUES.L,sector_energy,10.978781656399724,False,99.51,48.23
SXLE.L,SXLE.L,sector_energy,11.351129363449692,False,99.62,45.52
XLES.L,XLES.L,sector_energy,16.906228610540726,False,99.97,41.55
XDW0.L,WNRG.L,sector_energy,15.97262149212868,False,50.0,55.0
WNRG.L,WNRG.L,sector_energy,17.782340862423,False,50.0,47.38
IOGP.L,IOGP.L,sector_energy,15.156741957563312,False,99.97,36.17
IUCD.L,IUCD.L,sector_consumer_disc,10.978781656399724,False,99.51,42.92
SXLY.L,SXLY.L,sector_consumer_disc,11.351129363449692,False,99.62,36.23
XDWC.L,WCOD.L,sector_consumer_disc,15.97262149212868,False,50.0,57.95
WCOD.L,WCOD.L,sector_consumer_disc,17.71663244353183,False,50.0,44.31
IUCS.L,IUCS.L,sector_consumer_staples,9.64271047227926,False,98.82,46.39
SXLP.L,SXLP.L,sector_consumer_staples,11.351129363449692,False,99.62,43.73
XDWS.L,XDWS.L,sector_consumer_staples,15.97262149212868,False,99.97,41.16
IUIS.L,IUIS.L,sector_industrials,9.64271047227926,False,98.82,45.18
SXLI.L,SXLI.L,sector_industrials,11.351129363449692,False,99.62,45.18
XDWI.L,XDWI.L,sector_industrials,15.97262149212868,False,99.97,41.14
IUUS.L,IUUS.L,sector_utilities,9.64271047227926,False,98.82,48.81
SXLU.L,SXLU.L,sector_utilities,11.351129363449692,False,99.62,42.66
XDWU.L,XDWU.L,sector_utilities,15.97262149212868,False,99.97,40.73
IUMS.L,IUMS.L,sector_materials,9.64271047227926,False,98.82,44.14
SXLB.L,SXLB.L,sector_materials,11.351129363449692,False,99.62,39.26
XDWM.L,XDWM.L,sector_materials,15.97262149212868,False,99.97,39.7
IUCM.L,IUCM.L,sector_communication,8.153319644079398,False,96.88,45.41
SXLC.L,SXLC.L,sector_communication,8.243668720054757,False,97.06,40.19
XWTS.L,XWTS.L,sector_communication,15.97262149212868,False,99.97,35.61
SMH.L,SMH.L,theme_semiconductors,5.946611909650924,False,87.7,45.19
SEMI.L,SEMI.L,theme_semiconductors,5.270362765229295,False,81.96,45.1
SEMU.L,SEMU.L,theme_semiconductors,7.720739219712525,False,95.88,39.52
AIAI.L,AIAI.L,theme_ai,7.381245722108145,False,94.89,41.8
WTAI.L,WTAI.L,theme_ai,7.950718685831622,False,96.44,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,4.988364134154689,False,79.01,33.75
RBOT.L,RBOT.L,theme_ai_robotics,10.17659137577002,False,99.17,43.84
ROBO.L,ROBO.L,theme_ai_robotics,12.05475701574264,False,99.76,39.93
DGTL.L,DGTL.L,theme_digital_tech,10.17659137577002,False,99.17,37.07
XNGI.L,XNGI.L,theme_digital_tech,4.336755646817249,False,70.91,30.8
ITEK.L,ITEK.L,theme_digital_tech,8.10403832991102,False,96.78,32.68
WCLD.L,WCLD.L,theme_cloud,7.19233401779603,False,94.24,38.24
LOCK.L,LOCK.L,theme_cybersecurity,8.180698151950718,False,96.93,41.54
USPY.L,USPY.L,theme_cybersecurity,11.137577002053389,False,99.56,40.83
WCBR.L,WCBR.L,theme_cybersecurity,5.796030116358659,False,86.58,36.33
HEAL.L,HEAL.L,theme_health_innovation,10.17659137577002,False,99.17,42.54
BTEC.L,BTEC.L,theme_biotech,9.065023956194388,False,98.28,43.97
SBIO.L,SBIO.L,theme_biotech,12.01368925393566,False,99.75,41.16
INRG.L,INRG.L,theme_clean_energy,17.859000684462696,False,99.97,41.88
RENW.L,RENW.L,theme_clean_energy,6.001368925393567,False,88.09,36.63
HTWO.L,HTWO.L,theme_clean_energy,5.752224503764545,False,86.23,35.08
ECAR.L,ECAR.L,theme_ev_battery,7.72621492128679,False,95.89,37.63
BATT.L,BATT.L,theme_ev_battery,8.815879534565367,False,97.97,37.85
IH2O.L,IH2O.L,theme_water,17.859000684462696,False,99.97,41.27
WATU.L,WATU.L,theme_water,17.859000684462696,False,99.97,38.39
GLUG.L,GLUG.L,theme_water,7.381245722108145,False,94.89,39.87
NATO.L,NATO.L,theme_defence,3.36208076659822,False,56.01,39.05
DFNS.L,DFNS.L,theme_defence,3.619438740588638,False,60.18,42.49
IGLN.L,PHAU.L,gold_physical_etc,15.597535934291582,False,50.0,54.79
SGLD.L,PHAU.L,gold_physical_etc,17.37987679671458,False,50.0,54.36
XGDU.L,XGDU.L,gold_physical_etc,6.557152635181383,False,91.46,48.98
WGLD.L,PHAU.L,gold_physical_etc,5.949349760438056,False,0.24,45.81
PHAU.L,PHAU.L,gold_physical_etc,18.86105407255305,False,50.0,36.69
SGBX.L,SGBX.L,gold_physical_etc,16.906228610540726,False,99.97,42.94
XGLD.L,PHAU.L,gold_physical_etc,16.410677618069816,False,50.0,34.54
RMAU.L,RMAU.L,gold_physical_etc,6.743326488706366,False,92.38,41.74
GDX.L,GDX.L,gold_miners,11.63586584531143,False,99.69,47.27
GDXJ.L,GDXJ.L,gold_miners,11.63586584531143,False,99.69,43.98
IAUP.L,IAUP.L,gold_miners,15.156741957563312,False,99.97,45.68
AUCO.L,AUCO.L,gold_miners,18.168377823408623,False,99.97,41.04
ISLN.L,PHAG.L,silver_physical_etc,15.597535934291582,False,50.0,55.13
SSLV.L,PHAG.L,silver_physical_etc,15.58384668035592,False,50.0,53.25
PHAG.L,PHAG.L,silver_physical_etc,18.86105407255305,False,50.0,37.57
SILV.L,SILV.L,silver_miners,4.520191649555099,False,73.37,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,18.86105407255305,False,99.97,38.29
IPLT.L,IPLT.L,platinum_physical_etc,15.597535934291582,False,99.97,42.09
IPDM.L,IPDM.L,palladium_physical_etc,15.597535934291582,False,99.97,41.44
CMOD.L,CMOD.L,commodities_broad,9.839835728952773,False,98.96,43.98
ICOM.L,ICOM.L,commodities_broad,9.319644079397673,False,98.54,45.76
BCOM.L,BCOM.L,commodities_broad,9.352498288843258,False,98.57,38.59
COMF.L,COMF.L,commodities_broad,16.66255989048597,False,99.97,36.88
ROLL.L,ROLL.L,commodities_broad,8.109514031485284,False,96.79,39.95
WCOA.L,WCOA.L,commodities_broad,10.543463381245722,False,99.35,38.51
ENCO.L,ENCO.L,commodities_broad,5.355236139630391,False,82.78,36.22
AIGC.L,AIGC.L,commodities_broad_etc,18.86105407255305,False,99.97,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,18.86105407255305,False,99.97,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,18.86105407255305,False,99.97,43.59
BRNT.L,BRNT.L,commodities_energy_etc,14.72142368240931,False,99.96,42.51
CRUD.L,CRUD.L,commodities_energy_etc,18.86105407255305,False,99.97,42.13
GDIG.L,GDIG.L,commodity_equity_mining,8.569472963723477,False,97.62,43.0
COPX.L,COPX.L,commodity_equity_mining,4.971937029431896,False,78.83,42.56
REMX.L,REMX.L,commodity_equity_mining,5.13347022587269,False,80.57,41.2
URNU.L,URNU.L,commodity_equity_uranium,4.558521560574949,False,73.87,37.49
URNM.L,URNM.L,commodity_equity_uranium,4.528405201916495,False,73.48,36.43
SPAG.L,SPAG.L,commodity_equity_agri,15.156741957563312,False,99.97,40.15
WOOD.L,WOOD.L,commodity_equity_timber,17.859000684462696,False,99.97,34.99
DPYA.L,DPYA.L,reit_global,8.509240246406572,False,97.52,40.49
GLRA.L,GLRA.L,reit_global,7.0746064339493495,False,93.8,36.71
HPRD.L,HPRD.L,reit_global,15.394934976043803,False,99.97,40.52
EPRA.L,EPRA.L,reit_global,10.001368925393566,False,99.07,39.75
TRET.L,TRET.L,reit_global,15.679671457905544,False,99.97,36.78
IDUP.L,IDUP.L,reit_us,17.859000684462696,False,99.97,39.63
XRES.L,XRES.L,reit_us,10.735112936344969,False,99.43,44.93
IPRP.L,IPRP.L,reit_europe,17.859000684462696,False,99.97,39.51
XDER.L,XDER.L,reit_europe,16.635181382614647,False,99.97,37.62
IDAR.L,IDAR.L,reit_asia,18.86105407255305,False,99.97,35.09
IUKP.L,IUKP.L,reit_uk,17.859000684462696,False,99.97,43.05
IDIN.L,IDIN.L,infrastructure_global,18.86105407255305,False,99.97,40.84
XGID.L,XGID.L,infrastructure_global,18.82546201232033,False,99.97,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,11.58110882956879,False,99.67,37.41
PAVE.L,PAVE.L,infrastructure_us,5.026694045174538,False,79.43,38.56
MAGG.L,MAGG.L,multi_asset_growth,6.160164271047228,False,89.16,37.37
MAMG.L,MAMG.L,multi_asset_moderate,6.160164271047228,False,89.16,38.02
MACG.L,MACG.L,multi_asset_conservative,6.160164271047228,False,89.16,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,3.0910335386721424,False,51.52,30.24
ACWD.L,ACWD.L,global,15.49349760438056,False,50.0,56.16
SPYY.L,SPYY.L,global,2.193018480492813,False,36.87,36.04
EXUS.L,EXUS.L,developed_ex_us,2.6858316221765914,False,44.78,48.48

