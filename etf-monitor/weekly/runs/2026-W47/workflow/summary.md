# Workflow run record, 2026-W47

Agents started: 303; finished: 303; tokens: 28108962

| phase | agents |
|---|---|
| Committee | 6 |
| Engine | 1 |
| Families | 10 |
| News | 260 |
| Synthesis | 1 |
| Verify | 24 |
| Write | 1 |

Committee: unanimous after 1 round(s)
Stats: {"news_pillars": 24, "news_rounds": 48, "news_explorers": 227, "news_agents": 260, "verify_agents": 24, "other_agents": 18, "committee_rounds": 1, "unanimous": true, "skipped": 39}

Not finished: none
Errors: none

Read: `zcat agents.jsonl.gz | jq 'select(.phase=="News") | {label, result}'`
