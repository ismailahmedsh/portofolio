import sys,random,urllib.request,re,html,json,ssl,collections
O=sys.argv[1]
rows=[l.split('\t') for l in open(f"{O}/out/urls.txt").read().splitlines()]
urls=sorted(set(u.rstrip('.,;') for _,u in rows))
by=collections.defaultdict(list)
for u in urls: by[re.sub(r'https?://([^/]+).*',r'\1',u)].append(u)
random.seed(7); sample=[v[0] for k,v in sorted(by.items())][:30]
ctx=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
res=[]
for u in sample:
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/124"}),timeout=25,context=ctx)
        b=r.read(3_000_000).decode('utf8','ignore'); t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',b,flags=re.S))))
        res.append({"url":u,"code":r.status,"text_chars":len(t)})
    except Exception as e: res.append({"url":u,"err":repr(e)[:90]})
ok=[x for x in res if x.get('code')==200 and x['text_chars']>2000]
json.dump(res,open(f"{O}/out/urlcheck.json","w"),indent=1)
print("unique urls",len(urls),"domains",len(by),"sampled",len(sample),"ok_with_text",len(ok))
for x in res: print(x)
# quote check demo on Treasury release
u="https://home.treasury.gov/news/press-releases/sb0678"
try:
    b=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=25,context=ctx).read().decode('utf8','ignore')
    t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',b)))
    for q in ["next several quarters","at least the next several quarters"]: print("QUOTE",repr(q),q in t)
except Exception as e: print("treasury err",e)
