import re,sys,html
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
for k in ["NAV as of","NAV ","Shares Outstanding","Net Assets of Share Class","Net Assets of Fund","Securities Lending","Lending Return","Average on loan","Maximum on loan","Collateral","Total Expense Ratio","Holdings as of","Distribution Frequency","Use of Income","Domicile","Product Structure","Methodology","Rebalance"]:
    i=t.find(k); print(f"{k!r} ->",t[i:i+150] if i>=0 else None)
