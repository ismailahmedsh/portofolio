import sys, re, html, csv, io, collections, json, datetime as dt
D=sys.argv[1]
def txt(p):
    t=open(p,encoding='utf8',errors='ignore').read()
    t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t)))
def find(t,keys,n=140):
    for k in keys:
        i=t.find(k); print(f"   {k!r} ->", t[i:i+n] if i>=0 else None)
print("== S5/S6 holdings Location")
for f in ["cspx_latest.csv","ib01_latest.csv"]:
    L=open(f"{D}/{f}",encoding='utf-8-sig').read().splitlines()
    hi=next(i for i,l in enumerate(L) if l.startswith('Ticker'))
    r=list(csv.DictReader(io.StringIO("\n".join(L[hi:])))); w=collections.Counter()
    for x in r:
        try: w[x['Location']]+=float(x['Weight (%)'].replace(',',''))
        except: pass
    print(" ",f,L[0],"rows",len(r),"top",[(k,round(v,2)) for k,v in w.most_common(4)],"sum",round(sum(w.values()),2))
print("== S3 fund-document Historical NAVs")
x=open(f"{D}/fdoc.xml",encoding='utf8',errors='ignore').read()
m=re.search(r'ss:Name="Historical NAVs".*?</ss:Worksheet>',x,re.S); ws=m.group(0)
rows=[re.findall(r'<ss:Data[^>]*>(.*?)</ss:Data>',r) for r in re.findall(r'<ss:Row.*?</ss:Row>',ws,re.S)]
print("  header",rows[0][:4],"n",len(rows)-1,"first",rows[1][:3],"last",rows[-1][:3])
for nm in ["Key Facts"]:
    m=re.search(rf'ss:Name="{nm}".*?</ss:Worksheet>',x,re.S)
    for r in re.findall(r'<ss:Row.*?</ss:Row>',m.group(0),re.S):
        c=re.findall(r'<ss:Data[^>]*>(.*?)</ss:Data>',r)
        if c and any(k in c[0] for k in ["Shares Outstanding","Net Assets","Securities Lending","Total Expense"]): print("  KeyFacts",c[:2])
print("== S7/S8/S10 iShares pages")
t=txt(f"{D}/cspx.html"); find(t,["Shares Outstanding","Net Assets of Share Class","Securities Lending Return","Average on loan","Maximum on loan","Collateralisation"])
g=txt(f"{D}/igln.html"); find(g,["Tonnes","Ounces","Total Expense Ratio","Shares Outstanding","Bar List","Prospectus"])
print("== S10 justETF VWRA"); j=txt(f"{D}/je_vwra.html"); find(j,["Securities lending","Counterpart","Fund size","Replication"],200)
print("== S3 Vanguard VWRA page"); v=txt(f"{D}/vg_vwra.html"); find(v,["NAV at closure","NAV as at","Shares in issue","Fund size"],160)
print("== S9 justETF closed status / investegate")
print("  je_closed has 404 text:", "404" in txt(f"{D}/je_closed.html")[:3000] or "not found" in txt(f"{D}/je_closed.html").lower())
inv=open(f"{D}/investegate.html",encoding='utf8',errors='ignore').read()
titles=[html.unescape(s).strip() for s in re.findall(r'<a[^>]*href="/announcement/[^"]*"[^>]*>(.*?)</a>',inv,re.S)]
titles=[re.sub(r'<[^>]+>','',s).strip() for s in titles if s.strip()]
c=collections.Counter('NAV' if re.search(r'net asset value|\bnav\b',s,re.I) else 'other' for s in titles)
print("  investegate titles",len(titles),dict(c),[s for s in titles if re.search(r'delist|terminat|clos|merg|liquidat',s,re.I)][:5])
print("== S10 Xtrackers page bytes",len(open(f"{D}/xtr.html").read()), "has data?", "Securities lending" in txt(f"{D}/xtr.html"))
