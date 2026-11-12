# Pillar CST06: LSE traded value and zero-volume days
Definition: Log of the 63-session median daily traded value on the USD line (close x volume, US$), saturating at US$5m a day, minus a penalty for the share of zero-volume sessions (0% none, 20% or more maximum). Also sets the S1/S2 switch-size rule.
Source: yfinance .L daily volume and close (verified). Better when: higher, capped. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                      |   CST06 | buyable   |   CST06_score |   line_score |
|:-------|:----------|:---------------------------|--------:|:----------|--------------:|-------------:|
| XG7U.L | XG7U.L    | inflation-linked           | 0       | False     |          0    |        39.07 |
| XGGB.L | XGGB.L    | government                 | 0       | False     |          0    |        39.18 |
| XNGI.L | XNGI.L    | theme_digital_tech         | 0       | False     |          0    |        30.8  |
| XPXD.L | XPXD.L    | asia_pacific               | 0       | False     |          0    |        38.17 |
| UCRP.L | UCRP.L    | corporate                  | 0       | False     |          0    |        40.12 |
| NTSX.L | NTSX.L    | multi_asset_efficient_core | 2.41719 | False     |          0.08 |        30.24 |
| WCOD.L | WCOD.L    | sector_consumer_disc       | 2.61584 | False     |          9.46 |        44.31 |
| SPYY.L | SPYY.L    | global                     | 2.97935 | False     |          0.24 |        36.04 |
| IDTK.L | IDTK.L    | single_country             | 3.03861 | False     |          0.27 |        34.39 |
| GAGU.L | GAGU.L    | aggregate                  | 3.3477  | False     |          0.49 |        45.51 |
| XUT3.L | XUT3.L    | government                 | 3.47473 | False     |          0.64 |        46.44 |
| TRET.L | TRET.L    | reit_global                | 3.71169 | False     |          1.02 |        36.78 |
| USAG.L | USAG.L    | aggregate                  | 3.78704 | False     |          1.18 |        37.76 |
| MACG.L | MACG.L    | multi_asset_conservative   | 3.79904 | False     |          1.21 |        38.44 |
| IDAR.L | IDAR.L    | reit_asia                  | 3.84862 | False     |          1.34 |        35.09 |
|        | cluster   | scope                |   CST06 | buyable   |   CST06_score |   line_score |
|:-------|:----------|:---------------------|--------:|:----------|--------------:|-------------:|
| XDEW.L | XDEW.L    | us                   | 7.18209 | False     |         88.08 |        45.25 |
| EQQU.L | CNDX.L    | us                   | 7.20291 | False     |         50    |        51.98 |
| EIMI.L | EIMI.L    | emerging             | 7.2657  | False     |         88.08 |        50.71 |
| MIDD.L | MIDD.L    | uk                   | 7.26793 | False     |         62.41 |        41.43 |
| IUIT.L | IUIT.L    | sector_tech          | 7.28294 | False     |         88.08 |        49.92 |
| SPXS.L | XSPU.L    | us                   | 7.40695 | False     |         50    |        56.04 |
| VUAA.L | XSPU.L    | us                   | 7.43041 | False     |         50    |        48.24 |
| IGLN.L | PHAU.L    | gold_physical_etc    | 7.45799 | False     |         73.26 |        54.79 |
| SMH.L  | SMH.L     | theme_semiconductors | 7.53817 | False     |         88.08 |        45.19 |
| CNDX.L | CNDX.L    | us                   | 7.58932 | False     |         50    |        56.06 |
| VWRA.L | VWRA.L    | global               | 7.61498 | True      |         50    |        52.93 |
| ISAC.L | ACWD.L    | global               | 7.6477  | False     |         50    |        49.57 |
| IB01.L | IB01.L    | government           | 7.68771 | False     |         88.08 |        55.34 |
| IWDA.L | IWDA.L    | global               | 7.87299 | False     |         76.17 |        51.14 |
| CSPX.L | XSPU.L    | us                   | 8.03139 | False     |         50    |        52.34 |

## All lines (csv)
,cluster,scope,CST06,buyable,CST06_score,line_score
IB01.L,IB01.L,government,7.687705438251896,False,88.08,55.34
VDST.L,VDST.L,government,6.767532632293354,False,82.27,56.33
IBTA.L,IBTA.L,government,6.927537018409064,False,86.47,56.49
CBU3.L,CBU3.L,government,5.43366874481461,False,24.37,49.56
XUT3.L,XUT3.L,government,3.4747260421801167,False,0.64,46.44
TRE3.L,TRE3.L,government,4.257133335598967,False,2.97,48.81
US13.L,US13.L,government,5.201549781537607,False,16.84,49.83
CBU7.L,CBU7.L,government,7.068688667319999,False,88.08,55.46
CBU0.L,CBU0.L,government,6.996636843743892,False,88.01,57.53
TREX.L,TREX.L,government,5.436372209105364,False,24.47,50.59
US71.L,US71.L,government,5.250706589302956,False,18.26,50.86
DTLA.L,DTLA.L,government,6.991393387426196,False,87.9,56.46
US10.L,US10.L,government,4.71934786279266,False,7.17,48.53
VDTA.L,VDTA.L,government,6.085087303612997,False,54.24,54.89
XUTD.L,XUTD.L,government,4.279713367507536,False,3.11,48.42
TRES.L,TRES.L,government,4.892849270673914,False,9.85,49.65
TRSY.L,TRSY.L,government,5.320915705132863,False,20.45,51.52
IGLA.L,IGLA.L,government,5.823539291596694,False,41.27,43.86
XGGB.L,XGGB.L,government,0.0,False,0.0,39.18
IGLT.L,IGLT.L,government,6.749124864061924,False,81.73,55.37
IGLS.L,IGLS.L,government,6.731335539810813,False,81.19,55.3
SEGA.L,SEGA.L,government,6.0012000828474825,False,50.06,51.69
XGLE.L,XGLE.L,government,5.5054227586359135,False,27.11,50.27
AGGU.L,AGGU.L,aggregate,6.644844372604234,False,78.41,53.29
VAGU.L,VAGU.L,aggregate,6.003961257648243,False,50.2,52.19
GLAD.L,GLAD.L,aggregate,5.710323898989235,False,35.91,49.15
AGGG.L,AGGG.L,aggregate,6.122029635878587,False,56.07,50.77
GAGU.L,GAGU.L,aggregate,3.3477007200336266,False,0.49,45.51
IUAA.L,IUAA.L,aggregate,6.760059952825635,False,82.06,46.09
USAG.L,USAG.L,aggregate,3.78704474988872,False,1.18,37.76
IDTP.L,IDTP.L,inflation-linked,6.473536600883651,False,72.05,51.6
TIP5.L,TIP5.L,inflation-linked,6.011390114104366,False,50.57,50.32
TIPU.L,TIPU.L,inflation-linked,4.936805425963578,False,10.66,46.67
TIPS.L,TIPS.L,inflation-linked,4.702148139875049,False,6.94,50.29
IGIL.L,IGIL.L,inflation-linked,5.487094359456555,False,26.39,42.21
XG7U.L,XG7U.L,inflation-linked,0.0,False,0.0,39.07
INXG.L,INXG.L,inflation-linked,5.923645726772249,False,46.19,48.38
IBCI.L,IBCI.L,inflation-linked,5.882725490233762,False,44.16,50.61
LQDA.L,LQDA.L,corporate,6.697827815325488,False,80.15,47.08
VDPA.L,VDPA.L,corporate,6.546128387933363,False,74.88,55.04
SDIA.L,SDIA.L,corporate,7.001969745824344,False,88.08,47.71
VDCA.L,VDCA.L,corporate,6.400076667642332,False,69.0,52.24
SUSU.L,SUSU.L,corporate,4.657724577357166,False,6.39,44.72
ICBU.L,ICBU.L,corporate,5.582702860651361,False,30.27,44.79
XDGU.L,XDGU.L,corporate,4.788042176605488,False,8.14,45.21
CRPU.L,CRPU.L,corporate,6.101580859208551,False,55.06,43.78
HLQD.L,HLQD.L,corporate,5.096250119403265,False,14.09,38.11
FLOA.L,FLOA.L,corporate,6.797707533992267,False,83.14,53.11
UCRP.L,UCRP.L,corporate,0.0,False,0.0,40.12
IEAA.L,IEAA.L,corporate,6.463122309240391,False,71.63,53.5
IHYA.L,IHYA.L,high-yield,6.545236184504574,False,74.85,43.09
HYLA.L,HYLA.L,high-yield,5.871101721177774,False,43.59,41.94
XUHY.L,XUHY.L,high-yield,5.108586164899849,False,14.4,38.81
HYUS.L,HYUS.L,high-yield,5.477902379456894,False,26.03,37.91
DHYA.L,DHYA.L,high-yield,5.110490759003666,False,14.44,38.55
WIAU.L,WIAU.L,high-yield,5.571259448798347,False,29.79,40.71
SJNK.L,SJNK.L,high-yield,4.402024574798829,False,3.93,35.96
HIGH.L,HIGH.L,high-yield,5.807193948852034,False,80.14,41.38
XHYG.L,HIGH.L,high-yield,4.412092872201932,False,19.86,51.8
JPEA.L,JPEA.L,em-debt,6.638074289361468,False,78.18,44.92
VDEA.L,VDEA.L,em-debt,5.747314867258716,False,37.63,42.08
EMSA.L,EMSA.L,em-debt,5.157437085328041,False,15.64,39.48
EMCA.L,EMCA.L,em-debt,6.358000919844717,False,67.17,43.87
EMGA.L,EMGA.L,em-debt,5.814821296096819,False,40.85,43.83
EMDD.L,EMDD.L,em-debt,5.707312992576312,False,35.77,39.95
EMLC.L,EMLC.L,em-debt,5.092777626783099,False,14.01,36.44
EMLB.L,EMLB.L,em-debt,4.898134321716144,False,9.94,36.59
ERNA.L,ERNA.L,money-market,6.71697248073882,False,80.75,54.21
JPSA.L,JPSA.L,money-market,5.395818007330714,False,23.0,41.89
ERNS.L,ERNS.L,money-market,6.780248332293287,False,82.64,54.59
XSTR.L,XSTR.L,money-market,6.350336314621334,False,66.83,47.73
ERNE.L,ERNE.L,money-market,5.946058691295789,False,47.31,50.97
VWRA.L,VWRA.L,global,7.61497788919072,True,50.0,52.93
ISAC.L,ACWD.L,global,7.647700672248469,False,50.0,49.57
IWDA.L,IWDA.L,global,7.872992940785929,False,76.17,51.14
XDWD.L,IWDA.L,global,6.116226589535294,False,35.31,50.13
SWRD.L,IWDA.L,global,6.72147926879182,False,64.69,51.37
HMWD.L,IWDA.L,global,5.777636166664421,False,21.71,50.13
FWRA.L,VWRA.L,global,6.558890548701699,False,29.27,48.74
VHVE.L,VHVE.L,global,6.432024785214606,False,70.35,49.78
WSML.L,WDSC.L,global,6.592244826898522,False,73.87,57.19
CSPX.L,XSPU.L,us,8.031394105527507,False,50.0,52.34
VUAA.L,XSPU.L,us,7.430405447296306,False,50.0,48.24
SPXS.L,XSPU.L,us,7.406949552837676,False,50.0,56.04
SPY5.L,XSPU.L,us,6.714919917826868,False,36.12,52.82
HSPD.L,XSPU.L,us,5.927177656426413,False,10.47,47.04
XSPU.L,XSPU.L,us,6.165667430914417,False,15.86,45.12
CNDX.L,CNDX.L,us,7.589321274952368,False,50.0,56.06
EQQU.L,CNDX.L,us,7.202907451540202,False,50.0,51.98
XNAS.L,CNDX.L,us,6.521076605434114,False,27.73,52.88
XDEW.L,XDEW.L,us,7.182092183499122,False,88.08,45.25
CSUS.L,CSUS.L,us,6.572386844508626,False,75.86,55.65
VNRA.L,VNRA.L,us,6.457252229466944,False,71.39,50.32
R2US.L,R2US.L,us,6.623831352545938,False,77.69,41.95
SPY4.L,SPY4.L,us,6.5291232256271625,False,74.24,40.78
CUSS.L,CUSS.L,us,6.249254244972215,False,62.21,41.01
VEUA.L,VEUA.L,europe,6.369850898707776,False,67.69,53.64
VERG.L,VERG.L,europe,6.332419427951999,False,66.03,53.18
SMEA.L,SMEA.L,europe,7.135453153584803,False,88.08,53.99
IEUX.L,IEUX.L,europe,6.225342893003683,False,61.08,42.26
CSX5.L,CSX5.L,europe,6.627294404504494,False,77.81,54.36
XESC.L,XESC.L,europe,5.812720910800403,False,40.74,52.88
XDAX.L,XDAX.L,single_country,5.771321097121933,False,38.76,51.89
CACX.L,CACX.L,single_country,5.745908124367402,False,37.56,43.14
CSWG.L,CSWG.L,single_country,5.118812461517878,False,14.65,40.53
IAEX.L,IAEX.L,single_country,5.836352184612639,False,41.89,40.2
CUKX.L,CUKX.L,uk,6.852180719536338,False,84.61,56.68
VUKG.L,HUKX.L,uk,6.950591885741357,False,57.74,50.05
VMIG.L,MIDD.L,uk,6.225111134770793,False,26.06,50.69
MIDD.L,MIDD.L,uk,7.267932988859273,False,62.41,41.43
HUKX.L,HUKX.L,uk,6.638535960490722,False,42.26,50.86
CUKS.L,CUKS.L,uk,5.050842725484921,False,13.03,34.47
IJPA.L,IJPA.L,japan,7.004375013165036,False,88.08,49.67
CSJP.L,CSJP.L,japan,5.605586978490557,False,31.24,40.3
VJPA.L,VJPA.L,japan,6.00870470571889,False,50.44,46.36
XMJD.L,XMJD.L,japan,5.945132628324926,False,86.45,58.22
HMJD.L,XMJD.L,japan,4.091586786210968,False,13.55,45.61
LCJP.L,LCJP.L,japan,6.0848543618261735,False,54.23,49.25
XDJP.L,XDJP.L,japan,5.972952652188009,False,48.65,49.3
IDJP.L,IDJP.L,japan,4.70444545368095,False,6.97,36.72
CPXJ.L,CPXJ.L,asia_pacific,6.551276248712222,False,75.07,46.93
VAPU.L,VAPU.L,asia_pacific,6.249351111242042,False,62.22,48.27
HMXJ.L,HMXJ.L,asia_pacific,5.197434967586812,False,16.73,38.25
XPXD.L,XPXD.L,asia_pacific,0.0,False,0.0,38.17
IFFF.L,IFFF.L,asia_pacific,6.270429764018124,False,63.2,42.22
HMAD.L,HMAD.L,asia_pacific,4.927997331496418,False,10.49,36.71
XMAD.L,XMAD.L,asia_pacific,4.751791162103507,False,7.61,37.77
EIMI.L,EIMI.L,emerging,7.265699303527698,False,88.08,50.71
VFEA.L,VFEA.L,emerging,6.188059179639762,False,59.29,48.22
IEMA.L,IEMA.L,emerging,7.03894044459028,False,88.08,50.65
XMME.L,XMMD.L,emerging,6.635098421641359,False,78.83,54.27
HMEM.L,XMMD.L,emerging,5.977796532013517,False,50.0,50.55
EMXC.L,EMXC.L,emerging,6.606374187030354,False,77.08,50.31
EMSD.L,EMSD.L,emerging,4.33827158211182,False,3.48,35.56
XMMD.L,XMMD.L,emerging,4.63725666055514,False,6.41,43.02
NDIA.L,XCS5.L,single_country,6.677094165388676,False,81.31,41.67
FLXI.L,FLXI.L,single_country,5.713303580890038,False,36.05,43.0
XCS5.L,XCS5.L,single_country,5.2068499129289165,False,18.69,53.7
CNYA.L,CNYA.L,single_country,6.716683784746422,False,80.74,44.98
XCS6.L,XCS6.L,single_country,5.226013116698304,False,52.0,40.47
HMCD.L,XCS6.L,single_country,5.146130194414711,False,48.0,54.0
FXC.L,FXC.L,single_country,5.721324285919387,False,36.42,40.02
KWEB.L,KWEB.L,single_country,6.101788324425386,False,55.07,42.61
CSKR.L,CSKR.L,single_country,6.563434459821788,False,75.53,42.54
ITWN.L,ITWN.L,single_country,6.314859410732369,False,69.35,44.63
XMTD.L,ITWN.L,single_country,5.498325985436599,False,30.65,47.64
IBZL.L,IBZL.L,single_country,5.963622028018873,False,63.65,40.27
XMBD.L,IBZL.L,single_country,5.403296376463137,False,36.35,53.91
CMXC.L,CMXC.L,single_country,4.237513565944114,False,2.86,35.56
IKSA.L,IKSA.L,single_country,5.433312143602681,False,24.35,37.6
IRSA.L,IRSA.L,single_country,4.973924469852424,False,11.38,36.54
IDTK.L,IDTK.L,single_country,3.038612213345268,False,0.27,34.39
IAUS.L,IAUS.L,single_country,6.158876846934014,False,57.88,41.22
CCAU.L,CCAU.L,single_country,6.019189972803409,False,50.96,41.63
IPOL.L,IPOL.L,single_country,5.9862680045386965,False,49.31,42.22
XVTD.L,XVTD.L,single_country,4.267595605932006,False,3.03,36.69
HIDD.L,HIDD.L,single_country,4.911920159880013,False,10.19,35.88
IWVL.L,IWVL.L,factor_value,6.908509902767764,False,86.02,47.48
IWQU.L,IWQU.L,factor_quality,6.408159229534564,False,69.35,44.24
IWMO.L,IWMO.L,factor_momentum,6.399748980686123,False,68.99,44.06
MVOL.L,MVOL.L,factor_min_vol,6.384072338188178,False,68.31,44.02
XDEV.L,XDEV.L,factor_value,6.217722114598912,False,60.72,44.48
XDEQ.L,XDEQ.L,factor_quality,5.71134111829968,False,35.96,40.36
XDEM.L,XDEM.L,factor_momentum,5.899971996228572,False,45.02,40.51
XDEB.L,XDEB.L,factor_min_vol,5.518845704146889,False,27.64,40.46
IUVL.L,IUVL.L,factor_value,6.711310347931565,False,80.57,46.43
IUQA.L,IUQA.L,factor_quality,6.460482979003613,False,71.52,44.79
IUMO.L,IUMO.L,factor_momentum,6.628179237309038,False,77.84,43.29
SPMV.L,SPMV.L,factor_min_vol,5.952119182827995,False,47.61,41.17
EMVL.L,EMVL.L,factor_value,6.429873963600726,False,70.26,44.13
IEFV.L,IEFV.L,factor_value,5.7594482218399685,False,38.2,43.57
IEFQ.L,IEFQ.L,factor_quality,5.500678849609203,False,26.92,40.42
IEFM.L,IEFM.L,factor_momentum,5.639650014148692,False,32.72,41.08
JPGL.L,JPGL.L,factor_multi,5.1381541876276,False,15.14,38.53
MOAT.L,MOAT.L,factor_quality,5.604261496554293,False,31.19,36.86
WDSC.L,WDSC.L,size_small_cap,5.553000796257419,False,26.13,45.53
USSC.L,USSC.L,size_small_cap_value,5.936027667063775,False,46.81,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,5.046807739264287,False,12.94,37.07
SPEQ.L,SPEQ.L,equal_weight,6.225804057546936,False,61.1,42.26
VHYA.L,VHYD.L,dividend,6.5668559924904,False,59.35,48.01
VHYD.L,VHYD.L,dividend,6.188382475719509,False,40.65,50.34
FUSD.L,FUSD.L,dividend_quality,5.473225590828166,False,25.85,38.09
FGQI.L,FGQI.L,dividend_quality,5.24141032316422,False,17.99,37.29
GLDV.L,GLDV.L,dividend,5.469536748908836,False,25.71,39.83
UDVD.L,UDVD.L,dividend,6.03930565339155,False,51.96,41.58
WQDV.L,WQDV.L,dividend_quality,5.885608281444168,False,44.31,41.46
QDIV.L,QDIV.L,dividend_quality,5.389053172737992,False,22.76,37.32
TDIV.L,TDIV.L,dividend,6.195680592742099,False,59.66,44.59
HDLV.L,HDLV.L,dividend_low_vol,5.704000992844426,False,35.62,40.44
DGRA.L,DGRA.L,dividend_quality,5.595302546103721,False,30.8,38.48
GGRA.L,GGRA.L,dividend_quality,5.539360489565074,False,28.47,39.2
EUDV.L,EUDV.L,dividend,5.411240942294628,False,23.55,40.49
IDVY.L,IDVY.L,dividend,5.941884935592632,False,47.1,41.73
IUIT.L,IUIT.L,sector_tech,7.282935772405501,False,88.08,49.92
SXLK.L,SXLK.L,sector_tech,6.29620172010835,False,64.39,45.08
XLKS.L,XLKS.L,sector_tech,6.293344102696277,False,64.26,45.96
XDWT.L,XDWT.L,sector_tech,6.327156801350893,False,65.8,44.13
WTEC.L,WTEC.L,sector_tech,5.882263769154431,False,44.14,38.34
IUHC.L,IUHC.L,sector_health,6.754238467097834,False,81.88,49.63
SXLV.L,SXLV.L,sector_health,6.061140205883448,False,53.05,45.91
XLVS.L,XLVS.L,sector_health,5.68920227071177,False,34.94,44.01
XDWH.L,WHEA.L,sector_health,6.165251302091379,False,60.25,55.44
WHEA.L,WHEA.L,sector_health,5.749239708409457,False,39.75,47.22
IUFS.L,IUFS.L,sector_financials,6.598591489423826,False,76.8,47.69
SXLF.L,SXLF.L,sector_financials,5.6282437396002925,False,32.22,41.53
XLFS.L,XLFS.L,sector_financials,5.455586781648586,False,25.18,40.07
XDWF.L,WFIN.L,sector_financials,5.731065676653232,False,67.12,55.81
WFIN.L,WFIN.L,sector_financials,5.017307483383043,False,32.88,46.75
IUES.L,IUES.L,sector_energy,6.763166861343227,False,82.15,48.23
SXLE.L,SXLE.L,sector_energy,6.28115772592371,False,63.7,45.52
XLES.L,XLES.L,sector_energy,6.149333988939061,False,57.41,41.55
XDW0.L,WNRG.L,sector_energy,6.071916560969158,False,60.63,55.0
WNRG.L,WNRG.L,sector_energy,5.639954507996999,False,39.37,47.38
IOGP.L,IOGP.L,sector_energy,5.605258048233464,False,31.23,36.17
IUCD.L,IUCD.L,sector_consumer_disc,6.01374043168127,False,50.69,42.92
SXLY.L,SXLY.L,sector_consumer_disc,4.676206485888362,False,6.61,36.23
XDWC.L,WCOD.L,sector_consumer_disc,4.8750306899349765,False,90.54,57.95
WCOD.L,WCOD.L,sector_consumer_disc,2.6158448925043576,False,9.46,44.31
IUCS.L,IUCS.L,sector_consumer_staples,6.177124140499308,False,58.76,46.39
SXLP.L,SXLP.L,sector_consumer_staples,5.720978726030311,False,36.4,43.73
XDWS.L,XDWS.L,sector_consumer_staples,5.5868581338751735,False,30.44,41.16
IUIS.L,IUIS.L,sector_industrials,6.3480845314441625,False,66.73,45.18
SXLI.L,SXLI.L,sector_industrials,6.178675530713796,False,58.84,45.18
XDWI.L,XDWI.L,sector_industrials,5.72385956843171,False,36.53,41.14
IUUS.L,IUUS.L,sector_utilities,6.498984799213109,False,73.07,48.81
SXLU.L,SXLU.L,sector_utilities,5.594793585240955,False,30.78,42.66
XDWU.L,XDWU.L,sector_utilities,5.629568898735081,False,32.28,40.73
IUMS.L,IUMS.L,sector_materials,5.928484040783257,False,46.43,44.14
SXLB.L,SXLB.L,sector_materials,4.710582825818458,False,7.05,39.26
XDWM.L,XDWM.L,sector_materials,5.431784601674066,False,24.3,39.7
IUCM.L,IUCM.L,sector_communication,6.508308623548192,False,73.43,45.41
SXLC.L,SXLC.L,sector_communication,5.7099925553766,False,35.89,40.19
XWTS.L,XWTS.L,sector_communication,5.322017079170049,False,20.49,35.61
SMH.L,SMH.L,theme_semiconductors,7.53816818613404,False,88.08,45.19
SEMI.L,SEMI.L,theme_semiconductors,7.074329648703523,False,88.08,45.1
SEMU.L,SEMU.L,theme_semiconductors,5.75994992590114,False,38.22,39.52
AIAI.L,AIAI.L,theme_ai,6.3893147355346125,False,68.54,41.8
WTAI.L,WTAI.L,theme_ai,5.99286921610911,False,49.64,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,5.412275785694197,False,23.59,33.75
RBOT.L,RBOT.L,theme_ai_robotics,6.455001759858206,False,71.3,43.84
ROBO.L,ROBO.L,theme_ai_robotics,5.881798673151988,False,44.12,39.93
DGTL.L,DGTL.L,theme_digital_tech,5.5578001468842,False,29.23,37.07
XNGI.L,XNGI.L,theme_digital_tech,0.0,False,0.0,30.8
ITEK.L,ITEK.L,theme_digital_tech,4.41619672633666,False,4.04,32.68
WCLD.L,WCLD.L,theme_cloud,6.33988011883475,False,66.37,38.24
LOCK.L,LOCK.L,theme_cybersecurity,6.302752667047204,False,64.69,41.54
USPY.L,USPY.L,theme_cybersecurity,6.462876233709377,False,71.62,40.83
WCBR.L,WCBR.L,theme_cybersecurity,5.787336726105456,False,39.52,36.33
HEAL.L,HEAL.L,theme_health_innovation,6.00371174142288,False,50.19,42.54
BTEC.L,BTEC.L,theme_biotech,6.374577370542239,False,67.9,43.97
SBIO.L,SBIO.L,theme_biotech,6.158973649797511,False,57.88,41.16
INRG.L,INRG.L,theme_clean_energy,6.236580485971756,False,61.61,41.88
RENW.L,RENW.L,theme_clean_energy,5.514419304782578,False,27.46,36.63
HTWO.L,HTWO.L,theme_clean_energy,4.460195180134146,False,4.4,35.08
ECAR.L,ECAR.L,theme_ev_battery,5.528604087998969,False,28.03,37.63
BATT.L,BATT.L,theme_ev_battery,5.466426760715221,False,25.59,37.85
IH2O.L,IH2O.L,theme_water,5.847337982390824,False,42.43,41.27
WATU.L,WATU.L,theme_water,4.563812599787752,False,5.35,38.39
GLUG.L,GLUG.L,theme_water,5.735968937966619,False,37.1,39.87
NATO.L,NATO.L,theme_defence,5.933483928696754,False,46.68,39.05
DFNS.L,DFNS.L,theme_defence,6.541387592504507,False,74.7,42.49
IGLN.L,PHAU.L,gold_physical_etc,7.457986494694415,False,73.26,54.79
SGLD.L,PHAU.L,gold_physical_etc,7.154587335320441,False,73.26,54.36
XGDU.L,XGDU.L,gold_physical_etc,5.923864042722253,False,46.2,48.98
WGLD.L,PHAU.L,gold_physical_etc,6.089263918202438,False,30.71,45.81
PHAU.L,PHAU.L,gold_physical_etc,6.496056075265185,False,50.0,36.69
SGBX.L,SGBX.L,gold_physical_etc,5.131859277349202,False,14.98,42.94
XGLD.L,PHAU.L,gold_physical_etc,5.175010298699073,False,6.65,34.54
RMAU.L,RMAU.L,gold_physical_etc,5.663554879914911,False,33.78,41.74
GDX.L,GDX.L,gold_miners,7.118069855816217,False,88.08,47.27
GDXJ.L,GDXJ.L,gold_miners,6.491061157635495,False,72.75,43.98
IAUP.L,IAUP.L,gold_miners,6.394140742442056,False,68.75,45.68
AUCO.L,AUCO.L,gold_miners,5.933463669155026,False,46.68,41.04
ISLN.L,PHAG.L,silver_physical_etc,6.619130692254811,False,77.2,55.13
SSLV.L,PHAG.L,silver_physical_etc,5.945623100684371,False,46.83,53.25
PHAG.L,PHAG.L,silver_physical_etc,6.009172157936124,False,50.0,37.57
SILV.L,SILV.L,silver_miners,6.343682893559746,False,66.54,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,5.047778212389696,False,12.96,38.29
IPLT.L,IPLT.L,platinum_physical_etc,5.253982684916738,False,18.36,42.09
IPDM.L,IPDM.L,palladium_physical_etc,5.026606402925403,False,12.49,41.44
CMOD.L,CMOD.L,commodities_broad,6.639447938941959,False,78.23,43.98
ICOM.L,ICOM.L,commodities_broad,6.574887702832197,False,75.95,45.76
BCOM.L,BCOM.L,commodities_broad,4.704250802685055,False,6.97,38.59
COMF.L,COMF.L,commodities_broad,5.151269808112856,False,15.48,36.88
ROLL.L,ROLL.L,commodities_broad,5.641649130326413,False,32.81,39.95
WCOA.L,WCOA.L,commodities_broad,5.518293987229133,False,27.62,38.51
ENCO.L,ENCO.L,commodities_broad,5.486124034899779,False,26.35,36.22
AIGC.L,AIGC.L,commodities_broad_etc,3.923608321839785,False,1.55,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,5.655189269308588,False,33.41,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,6.391607750883785,False,68.64,43.59
BRNT.L,BRNT.L,commodities_energy_etc,7.00846486855976,False,88.08,42.51
CRUD.L,CRUD.L,commodities_energy_etc,6.812489328610703,False,83.55,42.13
GDIG.L,GDIG.L,commodity_equity_mining,6.0776454266702045,False,53.87,43.0
COPX.L,COPX.L,commodity_equity_mining,6.621796586951763,False,77.62,42.56
REMX.L,REMX.L,commodity_equity_mining,6.120602333412982,False,56.0,41.2
URNU.L,URNU.L,commodity_equity_uranium,5.96483390276574,False,48.24,37.49
URNM.L,URNM.L,commodity_equity_uranium,5.796681646877234,False,39.97,36.43
SPAG.L,SPAG.L,commodity_equity_agri,5.764402052003811,False,38.43,40.15
WOOD.L,WOOD.L,commodity_equity_timber,4.807793923261491,False,8.44,34.99
DPYA.L,DPYA.L,reit_global,5.497095879954314,False,26.78,40.49
GLRA.L,GLRA.L,reit_global,4.444566562997995,False,4.27,36.71
HPRD.L,HPRD.L,reit_global,5.403490150002849,False,23.27,40.52
EPRA.L,EPRA.L,reit_global,4.981131738641015,False,11.53,39.75
TRET.L,TRET.L,reit_global,3.711692101626226,False,1.02,36.78
IDUP.L,IDUP.L,reit_us,5.817654877639251,False,40.98,39.63
XRES.L,XRES.L,reit_us,6.067174160454463,False,53.35,44.93
IPRP.L,IPRP.L,reit_europe,5.57463257750919,False,29.93,39.51
XDER.L,XDER.L,reit_europe,4.032136842870633,False,1.92,37.62
IDAR.L,IDAR.L,reit_asia,3.848623199118934,False,1.34,35.09
IUKP.L,IUKP.L,reit_uk,6.241167458613552,False,61.83,43.05
IDIN.L,IDIN.L,infrastructure_global,5.720925950293439,False,36.4,40.84
XGID.L,XGID.L,infrastructure_global,4.069673819128155,False,2.06,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,5.06714608670519,False,13.4,37.41
PAVE.L,PAVE.L,infrastructure_us,6.0556244896662,False,52.78,38.56
MAGG.L,MAGG.L,multi_asset_growth,5.110408177393168,False,14.44,37.37
MAMG.L,MAMG.L,multi_asset_moderate,5.103552086663186,False,14.27,38.02
MACG.L,MACG.L,multi_asset_conservative,3.7990353037928615,False,1.21,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,2.417189271501976,False,0.08,30.24
ACWD.L,ACWD.L,global,7.090740983051966,False,50.0,56.16
SPYY.L,SPYY.L,global,2.979351665397929,False,0.24,36.04
EXUS.L,EXUS.L,developed_ex_us,6.801745632882057,False,83.25,48.48

