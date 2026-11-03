# Reviewer 2: software and agent engineer

Date: 2026-11-03. Object: `plan/plan_v3.md` (P6-P14), report R8-R14 and Tables F-J, `data/verify/*`, `audits/plan_audit_round2.md`. No new research.

## Verdict: APPROVE WITH CONDITIONS

The portfolio part needs no software. The monitor is buildable and the "Python computes, Claude narrates" split is the right shape, but three wiring faults mean the plan's own fail-closed and least-privilege claims are not yet true of the design as written. Each is a half-day fix; none changes a number in the plan.

## Blocking issues

**1. The grounding gate has no enforcement point (P8 daily SKILL.md, P10, P8 wrappers).** The daily skill never runs `run_daily.py --check` (only the monthly skill does); the model writes the final `reports/daily/<date>.md` itself; the wrapper rsyncs and pushes whatever file exists; the cloud task pushes "changes under reports/". A model that ignores step 5 produces a committed, pushed note with an ungrounded number, and idempotency ("if the .md exists, stop") then protects the bad file from a re-run. Fix: the model writes only `reports/daily/<date>.prose.md`; `python run_daily.py --assemble` runs the grounding check and writes the final file atomically (tmp, rename) or writes the tables-only stub with `state: DEGRADED (grounding)`; the wrapper runs `--assemble` after `claude` exits and commits only files that passed. Idempotency keys on the assembled file. Same for monthly.

**2. Least privilege rests on SKILL.md `allowed-tools` and an unverified flag (P8, P13).** Skill `allowed-tools` is a pre-approval list, not a deny list; what blocks an unlisted tool is the permission policy of the headless run. The plan's whole safety claim ("the two Bash strings are the only commands this skill may run") therefore depends on `--permission-prompts none` meaning "deny unprompted" rather than "skip prompts". The CLI accepted the flag in the probe, but its semantics were never exercised. Fix: commit `etf-monitor/.claude/settings.json` with `permissions.deny` for `Bash(git *)`, `Bash(curl *)`, `WebFetch`, `WebSearch`, all `mcp__*`, and `permissions.allow` carrying the exact strings; add to Phase 2a a negative test (skill asked to run `git status`, must be denied). This also makes `--strict-mcp-config` belt-and-braces instead of load-bearing.

**3. Two writers, two bases, one branch (P8 cloud task, wrappers, P9).** The cloud task clones the default branch, where `reports/` and `flags.csv` do not exist, yet the run needs the previous `flags.csv` for `CHANGED` and the previous `.tables.md` for "last good date"; its commit, based on main, is then pushed to `reports`, which the local wrapper also advances, so pushes are non-fast-forward from the first collision. Fix: one scheduler per artifact and reports on the default branch (private, single-owner repo; the worktree, rsync and rebase machinery goes away), or prove in Phase 3 that the task can check out `reports`. Until then run daily and monthly from local cron only.

## Material concerns

1. **FRED is not verified from Python (P9).** `t1_keyless_endpoints.sh` got HTTP/2 INTERNAL_ERROR then "empty reply" on HTTP/1.1 for every `fredgraph.csv` URL; the only data came "via WebFetch", a Claude tool unavailable in the pipeline. The backtest consumes `fred_DEXCAUS_via_webfetch.csv`. P9 also lists macro as a numeric source whose failure marks DEGRADED, so an unreachable FRED makes every daily note DEGRADED. Demote macro to context (news treatment), and verify the Python route in Phase 2a; BoC Valet is verified and covers FX.
2. **`claude -p` exits 0 on error.** The probe shows `subtype: success, is_error: true, total_cost_usd: 0`. `run || { sleep 900; run; }` never retries that. Parse `is_error` and `subtype` from the JSON before deciding retry and before assembling.
3. **Budget-interrupted runs leave partial files.** `--max-budget-usd 0.30` with `context: fork` (two contexts, CLAUDE.md, tables, news.json) is tight on change days; a mid-write stop plus existence-keyed idempotency equals a permanently half-written note. Blocking 1's atomic assemble fixes it; measure a change-day run before fixing 0.30.
4. **The digit-grep grounding check will false-positive constantly.** The stress line ("50.8%", "2007-09"), "S&P 500", "10-month SMA", "T1135", "12 months" and headline dates all contain digits not in the tables. Whitelist the template text, the headline strings from `news.json`, and the tables; otherwise the owner disables the check within a month.
5. **Ledger reconciliation tolerance (P10).** Recurring buys fill intraday; comparing units to `cad_amount / Close` at 0.5% will raise REVIEW on most volatile days. Test against the day's High-Low range, or reconcile to the broker's confirmed unit price recorded in the ledger.
6. **yfinance pin plus quarterly-only bumps (P13).** Yahoo breaks yfinance several times a year and the fix is usually a patch release within days; forbidding an out-of-cycle bump forces up to 12 weeks of stale prices or a $19.99 EODHD escalation. Allow a patch bump any time the dry-run reproduces a past report byte-for-byte. Also, verification ran on Python 3.13 while the plan pins 3.12; generate `requirements.lock` on 3.12. `pandas` has no version in the text.
7. **Cloud egress is the wrong primary.** Yahoo rate-limits by IP; shared cloud NAT addresses are the common 429 case. Make local cron primary and cloud the fallback (inverse of P8), which also resolves Blocking 3 and the unverified Telegram network-secret (the bot token travels in the URL path, not a header).
8. **Platform details.** `CRON_TZ` in a crontab and `date -d "-1 day"` are GNU/cronie only (not macOS); the `uvx` entry points are guesses (plan says so); check `Write(reports/daily/*)` against the fork's cwd.

## Simplification proposals (ship the MVP faster)

- **Python first, Claude only on change days.** Run `python run_daily.py` from cron; invoke `claude -p` only when it prints `CHANGED: yes`. Stubs need no model. That removes about 90% of model runs, most of the budget question, most of the injection surface, and the `context: fork` indirection.
- **Reports on the default branch, one scheduler (local cron).** Delete the worktree, rsync, rebase and ruleset. Cloud task becomes Phase 5 optional.
- **Defer** `.mcp.json` entirely, the `bt` cross-check (keep Portfolio Visualizer), the five-CSV look-through concentration table (XEQT's own CSV suffices), and the Opus monthly run (Sonnet, `--max-budget-usd 1`).
- **Notifier**: none in year 1; the owner opens the monthly review on the 1st. If kept, local only.
- Realistic effort with these cuts: 12-18 hours to a running daily and monthly note; the plan's 25-35 hours for the full design is optimistic by roughly half.

## Failure-mode table

| Component | Failure | Detection | Plan's fallback | Assessment |
|---|---|---|---|---|
| yfinance | empty frame, 429, crumb error | row count, exception | retry, backoff, DEGRADED with last-good date, EODHD adapter, manual NAV | Adequate, if out-of-cycle patch bump allowed |
| FRED CSV | unreachable from Python (seen in verification) | HTTP error | DEGRADED | Not adequate: context-only, do not gate state |
| BoC Valet | outage | HTTP error | DEGRADED, last-good FX | Adequate |
| iShares CSV | product-id ajax URL changes | parse failure | DEGRADED monthly | Adequate (monthly only); add schema assert on "Fund Holdings as of" |
| Google News RSS | 503 | status | `{"status":"failed"}`, state unchanged | Adequate |
| Claude run | auth error, 429, budget stop | JSON `is_error`/`subtype` | one retry after 15 min | Not adequate until JSON is parsed (concern 2, 3) |
| Grounding | number in prose not in tables | `--check` | "fails the run" | Not adequate: no enforcement point (Blocking 1) |
| Permissions | model calls git/web/MCP | none | `allowed-tools` | Not adequate (Blocking 2) |
| Push | non-FF between cloud and local | wrapper log | rebase, abort, retry | Not adequate for cloud writer (Blocking 3) |
| Scheduler | machine asleep, task late | M7 count | cloud/local swap, M7 waiver | Adequate |
| Ledger | mismatch > 0.5% | REVIEW | owner reads | Adequate once tolerance fixed |
| Dependencies | pin rot, licence change | quarterly `gh api` | drop or bump | Adequate |

## Process judgment

Caught: round 2 found that the monthly Account table with CAD balances was being committed to a branch the cloud clone holds, and that the wrapper pushed `HEAD:reports` with no fetch; both were real and both were fixed in v3. Missed: no auditor read `verify_log.md` against the "verified keyless" claim for FRED (it failed on both curl routes and only WebFetch succeeded), and nobody traced who actually executes the grounding check in the daily path. The audits scored consistency between sections; nobody executed the control flow.

## Summary for the owner

1. Buy XEQT on a recurring order; the software is optional and the plan says so correctly.
2. Before building, change three things: Python assembles every report after running the check (the model never writes the final file); a committed `settings.json` deny list, not SKILL.md, is the permission boundary; one scheduler, reports on the main branch.
3. Verify FRED from plain Python; until then macro is context and cannot mark a day DEGRADED.
4. Run Python first and call Claude only on change days; that cuts cost, risk and build time at once.
5. Budget 15-20 hours for the cut-down MVP, not 25-35 for the full design, and allow yfinance patch bumps whenever a past report reproduces.

## Re-review of plan v4 (2026-11-03)

Object: `plan/plan_v4.md`, "Changes from v3" table verified against P6, P8, P9, P10, P11, P12, P13, P14.

### Blocking issues from the v3 review

| # | Issue | Status | Pointer |
|---|---|---|---|
| B1 | Grounding gate had no enforcement point | **CLOSED** | P6 tree (model writes only gitignored `reports/staging/*.prose.md`); P8 SKILL.md steps 5-7 (`--check` explicit, model never writes the final file); P8 wrapper (`--assemble` after `claude` exits, tmp+rename, `DEGRADED (grounding)` stub on failure or missing staging file); P9 idempotency on the assembled file; P10 "Enforcement point" |
| B2 | Least privilege rested on SKILL.md `allowed-tools` | **CLOSED** | P8 `.claude/settings.json` (four exact allow strings; deny git, curl, wget, gh, pip, ssh, WebFetch, WebSearch, `mcp__*`, writes elsewhere); Assumption 20 negative test gating every scheduled run; P13; P14 Phase 2a. Leaving the deny spelling to the test is right |
| B3 | Two writers, two bases, one branch | **CLOSED** | P8 wrappers (single writer, default branch, fast-forward push, no worktree/rsync/rebase, refuses off-default commits); P8 cloud paragraph (Phase 5 replacement only); P11; P14 Phases 3 and 5 |

### Material concerns

| # | Concern | Status | Pointer |
|---|---|---|---|
| 1 | FRED unverified from Python | CLOSED | P9 Macro row; P10 policy states; Phase 2a; Assumption 19 |
| 2 | `claude -p` exits 0 on error | CLOSED | P8 wrapper `ok()` parses `subtype`/`is_error` |
| 3 | Partial files on budget stop | CLOSED | P9 caching; P8 atomic assembly; measured change-day run |
| 4 | Digit-grep false positives | CLOSED | P10 whitelist (tables, template, stress line, headlines, date) |
| 5 | Ledger tolerance vs Close | CLOSED | P10 two-check reconciliation; P6 `unit_price` = confirmed fill |
| 6 | yfinance bumps, 3.13 lock, pandas | CLOSED | P13 pinning and fallback ladder; P6 |
| 7 | Cloud egress as primary | CLOSED | P8 cloud paragraph; P14 Phase 5 |
| 8 | Platform details | CLOSED | P8 wrapper comments; `uvx` strings stay a stated Assumption, acceptable |

### Residual, non-blocking

1. On a change day `run_daily.py --date today` runs twice (wrapper, then skill step 1); the `flags.csv` append and hash chain must be idempotent by date or the chain check fires on a duplicate row.
2. The wrapper's `set -e` with `out=$(python run_daily.py ...)` ends the run on an uncaught Python exception before `--assemble`, contradicting "never a failed run"; `run_daily.py` must trap vendor errors and always exit 0 with a state.
3. The monthly Opus run at `--max-budget-usd 3` is unmeasured; a stop yields a stub review, acceptable, but measure one real run in Phase 4.

### Final verdict: APPROVE

No blocking issue remains. v4 is buildable by one person in the stated 15-20 hours, fails closed at a Python enforcement point, has a committed and tested permission boundary, and has one writer per artifact. The residual items are Phase 2a implementation notes, not plan changes.
