import re,sys,html
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
for k in sys.argv[2:]:
    i=t.find(k); print(f"[{sys.argv[1]}] {k!r} ->",t[i:i+170] if i>=0 else None)
