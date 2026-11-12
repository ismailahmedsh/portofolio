# Pillar DUR01: Fund and share-class size
Definition: min(fund AUM, 5 x share-class AUM) where the share-class AUM is known, otherwise fund AUM, in US$ at the same date's FX, log-scaled from US$50m and saturating at US$5bn.
Source: iShares UK net assets of fund and of share class; justETF fund size converted to USD (e.g. VWRA EUR 56.3bn); yfinance totalAssets (VUAA US$89.0bn, EXUS US$8.2bn); reconciled by ELG10 below US$5bn only (verified). Better when: higher, capped. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                      |   DUR01 | buyable   |   DUR01_score |   line_score |
|:-------|:----------|:---------------------------|--------:|:----------|--------------:|-------------:|
| SPYY.L | SPYY.L    | global                     | 6.93357 | False     |          1.58 |        36.04 |
| NTSX.L | NTSX.L    | multi_asset_efficient_core | 7.35484 | False     |          3.59 |        30.24 |
| SXLB.L | SXLB.L    | sector_materials           | 7.76205 | False     |          7.76 |        39.26 |
| WCOD.L | WCOD.L    | sector_consumer_disc       | 7.76367 | False     |         31.76 |        44.31 |
| XNGI.L | XNGI.L    | theme_digital_tech         | 7.85849 | False     |          9.25 |        30.8  |
| WOOD.L | WOOD.L    | commodity_equity_timber    | 7.8989  | False     |          9.96 |        34.99 |
| CUKS.L | CUKS.L    | uk                         | 7.96921 | False     |         11.29 |        34.47 |
| IDTK.L | IDTK.L    | single_country             | 8.00794 | False     |         12.09 |        34.39 |
| ITEK.L | ITEK.L    | theme_digital_tech         | 8.03846 | False     |         12.75 |        32.68 |
| CMXC.L | CMXC.L    | single_country             | 8.06624 | False     |         13.38 |        35.56 |
| SXLY.L | SXLY.L    | sector_consumer_disc       | 8.12658 | False     |         14.84 |        36.23 |
| XRES.L | XRES.L    | reit_us                    | 8.13175 | False     |         14.98 |        44.93 |
| XLES.L | XLES.L    | sector_energy              | 8.18926 | False     |         16.5  |        41.55 |
| BOTZ.L | BOTZ.L    | theme_ai_robotics          | 8.19481 | False     |         16.65 |        33.75 |
| USAG.L | USAG.L    | aggregate                  | 8.23364 | False     |         17.76 |        37.76 |
|        | cluster   | scope                             |   DUR01 | buyable   |   DUR01_score |   line_score |
|:-------|:----------|:----------------------------------|--------:|:----------|--------------:|-------------:|
| ENCO.L | ENCO.L    | commodities_broad                 |     nan | False     |           nan |        36.22 |
| AIGC.L | AIGC.L    | commodities_broad_etc             |     nan | False     |           nan |        35.25 |
| AIGI.L | AIGI.L    | commodities_industrial_metals_etc |     nan | False     |           nan |        40.34 |
| COPA.L | COPA.L    | commodities_industrial_metals_etc |     nan | False     |           nan |        43.59 |
| BRNT.L | BRNT.L    | commodities_energy_etc            |     nan | False     |           nan |        42.51 |
| CRUD.L | CRUD.L    | commodities_energy_etc            |     nan | False     |           nan |        42.13 |
| DPYA.L | DPYA.L    | reit_global                       |     nan | False     |           nan |        40.49 |
| HPRD.L | HPRD.L    | reit_global                       |     nan | False     |           nan |        40.52 |
| EPRA.L | EPRA.L    | reit_global                       |     nan | False     |           nan |        39.75 |
| IUKP.L | IUKP.L    | reit_uk                           |     nan | False     |           nan |        43.05 |
| IDIN.L | IDIN.L    | infrastructure_global             |     nan | False     |           nan |        40.84 |
| MAGG.L | MAGG.L    | multi_asset_growth                |     nan | False     |           nan |        37.37 |
| MAMG.L | MAMG.L    | multi_asset_moderate              |     nan | False     |           nan |        38.02 |
| MACG.L | MACG.L    | multi_asset_conservative          |     nan | False     |           nan |        38.44 |
| ACWD.L | ACWD.L    | global                            |     nan | False     |           nan |        56.16 |

## All lines (csv)
,cluster,scope,DUR01,buyable,DUR01_score,line_score
IB01.L,IB01.L,government,,False,,55.34
VDST.L,VDST.L,government,,False,,56.33
IBTA.L,IBTA.L,government,,False,,56.49
CBU3.L,CBU3.L,government,8.839659983047842,False,42.05,49.56
XUT3.L,XUT3.L,government,8.257038130367063,False,18.45,46.44
TRE3.L,TRE3.L,government,,False,,48.81
US13.L,US13.L,government,,False,,49.83
CBU7.L,CBU7.L,government,,False,,55.46
CBU0.L,CBU0.L,government,9.713252495914483,False,80.64,57.53
TREX.L,TREX.L,government,,False,,50.59
US71.L,US71.L,government,,False,,50.86
DTLA.L,DTLA.L,government,,False,,56.46
US10.L,US10.L,government,,False,,48.53
VDTA.L,VDTA.L,government,,False,,54.89
XUTD.L,XUTD.L,government,,False,,48.42
TRES.L,TRES.L,government,,False,,49.65
TRSY.L,TRSY.L,government,,False,,51.52
IGLA.L,IGLA.L,government,,False,,43.86
XGGB.L,XGGB.L,government,,False,,39.18
IGLT.L,IGLT.L,government,,False,,55.37
IGLS.L,IGLS.L,government,,False,,55.3
SEGA.L,SEGA.L,government,,False,,51.69
XGLE.L,XGLE.L,government,,False,,50.27
AGGU.L,AGGU.L,aggregate,,False,,53.29
VAGU.L,VAGU.L,aggregate,,False,,52.19
GLAD.L,GLAD.L,aggregate,,False,,49.15
AGGG.L,AGGG.L,aggregate,,False,,50.77
GAGU.L,GAGU.L,aggregate,,False,,45.51
IUAA.L,IUAA.L,aggregate,,False,,46.09
USAG.L,USAG.L,aggregate,8.233635855066867,False,17.76,37.76
IDTP.L,IDTP.L,inflation-linked,,False,,51.6
TIP5.L,TIP5.L,inflation-linked,,False,,50.32
TIPU.L,TIPU.L,inflation-linked,,False,,46.67
TIPS.L,TIPS.L,inflation-linked,,False,,50.29
IGIL.L,IGIL.L,inflation-linked,,False,,42.21
XG7U.L,XG7U.L,inflation-linked,,False,,39.07
INXG.L,INXG.L,inflation-linked,8.665792132494525,False,33.89,48.38
IBCI.L,IBCI.L,inflation-linked,9.259365742229356,False,62.69,50.61
LQDA.L,LQDA.L,corporate,,False,,47.08
VDPA.L,VDPA.L,corporate,,False,,55.04
SDIA.L,SDIA.L,corporate,,False,,47.71
VDCA.L,VDCA.L,corporate,,False,,52.24
SUSU.L,SUSU.L,corporate,,False,,44.72
ICBU.L,ICBU.L,corporate,,False,,44.79
XDGU.L,XDGU.L,corporate,,False,,45.21
CRPU.L,CRPU.L,corporate,,False,,43.78
HLQD.L,HLQD.L,corporate,,False,,38.11
FLOA.L,FLOA.L,corporate,,False,,53.11
UCRP.L,UCRP.L,corporate,,False,,40.12
IEAA.L,IEAA.L,corporate,,False,,53.5
IHYA.L,IHYA.L,high-yield,,False,,43.09
HYLA.L,HYLA.L,high-yield,,False,,41.94
XUHY.L,XUHY.L,high-yield,,False,,38.81
HYUS.L,HYUS.L,high-yield,,False,,37.91
DHYA.L,DHYA.L,high-yield,,False,,38.55
WIAU.L,WIAU.L,high-yield,,False,,40.71
SJNK.L,SJNK.L,high-yield,,False,,35.96
HIGH.L,HIGH.L,high-yield,,False,,41.38
XHYG.L,HIGH.L,high-yield,9.446384686170262,False,50.0,51.8
JPEA.L,JPEA.L,em-debt,,False,,44.92
VDEA.L,VDEA.L,em-debt,9.208564592586017,False,60.28,42.08
EMSA.L,EMSA.L,em-debt,,False,,39.48
EMCA.L,EMCA.L,em-debt,,False,,43.87
EMGA.L,EMGA.L,em-debt,9.756498241448815,False,81.95,43.83
EMDD.L,EMDD.L,em-debt,,False,,39.95
EMLC.L,EMLC.L,em-debt,8.37295263336675,False,22.2,36.44
EMLB.L,EMLB.L,em-debt,8.495835198003139,False,26.73,36.59
ERNA.L,ERNA.L,money-market,,False,,54.21
JPSA.L,JPSA.L,money-market,9.01259817721586,False,50.63,41.89
ERNS.L,ERNS.L,money-market,9.310273468446615,False,65.03,54.59
XSTR.L,XSTR.L,money-market,8.300113397340724,False,19.79,47.73
ERNE.L,ERNE.L,money-market,,False,,50.97
VWRA.L,VWRA.L,global,10.948626788219173,True,50.0,52.93
ISAC.L,ACWD.L,global,,False,,49.57
IWDA.L,IWDA.L,global,,False,,51.14
XDWD.L,IWDA.L,global,,False,,50.13
SWRD.L,IWDA.L,global,,False,,51.37
HMWD.L,IWDA.L,global,,False,,50.13
FWRA.L,VWRA.L,global,,False,,48.74
VHVE.L,VHVE.L,global,10.06186179688128,False,88.08,49.78
WSML.L,WDSC.L,global,9.952144038749127,False,67.08,57.19
CSPX.L,XSPU.L,us,,False,,52.34
VUAA.L,XSPU.L,us,10.951346276260706,False,50.0,48.24
SPXS.L,XSPU.L,us,,False,,56.04
SPY5.L,XSPU.L,us,,False,,52.82
HSPD.L,XSPU.L,us,,False,,47.04
XSPU.L,XSPU.L,us,,False,,45.12
CNDX.L,CNDX.L,us,,False,,56.06
EQQU.L,CNDX.L,us,,False,,51.98
XNAS.L,CNDX.L,us,9.47291673142885,False,50.0,52.88
XDEW.L,XDEW.L,us,,False,,45.25
CSUS.L,CSUS.L,us,9.718868457817738,False,80.81,55.65
VNRA.L,VNRA.L,us,9.837206673098503,False,84.22,50.32
R2US.L,R2US.L,us,,False,,41.95
SPY4.L,SPY4.L,us,,False,,40.78
CUSS.L,CUSS.L,us,9.439278980757496,False,70.65,41.01
VEUA.L,VEUA.L,europe,9.907203400033506,False,85.99,53.64
VERG.L,VERG.L,europe,9.72861605499359,False,81.11,53.18
SMEA.L,SMEA.L,europe,10.206813963791264,False,88.08,53.99
IEUX.L,IEUX.L,europe,9.1180845196733,False,55.88,42.26
CSX5.L,CSX5.L,europe,9.87645181607756,False,85.23,54.36
XESC.L,XESC.L,europe,10.080161001681232,False,88.08,52.88
XDAX.L,XDAX.L,single_country,9.856440013988731,False,84.72,51.89
CACX.L,CACX.L,single_country,9.614020875747102,False,77.35,43.14
CSWG.L,CSWG.L,single_country,,False,,40.53
IAEX.L,IAEX.L,single_country,8.928024068197818,False,46.41,40.2
CUKX.L,CUKX.L,uk,9.52134897193943,False,73.94,56.68
VUKG.L,HUKX.L,uk,9.817924337355892,False,70.68,50.05
VMIG.L,MIDD.L,uk,9.332093434096905,False,62.67,50.69
MIDD.L,MIDD.L,uk,8.814009654418948,False,37.33,41.43
HUKX.L,HUKX.L,uk,8.938043557534952,False,29.32,50.86
CUKS.L,CUKS.L,uk,7.9692100862883235,False,11.29,34.47
IJPA.L,IJPA.L,japan,,False,,49.67
CSJP.L,CSJP.L,japan,9.248723299041288,False,62.19,40.3
VJPA.L,VJPA.L,japan,,False,,46.36
XMJD.L,XMJD.L,japan,,False,,58.22
HMJD.L,XMJD.L,japan,8.39998417084486,False,50.0,45.61
LCJP.L,LCJP.L,japan,,False,,49.25
XDJP.L,XDJP.L,japan,,False,,49.3
IDJP.L,IDJP.L,japan,8.79214608397242,False,39.75,36.72
CPXJ.L,CPXJ.L,asia_pacific,9.631169916436718,False,77.94,46.93
VAPU.L,VAPU.L,asia_pacific,9.463909436346716,False,71.66,48.27
HMXJ.L,HMXJ.L,asia_pacific,9.084747748578764,False,54.23,38.25
XPXD.L,XPXD.L,asia_pacific,9.174474968120547,False,58.64,38.17
IFFF.L,IFFF.L,asia_pacific,9.219364156757026,False,60.8,42.22
HMAD.L,HMAD.L,asia_pacific,8.663009302226651,False,33.76,36.71
XMAD.L,XMAD.L,asia_pacific,8.83592333659549,False,41.87,37.77
EIMI.L,EIMI.L,emerging,10.637045558549016,False,88.08,50.71
VFEA.L,VFEA.L,emerging,9.767092641269642,False,82.26,48.22
IEMA.L,IEMA.L,emerging,9.997936329281366,False,88.04,50.65
XMME.L,XMMD.L,emerging,10.143753275016952,False,52.49,54.27
HMEM.L,XMMD.L,emerging,9.75637419306436,False,40.43,50.55
EMXC.L,EMXC.L,emerging,9.651577697852948,False,78.64,50.31
EMSD.L,EMSD.L,emerging,8.763748905449534,False,38.4,35.56
XMMD.L,XMMD.L,emerging,,False,,43.02
NDIA.L,XCS5.L,single_country,9.689332674505035,False,71.77,41.67
FLXI.L,FLXI.L,single_country,9.282053127635953,False,63.74,43.0
XCS5.L,XCS5.L,single_country,8.756133709456114,False,28.23,53.7
CNYA.L,CNYA.L,single_country,,False,,44.98
XCS6.L,XCS6.L,single_country,9.204677883657382,False,56.07,40.47
HMCD.L,XCS6.L,single_country,8.960750918887655,False,43.93,54.0
FXC.L,FXC.L,single_country,8.88670750696181,False,44.36,40.02
KWEB.L,KWEB.L,single_country,,False,,42.61
CSKR.L,CSKR.L,single_country,8.865731691902369,False,43.33,42.54
ITWN.L,ITWN.L,single_country,9.226543173621824,False,60.37,44.63
XMTD.L,ITWN.L,single_country,8.805801669059536,False,39.63,47.64
IBZL.L,IBZL.L,single_country,8.658892057953548,False,54.95,40.27
XMBD.L,IBZL.L,single_country,8.460313517616685,False,45.05,53.91
CMXC.L,CMXC.L,single_country,8.066236596898706,False,13.38,35.56
IKSA.L,IKSA.L,single_country,8.698557805769735,False,35.37,37.6
IRSA.L,IRSA.L,single_country,8.36359970666947,False,21.88,36.54
IDTK.L,IDTK.L,single_country,8.007942066384407,False,12.09,34.39
IAUS.L,IAUS.L,single_country,8.842865547464037,False,42.21,41.22
CCAU.L,CCAU.L,single_country,9.376107086841513,False,67.97,41.63
IPOL.L,IPOL.L,single_country,9.049538736168762,False,52.47,42.22
XVTD.L,XVTD.L,single_country,8.5338286527468,False,28.24,36.69
HIDD.L,HIDD.L,single_country,8.290765926247628,False,19.49,35.88
IWVL.L,IWVL.L,factor_value,9.879786720131529,False,85.32,47.48
IWQU.L,IWQU.L,factor_quality,9.825687443639142,False,83.91,44.24
IWMO.L,IWMO.L,factor_momentum,9.77715910196236,False,82.55,44.06
MVOL.L,MVOL.L,factor_min_vol,,False,,44.02
XDEV.L,XDEV.L,factor_value,9.63417583331997,False,78.05,44.48
XDEQ.L,XDEQ.L,factor_quality,9.478234954773376,False,72.24,40.36
XDEM.L,XDEM.L,factor_momentum,9.337413828716391,False,66.26,40.51
XDEB.L,XDEB.L,factor_min_vol,9.159955416075023,False,57.93,40.46
IUVL.L,IUVL.L,factor_value,9.588987377494714,False,76.46,46.43
IUQA.L,IUQA.L,factor_quality,9.507533020749989,False,73.4,44.79
IUMO.L,IUMO.L,factor_momentum,8.791928075134354,False,39.74,43.29
SPMV.L,SPMV.L,factor_min_vol,,False,,41.17
EMVL.L,EMVL.L,factor_value,9.230373443635736,False,61.32,44.13
IEFV.L,IEFV.L,factor_value,9.418578557173824,False,69.79,43.57
IEFQ.L,IEFQ.L,factor_quality,8.814338644151752,False,40.82,40.42
IEFM.L,IEFM.L,factor_momentum,8.877220733617094,False,43.89,41.08
JPGL.L,JPGL.L,factor_multi,8.490388232317207,False,26.52,38.53
MOAT.L,MOAT.L,factor_quality,8.594634679947815,False,30.77,36.86
WDSC.L,WDSC.L,size_small_cap,9.240248256800252,False,32.92,45.53
USSC.L,USSC.L,size_small_cap_value,9.013193041841596,False,50.66,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,8.653477410512286,False,33.34,37.07
SPEQ.L,SPEQ.L,equal_weight,9.236394394405798,False,61.6,42.26
VHYA.L,VHYD.L,dividend,10.18342582768701,False,50.0,48.01
VHYD.L,VHYD.L,dividend,10.18342582768701,False,50.0,50.34
FUSD.L,FUSD.L,dividend_quality,,False,,38.09
FGQI.L,FGQI.L,dividend_quality,,False,,37.29
GLDV.L,GLDV.L,dividend,9.255473168415852,False,62.5,39.83
UDVD.L,UDVD.L,dividend,,False,,41.58
WQDV.L,WQDV.L,dividend_quality,9.391813890412472,False,68.65,41.46
QDIV.L,QDIV.L,dividend_quality,,False,,37.32
TDIV.L,TDIV.L,dividend,10.01461113943237,False,88.08,44.59
HDLV.L,HDLV.L,dividend_low_vol,,False,,40.44
DGRA.L,DGRA.L,dividend_quality,,False,,38.48
GGRA.L,GGRA.L,dividend_quality,,False,,39.2
EUDV.L,EUDV.L,dividend,9.2632079078416,False,62.86,40.49
IDVY.L,IDVY.L,dividend,,False,,41.73
IUIT.L,IUIT.L,sector_tech,10.283303915530434,False,88.08,49.92
SXLK.L,SXLK.L,sector_tech,9.331931263423456,False,66.01,45.08
XLKS.L,XLKS.L,sector_tech,9.394365463413108,False,68.76,45.96
XDWT.L,XDWT.L,sector_tech,9.802804513012106,False,83.28,44.13
WTEC.L,WTEC.L,sector_tech,9.090124341620188,False,54.49,38.34
IUHC.L,IUHC.L,sector_health,,False,,49.63
SXLV.L,SXLV.L,sector_health,8.814064716591334,False,40.81,45.91
XLVS.L,XLVS.L,sector_health,8.778166815218954,False,39.09,44.01
XDWH.L,WHEA.L,sector_health,9.65989346487138,False,68.02,55.44
WHEA.L,WHEA.L,sector_health,8.905131818438889,False,31.98,47.22
IUFS.L,IUFS.L,sector_financials,9.368603178615048,False,67.64,47.69
SXLF.L,SXLF.L,sector_financials,8.85532986136272,False,42.82,41.53
XLFS.L,XLFS.L,sector_financials,8.568964210678752,False,29.69,40.07
XDWF.L,WFIN.L,sector_financials,9.171457686986695,False,64.14,55.81
WFIN.L,WFIN.L,sector_financials,8.589964748895811,False,35.86,46.75
IUES.L,IUES.L,sector_energy,9.320094603239369,False,65.48,48.23
SXLE.L,SXLE.L,sector_energy,9.034187236401914,False,51.71,45.52
XLES.L,XLES.L,sector_energy,8.189262433201092,False,16.5,41.55
XDW0.L,WNRG.L,sector_energy,9.342316794816716,False,62.47,55.0
WNRG.L,WNRG.L,sector_energy,8.832585832220195,False,37.53,47.38
IOGP.L,IOGP.L,sector_energy,8.679846187813055,False,34.52,36.17
IUCD.L,IUCD.L,sector_consumer_disc,8.8877079481603,False,44.41,42.92
SXLY.L,SXLY.L,sector_consumer_disc,8.126580710159045,False,14.84,36.23
XDWC.L,WCOD.L,sector_consumer_disc,8.528632367907905,False,68.24,57.95
WCOD.L,WCOD.L,sector_consumer_disc,7.7636739442422655,False,31.76,44.31
IUCS.L,IUCS.L,sector_consumer_staples,8.730055281750117,False,36.82,46.39
SXLP.L,SXLP.L,sector_consumer_staples,8.553670709079578,False,29.06,43.73
XDWS.L,XDWS.L,sector_consumer_staples,9.007677739168626,False,50.38,41.16
IUIS.L,IUIS.L,sector_industrials,8.844839828555846,False,42.3,45.18
SXLI.L,SXLI.L,sector_industrials,8.983694946225151,False,49.18,45.18
XDWI.L,XDWI.L,sector_industrials,9.127321129433277,False,56.33,41.14
IUUS.L,IUUS.L,sector_utilities,9.06929841493921,False,53.46,48.81
SXLU.L,SXLU.L,sector_utilities,8.260932441347776,False,18.57,42.66
XDWU.L,XDWU.L,sector_utilities,8.987208838919225,False,49.36,40.73
IUMS.L,IUMS.L,sector_materials,8.30134701912892,False,19.82,44.14
SXLB.L,SXLB.L,sector_materials,7.762051256691101,False,7.76,39.26
XDWM.L,XDWM.L,sector_materials,8.889357432081447,False,44.49,39.7
IUCM.L,IUCM.L,sector_communication,9.045888223400386,False,52.29,45.41
SXLC.L,SXLC.L,sector_communication,8.481869706879955,False,26.19,40.19
XWTS.L,XWTS.L,sector_communication,8.578830834789795,False,30.1,35.61
SMH.L,SMH.L,theme_semiconductors,9.920376880237606,False,86.3,45.19
SEMI.L,SEMI.L,theme_semiconductors,9.751445171079329,False,81.8,45.1
SEMU.L,SEMU.L,theme_semiconductors,9.291904437677694,False,64.19,39.52
AIAI.L,AIAI.L,theme_ai,9.292119202713986,False,64.2,41.8
WTAI.L,WTAI.L,theme_ai,9.122528054263093,False,56.1,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,8.194805646048803,False,16.65,33.75
RBOT.L,RBOT.L,theme_ai_robotics,9.742395720404858,False,81.53,43.84
ROBO.L,ROBO.L,theme_ai_robotics,9.212916751642076,False,60.49,39.93
DGTL.L,DGTL.L,theme_digital_tech,8.915324515791363,False,45.78,37.07
XNGI.L,XNGI.L,theme_digital_tech,7.858491046817526,False,9.25,30.8
ITEK.L,ITEK.L,theme_digital_tech,8.038463771887788,False,12.75,32.68
WCLD.L,WCLD.L,theme_cloud,8.580262427938418,False,30.16,38.24
LOCK.L,LOCK.L,theme_cybersecurity,9.406620897887649,False,69.28,41.54
USPY.L,USPY.L,theme_cybersecurity,,False,,40.83
WCBR.L,WCBR.L,theme_cybersecurity,8.883157529370985,False,44.18,36.33
HEAL.L,HEAL.L,theme_health_innovation,9.211281741961727,False,60.41,42.54
BTEC.L,BTEC.L,theme_biotech,9.12646051737624,False,56.29,43.97
SBIO.L,SBIO.L,theme_biotech,8.777136666071081,False,39.04,41.16
INRG.L,INRG.L,theme_clean_energy,9.473529804716057,False,72.05,41.88
RENW.L,RENW.L,theme_clean_energy,8.659761871719363,False,33.62,36.63
HTWO.L,HTWO.L,theme_clean_energy,8.590373498017957,False,30.59,35.08
ECAR.L,ECAR.L,theme_ev_battery,8.741099688494728,False,37.34,37.63
BATT.L,BATT.L,theme_ev_battery,8.789151755855443,False,39.61,37.85
IH2O.L,IH2O.L,theme_water,9.3444311847275,False,66.57,41.27
WATU.L,WATU.L,theme_water,9.204129814971694,False,60.07,38.39
GLUG.L,GLUG.L,theme_water,8.831619384752713,False,41.66,39.87
NATO.L,NATO.L,theme_defence,9.509699980207303,False,73.49,39.05
DFNS.L,DFNS.L,theme_defence,9.828418550422178,False,83.98,42.49
IGLN.L,PHAU.L,gold_physical_etc,,False,,54.79
SGLD.L,PHAU.L,gold_physical_etc,,False,,54.36
XGDU.L,XGDU.L,gold_physical_etc,,False,,48.98
WGLD.L,PHAU.L,gold_physical_etc,,False,,45.81
PHAU.L,PHAU.L,gold_physical_etc,,False,,36.69
SGBX.L,SGBX.L,gold_physical_etc,,False,,42.94
XGLD.L,PHAU.L,gold_physical_etc,,False,,34.54
RMAU.L,RMAU.L,gold_physical_etc,,False,,41.74
GDX.L,GDX.L,gold_miners,9.587453409267892,False,76.4,47.27
GDXJ.L,GDXJ.L,gold_miners,9.029093965188713,False,51.45,43.98
IAUP.L,IAUP.L,gold_miners,9.583186712434175,False,76.25,45.68
AUCO.L,AUCO.L,gold_miners,8.885952001385608,False,44.32,41.04
ISLN.L,PHAG.L,silver_physical_etc,,False,,55.13
SSLV.L,PHAG.L,silver_physical_etc,,False,,53.25
PHAG.L,PHAG.L,silver_physical_etc,,False,,37.57
SILV.L,SILV.L,silver_miners,9.046172869285948,False,52.31,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,,False,,38.29
IPLT.L,IPLT.L,platinum_physical_etc,,False,,42.09
IPDM.L,IPDM.L,palladium_physical_etc,,False,,41.44
CMOD.L,CMOD.L,commodities_broad,,False,,43.98
ICOM.L,ICOM.L,commodities_broad,9.388873084588058,False,68.52,45.76
BCOM.L,BCOM.L,commodities_broad,8.707056212424401,False,35.76,38.59
COMF.L,COMF.L,commodities_broad,8.966833078547484,False,48.34,36.88
ROLL.L,ROLL.L,commodities_broad,9.263598729491209,False,62.88,39.95
WCOA.L,WCOA.L,commodities_broad,,False,,38.51
ENCO.L,ENCO.L,commodities_broad,,False,,36.22
AIGC.L,AIGC.L,commodities_broad_etc,,False,,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,,False,,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,,False,,43.59
BRNT.L,BRNT.L,commodities_energy_etc,,False,,42.51
CRUD.L,CRUD.L,commodities_energy_etc,,False,,42.13
GDIG.L,GDIG.L,commodity_equity_mining,9.314631176188886,False,65.23,43.0
COPX.L,COPX.L,commodity_equity_mining,9.005044538164524,False,50.25,42.56
REMX.L,REMX.L,commodity_equity_mining,8.937927015281112,False,46.9,41.2
URNU.L,URNU.L,commodity_equity_uranium,8.73606212142485,False,37.1,37.49
URNM.L,URNM.L,commodity_equity_uranium,8.541854190100116,False,28.57,36.43
SPAG.L,SPAG.L,commodity_equity_agri,8.764782793854513,False,38.45,40.15
WOOD.L,WOOD.L,commodity_equity_timber,7.898898426141844,False,9.96,34.99
DPYA.L,DPYA.L,reit_global,,False,,40.49
GLRA.L,GLRA.L,reit_global,8.609851827932772,False,31.43,36.71
HPRD.L,HPRD.L,reit_global,,False,,40.52
EPRA.L,EPRA.L,reit_global,,False,,39.75
TRET.L,TRET.L,reit_global,8.66157542593627,False,33.7,36.78
IDUP.L,IDUP.L,reit_us,8.787566199956425,False,39.54,39.63
XRES.L,XRES.L,reit_us,8.131750998155098,False,14.98,44.93
IPRP.L,IPRP.L,reit_europe,8.968500701028761,False,48.43,39.51
XDER.L,XDER.L,reit_europe,8.792424324801864,False,39.77,37.62
IDAR.L,IDAR.L,reit_asia,8.325014383884028,False,20.59,35.09
IUKP.L,IUKP.L,reit_uk,,False,,43.05
IDIN.L,IDIN.L,infrastructure_global,,False,,40.84
XGID.L,XGID.L,infrastructure_global,8.873027447724033,False,43.69,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,8.86517916210406,False,43.3,37.41
PAVE.L,PAVE.L,infrastructure_us,8.93154908939396,False,46.58,38.56
MAGG.L,MAGG.L,multi_asset_growth,,False,,37.37
MAMG.L,MAMG.L,multi_asset_moderate,,False,,38.02
MACG.L,MACG.L,multi_asset_conservative,,False,,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,7.354839820537866,False,3.59,30.24
ACWD.L,ACWD.L,global,,False,,56.16
SPYY.L,SPYY.L,global,6.9335747959502205,False,1.58,36.04
EXUS.L,EXUS.L,developed_ex_us,9.91641313368972,False,86.21,48.48

