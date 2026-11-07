import pandas as pd, sys
for f,label in [("ie_data.xls","new"),("yale.html","yale")]:
    try:
        d=pd.read_excel(f,sheet_name="Data",header=7,dtype=str)
        d=d[d.iloc[:,0].str.match(r'^\d{4}\.\d+$',na=False)]
        cape_col=[c for c in d.columns if 'CAPE' in str(c)][0]
        last=d[d[cape_col].notna() & (d[cape_col]!='NA')].iloc[-1]
        print(label,'rows',len(d),'last_date',d.iloc[-1,0],'last CAPE row',last.iloc[0],last[cape_col])
    except Exception as e: print(label,'ERR',e)
x=pd.ExcelFile("pink.xlsx"); print(x.sheet_names)
p=pd.read_excel("pink.xlsx",sheet_name="Monthly Prices",header=None)
hdr=p.iloc[4].tolist(); gi=[i for i,h in enumerate(hdr) if isinstance(h,str) and h.strip().lower().startswith('gold')]
print('gold col',gi,[hdr[i] for i in gi]); rows=p[p.iloc[:,0].astype(str).str.match(r'^\d{4}M\d{2}$')]
print('first',rows.iloc[0,0],rows.iloc[0,gi[0]],'last',rows.iloc[-1,0],rows.iloc[-1,gi[0]],'n',len(rows))
