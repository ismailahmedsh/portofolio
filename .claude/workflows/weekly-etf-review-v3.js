export const meta = {
  name: 'weekly-etf-review-v3',
  description: 'Weekly ETF review v3: 24 news lead agents (NWS01-17, EVT01-09) each choosing topics, explorer counts and rounds until saturated, a verifier per pillar, cross-pillar synthesis, engine re-run, 6 family judges, committee until unanimous, one-page plan',
  whenToUse: 'Every Saturday after v3/data_v3.py, v2/data_v2.py, v3/run_v3.py and v3/packs_v3.py have run for the week',
  phases: [
    { title: 'News', detail: 'one lead per news pillar: topics, explorers, saturation test, rounds' },
    { title: 'Verify', detail: 'blind verifier per pillar re-checks +/-2 scores and severity 2+, fetches sources, writes news and event files' },
    { title: 'Synthesis', detail: 'de-duplicate facts across pillars, cross-topic chains' },
    { title: 'Engine', detail: 're-run engine v3 with events and news' },
    { title: 'Families', detail: '6 judges for the code-computed pillar families' },
    { title: 'Committee', detail: '5 members vote until unanimous' },
    { title: 'Write', detail: 'one-page weekly plan' },
  ],
}

const A = args || {}
const WEEK = A.week, ROOT = A.root, WINDOW = A.window
const RUN = `${ROOT}/runs/${WEEK}`
const NEWS_BUDGET = A.newsBudget || 260, OTHER_BUDGET = A.otherBudget || 60
const VERIFY_BUDGET = A.verifyBudget || 24  // own budget: one blind verifier per pillar, never used up by leads and explorers
const MAX_ROUNDS = A.maxRounds || 4, MAX_PER_ROUND = A.maxPerRound || 6, MAX_PER_PILLAR = A.maxPerPillar || 18
const MAX_COMMITTEE = A.maxCommitteeRounds || 3
const PILLARS = A.pillars || []  // contents of runs/<week>/news_packs/index.json
let newsSpent = 0, otherSpent = 0, verifySpent = 0; const skipped = []
async function spawnNews(prompt, opts) {
  if (newsSpent >= NEWS_BUDGET) { skipped.push(opts.label); log(`news budget ${NEWS_BUDGET} reached, skipped ${opts.label}`); return null }
  newsSpent++; return agent(prompt, opts)
}
async function spawnVerify(prompt, opts) {
  if (verifySpent >= VERIFY_BUDGET) { skipped.push(opts.label); log(`verify budget ${VERIFY_BUDGET} reached, skipped ${opts.label}`); return null }
  verifySpent++; return agent(prompt, opts)
}
async function spawnOther(prompt, opts) {
  if (otherSpent >= OTHER_BUDGET) { skipped.push(opts.label); log(`budget ${OTHER_BUDGET} reached, skipped ${opts.label}`); return null }
  otherSpent++; return agent(prompt, opts)
}

const GROUPS = ['global_equity','us_large_broad','us_small_mid_value','us_factor_dividend','tech_ai_semis','financials','healthcare_biotech','energy_oil','materials_mining_metals','industrials_defense_infra','consumer','utilities_realestate','clean_energy_thematic','developed_ex_us','europe','japan','asia_dev_other','em_broad','china','india','latam','mena_gulf','em_asia_other','govt_bonds','credit_bonds','gold_precious','commodities_broad','multi_asset_alt','sp500_premium_income','ndx100_premium_income','global_premium_income']
const TOPIC = { type: 'object', properties: { topic: { type: 'string' }, why: { type: 'string' }, groups: { type: 'array', items: { type: 'string', enum: GROUPS } }, search_hints: { type: 'string' } }, required: ['topic', 'why', 'groups'] }
const LPLAN = { type: 'object', properties: { headline_checks: { type: 'array', items: { type: 'string' } }, explorer_count_reason: { type: 'string' }, topics: { type: 'array', items: TOPIC, minItems: 1, maxItems: 6 } }, required: ['headline_checks', 'explorer_count_reason', 'topics'] }
const FACT = { type: 'object', properties: { id: { type: 'string' }, claim: { type: 'string' }, date: { type: 'string' }, source: { type: 'string' }, url: { type: 'string' }, quote: { type: 'string' }, tier: { type: 'string', enum: ['T1', 'T2', 'T3'] }, kind: { type: 'string', enum: ['fact', 'opinion'] }, in_window: { type: 'boolean' } }, required: ['id', 'claim', 'date', 'source', 'url', 'quote', 'tier', 'kind', 'in_window'] }
const GEFF = { type: 'object', properties: { group: { type: 'string', enum: GROUPS }, score: { type: 'integer', minimum: -2, maximum: 2 }, reason: { type: 'string' } }, required: ['group', 'score', 'reason'] }
const SEV = { type: 'object', properties: { target: { type: 'string' }, severity: { type: 'integer', minimum: 0, maximum: 3 }, issue: { type: 'string' }, url: { type: 'string' }, date: { type: 'string' } }, required: ['target', 'severity', 'issue', 'url'] }
const EXPL = { type: 'object', properties: { topic: { type: 'string' }, facts: { type: 'array', items: FACT }, group_effects: { type: 'array', items: GEFF }, severities: { type: 'array', items: SEV }, new_threads: { type: 'array', items: TOPIC } }, required: ['topic', 'facts', 'group_effects', 'severities', 'new_threads'] }
const GSCORE = { type: 'object', properties: { group: { type: 'string', enum: GROUPS }, score: { type: 'integer', minimum: -2, maximum: 2 }, confidence: { type: 'string', enum: ['high', 'medium', 'low'] }, rationale: { type: 'string' }, falsifier: { type: 'string' }, fact_ids: { type: 'array', items: { type: 'string' } }, n_sources: { type: 'integer' } }, required: ['group', 'score', 'confidence', 'rationale', 'falsifier', 'fact_ids', 'n_sources'] }
const LEVAL = { type: 'object', properties: {
  saturated: { type: 'boolean' }, tests: { type: 'object', properties: { no_score_change: { type: 'boolean' }, few_new_facts: { type: 'boolean' }, no_relevant_open_thread: { type: 'boolean' }, every_group_sourced: { type: 'boolean' } }, required: ['no_score_change', 'few_new_facts', 'no_relevant_open_thread', 'every_group_sourced'] },
  rationale: { type: 'string' }, group_scores: { type: 'array', items: GSCORE }, severities: { type: 'array', items: SEV },
  next_topics: { type: 'array', items: TOPIC, maxItems: 6 }, open_threads: { type: 'array', items: { type: 'string' } }, extra_round_reason: { type: 'string' } },
  required: ['saturated', 'tests', 'rationale', 'group_scores', 'severities', 'next_topics', 'open_threads'] }
const VOUT = { type: 'object', properties: { written: { type: 'boolean' }, changes: { type: 'array', items: { type: 'string' } }, digest: { type: 'string' }, group_scores: { type: 'array', items: GSCORE }, severities: { type: 'array', items: SEV }, top_facts: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, url: { type: 'string' }, date: { type: 'string' } }, required: ['claim', 'url'] } } }, required: ['written', 'changes', 'digest', 'group_scores', 'severities', 'top_facts'] }
const SYN = { type: 'object', properties: { duplicates_resolved: { type: 'array', items: { type: 'string' } }, contradictions: { type: 'array', items: { type: 'string' } }, chains: { type: 'array', items: { type: 'string' } }, owner_relevant: { type: 'array', items: { type: 'string' } } }, required: ['duplicates_resolved', 'contradictions', 'chains', 'owner_relevant'] }
const INV = { type: 'object', properties: { question: { type: 'string' }, answer: { type: 'string' }, evidence: { type: 'array', items: { type: 'string' } }, implication: { type: 'string' } }, required: ['question', 'answer', 'evidence', 'implication'] }
const FAMV = { type: 'object', properties: { family: { type: 'string' }, verdict: { type: 'string' }, deposit_view: { type: 'string' }, line_view: { type: 'string' }, sell_view: { type: 'string' }, watch: { type: 'array', items: { type: 'string' } }, questions: { type: 'array', items: { type: 'string' }, maxItems: 2 } }, required: ['family', 'verdict', 'deposit_view', 'line_view', 'sell_view', 'watch', 'questions'] }
const PLAN = { type: 'object', properties: {
  deposit: { type: 'array', items: { type: 'object', properties: { line: { type: 'string' }, units: { type: 'number' }, usd: { type: 'number' }, reason: { type: 'string' } }, required: ['line', 'units', 'usd', 'reason'] } },
  carry_usd: { type: 'number' }, sells: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, reason: { type: 'string' } }, required: ['ticker', 'reason'] } },
  why_not_others: { type: 'string' }, news_that_matters: { type: 'array', items: { type: 'string' } }, watchlist: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, trigger: { type: 'string' } }, required: ['item', 'trigger'] } },
  owner_todo: { type: 'array', items: { type: 'string' } }, rule_citations: { type: 'array', items: { type: 'string' } } },
  required: ['deposit', 'carry_usd', 'sells', 'why_not_others', 'news_that_matters', 'watchlist', 'owner_todo', 'rule_citations'] }
const VOTE = { type: 'object', properties: { approve: { type: 'boolean' }, comment: { type: 'string' }, objections: { type: 'array', items: { type: 'object', properties: { point: { type: 'string' }, evidence_needed: { type: 'string' } }, required: ['point', 'evidence_needed'] } } }, required: ['approve', 'comment', 'objections'] }

const OWNER = `Owner: Canadian citizen resident in the UAE (no US treaty: 30% US dividend withholding, US estate tax above US$60,000), IBKR, deposits 2,500 AED (about US$679) a month. Strategic mix (also the yardstick): world 70% (VWRA.L), S&P 500 20%, Nasdaq-100 10%. Crypto excluded by the owner for now. Options-income at 0% (information only). Rules: ${ROOT}/DECISION_RULES_V3.md.`
const SCORING = `Scoring rules (pillars v3): score each mapped fund group -2..+2 for expected USD return over the next 1-3 months against the world (premium-income groups against their underlying). Judge policy, fundamentals and flows, not price moves alone. 0 is the default; most groups score 0 or +/-1 in most weeks. |1| needs 2 independent dated sources inside the window; |2| needs a T1 primary source plus a T2 report (Reuters, Bloomberg, FT, WSJ, Nikkei) and a concrete, material development. Opinion never supports a 2; a T3 source can open a thread but never supports a score alone. Each score has confidence (high, medium, low), a 2-4 sentence rationale, what would prove it wrong, and fact ids. Material older than the window is background and never sets a score.`

// ---------- News: one lead per pillar, rounds until saturated ----------
async function runLead(p) {
  const pack = `${RUN}/news_packs/${p.id}.md`
  const evt = p.event
  const floor = Math.min(MAX_PER_ROUND, 1 + (p.A || 0))
  const plan = await spawnNews(`You are the lead agent for news pillar ${p.id} (${p.name}), week ${WEEK}, window ${WINDOW}. Read your week pack ${pack}. Run 1-2 dated headline searches for your scope, then choose your topics. You must seed a topic for: every unexplained group move in the pack; every owner-mix group in your map (at least a 'no material news' check); every carried-over open thread; every scheduled event in the window; every mapped MAC flag that is ON.${evt ? ' As an event pillar, also cover your fixed checklist from the pack (held and shortlisted lines and their same-index substitutes, issuers, tax rules, venues).' : ''} Topics must be specific (a release, decision, company, filing or country event), merged where they overlap. Choose how many explorers to send: at least ${floor} (floor = 1 + activity index), at most ${MAX_PER_ROUND}. A quiet scope may use the floor. ${OWNER}`,
    { label: `lead:${p.id}:plan`, phase: 'News', schema: LPLAN })
  if (!plan) return null
  let topics = plan.topics.slice(0, MAX_PER_ROUND); const asked = new Set(); const findings = []; const evals = []; let used = 0; let r = 0; let saturated = false
  const cap = evt ? MAX_ROUNDS + 1 : MAX_ROUNDS
  while (topics.length && r < cap && used < MAX_PER_PILLAR) {
    r++
    const fresh = topics.filter(t => !asked.has(t.topic.toLowerCase())).slice(0, Math.min(MAX_PER_ROUND, MAX_PER_PILLAR - used))
    fresh.forEach(t => asked.add(t.topic.toLowerCase())); used += fresh.length
    if (!fresh.length) break
    log(`${p.id} round ${r}: ${fresh.length} explorer(s)`)
    const got = (await parallel(fresh.map((t, k) => () => spawnNews(`News explorer for ${p.id} (${p.name}), week ${WEEK}, round ${r}. Topic: ${t.topic}\nWhy: ${t.why}\nGroups: ${t.groups.join(', ')}\nHints: ${t.search_hints || ''}\nUse web search and fetch the pages you cite. Window: ${WINDOW}; earlier material only as labelled background (in_window=false). Every fact needs a date, source, URL and a short verbatim quote copied from the page; no URL, no fact. Tier: T1 primary source (central bank, statistics office, company or issuer release, filing, regulator), T2 top-tier press, T3 other. Give a provisional score per affected group (-2..+2) and, for structural matters, a severity for the affected line or issuer (0 info, 1 watch, 2 adverse confirmed change, 3 severe: sanctions or market access). List new threads you could not cover. ${SCORING}`,
      { label: `explore:${p.id}:r${r}:${k + 1}`, phase: 'News', schema: EXPL })))).filter(Boolean)
    findings.push(...got.map(g => ({ ...g, round: r })))
    const ev = await spawnNews(`You are the lead for ${p.id} (${p.name}), week ${WEEK}, after round ${r} of at most ${cap}. Explorers used ${used} of ${MAX_PER_PILLAR}. Your pack: ${pack}. Topics asked: ${[...asked].join(' | ')}.\nAll findings:\n${JSON.stringify(findings)}\nPrevious evaluation: ${JSON.stringify(evals[evals.length - 1] || null)}\n\nScore every group in your map (${(p.groups || []).join(', ')}) under the rules below, and ${evt ? 'give a severity for each affected line or issuer (severity 2 or more needs a T1 source with the quoted text). ' : ''}Then run the saturation test. Saturated only when all four hold: (i) this round changed no group score by 1 or more and no severity; (ii) fewer than 20% of this round's facts are new distinct T1 or T2 facts; (iii) no open thread could change a group score by 1 or more, a severity, a gate or the US$60k cap; (iv) every mapped group has at least 2 dated sources or an explicit null check. If not saturated, give next topics only for threads that pass (iii), no repeats. ${r >= cap ? 'This is the round cap: you may request one extra round only with a logged reason in extra_round_reason.' : ''} ${SCORING} ${OWNER}`,
      { label: `lead:${p.id}:eval${r}`, phase: 'News', schema: LEVAL })
    if (!ev) break
    evals.push(ev); saturated = ev.saturated
    topics = saturated ? [] : ev.next_topics
    if (!saturated && r >= cap && ev.extra_round_reason && used < MAX_PER_PILLAR) { log(`${p.id}: extra round granted (${ev.extra_round_reason})`); r = cap - 1 }
  }
  const last = evals[evals.length - 1]
  if (!last) return null
  if (!saturated) log(`${p.id}: stopped unsaturated after ${r} round(s); scores capped at |1|, confidence low`)
  return { id: p.id, name: p.name, event: evt, rounds: r, explorers: used, saturated, final: last, findings, plan_reason: plan.explorer_count_reason }
}

async function verify(res) {
  if (!res) return null
  return spawnVerify(`You are the blind verifier for news pillar ${res.id} (${res.name}), week ${WEEK}, window ${WINDOW}. You did not produce these scores. (1) Fetch every URL behind a score of +/-2 and every severity of 2 or more and check the page exists, its date is inside the window, and the quoted text is on the page; also spot-check at least 3 other cited URLs. Search for a missing counter-fact for each +/-2. A +/-2 survives only if there is no missing counter-fact and no unconfirmed source; otherwise lower it to +/-1. A severity of 2+ survives only with a confirmed T1 quote; otherwise lower to 1. Any score left with fewer than 2 valid dated sources becomes 0 with low confidence. ${res.saturated ? '' : 'The pillar stopped unsaturated: cap every score at |1| and confidence at low.'} (2) Write ${RUN}/news/${res.id}.json (create the folder) with: {"pillar_id","week","saturated","rounds","explorers","group_scores":[{group,score,confidence,rationale,falsifier,fact_ids,n_sources}],"severities":[...],"facts":[{id,claim,date,source,url,quote,tier,kind,in_window,verified}],"open_threads":[...],"verifier_changes":[...]}${res.event ? ` and also ${RUN}/events/${res.id}.json with {"pillar_id":"${res.id}","week":"${WEEK}","summary":"...","events":[{"target":"line ticker such as VWRA.L or a sleeve name world/sp500/ndx100","severity":0,"issue":"...","url":"...","date":"YYYY-MM-DD"}]}` : ''}. (3) Write a digest under 300 words to ${RUN}/news/${res.id}.md. Return what you wrote.\n\nLead result:\n${JSON.stringify({ rounds: res.rounds, explorers: res.explorers, saturated: res.saturated, final: res.final, facts: res.findings.flatMap(f => f.facts) })}`,
    { label: `verify:${res.id}`, phase: 'Verify', schema: VOUT })
}

phase('News')
const order = [...PILLARS].sort((a, b) => (b.event - a.event) || (b.touches_owner - a.touches_owner) || ((b.A || 0) - (a.A || 0)))
const verified = (await pipeline(order, p => runLead(p), res => verify(res).then(v => v ? { id: res.id, rounds: res.rounds, explorers: res.explorers, saturated: res.saturated, ...v } : null))).filter(Boolean)
const leadsDone = verified.length
log(`news: ${leadsDone}/${order.length} pillars written; ${newsSpent} news agents, ${verifySpent} verifiers`)

phase('Synthesis')
const syn = await spawnOther(`You are the cross-pillar news synthesiser, week ${WEEK}. Read every ${RUN}/news/*.json. (1) De-duplicate facts by URL and event: each event gets one owning pillar and is scored once; where the same event drives a score in a second pillar, edit that second file so its group score no longer counts it (lower the score or set it to 0 with a note in verifier_changes). (2) Flag contradictions between pillars. (3) Name cross-topic chains (for example oil supply shock, then breakevens, then real yields, then the Nasdaq-100). (4) List what matters to this owner's three sleeves (global_equity, us_large_broad, tech_ai_semis) and any EVT severity of 1 or more. Write ${RUN}/news/SYNTHESIS.md (under 400 words). ${OWNER}`,
  { label: 'synthesiser', phase: 'Synthesis', schema: SYN })

phase('Engine')
const engine = await spawnOther(`Run from ${ROOT} and report: (1) python3 -I -c "import json,glob; [json.load(open(p)) for p in glob.glob('${RUN}/news/*.json')+glob.glob('${RUN}/events/*.json')]; print('ok')" and if it fails fix only JSON syntax in the failing file and retry; (2) python3 -I v3/run_v3.py --week ${WEEK}. Then reply with these sections of ${RUN}/REPORT_V3.md verbatim: "This month's deposit", "Sell anything?", "US-listed or London?", "Macro context", "News view N", "Structural events on lines" (if present), and the cross-wrapper backtest table.`,
  { label: 'engine', phase: 'Engine' })

phase('Families')
const FAMS = [
  ['line_choice', 'Line choice and safety (ELG, CST, TAX, DUR): which line in each sleeve, London vs US after the 30% dividend tax, gates, orderability'],
  ['exposure', 'Exposure, valuation and risk (EXR, FAC, RSK, CON) and options-income (OPT): ' + `${RUN}/v2_exposure.csv if present, ${RUN}/v3_options_income.csv`],
  ['fit', 'Fit with the owner mix (FIT01-FIT13): sleeve gaps, US look-through, US$60k gauge, line count'],
  ['macro', 'Macro context (MAC01-MAC10): flags and what they mean for a monthly depositor (never move money)'],
  ['record', 'Record and testing (REC01-REC10): backtests REC04 and REC07 in runs/v3_backtests_latest.json, cross-wrapper backtest, plan log, news log'],
  ['news', 'News and events (NWS, EVT): the verified news files and synthesis'],
]
const families = (await parallel(FAMS.map(([f, scope]) => () => spawnOther(`You are the family judge for "${f}": ${scope}. Week ${WEEK}. Read ${RUN}/REPORT_V3.md, ${RUN}/v3_plan.json and the files your family needs (${RUN}/v3_us_lines.csv, ${RUN}/v3_cross_wrapper.json, ${RUN}/v3_macro.json, ${RUN}/news/, ${ROOT}/config/pillars_v3.json for definitions). Say what your family implies for this month's deposit, the line in each sleeve, any sale, and what to watch. Scores are display-only unless the REC04 gate passed; news moves no money until REC08 passes. Ask at most 2 questions only if an answer could change a decision. Do not modify files. ${OWNER}\n\nEngine output:\n${engine}\n\nSynthesis:\n${JSON.stringify(syn)}`,
  { label: `family:${f}`, phase: 'Families', schema: FAMV })))).filter(Boolean)
const qs = families.flatMap(f => f.questions.map(q => ({ f: f.family, q }))).slice(0, 4)
const answers = (await parallel(qs.map((x, k) => () => spawnOther(`Investigator for family ${x.f}, week ${WEEK}. Question: ${x.q}\nAnswer from ${RUN}, ${ROOT}/cache data (python3 -I), the rules and the web as needed. Cite sources. Do not modify files.`,
  { label: `finv:${k + 1}`, phase: 'Families', schema: INV })))).filter(Boolean)

phase('Committee')
const MEMBERS = [
  ['rules', 'Evidence and rules keeper: DECISION_RULES_V3.md, the REC04 and REC08 gates; no action without a rule or a structural event'],
  ['risk', 'Risk manager: drawdown, concentration, behaviour of a monthly depositor, the US$60k cap'],
  ['macro_news', 'Macro and news strategist: what the verified news and macro flags imply over 1-3 months, and whether any of it is structural'],
  ['quant', 'Quant: exposure, factor, backtest and cross-wrapper evidence; whether any signal is strong enough to matter'],
  ['uae', 'UAE execution and tax: line choice and gates, whole shares and carry, 30% US withholding, IBKR costs, orderability'],
]
const CONTEXT = `${OWNER}\nReport: ${RUN}/REPORT_V3.md; plan: ${RUN}/v3_plan.json; backtests: ${ROOT}/runs/v3_backtests_latest.json; news: ${RUN}/news/.\nEngine output:\n${engine}\nFamily verdicts:\n${JSON.stringify(families)}\nInvestigations:\n${JSON.stringify(answers)}\nNews synthesis:\n${JSON.stringify(syn)}\nVerified pillar digests:\n${JSON.stringify(verified.map(v => ({ id: v.id, saturated: v.saturated, rounds: v.rounds, digest: (v.digest || '').slice(0, 600), scores: v.group_scores, sev: v.severities })))}`
let plan = null, votes = [], history = [], extra = []
for (let r = 1; r <= MAX_COMMITTEE; r++) {
  plan = await spawnOther(`You are the committee chair, week ${WEEK}, round ${r}. Draft the owner's plan: this month's order(s) (start from v3_plan.json, which follows the rules), any sale (only on a structural event under S1/S2), why the money does not go elsewhere this month, the news that matters to the owner (with links), the watchlist with triggers, and the owner's to-do list. Cite the rule or evidence behind every action. ${r > 1 ? 'Revise the previous plan to resolve the objections with the new evidence; keep what nobody objected to.\nPrevious plan: ' + JSON.stringify(history[history.length - 1].plan) + '\nObjections: ' + JSON.stringify(history[history.length - 1].votes) + '\nNew evidence: ' + JSON.stringify(extra) : ''}\n\n${CONTEXT}`,
    { label: `chair:r${r}`, phase: 'Committee', schema: PLAN })
  if (!plan) break
  votes = (await parallel(MEMBERS.map(([k, lens]) => () => spawnOther(`You are committee member "${k}". Lens: ${lens}. Week ${WEEK}, round ${r}. Vote on the plan. Approve only if you would sign it as written; otherwise list each objection with the evidence that would resolve it. No objections on style.\n\nPlan:\n${JSON.stringify(plan)}\n\n${CONTEXT}`,
    { label: `vote:${k}:r${r}`, phase: 'Committee', schema: VOTE }).then(v => v ? { member: k, ...v } : null)))).filter(Boolean)
  history.push({ round: r, plan, votes })
  const objections = votes.filter(v => !v.approve).flatMap(v => v.objections.map(o => ({ member: v.member, ...o })))
  log(`committee round ${r}: ${votes.filter(v => v.approve).length}/${votes.length} approve`)
  if (!objections.length && votes.length === MEMBERS.length) break
  extra = (await parallel(objections.slice(0, 5).map((o, k) => () => spawnOther(`Committee investigator, week ${WEEK}, round ${r}. Member "${o.member}" objected: ${o.point}\nEvidence needed: ${o.evidence_needed}\nFind it from ${RUN}, the rules, the backtests, the data or the web and state plainly whether it supports the objection. Do not modify files.`,
    { label: `cinv:r${r}:${k + 1}`, phase: 'Committee', schema: INV })))).filter(Boolean)
  if (objections.length > 5) log(`only 5 of ${objections.length} objections investigated this round`)
}
const unanimous = votes.length === MEMBERS.length && votes.every(v => v.approve)

phase('Write')
const stats = { news_pillars: leadsDone, news_rounds: verified.reduce((a, v) => a + (v.rounds || 0), 0), news_explorers: verified.reduce((a, v) => a + (v.explorers || 0), 0), news_agents: newsSpent, verify_agents: verifySpent, other_agents: otherSpent, committee_rounds: history.length, unanimous, skipped: skipped.length }
const written = await spawnOther(`Write the owner's one-page weekly plan to ${RUN}/WEEKLY_PLAN_V3.md. Plain language, short sentences, no em-dashes, no jargon codes in the main text (pillar ids only in the last line). Under 400 words. Sections, in this order:
1. "This month": the order as one line (buy N x LINE, about US$X, carry US$Y), then 3 short reasons.
2. "Hold or sell": one line.
3. "Why not elsewhere this month": 2-3 short lines (S&P 500, Nasdaq-100, US-listed, options-income).
4. "News that matters to you": at most 5 bullets, each one line with a link.
5. "Watch": at most 3 bullets with the trigger.
6. "Your to-do": at most 4 bullets.
7. One last line: committee ${unanimous ? 'unanimous' : 'not unanimous (rules default applied: engine order, no sales)'} after ${history.length} round(s); agents used: ${newsSpent} news, ${verifySpent} verifiers, ${otherSpent} other.
If the committee was not unanimous, the default under DECISION_RULES_V3.md applies (the engine's v3_plan.json order, no sales) and you must say so.
Final plan: ${JSON.stringify(plan)}\nVotes: ${JSON.stringify(votes)}\nReply with the full text you wrote.`,
  { label: 'writer', phase: 'Write' })

return { week: WEEK, unanimous, committee_rounds: history.length, final_plan: plan, final_votes: votes, stats,
  pillars: verified.map(v => ({ id: v.id, rounds: v.rounds, explorers: v.explorers, saturated: v.saturated, scores: v.group_scores, severities: v.severities, changes: v.changes })), synthesis: syn, skipped, written }
