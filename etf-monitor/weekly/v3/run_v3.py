"""Weekly run for engine v3 (pillars v3, crypto excluded, options-income information only).
Usage: python3 -I v3/run_v3.py --week 2026-W46 [--backtests]
Writes runs/<week>/: v3_plan.json, REPORT_V3.md, v3_us_lines.csv, v3_options_income.csv, v3_macro.json, v3_cross_wrapper.json,
and appends runs/news_log.csv (REC08, hash-chained) when news/*.json exist."""
import argparse, hashlib, json, sys
from pathlib import Path
import numpy as np, pandas as pd, yaml
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[0]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "v2")); sys.path.insert(0, str(ROOT / "src"))
import engine_v3 as E3
import run_v2 as R2

PAIRS = [("S&P 500", "SPY", "CSPX.L"), ("Nasdaq-100", "QQQ", "CNDX.L"), ("World", "VT", "VWRA.L")]

def us_after_tax_tr(D, t):
    """Daily total-return index of a US line for a UAE resident: price change plus 70% of each cash distribution."""
    px = D["raw"][t].dropna(); dv = D["divs"].get(t, pd.Series(dtype=float))
    dv = dv[~dv.index.duplicated()].reindex(px.index).fillna(0.0)
    r = (px + 0.7 * dv) / px.shift(1) - 1
    return (1 + r.fillna(0)).cumprod()

def cross_wrapper_backtest(R, monthly_usd):
    """REC07 cross-wrapper: the same monthly deposit into the US line (after 30% withholding) and the London line, same months."""
    D = R["Dus"]; rows = []
    for name, us, uc in PAIRS:
        a = us_after_tax_tr(D, us).resample("ME").last(); b = R["close"][uc].dropna().resample("ME").last()
        j = pd.concat([a, b], axis=1, keys=["us", "uc"]).dropna(); j = j.iloc[:-1] if j.index[-1] > R["asof"] else j
        if len(j) < 24: continue
        out = {"group": name, "us_line": us, "london_line": uc, "from": j.index[0].strftime("%Y-%m"), "months": len(j)}
        for k in ("us", "uc"):
            units, flows = 0.0, []
            comm = 1.0 if k == "us" else 1.70
            for d, p in j[k].items():
                units += (monthly_usd - comm) / p; flows.append((-monthly_usd, d))
            fv = units * j[k].iloc[-1]; out[f"{k}_final"] = round(fv); out[f"{k}_mwr"] = round(R2.xirr(flows + [(fv, j.index[-1])]) * 100, 2)
        out["paid_in"] = round(monthly_usd * len(j)); out["london_advantage_usd"] = out["uc_final"] - out["us_final"]
        out["london_advantage_pts"] = round(out["uc_mwr"] - out["us_mwr"], 2)
        rows.append(out)
    return rows

def append_news_log(week, rows):
    lp = ROOT / "runs" / "news_log.csv"
    old = pd.read_csv(lp) if lp.exists() else pd.DataFrame()
    if len(old) and (old["week"] == week).any(): return 0  # frozen: corrections are new rows, never rewrites
    prev = old["hash"].iloc[-1] if len(old) else "genesis"; out = []
    for r in rows:
        r = {"week": week, **r, "prev_hash": prev}; h = hashlib.sha256(json.dumps(r, sort_keys=True, default=str).encode()).hexdigest()[:16]
        r["hash"] = h; prev = h; out.append(r)
    pd.concat([old, pd.DataFrame(out)]).to_csv(lp, index=False); return len(out)

def fmt(x, d=0):
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:,.{d}f}"

def report(week, R, pl, bt, cfg):
    L, XW, F12, F7, M = R["L"], R["XW"], R["FIT12"], R["FIT07"], R["MAC"]
    o = [f"# Weekly report v3, {week} (prices to {R['asof'].date()})", "",
         "Engine v3 on pillars v3. Crypto excluded by the owner (2026-11-13). Options-income shown for information (target 0).", "",
         "## This month's deposit", f"Cash: US${pl['cash_usd']:,.2f} (2,500 AED less the US$2 conversion minimum). Portfolio value: US${pl['portfolio_value_usd']:,.2f}.", "",
         "| Sleeve | Target | Gap before (US$) |", "|---|---|---|"]
    o += [f"| {k} | {R['mix'][k]*100:.0f}% | {v:,.2f} |" for k, v in pl["gaps"].items()]
    o += ["", "| Order | Line | Units | Price (US$) | Cost incl. commission (US$) |", "|---|---|---|---|---|"]
    o += [f"| {i+1} | {x['ticker']} ({x['sleeve']}) | {x['units']} | {x['price_usd']:,.2f} | {x['cost_usd']:,.2f} |" for i, x in enumerate(pl["orders"])]
    o += ["", f"Carried to next month: US${pl['residue_usd']:,.2f}."] + [f"- {n}" for n in pl["notes"]]
    o += ["", "## Sell anything?", "No. Sells happen only on structural events (rules S0-S6); none are open this week." if not any(L.EVT_block.astype(bool)) else
          "Event blocks open: " + ", ".join(L.index[L.EVT_block.astype(bool)]) + ". These lines get no new money; the committee reviews S1/S2."]
    o += ["", "## US-listed or London? (ELG07 same-index groups, CST10 all-in cost in bps a year)",
          "A US-listed line pays 30% tax on its dividends (no US-UAE treaty) and adds US estate-tax exposure above US$60,000. It may win only if it is 10 bps or more cheaper after that tax.", "",
          "| Group | London lines (CST10) | US lines (CST10, 30% tax on yield) | Winner | Why |", "|---|---|---|---|---|"]
    for k, v in XW.items():
        o.append(f"| {k} | {', '.join(f'{t} {c:.0f}' for t, c in v['ucits_lines'].items())} | {', '.join(f'{x['ticker']} {x['CST10']:.0f} (yield {x['yield_pct']}%, tax {x['tax_bps']:.0f})' for x in v['us_lines'])} | {v['winner']} | {v['why']} |")
    o += ["", f"FIT12 US-situs gauge: US${F12['V_us']:,.0f} held ({F12['band']}); amber at US${F12['amber']:,.0f}, no US buys above US${F12['buy_limit']:,.0f}, cap US${F12['cap']:,.0f}. US buying ready: {'yes' if F12['ready_to_buy_us'] else 'no (W-8BEN date and IBKR entity not recorded)'}.",
          f"FIT07 US look-through of your mix: {F7['mix_us_weight']*100:.0f}% (the world sleeve alone is {F7['world_us_weight']*100:.0f}% US)."]
    xb = bt.get("cross_wrapper") or []
    if xb:
        o += ["", "### Backtest: same monthly deposit, US line after 30% dividend tax vs London line", "", "| Group | Since | Paid in | US line value | London line value | London ahead by | Return a year US / London |", "|---|---|---|---|---|---|---|"]
        o += [f"| {r['group']} ({r['us_line']} vs {r['london_line']}) | {r['from']} | {r['paid_in']:,} | {r['us_final']:,} | {r['uc_final']:,} | US${r['london_advantage_usd']:,} | {r['us_mwr']}% / {r['uc_mwr']}% |" for r in xb]
    r07 = bt["rec07"]; o += ["", f"## Your mix against alternatives (REC07, {r07['period']}, 2,500 AED a month)", "", "| Mix | Final (US$) | Return a year (money-weighted) | Worst year | Max drawdown |", "|---|---|---|---|---|"]
    o += [f"| {r['mix']} | {r['final']:,} | {r['mwr']}% | {r['worst_year']}% | {r['max_dd']}% |" for r in r07["rows"]]
    o += ["", f"Proxies: {r07['proxies']}. Past results do not predict which mix wins next."]
    r04 = bt["rec04"]; o += ["", "## Can scores move money? (REC04 gate)", f"Gate passed: {'yes' if r04['gate_pass'] else 'no'}. " + "; ".join(f"{k}: IR {v['info_ratio_annual']}, deflated probability {v['deflated_prob']}" for k, v in r04["variants"].items()) + f". Deflated probability uses an assumed trial IR spread of {r04['trial_ir_spread_assumed']} over {r04['n_trials']} trials (assumed, disclosed). Scores stay display-only."]
    op = R["OPT"]
    if len(op):
        o += ["", "## Options-income (information only, target 0 until you set one)", "Same months for the fund and its underlying index. After-tax return deducts 30% of distributions on US lines.", "",
              "| Group | Line | Since | Return a year after tax | Underlying | Up-capture | Down-capture | CST10 (bps) |", "|---|---|---|---|---|---|---|---|"]
        for _, r in op.sort_values(["group", "CST10_bps"]).iterrows():
            o.append(f"| {r['group']} | {r['ticker']} | {r['since']} | {r['after_tax_ann_pct']}% | {r['underlying_ann_pct']}% | {r['up_capture']} | {r['down_capture']} | {fmt(r['CST10_bps'])} |")
    o += ["", "## Macro context (MAC01-MAC10, never moves money)", "", "| Pillar | Reading | Flag |", "|---|---|---|"]
    o += [f"| {k} {v['name']} | {v['reading']} | {'ON' if v['flag'] else 'off'} |" for k, v in M.items()]
    if R["N"]:
        o += ["", "## News view N (display only; 50 neutral, 25-75)", "", "| Fund group | N |", "|---|---|"]
        o += [f"| {b} | {n} |" for b, n in sorted(R["N"].items(), key=lambda x: -abs(x[1] - 50))]
        o += ["", "Your sleeves: " + ", ".join(f"{k} {v if v is not None else 'not covered'}" for k, v in R["N_sleeve"].items()) + ". News moves no money until REC08 passes (104 weeks of log)."]
    ev = {t: json.loads(L.loc[t, "events"]) for t in L.index if L.loc[t, "events"] not in ("[]", "")}
    if ev:
        o += ["", "## Structural events on lines", ""] + [f"- {t}: " + "; ".join(f"{e[0]} severity {e[1]}: {e[2]}" for e in v) for t, v in ev.items()]
    return "\n".join(o) + "\n"

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--week", required=True); ap.add_argument("--backtests", action="store_true"); a = ap.parse_args()
    cfg = yaml.safe_load((ROOT / "config" / "portfolio_v2.yaml").read_text()); wd = ROOT / "runs" / a.week; wd.mkdir(parents=True, exist_ok=True)
    R = E3.run(week_dir=wd); pl = R2.plan(R, cfg)
    pl["line_choice"] = {k: {"winner": v["winner"], "why": v["why"]} for k, v in R["XW"].items()}
    bt = ROOT / "runs" / "v3_backtests_latest.json"
    if a.backtests or not bt.exists():
        res = {"rec07": R2.rec07(cfg, R["C_usd"]), "rec04": R2.rec04(cfg, R["C_usd"]), "cross_wrapper": cross_wrapper_backtest(R, R["C_usd"]),
               "note": "mix 70/20/10 (crypto excluded, options-income 0): identical to the v2 owner mix, so REC07/REC04 apply to v3 as run"}
        bt.write_text(json.dumps(res, indent=1, default=str))
    res = json.loads(bt.read_text())
    R["UL"].to_csv(wd / "v3_us_lines.csv"); R["OPT"].to_csv(wd / "v3_options_income.csv", index=False)
    (wd / "v3_macro.json").write_text(json.dumps(R["MAC"], indent=1)); (wd / "v3_cross_wrapper.json").write_text(json.dumps(R["XW"], indent=1, default=str))
    R["L"].drop(columns=["name"]).to_csv(wd / "v3_ucits_line_values.csv")
    pl.update({"fit12": R["FIT12"], "fit07": R["FIT07"], "news_by_sleeve": R["N_sleeve"], "macro_state": R["MAC"].get("MAC10", {}).get("state")})
    (wd / "v3_plan.json").write_text(json.dumps(pl, indent=1, default=str))
    n = append_news_log(a.week, R["news_rows"]) if R["news_rows"] else 0
    lp = ROOT / "runs" / "plan_log.csv"; row = pd.DataFrame([{"week": a.week, "asof": str(R["asof"].date()), "orders": json.dumps(pl["orders"]), "gate_pass": res["rec04"]["gate_pass"],
           "mix": json.dumps(R["mix"]), "top_X": json.dumps(R["XS"]["X"].sort_values(ascending=False).head(5).round(1).to_dict()), "engine": "v3"}])
    (pd.concat([pd.read_csv(lp), row]).drop_duplicates("week", keep="last") if lp.exists() else row).to_csv(lp, index=False)
    (wd / "REPORT_V3.md").write_text(report(a.week, R, pl, res, cfg))
    print("wrote", wd / "REPORT_V3.md", "| news rows logged:", n); print(json.dumps({k: pl[k] for k in ("orders", "residue_usd", "notes", "line_choice")}, indent=1))
