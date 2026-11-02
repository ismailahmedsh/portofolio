#!/bin/bash
# Task 1c: keyless endpoints: Bank of Canada Valet, FRED fredgraph CSV, Stooq CSV, BlackRock CA holdings CSV
D=/home/user/portofolio/investing-research/data/verify/downloads
LOG=/home/user/portofolio/investing-research/data/verify/verify_log.md
UA="Mozilla/5.0 (X11; Linux x86_64) etf-monitor-test/0.1"
echo -e "\n## Keyless endpoints ($(date -u '+%Y-%m-%d %H:%M:%S UTC'))" | tee -a $LOG
try() { # name url outfile
  code=$(curl -sS -L -A "$UA" -o "$3" -w "%{http_code}" --max-time 60 "$2" 2>&1); rc=$?
  size=$(stat -c %s "$3" 2>/dev/null || echo 0); lines=$(wc -l < "$3" 2>/dev/null || echo 0)
  ctype=$(file -b "$3" | cut -c1-60)
  echo "- $1: HTTP $code rc=$rc bytes=$size lines=$lines type=[$ctype] url=$2" | tee -a $LOG
  echo "  - head: $(head -c 300 "$3" | tr '\n' '|' | cut -c1-300)" | tee -a $LOG
}
try "BoC Valet FXUSDCAD json" "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?start_date=2010-01-01" "$D/boc_FXUSDCAD.json"
try "BoC Valet FXUSDCAD csv" "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/csv?start_date=2010-01-01" "$D/boc_FXUSDCAD.csv"
try "BoC Valet group FX_RATES_DAILY json (recent_weeks=1)" "https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/json?recent_weeks=1" "$D/boc_fx_group.json"
try "FRED fredgraph T10Y2Y" "https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y" "$D/fred_T10Y2Y.csv"
try "FRED fredgraph DGS10" "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10" "$D/fred_DGS10.csv"
try "FRED fredgraph SAHMREALTIME" "https://fred.stlouisfed.org/graph/fredgraph.csv?id=SAHMREALTIME" "$D/fred_SAHMREALTIME.csv"
try "FRED fredgraph multi (DGS10,DGS2,UNRATE)" "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10,DGS2,UNRATE" "$D/fred_multi.csv"
try "FRED fredgraph DEXCAUS (USD/CAD)" "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXCAUS" "$D/fred_DEXCAUS.csv"
try "Stooq XEQT.TO (symbol xeqt.ca?) daily" "https://stooq.com/q/d/l/?s=xeqt.ca&i=d" "$D/stooq_xeqt_ca.csv"
try "Stooq XEQT.TO literal" "https://stooq.com/q/d/l/?s=xeqt.to&i=d" "$D/stooq_xeqt_to.csv"
try "Stooq SPY.US daily" "https://stooq.com/q/d/l/?s=spy.us&i=d" "$D/stooq_spy_us.csv"
try "Stooq VT.US daily" "https://stooq.com/q/d/l/?s=vt.us&i=d" "$D/stooq_vt_us.csv"
