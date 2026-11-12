# Pillar TAX05: Distribution friction
Definition: 0 for an accumulating class. For a distributing class (for example EQQU): the cost of reinvesting each payment (US$1.70 per payment) or its cash drag at r_forgone, in bps a year. A distributing class is eligible only where its sleeve has no affordable accumulating USD line.
Source: universe_ucits_*.csv accumulating column; yield from the proxy's 12-month dividends ending today (verified). Better when: lower. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                             |   TAX05 | buyable   |   TAX05_score |   line_score |
|:-------|:----------|:----------------------------------|--------:|:----------|--------------:|-------------:|
| EXUS.L | EXUS.L    | developed_ex_us                   |       0 | False     |            50 |        48.48 |
| GLAD.L | GLAD.L    | aggregate                         |       0 | False     |            50 |        49.15 |
| GAGU.L | GAGU.L    | aggregate                         |       0 | False     |            50 |        45.51 |
| IUAA.L | IUAA.L    | aggregate                         |       0 | False     |            50 |        46.09 |
| IDTP.L | IDTP.L    | inflation-linked                  |       0 | False     |            50 |        51.6  |
| IGLA.L | IGLA.L    | government                        |       0 | False     |            50 |        43.86 |
| XGGB.L | XGGB.L    | government                        |       0 | False     |            50 |        39.18 |
| XGLE.L | XGLE.L    | government                        |       0 | False     |            50 |        50.27 |
| AGGU.L | AGGU.L    | aggregate                         |       0 | False     |            50 |        53.29 |
| CBU0.L | CBU0.L    | government                        |       0 | False     |            50 |        57.53 |
| DTLA.L | DTLA.L    | government                        |       0 | False     |            50 |        56.46 |
| VDTA.L | VDTA.L    | government                        |       0 | False     |            50 |        54.89 |
| AIGI.L | AIGI.L    | commodities_industrial_metals_etc |       0 | False     |            50 |        40.34 |
| VDST.L | VDST.L    | government                        |       0 | False     |            50 |        56.33 |
| IBTA.L | IBTA.L    | government                        |       0 | False     |            50 |        56.49 |
|        | cluster   | scope            |   TAX05 | buyable   |   TAX05_score |   line_score |
|:-------|:----------|:-----------------|--------:|:----------|--------------:|-------------:|
| TRE3.L | TRE3.L    | government       |       5 | False     |         33.92 |        48.81 |
| US13.L | US13.L    | government       |       5 | False     |         33.92 |        49.83 |
| EQQU.L | CNDX.L    | us               |       5 | False     |         33.92 |        51.98 |
| TREX.L | TREX.L    | government       |       5 | False     |         33.92 |        50.59 |
| US71.L | US71.L    | government       |       5 | False     |         33.92 |        50.86 |
| US10.L | US10.L    | government       |       5 | False     |         33.92 |        48.53 |
| XUTD.L | XUTD.L    | government       |       5 | False     |         33.92 |        48.42 |
| TRES.L | TRES.L    | government       |       5 | False     |         33.92 |        49.65 |
| IGLT.L | IGLT.L    | government       |       5 | False     |         33.92 |        55.37 |
| IGLS.L | IGLS.L    | government       |       5 | False     |         33.92 |        55.3  |
| SEGA.L | SEGA.L    | government       |       5 | False     |         33.92 |        51.69 |
| AGGG.L | AGGG.L    | aggregate        |       5 | False     |         33.92 |        50.77 |
| USAG.L | USAG.L    | aggregate        |       5 | False     |         33.92 |        37.76 |
| TIP5.L | TIP5.L    | inflation-linked |       5 | False     |         33.92 |        50.32 |
| TRSY.L | TRSY.L    | government       |       5 | False     |         33.92 |        51.52 |

## All lines (csv)
,cluster,scope,TAX05,buyable,TAX05_score,line_score
IB01.L,IB01.L,government,0.0,False,50.0,55.34
VDST.L,VDST.L,government,0.0,False,50.0,56.33
IBTA.L,IBTA.L,government,0.0,False,50.0,56.49
CBU3.L,CBU3.L,government,0.0,False,50.0,49.56
XUT3.L,XUT3.L,government,5.0,False,33.92,46.44
TRE3.L,TRE3.L,government,5.0,False,33.92,48.81
US13.L,US13.L,government,5.0,False,33.92,49.83
CBU7.L,CBU7.L,government,0.0,False,50.0,55.46
CBU0.L,CBU0.L,government,0.0,False,50.0,57.53
TREX.L,TREX.L,government,5.0,False,33.92,50.59
US71.L,US71.L,government,5.0,False,33.92,50.86
DTLA.L,DTLA.L,government,0.0,False,50.0,56.46
US10.L,US10.L,government,5.0,False,33.92,48.53
VDTA.L,VDTA.L,government,0.0,False,50.0,54.89
XUTD.L,XUTD.L,government,5.0,False,33.92,48.42
TRES.L,TRES.L,government,5.0,False,33.92,49.65
TRSY.L,TRSY.L,government,5.0,False,33.92,51.52
IGLA.L,IGLA.L,government,0.0,False,50.0,43.86
XGGB.L,XGGB.L,government,0.0,False,50.0,39.18
IGLT.L,IGLT.L,government,5.0,False,33.92,55.37
IGLS.L,IGLS.L,government,5.0,False,33.92,55.3
SEGA.L,SEGA.L,government,5.0,False,33.92,51.69
XGLE.L,XGLE.L,government,0.0,False,50.0,50.27
AGGU.L,AGGU.L,aggregate,0.0,False,50.0,53.29
VAGU.L,VAGU.L,aggregate,0.0,False,50.0,52.19
GLAD.L,GLAD.L,aggregate,0.0,False,50.0,49.15
AGGG.L,AGGG.L,aggregate,5.0,False,33.92,50.77
GAGU.L,GAGU.L,aggregate,0.0,False,50.0,45.51
IUAA.L,IUAA.L,aggregate,0.0,False,50.0,46.09
USAG.L,USAG.L,aggregate,5.0,False,33.92,37.76
IDTP.L,IDTP.L,inflation-linked,0.0,False,50.0,51.6
TIP5.L,TIP5.L,inflation-linked,5.0,False,33.92,50.32
TIPU.L,TIPU.L,inflation-linked,5.0,False,33.92,46.67
TIPS.L,TIPS.L,inflation-linked,5.0,False,33.92,50.29
IGIL.L,IGIL.L,inflation-linked,0.0,False,50.0,42.21
XG7U.L,XG7U.L,inflation-linked,0.0,False,50.0,39.07
INXG.L,INXG.L,inflation-linked,5.0,False,33.92,48.38
IBCI.L,IBCI.L,inflation-linked,0.0,False,50.0,50.61
LQDA.L,LQDA.L,corporate,0.0,False,50.0,47.08
VDPA.L,VDPA.L,corporate,0.0,False,50.0,55.04
SDIA.L,SDIA.L,corporate,0.0,False,50.0,47.71
VDCA.L,VDCA.L,corporate,0.0,False,50.0,52.24
SUSU.L,SUSU.L,corporate,5.0,False,33.92,44.72
ICBU.L,ICBU.L,corporate,5.0,False,33.92,44.79
XDGU.L,XDGU.L,corporate,5.0,False,33.92,45.21
CRPU.L,CRPU.L,corporate,0.0,False,50.0,43.78
HLQD.L,HLQD.L,corporate,0.0,False,50.0,38.11
FLOA.L,FLOA.L,corporate,0.0,False,50.0,53.11
UCRP.L,UCRP.L,corporate,0.0,False,50.0,40.12
IEAA.L,IEAA.L,corporate,0.0,False,50.0,53.5
IHYA.L,IHYA.L,high-yield,0.0,False,50.0,43.09
HYLA.L,HYLA.L,high-yield,0.0,False,50.0,41.94
XUHY.L,XUHY.L,high-yield,5.0,False,33.92,38.81
HYUS.L,HYUS.L,high-yield,5.0,False,33.92,37.91
DHYA.L,DHYA.L,high-yield,0.0,False,50.0,38.55
WIAU.L,WIAU.L,high-yield,0.0,False,50.0,40.71
SJNK.L,SJNK.L,high-yield,5.0,False,33.92,35.96
HIGH.L,HIGH.L,high-yield,0.0,False,50.0,41.38
XHYG.L,HIGH.L,high-yield,5.0,False,33.92,51.8
JPEA.L,JPEA.L,em-debt,0.0,False,50.0,44.92
VDEA.L,VDEA.L,em-debt,0.0,False,50.0,42.08
EMSA.L,EMSA.L,em-debt,0.0,False,50.0,39.48
EMCA.L,EMCA.L,em-debt,0.0,False,50.0,43.87
EMGA.L,EMGA.L,em-debt,0.0,False,50.0,43.83
EMDD.L,EMDD.L,em-debt,5.0,False,33.92,39.95
EMLC.L,EMLC.L,em-debt,0.0,False,50.0,36.44
EMLB.L,EMLB.L,em-debt,0.0,False,50.0,36.59
ERNA.L,ERNA.L,money-market,0.0,False,50.0,54.21
JPSA.L,JPSA.L,money-market,0.0,False,50.0,41.89
ERNS.L,ERNS.L,money-market,5.0,False,33.92,54.59
XSTR.L,XSTR.L,money-market,5.0,False,33.92,47.73
ERNE.L,ERNE.L,money-market,5.0,False,33.92,50.97
VWRA.L,VWRA.L,global,0.0,True,50.0,52.93
ISAC.L,ACWD.L,global,0.0,False,50.0,49.57
IWDA.L,IWDA.L,global,0.0,False,50.0,51.14
XDWD.L,IWDA.L,global,0.0,False,50.0,50.13
SWRD.L,IWDA.L,global,0.0,False,50.0,51.37
HMWD.L,IWDA.L,global,5.0,False,33.92,50.13
FWRA.L,VWRA.L,global,0.0,False,50.0,48.74
VHVE.L,VHVE.L,global,0.0,False,50.0,49.78
WSML.L,WDSC.L,global,0.0,False,50.0,57.19
CSPX.L,XSPU.L,us,0.0,False,50.0,52.34
VUAA.L,XSPU.L,us,0.0,False,50.0,48.24
SPXS.L,XSPU.L,us,0.0,False,50.0,56.04
SPY5.L,XSPU.L,us,5.0,False,33.92,52.82
HSPD.L,XSPU.L,us,5.0,False,33.92,47.04
XSPU.L,XSPU.L,us,0.0,False,50.0,45.12
CNDX.L,CNDX.L,us,0.0,False,50.0,56.06
EQQU.L,CNDX.L,us,5.0,False,33.92,51.98
XNAS.L,CNDX.L,us,0.0,False,50.0,52.88
XDEW.L,XDEW.L,us,0.0,False,50.0,45.25
CSUS.L,CSUS.L,us,0.0,False,50.0,55.65
VNRA.L,VNRA.L,us,0.0,False,50.0,50.32
R2US.L,R2US.L,us,5.0,False,33.92,41.95
SPY4.L,SPY4.L,us,5.0,False,33.92,40.78
CUSS.L,CUSS.L,us,0.0,False,50.0,41.01
VEUA.L,VEUA.L,europe,0.0,False,50.0,53.64
VERG.L,VERG.L,europe,0.0,False,50.0,53.18
SMEA.L,SMEA.L,europe,0.0,False,50.0,53.99
IEUX.L,IEUX.L,europe,5.0,False,33.92,42.26
CSX5.L,CSX5.L,europe,0.0,False,50.0,54.36
XESC.L,XESC.L,europe,0.0,False,50.0,52.88
XDAX.L,XDAX.L,single_country,0.0,False,50.0,51.89
CACX.L,CACX.L,single_country,5.0,False,33.92,43.14
CSWG.L,CSWG.L,single_country,0.0,False,50.0,40.53
IAEX.L,IAEX.L,single_country,5.0,False,33.92,40.2
CUKX.L,CUKX.L,uk,0.0,False,50.0,56.68
VUKG.L,HUKX.L,uk,0.0,False,50.0,50.05
VMIG.L,MIDD.L,uk,0.0,False,50.0,50.69
MIDD.L,MIDD.L,uk,5.0,False,33.92,41.43
HUKX.L,HUKX.L,uk,5.0,False,33.92,50.86
CUKS.L,CUKS.L,uk,0.0,False,50.0,34.47
IJPA.L,IJPA.L,japan,0.0,False,50.0,49.67
CSJP.L,CSJP.L,japan,0.0,False,50.0,40.3
VJPA.L,VJPA.L,japan,0.0,False,50.0,46.36
XMJD.L,XMJD.L,japan,0.0,False,50.0,58.22
HMJD.L,XMJD.L,japan,5.0,False,33.92,45.61
LCJP.L,LCJP.L,japan,0.0,False,50.0,49.25
XDJP.L,XDJP.L,japan,5.0,False,33.92,49.3
IDJP.L,IDJP.L,japan,5.0,False,33.92,36.72
CPXJ.L,CPXJ.L,asia_pacific,0.0,False,50.0,46.93
VAPU.L,VAPU.L,asia_pacific,0.0,False,50.0,48.27
HMXJ.L,HMXJ.L,asia_pacific,5.0,False,33.92,38.25
XPXD.L,XPXD.L,asia_pacific,0.0,False,50.0,38.17
IFFF.L,IFFF.L,asia_pacific,5.0,False,33.92,42.22
HMAD.L,HMAD.L,asia_pacific,5.0,False,33.92,36.71
XMAD.L,XMAD.L,asia_pacific,0.0,False,50.0,37.77
EIMI.L,EIMI.L,emerging,0.0,False,50.0,50.71
VFEA.L,VFEA.L,emerging,0.0,False,50.0,48.22
IEMA.L,IEMA.L,emerging,0.0,False,50.0,50.65
XMME.L,XMMD.L,emerging,0.0,False,50.0,54.27
HMEM.L,XMMD.L,emerging,5.0,False,33.92,50.55
EMXC.L,EMXC.L,emerging,0.0,False,50.0,50.31
EMSD.L,EMSD.L,emerging,0.0,False,50.0,35.56
XMMD.L,XMMD.L,emerging,0.0,False,50.0,43.02
NDIA.L,XCS5.L,single_country,0.0,False,50.0,41.67
FLXI.L,FLXI.L,single_country,5.0,False,33.92,43.0
XCS5.L,XCS5.L,single_country,0.0,False,50.0,53.7
CNYA.L,CNYA.L,single_country,0.0,False,50.0,44.98
XCS6.L,XCS6.L,single_country,0.0,False,50.0,40.47
HMCD.L,XCS6.L,single_country,5.0,False,33.92,54.0
FXC.L,FXC.L,single_country,5.0,False,33.92,40.02
KWEB.L,KWEB.L,single_country,0.0,False,50.0,42.61
CSKR.L,CSKR.L,single_country,0.0,False,50.0,42.54
ITWN.L,ITWN.L,single_country,5.0,False,33.92,44.63
XMTD.L,ITWN.L,single_country,0.0,False,50.0,47.64
IBZL.L,IBZL.L,single_country,5.0,False,33.92,40.27
XMBD.L,IBZL.L,single_country,0.0,False,50.0,53.91
CMXC.L,CMXC.L,single_country,0.0,False,50.0,35.56
IKSA.L,IKSA.L,single_country,0.0,False,50.0,37.6
IRSA.L,IRSA.L,single_country,0.0,False,50.0,36.54
IDTK.L,IDTK.L,single_country,5.0,False,33.92,34.39
IAUS.L,IAUS.L,single_country,0.0,False,50.0,41.22
CCAU.L,CCAU.L,single_country,0.0,False,50.0,41.63
IPOL.L,IPOL.L,single_country,0.0,False,50.0,42.22
XVTD.L,XVTD.L,single_country,0.0,False,50.0,36.69
HIDD.L,HIDD.L,single_country,5.0,False,33.92,35.88
IWVL.L,IWVL.L,factor_value,0.0,False,50.0,47.48
IWQU.L,IWQU.L,factor_quality,0.0,False,50.0,44.24
IWMO.L,IWMO.L,factor_momentum,0.0,False,50.0,44.06
MVOL.L,MVOL.L,factor_min_vol,0.0,False,50.0,44.02
XDEV.L,XDEV.L,factor_value,0.0,False,50.0,44.48
XDEQ.L,XDEQ.L,factor_quality,0.0,False,50.0,40.36
XDEM.L,XDEM.L,factor_momentum,0.0,False,50.0,40.51
XDEB.L,XDEB.L,factor_min_vol,0.0,False,50.0,40.46
IUVL.L,IUVL.L,factor_value,0.0,False,50.0,46.43
IUQA.L,IUQA.L,factor_quality,0.0,False,50.0,44.79
IUMO.L,IUMO.L,factor_momentum,0.0,False,50.0,43.29
SPMV.L,SPMV.L,factor_min_vol,0.0,False,50.0,41.17
EMVL.L,EMVL.L,factor_value,0.0,False,50.0,44.13
IEFV.L,IEFV.L,factor_value,0.0,False,50.0,43.57
IEFQ.L,IEFQ.L,factor_quality,0.0,False,50.0,40.42
IEFM.L,IEFM.L,factor_momentum,0.0,False,50.0,41.08
JPGL.L,JPGL.L,factor_multi,0.0,False,50.0,38.53
MOAT.L,MOAT.L,factor_quality,0.0,False,50.0,36.86
WDSC.L,WDSC.L,size_small_cap,0.0,False,50.0,45.53
USSC.L,USSC.L,size_small_cap_value,0.0,False,50.0,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,0.0,False,50.0,37.07
SPEQ.L,SPEQ.L,equal_weight,0.0,False,50.0,42.26
VHYA.L,VHYD.L,dividend,0.0,False,50.0,48.01
VHYD.L,VHYD.L,dividend,5.0,False,33.92,50.34
FUSD.L,FUSD.L,dividend_quality,5.0,False,33.92,38.09
FGQI.L,FGQI.L,dividend_quality,5.0,False,33.92,37.29
GLDV.L,GLDV.L,dividend,5.0,False,33.92,39.83
UDVD.L,UDVD.L,dividend,5.0,False,33.92,41.58
WQDV.L,WQDV.L,dividend_quality,5.0,False,33.92,41.46
QDIV.L,QDIV.L,dividend_quality,5.0,False,33.92,37.32
TDIV.L,TDIV.L,dividend,5.0,False,33.92,44.59
HDLV.L,HDLV.L,dividend_low_vol,5.0,False,33.92,40.44
DGRA.L,DGRA.L,dividend_quality,0.0,False,50.0,38.48
GGRA.L,GGRA.L,dividend_quality,0.0,False,50.0,39.2
EUDV.L,EUDV.L,dividend,5.0,False,33.92,40.49
IDVY.L,IDVY.L,dividend,5.0,False,33.92,41.73
IUIT.L,IUIT.L,sector_tech,0.0,False,50.0,49.92
SXLK.L,SXLK.L,sector_tech,0.0,False,50.0,45.08
XLKS.L,XLKS.L,sector_tech,0.0,False,50.0,45.96
XDWT.L,XDWT.L,sector_tech,0.0,False,50.0,44.13
WTEC.L,WTEC.L,sector_tech,0.0,False,50.0,38.34
IUHC.L,IUHC.L,sector_health,0.0,False,50.0,49.63
SXLV.L,SXLV.L,sector_health,0.0,False,50.0,45.91
XLVS.L,XLVS.L,sector_health,0.0,False,50.0,44.01
XDWH.L,WHEA.L,sector_health,0.0,False,50.0,55.44
WHEA.L,WHEA.L,sector_health,0.0,False,50.0,47.22
IUFS.L,IUFS.L,sector_financials,0.0,False,50.0,47.69
SXLF.L,SXLF.L,sector_financials,0.0,False,50.0,41.53
XLFS.L,XLFS.L,sector_financials,0.0,False,50.0,40.07
XDWF.L,WFIN.L,sector_financials,0.0,False,50.0,55.81
WFIN.L,WFIN.L,sector_financials,0.0,False,50.0,46.75
IUES.L,IUES.L,sector_energy,0.0,False,50.0,48.23
SXLE.L,SXLE.L,sector_energy,0.0,False,50.0,45.52
XLES.L,XLES.L,sector_energy,0.0,False,50.0,41.55
XDW0.L,WNRG.L,sector_energy,0.0,False,50.0,55.0
WNRG.L,WNRG.L,sector_energy,0.0,False,50.0,47.38
IOGP.L,IOGP.L,sector_energy,0.0,False,50.0,36.17
IUCD.L,IUCD.L,sector_consumer_disc,0.0,False,50.0,42.92
SXLY.L,SXLY.L,sector_consumer_disc,0.0,False,50.0,36.23
XDWC.L,WCOD.L,sector_consumer_disc,0.0,False,50.0,57.95
WCOD.L,WCOD.L,sector_consumer_disc,0.0,False,50.0,44.31
IUCS.L,IUCS.L,sector_consumer_staples,0.0,False,50.0,46.39
SXLP.L,SXLP.L,sector_consumer_staples,0.0,False,50.0,43.73
XDWS.L,XDWS.L,sector_consumer_staples,0.0,False,50.0,41.16
IUIS.L,IUIS.L,sector_industrials,0.0,False,50.0,45.18
SXLI.L,SXLI.L,sector_industrials,0.0,False,50.0,45.18
XDWI.L,XDWI.L,sector_industrials,0.0,False,50.0,41.14
IUUS.L,IUUS.L,sector_utilities,0.0,False,50.0,48.81
SXLU.L,SXLU.L,sector_utilities,0.0,False,50.0,42.66
XDWU.L,XDWU.L,sector_utilities,0.0,False,50.0,40.73
IUMS.L,IUMS.L,sector_materials,0.0,False,50.0,44.14
SXLB.L,SXLB.L,sector_materials,0.0,False,50.0,39.26
XDWM.L,XDWM.L,sector_materials,0.0,False,50.0,39.7
IUCM.L,IUCM.L,sector_communication,0.0,False,50.0,45.41
SXLC.L,SXLC.L,sector_communication,0.0,False,50.0,40.19
XWTS.L,XWTS.L,sector_communication,0.0,False,50.0,35.61
SMH.L,SMH.L,theme_semiconductors,0.0,False,50.0,45.19
SEMI.L,SEMI.L,theme_semiconductors,0.0,False,50.0,45.1
SEMU.L,SEMU.L,theme_semiconductors,0.0,False,50.0,39.52
AIAI.L,AIAI.L,theme_ai,0.0,False,50.0,41.8
WTAI.L,WTAI.L,theme_ai,0.0,False,50.0,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,0.0,False,50.0,33.75
RBOT.L,RBOT.L,theme_ai_robotics,0.0,False,50.0,43.84
ROBO.L,ROBO.L,theme_ai_robotics,0.0,False,50.0,39.93
DGTL.L,DGTL.L,theme_digital_tech,0.0,False,50.0,37.07
XNGI.L,XNGI.L,theme_digital_tech,0.0,False,50.0,30.8
ITEK.L,ITEK.L,theme_digital_tech,0.0,False,50.0,32.68
WCLD.L,WCLD.L,theme_cloud,0.0,False,50.0,38.24
LOCK.L,LOCK.L,theme_cybersecurity,0.0,False,50.0,41.54
USPY.L,USPY.L,theme_cybersecurity,0.0,False,50.0,40.83
WCBR.L,WCBR.L,theme_cybersecurity,0.0,False,50.0,36.33
HEAL.L,HEAL.L,theme_health_innovation,0.0,False,50.0,42.54
BTEC.L,BTEC.L,theme_biotech,0.0,False,50.0,43.97
SBIO.L,SBIO.L,theme_biotech,0.0,False,50.0,41.16
INRG.L,INRG.L,theme_clean_energy,5.0,False,33.92,41.88
RENW.L,RENW.L,theme_clean_energy,0.0,False,50.0,36.63
HTWO.L,HTWO.L,theme_clean_energy,0.0,False,50.0,35.08
ECAR.L,ECAR.L,theme_ev_battery,0.0,False,50.0,37.63
BATT.L,BATT.L,theme_ev_battery,0.0,False,50.0,37.85
IH2O.L,IH2O.L,theme_water,5.0,False,33.92,41.27
WATU.L,WATU.L,theme_water,5.0,False,33.92,38.39
GLUG.L,GLUG.L,theme_water,0.0,False,50.0,39.87
NATO.L,NATO.L,theme_defence,0.0,False,50.0,39.05
DFNS.L,DFNS.L,theme_defence,0.0,False,50.0,42.49
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
CMOD.L,CMOD.L,commodities_broad,0.0,False,50.0,43.98
ICOM.L,ICOM.L,commodities_broad,0.0,False,50.0,45.76
BCOM.L,BCOM.L,commodities_broad,0.0,False,50.0,38.59
COMF.L,COMF.L,commodities_broad,0.0,False,50.0,36.88
ROLL.L,ROLL.L,commodities_broad,0.0,False,50.0,39.95
WCOA.L,WCOA.L,commodities_broad,0.0,False,50.0,38.51
ENCO.L,ENCO.L,commodities_broad,0.0,False,50.0,36.22
AIGC.L,AIGC.L,commodities_broad_etc,0.0,False,50.0,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,0.0,False,50.0,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,0.0,False,50.0,43.59
BRNT.L,BRNT.L,commodities_energy_etc,0.0,False,50.0,42.51
CRUD.L,CRUD.L,commodities_energy_etc,0.0,False,50.0,42.13
GDIG.L,GDIG.L,commodity_equity_mining,0.0,False,50.0,43.0
COPX.L,COPX.L,commodity_equity_mining,0.0,False,50.0,42.56
REMX.L,REMX.L,commodity_equity_mining,0.0,False,50.0,41.2
URNU.L,URNU.L,commodity_equity_uranium,0.0,False,50.0,37.49
URNM.L,URNM.L,commodity_equity_uranium,0.0,False,50.0,36.43
SPAG.L,SPAG.L,commodity_equity_agri,0.0,False,50.0,40.15
WOOD.L,WOOD.L,commodity_equity_timber,5.0,False,33.92,34.99
DPYA.L,DPYA.L,reit_global,0.0,False,50.0,40.49
GLRA.L,GLRA.L,reit_global,0.0,False,50.0,36.71
HPRD.L,HPRD.L,reit_global,5.0,False,33.92,40.52
EPRA.L,EPRA.L,reit_global,0.0,False,50.0,39.75
TRET.L,TRET.L,reit_global,5.0,False,33.92,36.78
IDUP.L,IDUP.L,reit_us,5.0,False,33.92,39.63
XRES.L,XRES.L,reit_us,0.0,False,50.0,44.93
IPRP.L,IPRP.L,reit_europe,5.0,False,33.92,39.51
XDER.L,XDER.L,reit_europe,0.0,False,50.0,37.62
IDAR.L,IDAR.L,reit_asia,5.0,False,33.92,35.09
IUKP.L,IUKP.L,reit_uk,5.0,False,33.92,43.05
IDIN.L,IDIN.L,infrastructure_global,5.0,False,33.92,40.84
XGID.L,XGID.L,infrastructure_global,0.0,False,50.0,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,5.0,False,33.92,37.41
PAVE.L,PAVE.L,infrastructure_us,0.0,False,50.0,38.56
MAGG.L,MAGG.L,multi_asset_growth,0.0,False,50.0,37.37
MAMG.L,MAMG.L,multi_asset_moderate,0.0,False,50.0,38.02
MACG.L,MACG.L,multi_asset_conservative,0.0,False,50.0,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,0.0,False,50.0,30.24
ACWD.L,ACWD.L,global,0.0,False,50.0,56.16
SPYY.L,SPYY.L,global,0.0,False,50.0,36.04
EXUS.L,EXUS.L,developed_ex_us,0.0,False,50.0,48.48

