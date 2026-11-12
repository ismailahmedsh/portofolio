# Pillar CST10: 15-year all-in cost per deposited dollar (line choice)
Definition: Expected annual cost in bps:
CST10_i = -(TD_ref + G_i) + 0.5 x TAX03_i + amortised entry costs + FX cost for a non-USD line.
- TD_ref is the reference line's absolute tracking difference against the net index (iShares table; positive means it beat the index). Where it is unavailable it is set to 0; it is common to every line in the sleeve, so the ranking is unchanged.
- G_i is CST02's TER-restated raw gap, so the TER currently charged is included exactly once.
- TAX03 is now the tax-rule-dependent advantage beyond TER.
- Entry costs are spread over 15 years: the commission share, half the spread where CST05 or CST09 exist, and residue x r_forgone. r_forgone = 0.6% a month, the expected nominal equity return given up while money waits; it is one constant in pillar_scales.yaml, shared with allocation 3(a).
If CST02 is missing for the sleeve (fail-closed), every candidate uses TERnow + TAX01 instead. Weight 0; it ranks lines inside a sleeve. A unit test reproduces the worked figures below.
Source: Derived from CST01, CST02, CST05, CST08, CST09, TAX01, TAX03; IBKR commission US$1.70 minimum and FX US$2 minimum | STATUS: verified for iShares-only sleeves; unverified and fails closed for Vanguard, Invesco and Xtrackers lines until ter_history is seeded from another source (justETF snapshots from now on, or annual reports via the Central Bank of Ireland register) (unverified). Better when: lower. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope        |    CST10 | buyable   |   line_score |
|:-------|:----------|:-------------|---------:|:----------|-------------:|
| VDTA.L | VDTA.L    | government   |  6.66977 | False     |        54.89 |
| VDST.L | VDST.L    | government   |  6.66977 | False     |        56.33 |
| IB01.L | IB01.L    | government   |  8.66977 | False     |        55.34 |
| VDPA.L | VDPA.L    | corporate    |  8.66977 | False     |        55.04 |
| CBU0.L | CBU0.L    | government   |  8.66977 | False     |        57.53 |
| CBU7.L | CBU7.L    | government   |  8.66977 | False     |        55.46 |
| IBTA.L | IBTA.L    | government   |  8.66977 | False     |        56.49 |
| CBU3.L | CBU3.L    | government   |  8.66977 | False     |        49.56 |
| DTLA.L | DTLA.L    | government   |  8.66977 | False     |        56.46 |
| VAGU.L | VAGU.L    | aggregate    |  9.66977 | False     |        52.19 |
| ERNA.L | ERNA.L    | money-market | 10.6698  | False     |        54.21 |
| VDCA.L | VDCA.L    | corporate    | 10.6698  | False     |        52.24 |
| GLAD.L | GLAD.L    | aggregate    | 11.6698  | False     |        49.15 |
| AGGU.L | AGGU.L    | aggregate    | 11.6698  | False     |        53.29 |
| TRSY.L | TRSY.L    | government   | 11.6698  | False     |        51.52 |
|        | cluster   | scope                    |   CST10 | buyable   |   line_score |
|:-------|:----------|:-------------------------|--------:|:----------|-------------:|
| URNU.L | URNU.L    | commodity_equity_uranium | 74.7502 | False     |        37.49 |
| IPOL.L | IPOL.L    | single_country           | 75.6698 | False     |        42.22 |
| IH2O.L | IH2O.L    | theme_water              | 76.6698 | False     |        41.27 |
| WOOD.L | WOOD.L    | commodity_equity_timber  | 76.6698 | False     |        34.99 |
| KWEB.L | KWEB.L    | single_country           | 76.9629 | False     |        42.61 |
| IDTK.L | IDTK.L    | single_country           | 80.6698 | False     |        34.39 |
| USPY.L | USPY.L    | theme_cybersecurity      | 85.64   | False     |        40.83 |
| FXC.L  | FXC.L     | single_country           | 85.6698 | False     |        40.02 |
| IBZL.L | IBZL.L    | single_country           | 85.6698 | False     |        40.27 |
| INRG.L | INRG.L    | theme_clean_energy       | 85.865  | False     |        41.88 |
| IFFF.L | IFFF.L    | asia_pacific             | 86.2847 | False     |        42.22 |
| XVTD.L | XVTD.L    | single_country           | 86.6698 | False     |        36.69 |
| ROBO.L | ROBO.L    | theme_ai_robotics        | 90.5052 | False     |        39.93 |
| ITWN.L | ITWN.L    | single_country           | 90.823  | False     |        44.63 |
| URNM.L | URNM.L    | commodity_equity_uranium | 93.2892 | False     |        36.43 |

## All lines (csv)
,cluster,scope,CST10,buyable,line_score
IB01.L,IB01.L,government,8.669772458148708,False,55.34
VDST.L,VDST.L,government,6.669772458148708,False,56.33
IBTA.L,IBTA.L,government,8.669772458148708,False,56.49
CBU3.L,CBU3.L,government,8.669772458148708,False,49.56
XUT3.L,XUT3.L,government,12.669772458148708,False,46.44
TRE3.L,TRE3.L,government,12.669772458148708,False,48.81
US13.L,US13.L,government,12.669772458148708,False,49.83
CBU7.L,CBU7.L,government,8.669772458148708,False,55.46
CBU0.L,CBU0.L,government,8.669772458148708,False,57.53
TREX.L,TREX.L,government,12.669772458148708,False,50.59
US71.L,US71.L,government,12.669772458148708,False,50.86
DTLA.L,DTLA.L,government,8.669772458148708,False,56.46
US10.L,US10.L,government,12.669772458148708,False,48.53
VDTA.L,VDTA.L,government,6.669772458148708,False,54.89
XUTD.L,XUTD.L,government,12.669772458148708,False,48.42
TRES.L,TRES.L,government,12.669772458148708,False,49.65
TRSY.L,TRSY.L,government,11.669772458148708,False,51.52
IGLA.L,IGLA.L,government,21.669772458148707,False,43.86
XGGB.L,XGGB.L,government,21.669772458148707,False,39.18
IGLT.L,IGLT.L,government,18.669772458148707,False,55.37
IGLS.L,IGLS.L,government,18.669772458148707,False,55.3
SEGA.L,SEGA.L,government,18.669772458148707,False,51.69
XGLE.L,XGLE.L,government,13.669772458148708,False,50.27
AGGU.L,AGGU.L,aggregate,11.669772458148708,False,53.29
VAGU.L,VAGU.L,aggregate,9.669772458148708,False,52.19
GLAD.L,GLAD.L,aggregate,11.669772458148708,False,49.15
AGGG.L,AGGG.L,aggregate,16.669772458148707,False,50.77
GAGU.L,GAGU.L,aggregate,11.669772458148708,False,45.51
IUAA.L,IUAA.L,aggregate,26.669772458148707,False,46.09
USAG.L,USAG.L,aggregate,23.669772458148707,False,37.76
IDTP.L,IDTP.L,inflation-linked,11.669772458148708,False,51.6
TIP5.L,TIP5.L,inflation-linked,16.669772458148707,False,50.32
TIPU.L,TIPU.L,inflation-linked,15.669772458148708,False,46.67
TIPS.L,TIPS.L,inflation-linked,11.669772458148708,False,50.29
IGIL.L,IGIL.L,inflation-linked,21.669772458148707,False,42.21
XG7U.L,XG7U.L,inflation-linked,26.669772458148707,False,39.07
INXG.L,INXG.L,inflation-linked,21.669772458148707,False,48.38
IBCI.L,IBCI.L,inflation-linked,15.669772458148708,False,50.61
LQDA.L,LQDA.L,corporate,21.669772458148707,False,47.08
VDPA.L,VDPA.L,corporate,8.669772458148708,False,55.04
SDIA.L,SDIA.L,corporate,21.669772458148707,False,47.71
VDCA.L,VDCA.L,corporate,10.669772458148708,False,52.24
SUSU.L,SUSU.L,corporate,18.669772458148707,False,44.72
ICBU.L,ICBU.L,corporate,21.669772458148707,False,44.79
XDGU.L,XDGU.L,corporate,18.669772458148707,False,45.21
CRPU.L,CRPU.L,corporate,26.669772458148707,False,43.78
HLQD.L,HLQD.L,corporate,34.855855621211155,False,38.11
FLOA.L,FLOA.L,corporate,13.502135711348297,False,53.11
UCRP.L,UCRP.L,corporate,30.676266762312448,False,40.12
IEAA.L,IEAA.L,corporate,15.669772458148708,False,53.5
IHYA.L,IHYA.L,high-yield,57.66017263990695,False,43.09
HYLA.L,HYLA.L,high-yield,51.66977245814871,False,41.94
XUHY.L,XUHY.L,high-yield,33.73305113599181,False,38.81
HYUS.L,HYUS.L,high-yield,33.020936241244826,False,37.91
DHYA.L,DHYA.L,high-yield,31.831163478809245,False,38.55
WIAU.L,WIAU.L,high-yield,51.66977245814871,False,40.71
SJNK.L,SJNK.L,high-yield,45.78450363722956,False,35.96
HIGH.L,HIGH.L,high-yield,56.66977245814871,False,41.38
XHYG.L,HIGH.L,high-yield,31.669772458148707,False,51.8
JPEA.L,JPEA.L,em-debt,46.66977245814871,False,44.92
VDEA.L,VDEA.L,em-debt,24.669772458148707,False,42.08
EMSA.L,EMSA.L,em-debt,46.66977245814871,False,39.48
EMCA.L,EMCA.L,em-debt,51.66977245814871,False,43.87
EMGA.L,EMGA.L,em-debt,51.66977245814871,False,43.83
EMDD.L,EMDD.L,em-debt,61.66977245814872,False,39.95
EMLC.L,EMLC.L,em-debt,31.669772458148707,False,36.44
EMLB.L,EMLB.L,em-debt,40.66977245814871,False,36.59
ERNA.L,ERNA.L,money-market,10.669772458148708,False,54.21
JPSA.L,JPSA.L,money-market,19.669772458148707,False,41.89
ERNS.L,ERNS.L,money-market,20.669772458148707,False,54.59
XSTR.L,XSTR.L,money-market,21.669772458148707,False,47.73
ERNE.L,ERNE.L,money-market,20.669772458148707,False,50.97
VWRA.L,VWRA.L,global,24.63873785352389,True,52.93
ISAC.L,ACWD.L,global,30.91896416579217,False,49.57
IWDA.L,IWDA.L,global,32.25217985255145,False,51.14
XDWD.L,IWDA.L,global,24.14238426759845,False,50.13
SWRD.L,IWDA.L,global,24.28678027582939,False,51.37
HMWD.L,IWDA.L,global,32.3363472198326,False,50.13
FWRA.L,VWRA.L,global,25.630918768769803,False,48.74
VHVE.L,VHVE.L,global,23.345094914783843,False,49.78
WSML.L,WDSC.L,global,42.88620372281567,False,57.19
CSPX.L,XSPU.L,us,23.46099795421306,False,52.34
VUAA.L,XSPU.L,us,23.258141430784427,False,48.24
SPXS.L,XSPU.L,us,13.961463520771488,False,56.04
SPY5.L,XSPU.L,us,24.36870428496568,False,52.82
HSPD.L,XSPU.L,us,30.402895181179083,False,47.04
XSPU.L,XSPU.L,us,24.03785316349224,False,45.12
CNDX.L,CNDX.L,us,43.37862858576318,False,56.06
EQQU.L,CNDX.L,us,48.50650221542267,False,51.98
XNAS.L,CNDX.L,us,33.362373682292166,False,52.88
XDEW.L,XDEW.L,us,28.33807619356309,False,45.25
CSUS.L,CSUS.L,us,19.63996242215065,False,55.65
VNRA.L,VNRA.L,us,26.50872827403281,False,50.32
R2US.L,R2US.L,us,47.00656041373782,False,41.95
SPY4.L,SPY4.L,us,46.434351356941065,False,40.78
CUSS.L,CUSS.L,us,55.047779001075845,False,41.01
VEUA.L,VEUA.L,europe,16.669772458148707,False,53.64
VERG.L,VERG.L,europe,16.669772458148707,False,53.18
SMEA.L,SMEA.L,europe,18.669772458148707,False,53.99
IEUX.L,IEUX.L,europe,51.66977245814871,False,42.26
CSX5.L,CSX5.L,europe,16.669772458148707,False,54.36
XESC.L,XESC.L,europe,15.669772458148708,False,52.88
XDAX.L,XDAX.L,single_country,15.669772458148708,False,51.89
CACX.L,CACX.L,single_country,36.66977245814871,False,43.14
CSWG.L,CSWG.L,single_country,31.669772458148707,False,40.53
IAEX.L,IAEX.L,single_country,41.66977245814871,False,40.2
CUKX.L,CUKX.L,uk,13.669772458148708,False,56.68
VUKG.L,HUKX.L,uk,15.669772458148708,False,50.05
VMIG.L,MIDD.L,uk,19.19467961271496,False,50.69
MIDD.L,MIDD.L,uk,54.4146631531392,False,41.43
HUKX.L,HUKX.L,uk,18.669772458148707,False,50.86
CUKS.L,CUKS.L,uk,66.14962188113282,False,34.47
IJPA.L,IJPA.L,japan,16.669772458148707,False,49.67
CSJP.L,CSJP.L,japan,54.98241944262298,False,40.3
VJPA.L,VJPA.L,japan,16.669772458148707,False,46.36
XMJD.L,XMJD.L,japan,13.669772458148708,False,58.22
HMJD.L,XMJD.L,japan,25.669772458148707,False,45.61
LCJP.L,LCJP.L,japan,18.864270635388092,False,49.25
XDJP.L,XDJP.L,japan,27.5272810835473,False,49.3
IDJP.L,IDJP.L,japan,64.6697724581487,False,36.72
CPXJ.L,CPXJ.L,asia_pacific,22.431577893889784,False,46.93
VAPU.L,VAPU.L,asia_pacific,16.669772458148707,False,48.27
HMXJ.L,HMXJ.L,asia_pacific,55.15044792829015,False,38.25
XPXD.L,XPXD.L,asia_pacific,30.750096763430584,False,38.17
IFFF.L,IFFF.L,asia_pacific,86.28472371277275,False,42.22
HMAD.L,HMAD.L,asia_pacific,52.07677079673078,False,36.71
XMAD.L,XMAD.L,asia_pacific,66.8971869774331,False,37.77
EIMI.L,EIMI.L,emerging,19.669772458148707,False,50.71
VFEA.L,VFEA.L,emerging,18.987907660889977,False,48.22
IEMA.L,IEMA.L,emerging,19.669772458148707,False,50.65
XMME.L,XMMD.L,emerging,19.669772458148707,False,54.27
HMEM.L,XMMD.L,emerging,46.66977245814871,False,50.55
EMXC.L,EMXC.L,emerging,16.87337182535895,False,50.31
EMSD.L,EMSD.L,emerging,59.14285288967295,False,35.56
XMMD.L,XMMD.L,emerging,50.66977245814871,False,43.02
NDIA.L,XCS5.L,single_country,66.66977245814871,False,41.67
FLXI.L,FLXI.L,single_country,25.669772458148707,False,43.0
XCS5.L,XCS5.L,single_country,20.669772458148707,False,53.7
CNYA.L,CNYA.L,single_country,42.64896595981013,False,44.98
XCS6.L,XCS6.L,single_country,66.66977245814871,False,40.47
HMCD.L,XCS6.L,single_country,36.66977245814871,False,54.0
FXC.L,FXC.L,single_country,85.66977245814871,False,40.02
KWEB.L,KWEB.L,single_country,76.96291297517291,False,42.61
CSKR.L,CSKR.L,single_country,66.66977245814871,False,42.54
ITWN.L,ITWN.L,single_country,90.82302081756222,False,44.63
XMTD.L,ITWN.L,single_country,71.49064403852068,False,47.64
IBZL.L,IBZL.L,single_country,85.66977245814871,False,40.27
XMBD.L,IBZL.L,single_country,26.669772458148707,False,53.91
CMXC.L,CMXC.L,single_country,66.66977245814871,False,35.56
IKSA.L,IKSA.L,single_country,65.66287355386159,False,37.6
IRSA.L,IRSA.L,single_country,66.66977245814871,False,36.54
IDTK.L,IDTK.L,single_country,80.66977245814871,False,34.39
IAUS.L,IAUS.L,single_country,53.38740041778252,False,41.22
CCAU.L,CCAU.L,single_country,54.32181813276088,False,41.63
IPOL.L,IPOL.L,single_country,75.66977245814871,False,42.22
XVTD.L,XVTD.L,single_country,86.66977245814871,False,36.69
HIDD.L,HIDD.L,single_country,56.66977245814871,False,35.88
IWVL.L,IWVL.L,factor_value,28.08375628868656,False,47.48
IWQU.L,IWQU.L,factor_quality,35.534077226703154,False,44.24
IWMO.L,IWMO.L,factor_momentum,36.02645688692413,False,44.06
MVOL.L,MVOL.L,factor_min_vol,31.669772458148707,False,44.02
XDEV.L,XDEV.L,factor_value,35.47749193616076,False,44.48
XDEQ.L,XDEQ.L,factor_quality,42.5138140124507,False,40.36
XDEM.L,XDEM.L,factor_momentum,41.86738281678407,False,40.51
XDEB.L,XDEB.L,factor_min_vol,34.78597433056916,False,40.46
IUVL.L,IUVL.L,factor_value,29.593048832155148,False,46.43
IUQA.L,IUQA.L,factor_quality,33.59531702729787,False,44.79
IUMO.L,IUMO.L,factor_momentum,31.151664911632977,False,43.29
SPMV.L,SPMV.L,factor_min_vol,31.056474235561154,False,41.17
EMVL.L,EMVL.L,factor_value,41.66977245814871,False,44.13
IEFV.L,IEFV.L,factor_value,31.669772458148707,False,43.57
IEFQ.L,IEFQ.L,factor_quality,31.669772458148707,False,40.42
IEFM.L,IEFM.L,factor_momentum,31.669772458148707,False,41.08
JPGL.L,JPGL.L,factor_multi,22.476182809404985,False,38.53
MOAT.L,MOAT.L,factor_quality,57.643069695828665,False,36.86
WDSC.L,WDSC.L,size_small_cap,53.01554213033824,False,45.53
USSC.L,USSC.L,size_small_cap_value,39.08729235168951,False,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,40.37550522316623,False,37.07
SPEQ.L,SPEQ.L,equal_weight,29.290077120452946,False,42.26
VHYA.L,VHYD.L,dividend,30.869484720826527,False,48.01
VHYD.L,VHYD.L,dividend,35.91980765535742,False,50.34
FUSD.L,FUSD.L,dividend_quality,42.57361681325602,False,38.09
FGQI.L,FGQI.L,dividend_quality,54.152134726626045,False,37.29
GLDV.L,GLDV.L,dividend,51.66977245814871,False,39.83
UDVD.L,UDVD.L,dividend,41.81138685800129,False,41.58
WQDV.L,WQDV.L,dividend_quality,48.368765203334654,False,41.46
QDIV.L,QDIV.L,dividend_quality,52.356246859823706,False,37.32
TDIV.L,TDIV.L,dividend,44.66977245814871,False,44.59
HDLV.L,HDLV.L,dividend_low_vol,36.66977245814871,False,40.44
DGRA.L,DGRA.L,dividend_quality,44.94893826534251,False,38.48
GGRA.L,GGRA.L,dividend_quality,44.44440507650769,False,39.2
EUDV.L,EUDV.L,dividend,41.66977245814871,False,40.49
IDVY.L,IDVY.L,dividend,51.66977245814871,False,41.73
IUIT.L,IUIT.L,sector_tech,28.47168873516488,False,49.92
SXLK.L,SXLK.L,sector_tech,28.53401964648624,False,45.08
XLKS.L,XLKS.L,sector_tech,27.505365372008605,False,45.96
XDWT.L,XDWT.L,sector_tech,38.33684295759293,False,44.13
WTEC.L,WTEC.L,sector_tech,43.41012256966769,False,38.34
IUHC.L,IUHC.L,sector_health,16.669772458148707,False,49.63
SXLV.L,SXLV.L,sector_health,16.669772458148707,False,45.91
XLVS.L,XLVS.L,sector_health,15.66977245814871,False,44.01
XDWH.L,WHEA.L,sector_health,26.669772458148707,False,55.44
WHEA.L,WHEA.L,sector_health,31.669772458148707,False,47.22
IUFS.L,IUFS.L,sector_financials,26.44769122913585,False,47.69
SXLF.L,SXLF.L,sector_financials,26.41922506752667,False,41.53
XLFS.L,XLFS.L,sector_financials,25.491977553268136,False,40.07
XDWF.L,WFIN.L,sector_financials,32.61280763377837,False,55.81
WFIN.L,WFIN.L,sector_financials,37.58651094340518,False,46.75
IUES.L,IUES.L,sector_energy,26.46205343236577,False,48.23
SXLE.L,SXLE.L,sector_energy,26.6693081538707,False,45.52
XLES.L,XLES.L,sector_energy,26.70129739261276,False,41.55
XDW0.L,WNRG.L,sector_energy,34.070822244249506,False,55.0
WNRG.L,WNRG.L,sector_energy,39.42135322789484,False,47.38
IOGP.L,IOGP.L,sector_energy,70.71281927185203,False,36.17
IUCD.L,IUCD.L,sector_consumer_disc,31.60344786813528,False,42.92
SXLY.L,SXLY.L,sector_consumer_disc,31.63996242215065,False,36.23
XDWC.L,WCOD.L,sector_consumer_disc,38.31068611184623,False,57.95
WCOD.L,WCOD.L,sector_consumer_disc,43.3314402606684,False,44.31
IUCS.L,IUCS.L,sector_consumer_staples,16.669772458148707,False,46.39
SXLP.L,SXLP.L,sector_consumer_staples,16.669772458148707,False,43.73
XDWS.L,XDWS.L,sector_consumer_staples,26.669772458148707,False,41.16
IUIS.L,IUIS.L,sector_industrials,25.29163053474027,False,45.18
SXLI.L,SXLI.L,sector_industrials,25.13093584110007,False,45.18
XDWI.L,XDWI.L,sector_industrials,30.97439559920726,False,41.14
IUUS.L,IUUS.L,sector_utilities,16.669772458148707,False,48.81
SXLU.L,SXLU.L,sector_utilities,16.669772458148707,False,42.66
XDWU.L,XDWU.L,sector_utilities,26.669772458148707,False,40.73
IUMS.L,IUMS.L,sector_materials,16.71826639224141,False,44.14
SXLB.L,SXLB.L,sector_materials,16.78115306094883,False,39.26
XDWM.L,XDWM.L,sector_materials,26.669772458148707,False,39.7
IUCM.L,IUCM.L,sector_communication,31.37414244728744,False,45.41
SXLC.L,SXLC.L,sector_communication,30.95129575261811,False,40.19
XWTS.L,XWTS.L,sector_communication,41.00596134425716,False,35.61
SMH.L,SMH.L,theme_semiconductors,44.41304670542057,False,45.19
SEMI.L,SEMI.L,theme_semiconductors,48.366626461996965,False,45.1
SEMU.L,SEMU.L,theme_semiconductors,45.12411241903513,False,39.52
AIAI.L,AIAI.L,theme_ai,61.91789193197146,False,41.8
WTAI.L,WTAI.L,theme_ai,51.38827230471881,False,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,62.10993572120945,False,33.75
RBOT.L,RBOT.L,theme_ai_robotics,50.87812489849309,False,43.84
ROBO.L,ROBO.L,theme_ai_robotics,90.5052249620727,False,39.93
DGTL.L,DGTL.L,theme_digital_tech,56.39215630180696,False,37.07
XNGI.L,XNGI.L,theme_digital_tech,43.04394531996387,False,30.8
ITEK.L,ITEK.L,theme_digital_tech,71.88946932580164,False,32.68
WCLD.L,WCLD.L,theme_cloud,56.639962422150646,False,38.24
LOCK.L,LOCK.L,theme_cybersecurity,56.639962422150646,False,41.54
USPY.L,USPY.L,theme_cybersecurity,85.63996242215066,False,40.83
WCBR.L,WCBR.L,theme_cybersecurity,61.639962422150646,False,36.33
HEAL.L,HEAL.L,theme_health_innovation,43.54557804630997,False,42.54
BTEC.L,BTEC.L,theme_biotech,37.40321541918766,False,43.97
SBIO.L,SBIO.L,theme_biotech,41.90744563421256,False,41.16
INRG.L,INRG.L,theme_clean_energy,85.8649722229916,False,41.88
RENW.L,RENW.L,theme_clean_energy,57.491264700086646,False,36.63
HTWO.L,HTWO.L,theme_clean_energy,54.43840610932351,False,35.08
ECAR.L,ECAR.L,theme_ev_battery,47.87631648336337,False,37.63
BATT.L,BATT.L,theme_ev_battery,54.90381640330969,False,37.85
IH2O.L,IH2O.L,theme_water,76.66977245814871,False,41.27
WATU.L,WATU.L,theme_water,66.66977245814871,False,38.39
GLUG.L,GLUG.L,theme_water,51.25329567992185,False,39.87
NATO.L,NATO.L,theme_defence,58.31960267975041,False,39.05
DFNS.L,DFNS.L,theme_defence,61.331764953860926,False,42.49
IGLN.L,PHAU.L,gold_physical_etc,13.669772458148708,False,54.79
SGLD.L,PHAU.L,gold_physical_etc,13.669772458148708,False,54.36
XGDU.L,XGDU.L,gold_physical_etc,12.669772458148708,False,48.98
WGLD.L,PHAU.L,gold_physical_etc,13.669772458148708,False,45.81
PHAU.L,PHAU.L,gold_physical_etc,40.66977245814871,False,36.69
SGBX.L,SGBX.L,gold_physical_etc,21.669772458148707,False,42.94
XGLD.L,PHAU.L,gold_physical_etc,26.669772458148707,False,34.54
RMAU.L,RMAU.L,gold_physical_etc,23.669772458148707,False,41.74
GDX.L,GDX.L,gold_miners,54.66977245814871,False,47.27
GDXJ.L,GDXJ.L,gold_miners,56.66977245814872,False,43.98
IAUP.L,IAUP.L,gold_miners,56.66977245814872,False,45.68
AUCO.L,AUCO.L,gold_miners,56.66977245814872,False,41.04
ISLN.L,PHAG.L,silver_physical_etc,21.669772458148707,False,55.13
SSLV.L,PHAG.L,silver_physical_etc,20.669772458148707,False,53.25
PHAG.L,PHAG.L,silver_physical_etc,50.66977245814871,False,37.57
SILV.L,SILV.L,silver_miners,66.66977245814871,False,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,45.66977245814871,False,38.29
IPLT.L,IPLT.L,platinum_physical_etc,21.669772458148707,False,42.09
IPDM.L,IPDM.L,palladium_physical_etc,21.669772458148707,False,41.44
CMOD.L,CMOD.L,commodities_broad,35.639962422150646,False,43.98
ICOM.L,ICOM.L,commodities_broad,28.15486744014968,False,45.76
BCOM.L,BCOM.L,commodities_broad,31.63996242215065,False,38.59
COMF.L,COMF.L,commodities_broad,40.97127117973795,False,36.88
ROLL.L,ROLL.L,commodities_broad,36.51084263190409,False,39.95
WCOA.L,WCOA.L,commodities_broad,39.639962422150646,False,38.51
ENCO.L,ENCO.L,commodities_broad,46.639962422150646,False,36.22
AIGC.L,AIGC.L,commodities_broad_etc,65.63996242215065,False,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,53.42459747262786,False,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,50.66977245814871,False,43.59
BRNT.L,BRNT.L,commodities_energy_etc,65.63996242215065,False,42.51
CRUD.L,CRUD.L,commodities_energy_etc,65.63996242215065,False,42.13
GDIG.L,GDIG.L,commodity_equity_mining,51.66977245814871,False,43.0
COPX.L,COPX.L,commodity_equity_mining,56.66977245814872,False,42.56
REMX.L,REMX.L,commodity_equity_mining,61.2251339364121,False,41.2
URNU.L,URNU.L,commodity_equity_uranium,74.75021120105411,False,37.49
URNM.L,URNM.L,commodity_equity_uranium,93.28917605176974,False,36.43
SPAG.L,SPAG.L,commodity_equity_agri,61.66977245814872,False,40.15
WOOD.L,WOOD.L,commodity_equity_timber,76.66977245814871,False,34.99
DPYA.L,DPYA.L,reit_global,60.66977245814871,False,40.49
GLRA.L,GLRA.L,reit_global,41.66977245814871,False,36.71
HPRD.L,HPRD.L,reit_global,30.669772458148707,False,40.52
EPRA.L,EPRA.L,reit_global,31.15603944471648,False,39.75
TRET.L,TRET.L,reit_global,31.669772458148707,False,36.78
IDUP.L,IDUP.L,reit_us,46.85940594227321,False,39.63
XRES.L,XRES.L,reit_us,15.66977245814871,False,44.93
IPRP.L,IPRP.L,reit_europe,51.66977245814871,False,39.51
XDER.L,XDER.L,reit_europe,39.66977245814871,False,37.62
IDAR.L,IDAR.L,reit_asia,65.66977245814871,False,35.09
IUKP.L,IUKP.L,reit_uk,51.66977245814871,False,43.05
IDIN.L,IDIN.L,infrastructure_global,71.66977245814871,False,40.84
XGID.L,XGID.L,infrastructure_global,61.66977245814871,False,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,51.66977245814871,False,37.41
PAVE.L,PAVE.L,infrastructure_us,57.1466441409328,False,38.56
MAGG.L,MAGG.L,multi_asset_growth,40.130955265963294,False,37.37
MAMG.L,MAMG.L,multi_asset_moderate,36.76140861434687,False,38.02
MACG.L,MACG.L,multi_asset_conservative,31.669772458148707,False,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,35.44470645055935,False,30.24
ACWD.L,ACWD.L,global,22.973500975130683,False,56.16
SPYY.L,SPYY.L,global,66.36431870918585,False,36.04
EXUS.L,EXUS.L,developed_ex_us,16.669772458148707,False,48.48

