# Pillar CST08: Whole-share residue at deposit size
Definition: Expected uninvested share of a whole-share order, averaged over orders of US$340-760: (order - commission - floor((order - commission) / price) x price) / order. A line priced above 0.9 x US$679 is flagged as not buyable in one month. Weight 0.05 in the line score, because residue is carried into next month and its money cost is priced in CST10. Fractional shares are assumed unavailable until EVT08 confirms otherwise.
Source: yfinance .L USD price; deposit size from config/portfolio.yaml (verified). Better when: lower. Informs: monthly_allocation.
Week 2026-W46.

## Lines in your sleeves (VWRA, S&P 500 and Nasdaq-100 groups) and the 15 most extreme values
|        | cluster   | scope                    |       CST08 | buyable   |   CST08_score |   line_score |
|:-------|:----------|:-------------------------|------------:|:----------|--------------:|-------------:|
| EMGA.L | EMGA.L    | em-debt                  | 5.92564e-05 | False     |         49.97 |        43.83 |
| HMXJ.L | HMXJ.L    | asia_pacific             | 0.000156716 | False     |         49.92 |        38.25 |
| IUMS.L | IUMS.L    | sector_materials         | 0.000236018 | False     |         49.88 |        44.14 |
| IGLA.L | IGLA.L    | government               | 0.000364178 | False     |         49.82 |        43.86 |
| MACG.L | MACG.L    | multi_asset_conservative | 0.00046952  | False     |         49.77 |        38.44 |
| DGTL.L | DGTL.L    | theme_digital_tech       | 0.000655927 | False     |         49.67 |        37.07 |
| QDIV.L | QDIV.L    | dividend_quality         | 0.000788494 | False     |         49.61 |        37.32 |
| IUES.L | IUES.L    | sector_energy            | 0.000788536 | False     |         49.61 |        48.23 |
| IPLT.L | IPLT.L    | platinum_physical_etc    | 0.0010206   | False     |         49.49 |        42.09 |
| IBTA.L | IBTA.L    | government               | 0.00107579  | False     |         49.46 |        56.49 |
| HMCD.L | XCS6.L    | single_country           | 0.00124496  | False     |         49.38 |        54    |
| CMXC.L | CMXC.L    | single_country           | 0.00145149  | False     |         49.27 |        35.56 |
| AGGG.L | AGGG.L    | aggregate                | 0.00165927  | False     |         49.17 |        50.77 |
| DHYA.L | DHYA.L    | high-yield               | 0.00169317  | False     |         49.15 |        38.55 |
| MAGG.L | MAGG.L    | multi_asset_growth       | 0.00226821  | False     |         48.87 |        37.37 |
|        | cluster   | scope             |    CST08 | buyable   |   CST08_score |   line_score |
|:-------|:----------|:------------------|---------:|:----------|--------------:|-------------:|
| WGLD.L | PHAU.L    | gold_physical_etc | 0.420422 | False     |          0.02 |        45.81 |
| CUKS.L | CUKS.L    | uk                | 0.421949 | False     |          0.02 |        34.47 |
| SGLD.L | PHAU.L    | gold_physical_etc | 0.438559 | False     |          0.02 |        54.36 |
| XGLD.L | PHAU.L    | gold_physical_etc | 0.440577 | False     |          0.01 |        34.54 |
| SGBX.L | SGBX.L    | gold_physical_etc | 0.441561 | False     |          0.01 |        42.94 |
| PHAU.L | PHAU.L    | gold_physical_etc | 0.458773 | False     |          0.01 |        36.69 |
| XLKS.L | XLKS.L    | sector_tech       | 1        | False     |          0    |        45.96 |
| XLVS.L | XLVS.L    | sector_health     | 1        | False     |          0    |        44.01 |
| SPY5.L | XSPU.L    | us                | 1        | False     |          0    |        52.82 |
| CUSS.L | CUSS.L    | us                | 1        | False     |          0    |        41.01 |
| EQQU.L | CNDX.L    | us                | 1        | False     |          0    |        51.98 |
| CSPX.L | XSPU.L    | us                | 1        | False     |          0    |        52.34 |
| CSUS.L | CSUS.L    | us                | 1        | False     |          0    |        55.65 |
| XLES.L | XLES.L    | sector_energy     | 1        | False     |          0    |        41.55 |
| CNDX.L | CNDX.L    | us                | 1        | False     |          0    |        56.06 |

## All lines (csv)
,cluster,scope,CST08,buyable,CST08_score,line_score
IB01.L,IB01.L,government,0.0944922046481596,False,13.13,55.34
VDST.L,VDST.L,government,0.0261356492228109,False,37.22,56.33
IBTA.L,IBTA.L,government,0.0010757935183664,False,49.46,56.49
CBU3.L,CBU3.L,government,0.0663148168981111,False,20.98,49.56
XUT3.L,XUT3.L,government,0.0155512984061234,False,42.29,46.44
TRE3.L,TRE3.L,government,0.0395259755208838,False,31.21,48.81
US13.L,US13.L,government,0.0945929654355502,False,13.1,49.83
CBU7.L,CBU7.L,government,0.1617644182063935,False,3.79,55.46
CBU0.L,CBU0.L,government,0.1050707609327297,False,10.9,57.53
TREX.L,TREX.L,government,0.0412656671678344,False,30.46,50.59
US71.L,US71.L,government,0.0038243793860111,False,48.09,50.86
DTLA.L,DTLA.L,government,0.0031752962437222,False,48.41,56.46
US10.L,US10.L,government,0.1309129128973698,False,6.8,48.53
VDTA.L,VDTA.L,government,0.0055031975340645,False,47.25,54.89
XUTD.L,XUTD.L,government,0.1635766061382923,False,3.66,48.42
TRES.L,TRES.L,government,0.0189634628793423,False,40.63,49.65
TRSY.L,TRSY.L,government,0.0238331292196091,False,38.3,51.52
IGLA.L,IGLA.L,government,0.0003641781853364,False,49.82,43.86
XGGB.L,XGGB.L,government,0.2689343290587747,False,0.46,39.18
IGLT.L,IGLT.L,government,0.0126107403849436,False,43.73,55.37
IGLS.L,IGLS.L,government,0.0143898939206249,False,42.85,55.3
SEGA.L,SEGA.L,government,0.1314812153629841,False,6.73,51.69
XGLE.L,XGLE.L,government,0.2821634461047533,False,0.35,50.27
AGGU.L,AGGU.L,aggregate,0.0035053372810905,False,48.25,53.29
VAGU.L,VAGU.L,aggregate,0.0092601591494763,False,45.38,52.19
GLAD.L,GLAD.L,aggregate,0.0157722830892677,False,42.18,49.15
AGGG.L,AGGG.L,aggregate,0.0016592708668572,False,49.17,50.77
GAGU.L,GAGU.L,aggregate,0.0138274616331816,False,43.13,45.51
IUAA.L,IUAA.L,aggregate,0.0023443309720134,False,48.83,46.09
USAG.L,USAG.L,aggregate,0.0502702464315256,False,26.79,37.76
IDTP.L,IDTP.L,inflation-linked,0.2519910497040304,False,0.64,51.6
TIP5.L,TIP5.L,inflation-linked,0.0045852644004088,False,47.71,50.32
TIPU.L,TIPU.L,inflation-linked,0.1468918607092491,False,5.03,46.67
TIPS.L,TIPS.L,inflation-linked,0.0279272275045891,False,36.39,50.29
IGIL.L,IGIL.L,inflation-linked,0.0434266510873203,False,29.56,42.21
XG7U.L,XG7U.L,inflation-linked,0.0217392741959617,False,39.3,39.07
INXG.L,INXG.L,inflation-linked,0.0055137299557422,False,47.25,48.38
IBCI.L,IBCI.L,inflation-linked,0.2430199835226184,False,0.77,50.61
LQDA.L,LQDA.L,corporate,0.0058346366217376,False,47.09,47.08
VDPA.L,VDPA.L,corporate,0.015795820917112,False,42.17,55.04
SDIA.L,SDIA.L,corporate,0.0085013726156113,False,45.76,47.71
VDCA.L,VDCA.L,corporate,0.0807166178383702,False,16.6,52.24
SUSU.L,SUSU.L,corporate,0.0068114592874258,False,46.6,44.72
ICBU.L,ICBU.L,corporate,0.0024253743323422,False,48.79,44.79
XDGU.L,XDGU.L,corporate,0.0036246464725745,False,48.19,45.21
CRPU.L,CRPU.L,corporate,0.0039075858603541,False,48.05,43.78
HLQD.L,HLQD.L,corporate,0.0068306455958793,False,46.59,38.11
FLOA.L,FLOA.L,corporate,0.0046604345443821,False,47.67,53.11
UCRP.L,UCRP.L,corporate,0.0851955260009499,False,15.4,40.12
IEAA.L,IEAA.L,corporate,0.0087010040539095,False,45.66,53.5
IHYA.L,IHYA.L,high-yield,0.0034788101547303,False,48.26,43.09
HYLA.L,HYLA.L,high-yield,0.0090686473338618,False,45.48,41.94
XUHY.L,XUHY.L,high-yield,0.0182916638784838,False,40.95,38.81
HYUS.L,HYUS.L,high-yield,0.0045794431718535,False,47.71,37.91
DHYA.L,DHYA.L,high-yield,0.0016931711278648,False,49.15,38.55
WIAU.L,WIAU.L,high-yield,0.0105846706031133,False,44.73,40.71
SJNK.L,SJNK.L,high-yield,0.020463094535674,False,39.91,35.96
HIGH.L,HIGH.L,high-yield,0.0048905807293543,False,47.56,41.38
XHYG.L,HIGH.L,high-yield,0.0059580282720946,False,47.02,51.8
JPEA.L,JPEA.L,em-debt,0.0071945770587254,False,46.41,44.92
VDEA.L,VDEA.L,em-debt,0.0766649415984161,False,17.75,42.08
EMSA.L,EMSA.L,em-debt,0.0090538933366508,False,45.49,39.48
EMCA.L,EMCA.L,em-debt,0.0068291674562606,False,46.59,43.87
EMGA.L,EMGA.L,em-debt,5.925638849374108e-05,False,49.97,43.83
EMDD.L,EMDD.L,em-debt,0.0822267819420229,False,16.18,39.95
EMLC.L,EMLC.L,em-debt,0.0864036560456491,False,15.08,36.44
EMLB.L,EMLB.L,em-debt,0.0506607001029669,False,26.64,36.59
ERNA.L,ERNA.L,money-market,0.0053558500573231,False,47.32,54.21
JPSA.L,JPSA.L,money-market,0.0621158325235347,False,22.4,41.89
ERNS.L,ERNS.L,money-market,0.0083261151681625,False,45.85,54.59
XSTR.L,XSTR.L,money-market,0.2883177898130731,False,0.31,47.73
ERNE.L,ERNE.L,money-market,0.0061002553583947,False,46.95,50.97
VWRA.L,VWRA.L,global,0.1622947724534555,True,3.75,52.93
ISAC.L,ACWD.L,global,0.1053211791412848,False,10.85,49.57
IWDA.L,IWDA.L,global,0.1425521551948531,False,5.46,51.14
XDWD.L,IWDA.L,global,0.0613422877772317,False,22.67,50.13
SWRD.L,IWDA.L,global,0.0595743428684441,False,23.3,51.37
HMWD.L,IWDA.L,global,0.0611397264464449,False,22.74,50.13
FWRA.L,VWRA.L,global,0.0078251132019966,False,46.1,48.74
VHVE.L,VHVE.L,global,0.1106693917780243,False,9.86,49.78
WSML.L,WDSC.L,global,0.0078457959160527,False,46.09,57.19
CSPX.L,XSPU.L,us,1.0,False,0.0,52.34
VUAA.L,XSPU.L,us,0.1316495772171413,False,6.7,48.24
SPXS.L,XSPU.L,us,0.0074656217783093,False,46.27,56.04
SPY5.L,XSPU.L,us,1.0,False,0.0,52.82
HSPD.L,XSPU.L,us,0.0925768729205115,False,13.57,47.04
XSPU.L,XSPU.L,us,0.0921053969648765,False,13.68,45.12
CNDX.L,CNDX.L,us,1.0,False,0.0,56.06
EQQU.L,CNDX.L,us,1.0,False,0.0,51.98
XNAS.L,CNDX.L,us,0.0346750978526522,False,33.33,52.88
XDEW.L,XDEW.L,us,0.0799799085561769,False,16.8,45.25
CSUS.L,CSUS.L,us,1.0,False,0.0,55.65
VNRA.L,VNRA.L,us,0.150360823961884,False,4.71,50.32
R2US.L,R2US.L,us,0.0164941603925497,False,41.83,41.95
SPY4.L,SPY4.L,us,0.1400180618581587,False,5.73,40.78
CUSS.L,CUSS.L,us,1.0,False,0.0,41.01
VEUA.L,VEUA.L,europe,0.0826817065772783,False,16.06,53.64
VERG.L,VERG.L,europe,0.0763542006367177,False,17.84,53.18
SMEA.L,SMEA.L,europe,0.110561546353151,False,9.87,53.99
IEUX.L,IEUX.L,europe,0.0639322704581061,False,21.78,42.26
CSX5.L,CSX5.L,europe,0.1788522896868657,False,2.72,54.36
XESC.L,XESC.L,europe,0.0601198139383855,False,23.1,52.88
XDAX.L,XDAX.L,single_country,0.1781104554589707,False,2.76,51.89
CACX.L,CACX.L,single_country,0.0236314184511436,False,38.4,43.14
CSWG.L,CSWG.L,single_country,0.0046433019550588,False,47.68,40.53
IAEX.L,IAEX.L,single_country,0.0630524727997091,False,22.08,40.2
CUKX.L,CUKX.L,uk,0.1171111511434402,False,8.77,56.68
VUKG.L,HUKX.L,uk,0.0796904192997437,False,16.88,50.05
VMIG.L,MIDD.L,uk,0.0639831349535341,False,21.76,50.69
MIDD.L,MIDD.L,uk,0.0034803957966896,False,48.26,41.43
HUKX.L,HUKX.L,uk,0.1494486028543015,False,4.79,50.86
CUKS.L,CUKS.L,uk,0.4219487821804412,False,0.02,34.47
IJPA.L,IJPA.L,japan,0.0634049838425293,False,21.96,49.67
CSJP.L,CSJP.L,japan,0.1601234811095193,False,3.91,40.3
VJPA.L,VJPA.L,japan,0.027426323643846,False,36.62,46.36
XMJD.L,XMJD.L,japan,0.1491526836864775,False,4.82,58.22
HMJD.L,XMJD.L,japan,0.0240376183142332,False,38.21,45.61
LCJP.L,LCJP.L,japan,0.0235397901646054,False,38.44,49.25
XDJP.L,XDJP.L,japan,0.0053768485270122,False,47.31,49.3
IDJP.L,IDJP.L,japan,0.040170596142803,False,30.93,36.72
CPXJ.L,CPXJ.L,asia_pacific,0.2711737724044081,False,0.44,46.93
VAPU.L,VAPU.L,asia_pacific,0.0730110703858777,False,18.84,48.27
HMXJ.L,HMXJ.L,asia_pacific,0.0001567157538562,False,49.92,38.25
XPXD.L,XPXD.L,asia_pacific,0.0212382804103749,False,39.54,38.17
IFFF.L,IFFF.L,asia_pacific,0.1214190475381119,False,8.1,42.22
HMAD.L,HMAD.L,asia_pacific,0.020265878112786,False,40.0,36.71
XMAD.L,XMAD.L,asia_pacific,0.0216508218715556,False,39.34,37.77
EIMI.L,EIMI.L,emerging,0.0358095559592339,False,32.82,50.71
VFEA.L,VFEA.L,emerging,0.0147262379649731,False,42.69,48.22
IEMA.L,IEMA.L,emerging,0.0413050542493847,False,30.45,50.65
XMME.L,XMMD.L,emerging,0.1170488512819633,False,8.78,54.27
HMEM.L,XMMD.L,emerging,0.0152050301496903,False,42.46,50.55
EMXC.L,EMXC.L,emerging,0.0446568398103469,False,29.05,50.31
EMSD.L,EMSD.L,emerging,0.1606446740523658,False,3.87,35.56
XMMD.L,XMMD.L,emerging,0.0837958917807354,False,15.76,43.02
NDIA.L,XCS5.L,single_country,0.0029528643326242,False,48.52,41.67
FLXI.L,FLXI.L,single_country,0.0453198950252291,False,28.77,43.0
XCS5.L,XCS5.L,single_country,0.0028953995473344,False,48.55,53.7
CNYA.L,CNYA.L,single_country,0.0064755436286262,False,46.77,44.98
XCS6.L,XCS6.L,single_country,0.0077131567715626,False,46.15,40.47
HMCD.L,XCS6.L,single_country,0.0012449597128537,False,49.38,54.0
FXC.L,FXC.L,single_country,0.0036370715689293,False,48.18,40.02
KWEB.L,KWEB.L,single_country,0.0121331258292833,False,43.96,42.61
CSKR.L,CSKR.L,single_country,0.4024179127938527,False,0.03,42.54
ITWN.L,ITWN.L,single_country,0.2058534082870916,False,1.6,44.63
XMTD.L,ITWN.L,single_country,0.1889326019165597,False,2.23,47.64
IBZL.L,IBZL.L,single_country,0.0113399215450368,False,44.35,40.27
XMBD.L,IBZL.L,single_country,0.0220192046141659,False,39.16,53.91
CMXC.L,CMXC.L,single_country,0.001451487572294,False,49.27,35.56
IKSA.L,IKSA.L,single_country,0.0076129439636884,False,46.2,37.6
IRSA.L,IRSA.L,single_country,0.0293121319212396,False,35.75,36.54
IDTK.L,IDTK.L,single_country,0.0142805310973672,False,42.91,34.39
IAUS.L,IAUS.L,single_country,0.0530917058469394,False,25.7,41.22
CCAU.L,CCAU.L,single_country,0.0731584122423163,False,18.8,41.63
IPOL.L,IPOL.L,single_country,0.0155512984061234,False,42.29,42.22
XVTD.L,XVTD.L,single_country,0.0023944563444722,False,48.8,36.69
HIDD.L,HIDD.L,single_country,0.0080077730408071,False,46.0,35.88
IWVL.L,IWVL.L,factor_value,0.0788454392089897,False,17.12,47.48
IWQU.L,IWQU.L,factor_quality,0.0672356697790364,False,20.67,44.24
IWMO.L,IWMO.L,factor_momentum,0.0616959172251688,False,22.55,44.06
MVOL.L,MVOL.L,factor_min_vol,0.0432498588445626,False,29.63,44.02
XDEV.L,XDEV.L,factor_value,0.0457497855178999,False,28.6,44.48
XDEQ.L,XDEQ.L,factor_quality,0.0507157545230746,False,26.61,40.36
XDEM.L,XDEM.L,factor_momentum,0.0782240946422897,False,17.3,40.51
XDEB.L,XDEB.L,factor_min_vol,0.0376947491787979,False,32.0,40.46
IUVL.L,IUVL.L,factor_value,0.0268664740480432,False,36.88,46.43
IUQA.L,IUQA.L,factor_quality,0.0192788264961244,False,40.48,44.79
IUMO.L,IUMO.L,factor_momentum,0.0120594492807613,False,44.0,43.29
SPMV.L,SPMV.L,factor_min_vol,0.0975125553366758,False,12.45,41.17
EMVL.L,EMVL.L,factor_value,0.0434118921723444,False,29.56,44.13
IEFV.L,IEFV.L,factor_value,0.0024657717246754,False,48.77,43.57
IEFQ.L,IEFQ.L,factor_quality,0.0031128587974677,False,48.44,40.42
IEFM.L,IEFM.L,factor_momentum,0.0068588006667448,False,46.58,41.08
JPGL.L,JPGL.L,factor_multi,0.0508485531015024,False,26.56,38.53
MOAT.L,MOAT.L,factor_quality,0.0435739479813371,False,29.49,36.86
WDSC.L,WDSC.L,size_small_cap,0.1373660995325555,False,6.02,45.53
USSC.L,USSC.L,size_small_cap_value,0.0221665183690909,False,39.09,40.15
IWFS.L,IWFS.L,size_mid_cap_equal_weight,0.0105774302410926,False,44.73,37.07
SPEQ.L,SPEQ.L,equal_weight,0.0959361053825945,False,12.8,42.26
VHYA.L,VHYD.L,dividend,0.0399495945987504,False,31.02,48.01
VHYD.L,VHYD.L,dividend,0.0316031977474723,False,34.7,50.34
FUSD.L,FUSD.L,dividend_quality,0.0033962753065638,False,48.3,38.09
FGQI.L,FGQI.L,dividend_quality,0.0077942071572699,False,46.11,37.29
GLDV.L,GLDV.L,dividend,0.0585724227409034,False,23.66,39.83
UDVD.L,UDVD.L,dividend,0.0592943843487263,False,23.4,41.58
WQDV.L,WQDV.L,dividend_quality,0.0063134990602389,False,46.85,41.46
QDIV.L,QDIV.L,dividend_quality,0.0007884941807418,False,49.61,37.32
TDIV.L,TDIV.L,dividend,0.0625210001475301,False,22.26,44.59
HDLV.L,HDLV.L,dividend_low_vol,0.0566866088432071,False,24.35,40.44
DGRA.L,DGRA.L,dividend_quality,0.0205606067880852,False,39.86,38.48
GGRA.L,GGRA.L,dividend_quality,0.0342772591034201,False,33.5,39.2
EUDV.L,EUDV.L,dividend,0.0147711352468774,False,42.67,40.49
IDVY.L,IDVY.L,dividend,0.0109989426739145,False,44.52,41.73
IUIT.L,IUIT.L,sector_tech,0.0134002287006578,False,43.34,49.92
SXLK.L,SXLK.L,sector_tech,0.2251469776118496,False,1.1,45.08
XLKS.L,XLKS.L,sector_tech,1.0,False,0.0,45.96
XDWT.L,XDWT.L,sector_tech,0.0062884100288405,False,46.86,44.13
WTEC.L,WTEC.L,sector_tech,0.2549377069831164,False,0.61,38.34
IUHC.L,IUHC.L,sector_health,0.0190062446237431,False,40.61,49.63
SXLV.L,SXLV.L,sector_health,0.0322293275734011,False,34.42,45.91
XLVS.L,XLVS.L,sector_health,1.0,False,0.0,44.01
XDWH.L,WHEA.L,sector_health,0.0775195086289127,False,17.5,55.44
WHEA.L,WHEA.L,sector_health,0.0529148911229708,False,25.76,47.22
IUFS.L,IUFS.L,sector_financials,0.0199713068059633,False,40.15,47.69
SXLF.L,SXLF.L,sector_financials,0.0683369231370737,False,20.31,41.53
XLFS.L,XLFS.L,sector_financials,0.3126185142287396,False,0.19,40.07
XDWF.L,WFIN.L,sector_financials,0.0631987412134527,False,22.03,55.81
WFIN.L,WFIN.L,sector_financials,0.0732762587500141,False,18.76,46.75
IUES.L,IUES.L,sector_energy,0.0007885363330123,False,49.61,48.23
SXLE.L,SXLE.L,sector_energy,0.0073190780048587,False,46.35,45.52
XLES.L,XLES.L,sector_energy,1.0,False,0.0,41.55
XDW0.L,WNRG.L,sector_energy,0.0919804913569465,False,13.71,55.0
WNRG.L,WNRG.L,sector_energy,0.0710663107531215,False,19.45,47.38
IOGP.L,IOGP.L,sector_energy,0.0230504739625765,False,38.67,36.17
IUCD.L,IUCD.L,sector_consumer_disc,0.0222107108094776,False,39.07,42.92
SXLY.L,SXLY.L,sector_consumer_disc,0.1003708389755938,False,11.84,36.23
XDWC.L,WCOD.L,sector_consumer_disc,0.067441912408113,False,20.61,57.95
WCOD.L,WCOD.L,sector_consumer_disc,0.0938439252091614,False,13.27,44.31
IUCS.L,IUCS.L,sector_consumer_staples,0.0065344949839888,False,46.74,46.39
SXLP.L,SXLP.L,sector_consumer_staples,0.0241241484951048,False,38.17,43.73
XDWS.L,XDWS.L,sector_consumer_staples,0.0242881208273293,False,38.09,41.16
IUIS.L,IUIS.L,sector_industrials,0.0144462653944984,False,42.83,45.18
SXLI.L,SXLI.L,sector_industrials,0.0101588989493,False,44.94,45.18
XDWI.L,XDWI.L,sector_industrials,0.0104830442891018,False,44.78,41.14
IUUS.L,IUUS.L,sector_utilities,0.0093411996996538,False,45.34,48.81
SXLU.L,SXLU.L,sector_utilities,0.0095843129197322,False,45.22,42.66
XDWU.L,XDWU.L,sector_utilities,0.0695192830838456,False,19.93,40.73
IUMS.L,IUMS.L,sector_materials,0.0002360184221242,False,49.88,44.14
SXLB.L,SXLB.L,sector_materials,0.0548007499830889,False,25.05,39.26
XDWM.L,XDWM.L,sector_materials,0.0694161898708209,False,19.97,39.7
IUCM.L,IUCM.L,sector_communication,0.0144904831262474,False,42.81,45.41
SXLC.L,SXLC.L,sector_communication,0.0256774877643495,False,37.44,40.19
XWTS.L,XWTS.L,sector_communication,0.0292264616466861,False,35.79,35.61
SMH.L,SMH.L,theme_semiconductors,0.0360894582759244,False,32.7,45.19
SEMI.L,SEMI.L,theme_semiconductors,0.0099166300406677,False,45.06,45.1
SEMU.L,SEMU.L,theme_semiconductors,0.0473751385691033,False,27.94,39.52
AIAI.L,AIAI.L,theme_ai,0.0140042988383611,False,43.04,41.8
WTAI.L,WTAI.L,theme_ai,0.0715967099626054,False,19.28,39.33
BOTZ.L,BOTZ.L,theme_ai_robotics,0.0073388221283584,False,46.34,33.75
RBOT.L,RBOT.L,theme_ai_robotics,0.0250984392144119,False,37.71,43.84
ROBO.L,ROBO.L,theme_ai_robotics,0.0333637856799828,False,33.91,39.93
DGTL.L,DGTL.L,theme_digital_tech,0.0006559266951116,False,49.67,37.07
XNGI.L,XNGI.L,theme_digital_tech,0.0135401517574894,False,43.27,30.8
ITEK.L,ITEK.L,theme_digital_tech,0.0080270310081205,False,46.0,32.68
WCLD.L,WCLD.L,theme_cloud,0.0337027180362741,False,33.76,38.24
LOCK.L,LOCK.L,theme_cybersecurity,0.0095459487332792,False,45.24,41.54
USPY.L,USPY.L,theme_cybersecurity,0.0379458555091181,False,31.89,40.83
WCBR.L,WCBR.L,theme_cybersecurity,0.0572538772386171,False,24.14,36.33
HEAL.L,HEAL.L,theme_health_innovation,0.0034920382397494,False,48.25,42.54
BTEC.L,BTEC.L,theme_biotech,0.0091275846384676,False,45.45,43.97
SBIO.L,SBIO.L,theme_biotech,0.082145680973591,False,16.21,41.16
INRG.L,INRG.L,theme_clean_energy,0.0078989351477504,False,46.06,41.88
RENW.L,RENW.L,theme_clean_energy,0.0063135117059201,False,46.85,36.63
HTWO.L,HTWO.L,theme_clean_energy,0.0091511266815389,False,45.44,35.08
ECAR.L,ECAR.L,theme_ev_battery,0.0030574792426137,False,48.47,37.63
BATT.L,BATT.L,theme_ev_battery,0.0270653147384209,False,36.79,37.85
IH2O.L,IH2O.L,theme_water,0.089074932429187,False,14.41,41.27
WATU.L,WATU.L,theme_water,0.019617699839237,False,40.32,38.39
GLUG.L,GLUG.L,theme_water,0.0203174668715688,False,39.98,39.87
NATO.L,NATO.L,theme_defence,0.0212088553154182,False,39.55,39.05
DFNS.L,DFNS.L,theme_defence,0.0818215918368165,False,16.3,42.49
IGLN.L,PHAU.L,gold_physical_etc,0.0959950061552325,False,12.79,54.79
SGLD.L,PHAU.L,gold_physical_etc,0.4385586625233451,False,0.02,54.36
XGDU.L,XGDU.L,gold_physical_etc,0.0136727459395577,False,43.21,48.98
WGLD.L,PHAU.L,gold_physical_etc,0.4204219905675648,False,0.02,45.81
PHAU.L,PHAU.L,gold_physical_etc,0.4587727332563716,False,0.01,36.69
SGBX.L,SGBX.L,gold_physical_etc,0.4415609765012049,False,0.01,42.94
XGLD.L,PHAU.L,gold_physical_etc,0.4405771155655315,False,0.01,34.54
RMAU.L,RMAU.L,gold_physical_etc,0.024310219857674,False,38.08,41.74
GDX.L,GDX.L,gold_miners,0.0161847852083292,False,41.98,47.27
GDXJ.L,GDXJ.L,gold_miners,0.0238166055295751,False,38.31,43.98
IAUP.L,IAUP.L,gold_miners,0.0144168065777253,False,42.84,45.68
AUCO.L,AUCO.L,gold_miners,0.0424247759222014,False,29.97,41.04
ISLN.L,PHAG.L,silver_physical_etc,0.0685137772031614,False,20.26,55.13
SSLV.L,PHAG.L,silver_physical_etc,0.0664547624361536,False,20.93,53.25
PHAG.L,PHAG.L,silver_physical_etc,0.0371207725867568,False,32.25,37.57
SILV.L,SILV.L,silver_miners,0.0472867199665135,False,27.97,41.74
PHPM.L,PHPM.L,precious_metals_basket_etc,0.3067988930799979,False,0.22,38.29
IPLT.L,IPLT.L,platinum_physical_etc,0.0010206042531454,False,49.49,42.09
IPDM.L,IPDM.L,palladium_physical_etc,0.0127519633124166,False,43.66,41.44
CMOD.L,CMOD.L,commodities_broad,0.0164851004645447,False,41.83,43.98
ICOM.L,ICOM.L,commodities_broad,0.0123394583832037,False,43.86,45.76
BCOM.L,BCOM.L,commodities_broad,0.0192640169984239,False,40.49,38.59
COMF.L,COMF.L,commodities_broad,0.0296952033250417,False,35.57,36.88
ROLL.L,ROLL.L,commodities_broad,0.0053923370626634,False,47.31,39.95
WCOA.L,WCOA.L,commodities_broad,0.0206784364348748,False,39.81,38.51
ENCO.L,ENCO.L,commodities_broad,0.0025423546108814,False,48.73,36.22
AIGC.L,AIGC.L,commodities_broad_etc,0.0197560997940281,False,40.25,35.25
AIGI.L,AIGI.L,commodities_industrial_metals_etc,0.0200522925581891,False,40.11,40.34
COPA.L,COPA.L,commodities_industrial_metals_etc,0.0588671289349916,False,23.55,43.59
BRNT.L,BRNT.L,commodities_energy_etc,0.0183505688663488,False,40.93,42.51
CRUD.L,CRUD.L,commodities_energy_etc,0.0182622401886028,False,40.97,42.13
GDIG.L,GDIG.L,commodity_equity_mining,0.0515152390319499,False,26.3,43.0
COPX.L,COPX.L,commodity_equity_mining,0.0737182843193302,False,18.63,42.56
REMX.L,REMX.L,commodity_equity_mining,0.0079842886058388,False,46.02,41.2
URNU.L,URNU.L,commodity_equity_uranium,0.0099584789538544,False,45.04,37.49
URNM.L,URNM.L,commodity_equity_uranium,0.0117500923625247,False,44.15,36.43
SPAG.L,SPAG.L,commodity_equity_agri,0.0226795358088213,False,38.85,40.15
WOOD.L,WOOD.L,commodity_equity_timber,0.0086027732744681,False,45.71,34.99
DPYA.L,DPYA.L,reit_global,0.0071945770587254,False,46.41,40.49
GLRA.L,GLRA.L,reit_global,0.0038899093057222,False,48.06,36.71
HPRD.L,HPRD.L,reit_global,0.0206937854816376,False,39.8,40.52
EPRA.L,EPRA.L,reit_global,0.0399626720315549,False,31.02,39.75
TRET.L,TRET.L,reit_global,0.0228884462550974,False,38.75,36.78
IDUP.L,IDUP.L,reit_us,0.0330544273566705,False,34.05,39.63
XRES.L,XRES.L,reit_us,0.0109544977635259,False,44.54,44.93
IPRP.L,IPRP.L,reit_europe,0.0269025645691272,False,36.86,39.51
XDER.L,XDER.L,reit_europe,0.0038127638009729,False,48.09,37.62
IDAR.L,IDAR.L,reit_asia,0.0171203576621113,False,41.52,35.09
IUKP.L,IUKP.L,reit_uk,0.0050053784045778,False,47.5,43.05
IDIN.L,IDIN.L,infrastructure_global,0.0080299001726655,False,45.99,40.84
XGID.L,XGID.L,infrastructure_global,0.0371207613461514,False,32.25,37.32
GIN.L,GIN.L,infrastructure_global_multi_asset,0.0526096734258785,False,25.88,37.41
PAVE.L,PAVE.L,infrastructure_us,0.0306381636667658,False,35.14,38.56
MAGG.L,MAGG.L,multi_asset_growth,0.0022682134277819,False,48.87,37.37
MAMG.L,MAMG.L,multi_asset_moderate,0.0101453832268235,False,44.94,38.02
MACG.L,MACG.L,multi_asset_conservative,0.0004695195727426,False,49.77,38.44
NTSX.L,NTSX.L,multi_asset_efficient_core,0.0421153951176782,False,30.1,30.24
ACWD.L,ACWD.L,global,0.0488484896898572,False,27.35,56.16
SPYY.L,SPYY.L,global,0.0024680654493615,False,48.77,36.04
EXUS.L,EXUS.L,developed_ex_us,0.0566129041931714,False,24.37,48.48

