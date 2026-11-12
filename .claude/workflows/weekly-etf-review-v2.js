export const meta = {
  name: 'weekly-etf-review-v2',
  description: 'Weekly ETF review v2: one agent per computed v2 pillar with self-expanding investigations, expanding news rounds feeding 10 event agents (EVT01-EVT10), 13 family judges, committee under DECISION_RULES_V2 until unanimous',
  whenToUse: 'Every Saturday after v2/data_v2.py, v2/run_v2.py and v2/packs_v2.py have run for the week',
  phases: [
    { title: 'Pillars', detail: 'one agent per computed v2 pillar; each decides whether to open investigation rounds' },
    { title: 'News', detail: 'planner picks topics and agent count; rounds expand until saturated' },
    { title: 'Score', detail: '10 event agents write EVT01-EVT10; engine v2 re-scores 321 lines and re-plans the deposit' },
    { title: 'Families', detail: '13 family judges synthesise their pillars' },
    { title: 'Committee', detail: '5 members vote; objections trigger investigations; repeat until unanimous' },
    { title: 'Write', detail: 'final weekly plan' },
  ],
}

const A = args || {}
const WEEK = A.week, ROOT = A.root, WINDOW = A.window
const MAX_AGENTS = A.maxAgents || 450, MAX_PILLAR_ROUNDS = A.maxPillarRounds || 3
const MAX_NEWS_ROUNDS = A.maxNewsRounds || 4, MAX_COMMITTEE_ROUNDS = A.maxCommitteeRounds || 4
const RUN = `${ROOT}/runs/${WEEK}`
let spawned = 0; const dropped = []
async function spawn(prompt, opts) {
  if (spawned >= MAX_AGENTS) { dropped.push(opts.label); log(`agent cap ${MAX_AGENTS} reached, skipped ${opts.label}`); return null }
  spawned++; return agent(prompt, opts)
}

const BUCKETS = ['global_equity','us_large_broad','us_small_mid_value','us_factor_dividend','tech_ai_semis','financials','healthcare_biotech','energy_oil','materials_mining_metals','industrials_defense_infra','consumer','utilities_realestate','clean_energy_thematic','developed_ex_us','europe','japan','asia_dev_other','em_broad','china','india','latam','mena_gulf','em_asia_other','govt_bonds','credit_bonds','gold_precious','commodities_broad','multi_asset_alt']
const FAMS = { ELG: 'Eligibility and data integrity', CST: 'Cost on the London line', TAX: 'Tax drag', DUR: 'Fund durability', EXR: 'Long-horizon expected return', FAC: 'Rewarded factors', RSK: 'Holdability and crash risk', CON: 'Concentration hazards', FIT: 'Fit with your mix', MOM: 'Trend, record only', REC: 'Live record and rule testing', MAC: 'Macro context', EVT: 'News and structural events' }
const PILLARS = A.pillars || []
if (!PILLARS.length) log('no pillar ids passed in args.pillars; pillar phase skipped')

const Q = { type: 'object', properties: { question: { type: 'string' }, why: { type: 'string' }, method: { type: 'string', enum: ['data', 'web', 'both'] } }, required: ['question', 'why', 'method'] }
const BSIG = { type: 'object', properties: { bucket: { type: 'string', enum: BUCKETS }, score: { type: 'integer', minimum: -2, maximum: 2 }, reason: { type: 'string' } }, required: ['bucket', 'score', 'reason'] }
const SCAN = { type: 'object', properties: {
  summary: { type: 'string' }, signal_by_bucket: { type: 'array', items: BSIG },
  notable: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, value: { type: 'string' }, why: { type: 'string' } }, required: ['ticker', 'why'] } },
  questions: { type: 'array', items: Q, maxItems: 4 }, confidence: { type: 'string', enum: ['low', 'medium', 'high'] } },
  required: ['summary', 'signal_by_bucket', 'notable', 'questions', 'confidence'] }
const INV = { type: 'object', properties: { question: { type: 'string' }, answer: { type: 'string' },
  evidence: { type: 'array', items: { type: 'object', properties: { source: { type: 'string' }, ref: { type: 'string' }, detail: { type: 'string' } }, required: ['source', 'detail'] } },
  new_threads: { type: 'array', items: { type: 'string' } }, implication: { type: 'string' } }, required: ['question', 'answer', 'evidence', 'new_threads', 'implication'] }
const SAT = { type: 'object', properties: { saturated: { type: 'boolean' }, rationale: { type: 'string' }, next_questions: { type: 'array', items: Q, maxItems: 4 },
  updated_summary: { type: 'string' }, signal_by_bucket: { type: 'array', items: BSIG } }, required: ['saturated', 'rationale', 'next_questions', 'updated_summary', 'signal_by_bucket'] }
const TOPIC = { type: 'object', properties: { topic: { type: 'string' }, why: { type: 'string' }, buckets: { type: 'array', items: { type: 'string', enum: BUCKETS } }, search_hints: { type: 'string' } }, required: ['topic', 'why', 'buckets'] }
const NPLAN = { type: 'object', properties: { rationale: { type: 'string' }, topics: { type: 'array', items: TOPIC, minItems: 1, maxItems: 15 } }, required: ['rationale', 'topics'] }
const NFIND = { type: 'object', properties: { topic: { type: 'string' },
  facts: { type: 'array', items: { type: 'object', properties: { date: { type: 'string' }, claim: { type: 'string' }, source: { type: 'string' }, url: { type: 'string' } }, required: ['date', 'claim', 'source', 'url'] } },
  bucket_effects: { type: 'array', items: BSIG }, new_threads: { type: 'array', items: TOPIC }, correlations: { type: 'array', items: { type: 'string' } } },
  required: ['topic', 'facts', 'bucket_effects', 'new_threads', 'correlations'] }
const NSYN = { type: 'object', properties: { saturated: { type: 'boolean' }, rationale: { type: 'string' }, correlations: { type: 'array', items: { type: 'string' } },
  coverage_gaps: { type: 'array', items: { type: 'string' } }, next_topics: { type: 'array', items: TOPIC, maxItems: 10 } }, required: ['saturated', 'rationale', 'correlations', 'coverage_gaps', 'next_topics'] }
const FAMV = { type: 'object', properties: { family: { type: 'string' }, verdict: { type: 'string' }, bucket_views: { type: 'array', items: BSIG },
  core_view: { type: 'string' }, deposit_view: { type: 'string' }, sell_view: { type: 'string' }, watch: { type: 'array', items: { type: 'string' } },
  key_evidence: { type: 'array', items: { type: 'string' } } }, required: ['family', 'verdict', 'bucket_views', 'core_view', 'deposit_view', 'sell_view', 'watch', 'key_evidence'] }
const PLAN = { type: 'object', properties: {
  core_action: { type: 'string', enum: ['FOLLOW_MIX', 'REVIEW_LINE_SWITCH'] }, core_reason: { type: 'string' },
  deposit: { type: 'array', items: { type: 'object', properties: { ucits: { type: 'string' }, units: { type: 'number' }, usd: { type: 'number' }, reason: { type: 'string' } }, required: ['ucits', 'units', 'usd', 'reason'] } },
  sells: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, reason: { type: 'string' } }, required: ['ticker', 'reason'] } },
  watchlist: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, reason: { type: 'string' }, trigger: { type: 'string' } }, required: ['item', 'reason', 'trigger'] } },
  risks: { type: 'array', items: { type: 'string' } }, rule_citations: { type: 'array', items: { type: 'string' } }, changes_from_last_round: { type: 'string' } },
  required: ['core_action', 'core_reason', 'deposit', 'sells', 'watchlist', 'risks', 'rule_citations', 'changes_from_last_round'] }
const VOTE = { type: 'object', properties: { approve: { type: 'boolean' }, comment: { type: 'string' },
  objections: { type: 'array', items: { type: 'object', properties: { point: { type: 'string' }, evidence_needed: { type: 'string' } }, required: ['point', 'evidence_needed'] } } },
  required: ['approve', 'comment', 'objections'] }

const DATA_HOW = `Data access: UCITS line prices in USD are pickled in ${ROOT}/cache (v2_close_usd.pkl dividend-adjusted, v2_rawclose_usd.pkl traded prices, v2_usdvol.pkl, v2_universe.pkl, v2_facts.json, v2_french.pkl, fred_*.csv). Engine: python3 -I with sys.path.insert(0, "${ROOT}/v2"); import engine_v2 as E; R = E.run(). This week's outputs: ${RUN}/v2_line_values.csv, v2_line_scores.csv, v2_exposure.csv, v2_fit.csv, v2_plan.json, REPORT_V2.md. Pillar definitions: ${ROOT}/config/pillars_v2.json. Do not modify any file.`

// ---------- Pillars: scan, then self-expanding investigation rounds ----------
async function runPillar(pid) {
  const fam = pid.slice(0, 3)
  const scan = await spawn(`You are the ${pid} pillar agent for the weekly review of 321 UCITS lines (week ${WEEK}). Read your data pack ${RUN}/packs_v2/${pid}.md (and only what you need beyond it). Interpret this pillar for the week: what stands out, which buckets it favours or penalises (score -2..+2, most should be 0 or +/-1), and which readings are surprising enough to need investigation. Ask questions only when an answer could change a weekly decision or a bucket view; ask none if the pillar is unremarkable this week. Owner context: Canadian living in the UAE, deposits 2,500 AED (about US$679) monthly through IBKR into the LSE UCITS lines of their strategic mix in ${ROOT}/config/portfolio_v2.yaml; rules in ${ROOT}/DECISION_RULES_V2.md. ${DATA_HOW}`,
    { label: `scan:${pid}`, phase: 'Pillars', schema: SCAN, effort: 'low' })
  if (!scan) return null
  const rounds = []; let state = { summary: scan.summary, signal_by_bucket: scan.signal_by_bucket, questions: scan.questions }
  const asked = new Set()
  for (let r = 1; r <= MAX_PILLAR_ROUNDS && state.questions.length; r++) {
    const qs = state.questions.filter(q => !asked.has(q.question.toLowerCase())); qs.forEach(q => asked.add(q.question.toLowerCase()))
    if (!qs.length) break
    log(`${pid} round ${r}: ${qs.length} investigator(s)`)
    const inv = (await parallel(qs.map((q, k) => () => spawn(`Investigator for pillar ${pid} (${FAMS[fam]}), week ${WEEK}, round ${r}. Question: ${q.question}\nWhy it matters: ${q.why}\nMethod: ${q.method === 'data' ? 'answer from the data' : q.method === 'web' ? 'answer with web search, news published ' + WINDOW + ' preferred' : 'use both the data and web search'}. Cite every source (URL or file plus the computation). Report new threads only if they could change a weekly decision. ${DATA_HOW}`,
      { label: `inv:${pid}:r${r}:${k + 1}`, phase: 'Pillars', schema: INV })))).filter(Boolean)
    rounds.push({ round: r, investigations: inv })
    const sat = await spawn(`You are the ${pid} pillar agent again (week ${WEEK}). Your scan said: ${state.summary}\nInvestigations this round:\n${JSON.stringify(inv)}\nDecide whether the pillar is saturated (no open thread that could change a decision) or needs another round. Update your summary and bucket signals with what was learned. Already asked: ${[...asked].join(' | ')}.`,
      { label: `sat:${pid}:r${r}`, phase: 'Pillars', schema: SAT, effort: 'low' })
    if (!sat) break
    state = { summary: sat.updated_summary, signal_by_bucket: sat.signal_by_bucket, questions: sat.saturated ? [] : sat.next_questions }
  }
  return { pid, family: fam, confidence: scan.confidence, notable: scan.notable, summary: state.summary, signal_by_bucket: state.signal_by_bucket, rounds: rounds.length, investigations: rounds.flatMap(x => x.investigations) }
}

// ---------- News: planner decides topics and agent count; rounds expand until saturated ----------
async function runNews() {
  const plan = await spawn(`You are the news planner for the weekly review of 321 UCITS lines, week ${WEEK} (news window ${WINDOW}). Read ${RUN}/REPORT_V2.md (this week's plan, your sleeves against the world, macro context) and any previous single-pass digests in ${RUN}/news_round0/*.md. The owner holds the strategic mix in ${ROOT}/config/portfolio_v2.yaml; fund-level events on its lines (VWRA, FWRA, ACWD, the S&P 500 and Nasdaq-100 UCITS lines) matter most. Decide what news needs exploring this week and how many explorer agents to send (one per topic, between 5 and 15). Prefer topics that explain big price moves, that touch the owner's lines and sleeves or the equity groups in the exposure view, and that the single pass covered thinly. Each topic should be specific (a company, policy, data release, country, commodity or event), not a whole region.`,
    { label: 'news:plan', phase: 'News', schema: NPLAN })
  if (!plan) return { rounds: [], findings: [], synth: [] }
  let topics = plan.topics.slice(0, A.maxTopics || 15); const seen = new Set(); const findings = []; const synth = []
  for (let r = 1; r <= MAX_NEWS_ROUNDS && topics.length; r++) {
    const fresh = topics.filter(t => !seen.has(t.topic.toLowerCase())); fresh.forEach(t => seen.add(t.topic.toLowerCase()))
    if (!fresh.length) break
    log(`news round ${r}: ${fresh.length} explorer(s)`)
    const got = (await parallel(fresh.map((t, k) => () => spawn(`News explorer, week ${WEEK}, round ${r}. Topic: ${t.topic}\nWhy: ${t.why}\nBuckets: ${t.buckets.join(', ')}\nHints: ${t.search_hints || ''}\nUse web search. Prefer news published ${WINDOW}; earlier background only to explain it. Every fact needs date, source and URL; no URL, no fact. Score each affected bucket -2..+2 for the next 1-3 months (most 0 or +/-1; +/-2 only for a concrete, material, sourced development). Report new threads you could not cover and any correlations you notice with other topics or with price moves.`,
      { label: `news:r${r}:${k + 1}`, phase: 'News', schema: NFIND })))).filter(Boolean)
    findings.push(...got.map(g => ({ ...g, round: r })))
    const s = await spawn(`You are the news synthesiser, week ${WEEK}, after round ${r}. Topics covered so far: ${[...seen].join(' | ')}.\nAll findings so far:\n${JSON.stringify(findings.map(f => ({ topic: f.topic, round: f.round, facts: f.facts.slice(0, 6), bucket_effects: f.bucket_effects, new_threads: f.new_threads, correlations: f.correlations })))}\nGoal: the news picture is complete enough that no uncovered thread could change the owner's weekly decisions or a bucket view. Identify correlations across topics, coverage gaps, and the next topics (new, specific, not already covered). Say saturated=true when further rounds would only repeat what is known.`,
      { label: `news:synth:r${r}`, phase: 'News', schema: NSYN })
    if (!s) break
    synth.push({ round: r, ...s }); topics = s.saturated ? [] : s.next_topics.slice(0, A.maxTopics || 10)
  }
  return { plan, findings, synth, rounds: synth.length }
}

phase('Pillars')
const [pillarResults, news] = await parallel([
  () => parallel(PILLARS.map(pid => () => runPillar(pid))),
  () => runNews(),
])
const pillars = (pillarResults || []).filter(Boolean)
log(`pillars done: ${pillars.length}/90, investigation rounds total ${pillars.reduce((a, p) => a + p.rounds, 0)}; news rounds ${news ? news.rounds : 0}, explorers ${news ? news.findings.length : 0}`)

// ---------- Score: 10 news-pillar scorers write J files, then the engine re-scores ----------
phase('Score')
const EVTDEF = [
  ['EVT01', 'Fund corporate actions: closures, mergers, liquidations, suspensions, delistings, share-class changes on the lines in the owner mix and their same-index substitutes'],
  ['EVT02', 'Fees, structure and KID: TER changes, replication or lending changes, distribution policy, domicile, new cheaper LSE USD lines on the same index'],
  ['EVT03', 'Thesis log for any sleeve the owner holds beyond the world sleeve: what has changed in the case for holding S&P 500 and Nasdaq-100 (record only)'],
  ['EVT04', 'Index methodology, reclassification and mega-cap events: FTSE All-World, S&P 500 and Nasdaq-100 rule changes, rebalances, special rebalances, concentration'],
  ['EVT05', 'Issuer, custodian and counterparty health: Vanguard, iShares/BlackRock, Invesco, Xtrackers, SPDR, their custodians and swap counterparties'],
  ['EVT06', 'Tax and legal regime for the owner: UAE, Canada non-resident rules, US withholding and section 871(m), Irish fund rules'],
  ['EVT07', 'Sanctions, capital controls and market access affecting fund holdings or the owner\'s ability to transact'],
  ['EVT08', 'Broker, venue and funding channel: IBKR (entity, fees, outages), the LSE, AED to USD conversion, UAE bank transfers'],
  ['EVT09', 'Deposit-week calendar and market dislocations: holidays, central bank meetings, CPI, major earnings in the coming deposit window'],
  ['EVT10', 'Capital market assumption and valuation data harvest: new 10-year return forecasts and CAPE figures, with sources (record)'],
]
const newsDigest = JSON.stringify((news.findings || []).map(f => ({ topic: f.topic, facts: f.facts, bucket_effects: f.bucket_effects, correlations: f.correlations })))
await parallel(EVTDEF.map(([id, scope]) => () => spawn(`You are event agent ${id}, week ${WEEK}. Scope: ${scope}. Use the explorer findings below first, then web search for anything specific to your scope that they do not cover (news published ${WINDOW} preferred). Write JSON to ${RUN}/events/${id}.json (create the folder) with exactly this shape: {"pillar_id": "${id}", "week": "${WEEK}", "summary": "3-6 sentences", "events": [{"target": "LSE ticker such as VWRA.L, or a sleeve name: world, sp500, ndx100", "severity": 0, "issue": "...", "url": "...", "date": "YYYY-MM-DD"}]}. Severity: 0 information, 1 watch (penalises the line score), 2 adverse confirmed change (blocks buying the line), 3 severe (sanctions or market access: blocks buying). Every event needs a primary or top-tier source URL; unconfirmed reports are severity 0 or 1. An empty events list is a valid answer. Also write a digest under 300 words to ${RUN}/events/${id}.md. Reply with the events list.\n\nExplorer findings:\n${newsDigest}`,
  { label: `event:${id}`, phase: 'Score' })))
const engine = await spawn(`Run these commands from ${ROOT} and report results: (1) python3 -I -c "import json,glob; [json.load(open(p)) for p in glob.glob('${RUN}/events/EVT*.json')]; print('events ok')" (2) python3 -I v2/run_v2.py --week ${WEEK} (3) python3 -I v2/packs_v2.py --week ${WEEK}. If step 1 fails, fix only the malformed JSON syntax in the failing file and retry. Then reply with the sections "This month's deposit", "Sell anything?" and "Portfolio limits and context" from ${RUN}/REPORT_V2.md, verbatim.`,
  { label: 'engine', phase: 'Score' })

// ---------- Families: 10 judges ----------
phase('Families')
const famInputs = Object.keys(FAMS).map(f => f === 'EVT'
  ? { f, body: JSON.stringify({ news_rounds: news.rounds, plan: news.plan && news.plan.rationale, synth: news.synth, findings: (news.findings || []).map(x => ({ topic: x.topic, facts: x.facts.slice(0, 5), bucket_effects: x.bucket_effects })) }) }
  : { f, body: JSON.stringify(pillars.filter(p => p.family === f)) }).filter(x => x.f === 'EVT' || pillars.some(p => p.family === x.f))
const families = (await parallel(famInputs.map(({ f, body }) => () => spawn(`You are the family judge for ${f}. ${FAMS[f]}, week ${WEEK}. Below are the outputs of its pillar agents and their investigations. Synthesise: overall verdict, bucket views (-2..+2), and what this family implies for the owner's decisions (where this month's 2,500 AED goes within the strategic mix, which line in each sleeve, whether to sell anything, what to watch). Respect ${ROOT}/DECISION_RULES_V2.md: scores are display-only unless the REC04 gate in ${ROOT}/runs/v2_backtests_latest.json has passed. Engine output this week:\n${engine}\n\nPillar outputs:\n${body}`,
  { label: `family:${f}`, phase: 'Families', schema: FAMV })))).filter(Boolean)

// ---------- Committee: chair drafts, 5 members vote, objections investigated, repeat until unanimous ----------
phase('Committee')
const MEMBERS = [
  ['rules', 'Evidence and rules keeper: enforce DECISION_RULES_V2.md and the REC04 gate; no action without a rule or a structural event'],
  ['risk', 'Risk manager: drawdown, concentration, liquidity and behavioural risk for a monthly depositor'],
  ['macro', 'Macro and news strategist: what the news and macro families imply over 1-3 months, and whether any of it is structural'],
  ['quant', 'Quant: what trend, relative strength, volatility and risk-adjusted pillars say, and whether any signal is strong enough to matter'],
  ['uae', 'UAE execution and tax: line choice and gates, whole shares and residue, withholding and swap tax-rule risk, IBKR costs, residency rules in plan v5'],
]
const CONTEXT = `Owner: Canadian citizen resident in the UAE (plan v5 Branch A), IBKR, deposits 2,500 AED (about US$679) monthly into the strategic mix in ${ROOT}/config/portfolio_v2.yaml, which is also the yardstick. Rules: ${ROOT}/DECISION_RULES_V2.md. Backtests (REC07 mix comparison, REC04 gate): ${ROOT}/runs/v2_backtests_latest.json. Report and plan: ${RUN}/REPORT_V2.md, ${RUN}/v2_plan.json.\n\nEngine decisions:\n${engine}\n\nFamily verdicts:\n${JSON.stringify(families)}`
let plan = null, votes = [], history = [], extra = []
for (let r = 1; r <= MAX_COMMITTEE_ROUNDS; r++) {
  plan = await spawn(`You are the committee chair, week ${WEEK}, round ${r}. Draft the week's plan for the owner: this month's order(s) within the strategic mix (start from v2_plan.json), any line switch, any sell, and the watchlist. Cite the rule or evidence behind every action; a sell or line switch needs a structural event under rule S1 or S2 of DECISION_RULES_V2.md, and any tilt away from the mix needs a passed REC04 gate. ${r > 1 ? 'Revise the previous plan to resolve the objections using the new evidence; keep what nobody objected to.' : ''}\n\n${CONTEXT}\n\n${r > 1 ? 'Previous plan: ' + JSON.stringify(history[history.length - 1].plan) + '\nObjections: ' + JSON.stringify(history[history.length - 1].votes) + '\nNew evidence: ' + JSON.stringify(extra) : ''}`,
    { label: `chair:r${r}`, phase: 'Committee', schema: PLAN })
  if (!plan) break
  votes = (await parallel(MEMBERS.map(([k, lens]) => () => spawn(`You are committee member "${k}". Lens: ${lens}. Week ${WEEK}, round ${r}. Vote on the plan below. Approve only if you would sign it as written; otherwise list each objection with the evidence that would resolve it. Do not object on matters of style.\n\nPlan:\n${JSON.stringify(plan)}\n\n${CONTEXT}`,
    { label: `vote:${k}:r${r}`, phase: 'Committee', schema: VOTE })))).filter(Boolean).map((v, i) => ({ member: MEMBERS[i][0], ...v }))
  history.push({ round: r, plan, votes })
  const objections = votes.filter(v => !v.approve).flatMap(v => v.objections.map(o => ({ member: v.member, ...o })))
  log(`committee round ${r}: ${votes.filter(v => v.approve).length}/${votes.length} approve`)
  if (!objections.length && votes.length === MEMBERS.length) break
  extra = (await parallel(objections.slice(0, 6).map((o, k) => () => spawn(`Committee investigator, week ${WEEK}, round ${r}. Member "${o.member}" objected: ${o.point}\nEvidence needed: ${o.evidence_needed}\nFind that evidence from the data, the report, the rules, the backtest or the web, and state plainly whether it supports the objection. ${DATA_HOW}`,
    { label: `cinv:r${r}:${k + 1}`, phase: 'Committee', schema: INV })))).filter(Boolean)
  if (objections.length > 6) log(`only 6 of ${objections.length} objections investigated this round`)
}
const unanimous = votes.length === MEMBERS.length && votes.every(v => v.approve)

// ---------- Write ----------
phase('Write')
const written = await spawn(`Write the final weekly plan to ${RUN}/WEEKLY_PLAN_V2.md for the owner, in plain language, no em-dashes. Structure: (1) a decisions table: this month's order(s) with line, units and cost, any line switch, sell anything, what to watch with triggers; (2) whether the committee was unanimous (${unanimous ? 'yes' : 'no'}) after ${history.length} round(s), and any dissent with reasons; (3) why: the evidence from the families and the rules, with the backtest result in one line; (4) the five most important news facts with links; (5) the structural events found by EVT01-EVT10 with severities; (6) what the agents did: ${pillars.length} pillar agents, ${pillars.reduce((a, p) => a + p.rounds, 0)} pillar investigation rounds, ${news.rounds} news rounds with ${(news.findings || []).length} explorers, ${families.length} family judges, ${history.length} committee rounds, ${spawned} agents in total${dropped.length ? ', ' + dropped.length + ' skipped by the agent cap' : ''}. If not unanimous, the default under DECISION_RULES_V2.md applies (the engine's v2_plan.json order, no sells) and you must say so. Keep it under 900 words. Final plan: ${JSON.stringify(plan)}\nVotes by round: ${JSON.stringify(history.map(h => ({ round: h.round, votes: h.votes })))}\nFamily verdicts: ${JSON.stringify(families.map(f => ({ family: f.family, verdict: f.verdict })))}\nNews correlations: ${JSON.stringify((news.synth || []).flatMap(s => s.correlations))}\nTop news facts: ${JSON.stringify((news.findings || []).flatMap(f => f.facts.slice(0, 2)).slice(0, 25))}. Reply with "written".`,
  { label: 'writer', phase: 'Write' })

return { week: WEEK, unanimous, committee_rounds: history.length, final_plan: plan, final_votes: votes,
  agents: spawned, dropped, pillar_rounds: pillars.reduce((a, p) => a + p.rounds, 0), pillars_done: pillars.length,
  news_rounds: news.rounds, news_explorers: (news.findings || []).length, news_saturation: (news.synth || []).map(s => ({ round: s.round, saturated: s.saturated, rationale: s.rationale })),
  families: families.map(f => ({ family: f.family, verdict: f.verdict })), written }
