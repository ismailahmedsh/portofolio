# Workflow run record, 2026-W46

Agents started: 296; finished: 295; tokens: 27795048

| phase | agents |
|---|---|
| Committee | 23 |
| Engine | 1 |
| Families | 10 |
| News | 260 |
| Synthesis | 1 |
| Write | 1 |

Committee: unanimous after 3 round(s)
Stats: {"news_pillars": 0, "news_rounds": 0, "news_explorers": 0, "news_agents": 260, "other_agents": 35, "committee_rounds": 3, "unanimous": true, "skipped": 53}

Not finished: writer
Errors: writer: You've hit your 5-hour limit · resets 8pm (UTC)

Read: `zcat agents.jsonl.gz | jq 'select(.phase=="News") | {label, result}'`
