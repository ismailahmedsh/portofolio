import sys, re, html
D=sys.argv[1]
def txt(p):
    t=open(p,encoding='utf8',errors='ignore').read()
    t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t)))
def find(t,keys,n=160):
    for k in keys:
        i=t.find(k); print(f"   {k!r} ->", t[i:i+n] if i>=0 else None)
for f,keys in [
 ("je_vwra.html",["Replication","Securities lending","counterpart","Counterpart","Total expense ratio","Fund size","Distribution policy","Fund domicile"]),
 ("je_cspx.html",["Replication","Securities lending","Counterpart","Total expense ratio","Tracking difference"]),
 ("ish_cspx.html",["Total Expense Ratio","Calendar Year","Tracking Difference","Securities Lending Return","Average on loan","Maximum on loan","Fund Holdings as of","Key Information Document","KID","Prospectus","Annual Report"]),
 ("ish_ibit.html",["Sponsor Fee","Bitcoin in Trust","Shares Outstanding","Net Assets","Prospectus","10-K","Custodian"]),
 ("ish_aggu.html",["Weighted Avg Yield to Maturity","Yield to Maturity","Effective Duration","Modified Duration","Distribution Yield","Total Expense Ratio"]),
 ("jpm_jepq.html",["ELN","Equity Linked","SEC 30","30-Day SEC","Distribution","Expense ratio","Prospectus"]),
 ("spdr_spy.html",["Gross Expense Ratio","Distribution","Prospectus","Securities Lending"]),
 ("inv_qqq.html",["Expense ratio","Total expense ratio","Prospectus","Distribution"]),
 ("vg_vwra.html",["Ongoing charges","OCF","Key investor","KID","Prospectus","Replication","Securities lending"]),
]:
    print("==",f); 
    try: find(txt(f"{D}/{f}"),keys)
    except Exception as e: print("  err",e)
