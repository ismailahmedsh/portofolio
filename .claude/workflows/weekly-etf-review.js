export const meta = {
  name: 'weekly-etf-review',
  description: 'Adaptive weekly ETF review: 90 pillar agents with self-expanding investigations, expanding news rounds, family judges, committee until unanimous',
  whenToUse: 'Every Saturday after etf-monitor/weekly fetch, run_weekly and packs have run for the week',
  phases: [
    { title: 'Pillars', detail: '90 pillar agents; each decides whether to open investigation rounds' },
    { title: 'News', detail: 'planner picks topics and agent count; rounds expand until saturated' },
    { title: 'Score', detail: '10 news-pillar scorers write J01-J10, engine re-scores 200 ETFs' },
    { title: 'Families', detail: '10 family judges synthesise their pillars' },
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
const FAMS = { A: 'Trend and momentum', B: 'Relative strength', C: 'Volatility', D: 'Drawdown and tail risk', E: 'Risk-adjusted return', F: 'Liquidity and trading', G: 'Cost, structure and UAE investability', H: 'Macro regime', I: 'Valuation and holdings', J: 'News and events' }
const PILLARS = []
for (const f of 'ABCDEFGHI') for (let i = 1; i <= 10; i++) PILLARS.push(`${f}${String(i).padStart(2, '0')}`)

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
  core_action: { type: 'string', enum: ['HOLD', 'REVIEW_SWITCH'] }, core_reason: { type: 'string' },
  deposit: { type: 'array', items: { type: 'object', properties: { ucits: { type: 'string' }, usd: { type: 'number' }, reason: { type: 'string' } }, required: ['ucits', 'usd', 'reason'] } },
  sells: { type: 'array', items: { type: 'object', properties: { ticker: { type: 'string' }, reason: { type: 'string' } }, required: ['ticker', 'reason'] } },
  watchlist: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, reason: { type: 'string' }, trigger: { type: 'string' } }, required: ['item', 'reason', 'trigger'] } },
  risks: { type: 'array', items: { type: 'string' } }, rule_citations: { type: 'array', items: { type: 'string' } }, changes_from_last_round: { type: 'string' } },
  required: ['core_action', 'core_reason', 'deposit', 'sells', 'watchlist', 'risks', 'rule_citations', 'changes_from_last_round'] }
const VOTE = { type: 'object', properties: { approve: { type: 'boolean' }, comment: { type: 'string' },
  objections: { type: 'array', items: { type: 'object', properties: { point: { type: 'string' }, evidence_needed: { type: 'string' } }, required: ['point', 'evidence_needed'] } } },
  required: ['approve', 'comment', 'objections'] }

const DATA_HOW = `Data access: price and fund data are pickled in ${ROOT}/cache (adj.pkl, close.pkl, high.pkl, low.pkl, vol.pkl, facts.json, fred_*.csv). Read them with python3 -I and sys.path.insert(0, "${ROOT}/src"); import pillars as P; d = P.load(). This week's values: ${RUN}/pillar_values.csv, scores: ${RUN}/pillar_scores.csv, families: ${RUN}/family_scores.csv. Do not modify any file.`

// ---------- Pillars: scan, then self-expanding investigation rounds ----------
async function runPillar(pid) {
  const fam = pid[0]
  const scan = await spawn(`You are the ${pid} pillar agent for the weekly review of 200 ETFs (week ${WEEK}). Read your data pack ${RUN}/packs/${pid}.md (and only what you need beyond it). Interpret this pillar for the week: what stands out, which buckets it favours or penalises (score -2..+2, most should be 0 or +/-1), and which readings are surprising enough to need investigation. Ask questions only when an answer could change a weekly decision or a bucket view; ask none if the pillar is unremarkable this week. Owner context: Canadian living in the UAE, deposits US$2,500 monthly into VWRA (proxy VT), buys UCITS funds on the LSE. ${DATA_HOW}`,
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
  const plan = await spawn(`You are the news planner for the weekly review of 200 ETFs, week ${WEEK} (news window ${WINDOW}). Read ${RUN}/packs/MOVERS.md (this week's biggest price moves and macro readings) and the previous single-pass news digests in ${RUN}/news_round0/*.md. Decide what news needs exploring this week and how many explorer agents to send (one per topic, between 5 and 15). Prefer topics that explain big price moves, that touch the owner's core (VWRA, a global all-cap fund) or the 28 buckets, and that the single pass covered thinly. Each topic should be specific (a company, policy, data release, country, commodity or event), not a whole region.`,
    { label: 'news:plan', phase: 'News', schema: NPLAN })
  if (!plan) return { rounds: [], findings: [], synth: [] }
  let topics = plan.topics; const seen = new Set(); const findings = []; const synth = []
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
    synth.push({ round: r, ...s }); topics = s.saturated ? [] : s.next_topics
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
const JDEF = [
  ['J01', 'Global macro and central banks', 'govt_bonds, credit_bonds, global_equity, us_large_broad, multi_asset_alt, gold_precious'],
  ['J02', 'US equities and earnings', 'us_large_broad, us_small_mid_value, us_factor_dividend, consumer, financials'],
  ['J03', 'Tech, AI and semiconductors', 'tech_ai_semis, us_large_broad'],
  ['J04', 'Sectors: health, industrials, utilities, clean energy', 'healthcare_biotech, industrials_defense_infra, utilities_realestate, clean_energy_thematic'],
  ['J05', 'Europe and developed ex-US', 'europe, developed_ex_us, asia_dev_other'],
  ['J06', 'Japan and China', 'japan, china'],
  ['J07', 'Emerging markets ex-China', 'india, em_asia_other, latam, em_broad'],
  ['J08', 'Middle East, Gulf and geopolitics', 'mena_gulf, global_equity, energy_oil'],
  ['J09', 'Commodities', 'energy_oil, materials_mining_metals, gold_precious, commodities_broad'],
  ['J10', 'ETF flows and fund events', 'any bucket with reported flow data; red flags for specific funds'],
]
const newsDigest = JSON.stringify((news.findings || []).map(f => ({ topic: f.topic, facts: f.facts, bucket_effects: f.bucket_effects, correlations: f.correlations })))
await parallel(JDEF.map(([id, name, buckets]) => () => spawn(`You are news-pillar scorer ${id} (${name}), week ${WEEK}. Read the brief ${ROOT}/config/news_agent_brief.md for the JSON format and scoring scale. Do not search the web: score only from the explorer findings below plus the single-pass file ${RUN}/news_round0/${id}.json. Score these buckets: ${buckets}. Keep every headline that supports a score (date, source, URL). Include red_flags and upcoming_events. Write the JSON to ${RUN}/news/${id}.json (overwrite) and a digest under 400 words to ${RUN}/news/${id}.md. Then reply with one line per bucket: bucket, score, confidence.\n\nExplorer findings:\n${newsDigest}\n\nCross-topic correlations found: ${JSON.stringify((news.synth || []).flatMap(s => s.correlations))}`,
  { label: `score:${id}`, phase: 'Score' })))
const engine = await spawn(`Run these commands from ${ROOT} and report results: (1) python3 -I -c "import json,glob; [json.load(open(p)) for p in glob.glob('${RUN}/news/J*.json')]; print('news ok')" (2) python3 -I src/run_weekly.py --week ${WEEK} (3) python3 -I src/packs.py --week ${WEEK}. If step 1 fails, fix only the malformed JSON syntax in the failing file and retry. Then reply with the full "This week's decisions" table and the "Your core today" section from ${RUN}/REPORT.md, verbatim.`,
  { label: 'engine', phase: 'Score' })

// ---------- Families: 10 judges ----------
phase('Families')
const famInputs = Object.keys(FAMS).map(f => f === 'J'
  ? { f, body: JSON.stringify({ news_rounds: news.rounds, plan: news.plan && news.plan.rationale, synth: news.synth, findings: (news.findings || []).map(x => ({ topic: x.topic, facts: x.facts.slice(0, 5), bucket_effects: x.bucket_effects })) }) }
  : { f, body: JSON.stringify(pillars.filter(p => p.family === f)) })
const families = (await parallel(famInputs.map(({ f, body }) => () => spawn(`You are the family judge for ${f}. ${FAMS[f]}, week ${WEEK}. Below are the outputs of its pillar agents and their investigations. Synthesise: overall verdict, bucket views (-2..+2), and what this family implies for the owner's four weekly decisions (hold or review the core VWRA, where the US$2,500 deposit goes, whether to sell anything, what to watch). Respect ${ROOT}/DECISION_RULES.md: price signals are flags unless a rule passes the backtest gate in ${ROOT}/runs/backtest_latest.json. Engine output this week:\n${engine}\n\nPillar outputs:\n${body}`,
  { label: `family:${f}`, phase: 'Families', schema: FAMV })))).filter(Boolean)

// ---------- Committee: chair drafts, 5 members vote, objections investigated, repeat until unanimous ----------
phase('Committee')
const MEMBERS = [
  ['rules', 'Evidence and rules keeper: enforce DECISION_RULES.md and the backtest gate; no action without a rule or a structural flag'],
  ['risk', 'Risk manager: drawdown, concentration, liquidity and behavioural risk for a monthly depositor'],
  ['macro', 'Macro and news strategist: what the news and macro families imply over 1-3 months, and whether any of it is structural'],
  ['quant', 'Quant: what trend, relative strength, volatility and risk-adjusted pillars say, and whether any signal is strong enough to matter'],
  ['uae', 'UAE execution and tax: UCITS availability on the LSE, withholding, estate tax, IBKR costs, residency rules in plan v5'],
]
const CONTEXT = `Owner: Canadian citizen resident in the UAE (plan v5 Branch A), IBKR, deposits US$2,500 monthly into VWRA; satellite_share in ${ROOT}/config/portfolio.yaml is 0. Rules: ${ROOT}/DECISION_RULES.md. Backtest: ${ROOT}/runs/backtest_latest.json. Report: ${RUN}/REPORT.md.\n\nEngine decisions:\n${engine}\n\nFamily verdicts:\n${JSON.stringify(families)}`
let plan = null, votes = [], history = [], extra = []
for (let r = 1; r <= MAX_COMMITTEE_ROUNDS; r++) {
  plan = await spawn(`You are the committee chair, week ${WEEK}, round ${r}. Draft the week's plan for the owner. It must cite the rule or evidence behind every action; a sell or core switch needs a structural red flag or a passed backtest gate. ${r > 1 ? 'Revise the previous plan to resolve the objections using the new evidence; keep what nobody objected to.' : ''}\n\n${CONTEXT}\n\n${r > 1 ? 'Previous plan: ' + JSON.stringify(history[history.length - 1].plan) + '\nObjections: ' + JSON.stringify(history[history.length - 1].votes) + '\nNew evidence: ' + JSON.stringify(extra) : ''}`,
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
const written = await spawn(`Write the final weekly plan to ${RUN}/WEEKLY_PLAN.md for the owner, in plain language, no em-dashes. Structure: (1) a decisions table: keep or review the core, where this month's deposit goes, sell anything, what to watch with triggers; (2) whether the committee was unanimous (${unanimous ? 'yes' : 'no'}) after ${history.length} round(s), and any dissent with reasons; (3) why: the evidence from the families and the rules, with the backtest result in one line; (4) the five most important news facts with links; (5) the bucket views that changed the most; (6) what the agents did: ${pillars.length} pillar agents, ${pillars.reduce((a, p) => a + p.rounds, 0)} pillar investigation rounds, ${news.rounds} news rounds with ${(news.findings || []).length} explorers, ${families.length} family judges, ${history.length} committee rounds, ${spawned} agents in total${dropped.length ? ', ' + dropped.length + ' skipped by the agent cap' : ''}. If not unanimous, the default under DECISION_RULES.md applies and you must say so. Keep it under 900 words. Final plan: ${JSON.stringify(plan)}\nVotes by round: ${JSON.stringify(history.map(h => ({ round: h.round, votes: h.votes })))}\nFamily verdicts: ${JSON.stringify(families.map(f => ({ family: f.family, verdict: f.verdict })))}\nNews correlations: ${JSON.stringify((news.synth || []).flatMap(s => s.correlations))}\nTop news facts: ${JSON.stringify((news.findings || []).flatMap(f => f.facts.slice(0, 2)).slice(0, 25))}. Reply with "written".`,
  { label: 'writer', phase: 'Write' })

return { week: WEEK, unanimous, committee_rounds: history.length, final_plan: plan, final_votes: votes,
  agents: spawned, dropped, pillar_rounds: pillars.reduce((a, p) => a + p.rounds, 0), pillars_done: pillars.length,
  news_rounds: news.rounds, news_explorers: (news.findings || []).length, news_saturation: (news.synth || []).map(s => ({ round: s.round, saturated: s.saturated, rationale: s.rationale })),
  families: families.map(f => ({ family: f.family, verdict: f.verdict })), written }
