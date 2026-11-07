import csv,sys,io,collections
for f in sys.argv[1:]:
    L=open(f,encoding='utf-8-sig',errors='ignore').read().splitlines()
    hi=next((i for i,l in enumerate(L) if l.startswith('Ticker') or l.startswith('Issuer Ticker') or 'Weight (%)' in l),None)
    if hi is None: print(f,'no header'); continue
    r=list(csv.DictReader(io.StringIO("\n".join(L[hi:]))))
    w=collections.Counter()
    for x in r:
        try: w[x.get('Location','?')]+=float(x['Weight (%)'].replace(',',''))
        except: pass
    print(f,L[0][:40],'rows',len(r),'cols',list(r[0].keys())[:17]); print(' top Location',[(k,round(v,2)) for k,v in w.most_common(6)],'sum',round(sum(w.values()),2))
