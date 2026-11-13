"""Week packs for the 24 news lead agents (NWS01-NWS17 without NWS15, EVT01, EVT02, EVT04-EVT09), pillars v3 news_agent_design step 1.
NWS15 (crypto) is skipped while the owner excludes crypto. Writes runs/<week>/news_packs/<ID>.md and news_packs/index.json.
Usage: python3 -I v3/packs_v3.py --week 2026-W46"""
import argparse, json, sys
from pathlib import Path
import numpy as np, pandas as pd, yaml
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[0]; CACHE = ROOT / "cache"
sys.path.insert(0, str(ROOT / "v2"))
import engine_v2 as E2

SPEC = {p["id"]: p for p in json.loads((ROOT / "config" / "pillars_v3.json").read_text())["pillars"]}
CFG = yaml.safe_load((ROOT / "config" / "portfolio_v2.yaml").read_text())
EXCLUDED = {"NWS15"} if "crypto" in (CFG.get("excluded") or []) else set()
GROUP_PROXY = {"global_equity": "VT", "us_large_broad": "SPY", "us_small_mid_value": "IJR", "us_factor_dividend": "SCHD", "tech_ai_semis": "QQQ",
               "financials": "XLF", "healthcare_biotech": "XLV", "energy_oil": "XLE", "materials_mining_metals": "XLB", "industrials_defense_infra": "XLI",
               "consumer": "XLY", "utilities_realestate": "XLU", "clean_energy_thematic": "ICLN", "developed_ex_us": "EFA", "europe": "VGK", "japan": "EWJ",
               "em_broad": "EEM", "china": "MCHI", "india": "INDA", "govt_bonds": "IEF", "credit_bonds": "LQD", "gold_precious": "GLD",
               "commodities_broad": "CL=F", "sp500_premium_income": "JEPI", "ndx100_premium_income": "JEPQ", "global_premium_income": "JEPG.L"}
ALL_GROUPS = ["global_equity", "us_large_broad", "us_small_mid_value", "us_factor_dividend", "tech_ai_semis", "financials", "healthcare_biotech", "energy_oil",
              "materials_mining_metals", "industrials_defense_infra", "consumer", "utilities_realestate", "clean_energy_thematic", "developed_ex_us", "europe",
              "japan", "asia_dev_other", "em_broad", "china", "india", "latam", "mena_gulf", "em_asia_other", "govt_bonds", "credit_bonds", "gold_precious",
              "commodities_broad", "multi_asset_alt", "sp500_premium_income", "ndx100_premium_income", "global_premium_income"]
NEWS_MAP = {  # config/news_map: pillar -> fund groups it scores (owner-mix groups in every relevant map)
    "NWS01": ["global_equity", "us_large_broad", "developed_ex_us", "em_broad", "govt_bonds", "gold_precious"],
    "NWS02": ["govt_bonds", "credit_bonds", "us_large_broad", "tech_ai_semis", "utilities_realestate", "gold_precious"],
    "NWS03": ["us_large_broad", "us_small_mid_value", "us_factor_dividend", "global_equity"],
    "NWS04": ["tech_ai_semis", "us_large_broad", "global_equity"],
    "NWS05": ["financials", "industrials_defense_infra", "materials_mining_metals", "consumer", "us_small_mid_value"],
    "NWS06": ["healthcare_biotech", "utilities_realestate", "consumer", "us_factor_dividend"],
    "NWS07": ["europe", "developed_ex_us", "global_equity"],
    "NWS08": ["japan", "asia_dev_other", "developed_ex_us"],
    "NWS09": ["china", "em_broad", "em_asia_other"],
    "NWS10": ["india", "em_broad"],
    "NWS11": ["em_broad", "latam", "em_asia_other", "mena_gulf"],
    "NWS12": ["mena_gulf", "energy_oil", "global_equity", "gold_precious"],
    "NWS13": ["energy_oil", "commodities_broad", "materials_mining_metals", "gold_precious", "clean_energy_thematic"],
    "NWS14": ["global_equity", "us_large_broad", "tech_ai_semis", "em_broad", "govt_bonds", "credit_bonds"],
    "NWS16": ["sp500_premium_income", "ndx100_premium_income", "global_premium_income"],
    "NWS17": ["global_equity", "us_large_broad", "china", "europe", "industrials_defense_infra", "em_broad"],
}
OWNER_GROUPS = {"world": "global_equity", "sp500": "us_large_broad", "ndx100": "tech_ai_semis"}
EVT_IDS = ["EVT01", "EVT02", "EVT04", "EVT05", "EVT06", "EVT07", "EVT08", "EVT09"]

def group_moves():
    c = pd.concat([pd.read_pickle(CACHE / "v3_close_usd.pkl"), pd.read_pickle(CACHE / "v2_close_usd.pkl")], axis=1)
    c = c.loc[:, ~c.columns.duplicated()]
    wk = c.resample("W-FRI").last().pct_change(fill_method=None).iloc[-53:]
    out = {}
    for g, t in GROUP_PROXY.items():
        if t not in wk or "VT" not in wk: continue
        ex = (wk[t] - wk["VT"]).dropna()
        if len(ex) < 30: continue
        sd = ex.iloc[:-1].std()
        if not sd or np.isnan(sd): sd = np.inf  # the world proxy against itself
        r1 = float(ex.iloc[-1]); r4 = float(ex.iloc[-4:].sum())
        out[g] = {"proxy": t, "1w_vs_world_pct": round(r1 * 100, 2), "4w_vs_world_pct": round(r4 * 100, 2),
                  "z_1w": round(r1 / sd, 2), "z_4w": round(r4 / (sd * 2), 2), "unexplained": bool(abs(r1 / sd) > 2 or abs(r4 / (sd * 2)) > 2)}
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--week", required=True); a = ap.parse_args()
    wd = ROOT / "runs" / a.week; pd_ = wd / "news_packs"; pd_.mkdir(parents=True, exist_ok=True)
    mac = json.loads((wd / "v3_macro.json").read_text()) if (wd / "v3_macro.json").exists() else {}
    plan = json.loads((wd / "v3_plan.json").read_text()) if (wd / "v3_plan.json").exists() else {}
    xw = json.loads((wd / "v3_cross_wrapper.json").read_text()) if (wd / "v3_cross_wrapper.json").exists() else {}
    held = sorted((CFG.get("positions") or {}).keys())
    short = sorted({v["winner"] for v in xw.values()} | {x["ticker"] for x in plan.get("orders", [])} | set(CFG.get("orderable") or []))
    subs = {k: list(v["ucits_lines"]) + [x["ticker"] for x in v["us_lines"]] for k, v in xw.items()}
    moves = group_moves()
    prev = sorted((ROOT / "runs").glob("20*-W*")); prev = [p for p in prev if p.name < a.week]
    last = {}
    if prev and (prev[-1] / "news").exists():
        for f in (prev[-1] / "news").glob("*.json"):
            try: j = json.loads(f.read_text()); last[j.get("pillar_id", f.stem)] = {"group_scores": j.get("group_scores"), "open_threads": j.get("open_threads", [])}
            except Exception: pass
    mac_map = {"NWS01": ["MAC01", "MAC04", "MAC08"], "NWS02": ["MAC02", "MAC04"], "NWS11": ["MAC05"], "EVT08": ["MAC05"], "NWS12": ["MAC07"], "NWS13": ["MAC07"], "NWS16": ["MAC03"]}
    index = []
    for pid in [f"NWS{i:02d}" for i in range(1, 18)] + EVT_IDS:
        if pid in EXCLUDED: continue
        p = SPEC[pid]; groups = NEWS_MAP.get(pid, list(OWNER_GROUPS.values()))
        unexpl = [g for g in groups if moves.get(g, {}).get("unexplained")]
        macs = {m: mac.get(m) for m in mac_map.get(pid, [])}
        A = min(4, (1 if unexpl else 0) + (1 if any(v and v.get("flag") for v in macs.values()) else 0) + (1 if last.get(pid, {}).get("open_threads") else 0)
                + (1 if (held and pid.startswith("EVT")) or set(groups) & set(OWNER_GROUPS.values()) else 0))
        body = [f"# Week pack {pid}: {p['name']} (week {a.week})", "", "## Scope (pillars v3)", p["definition"], "", f"Sources: {p['data_source']}", "",
                "## Fund groups you score (-2..+2 for the next 1-3 months; NWS: against the world; premium-income groups: against their underlying)", ", ".join(groups),
                "", "Owner mix: world 70% (VWRA.L), S&P 500 20%, Nasdaq-100 10%. Owner-mix groups: global_equity (world), us_large_broad (S&P 500), tech_ai_semis and us_large_broad (Nasdaq-100). Crypto excluded by the owner.",
                "", "## Group moves against the world (proxy ETF; z on 52-week volatility; |z| > 2 = unexplained, seed a topic)", "| group | proxy | 1w vs world % | z | 4w vs world % | z | unexplained |", "|---|---|---|---|---|---|---|"]
        body += [f"| {g} | {moves[g]['proxy']} | {moves[g]['1w_vs_world_pct']} | {moves[g]['z_1w']} | {moves[g]['4w_vs_world_pct']} | {moves[g]['z_4w']} | {'YES' if moves[g]['unexplained'] else ''} |" for g in groups if g in moves]
        body += ["", "## Lines", f"Held: {', '.join(held) or 'none yet (first deposit this month)'}", f"Shortlisted (orders, line-choice winners, owner-confirmed): {', '.join(short)}",
                 "Same-index substitutes: " + "; ".join(f"{k}: {', '.join(v)}" for k, v in subs.items())]
        if pid == "EVT09": body += ["", f"Deposit window: the first LSE trading days of next month after the AED arrives; this month's planned order: {json.dumps(plan.get('orders', []))}"]
        body += ["", "## Macro readings mapped to you", json.dumps(macs, indent=1) if macs else "none mapped", "", "All MAC readings: " + "; ".join(f"{k} {v['reading']} ({'ON' if v['flag'] else 'off'})" for k, v in mac.items()),
                 "", "## Last week", json.dumps(last.get(pid, "no previous v3 run"), default=str), "", f"## Activity index A = {A} (explorer floor = 1 + A = {1 + A}, cap 6 per round)"]
        (pd_ / f"{pid}.md").write_text("\n".join(body) + "\n")
        index.append({"id": pid, "name": p["name"], "groups": groups, "A": A, "unexplained": unexpl, "event": pid.startswith("EVT"), "touches_owner": bool(set(groups) & set(OWNER_GROUPS.values())) or pid.startswith("EVT")})
    (pd_ / "index.json").write_text(json.dumps(index, indent=1)); print("packs:", len(index), "| groups with unexplained moves:", [g for g, v in moves.items() if v["unexplained"]])
