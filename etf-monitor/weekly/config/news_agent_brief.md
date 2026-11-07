# News pillar agent brief (family J, pillars J01-J10)

Run week: given in your prompt. Read news published from the Saturday before that ISO week through the Saturday after it, plus earlier background only where it explains the week. (First run: 2026-W45, window 2026-10-31 to 2026-11-07.)

Your job: research recent news for your pillar's scope with web search, then score each assigned bucket for the next 1 to 3 months on this scale:
- -2 strong headwind, -1 mild headwind, 0 neutral or mixed, +1 mild tailwind, +2 strong tailwind.
Score the news flow and fundamentals reported, not price moves alone. Be calibrated: most weeks most buckets are 0 or +/-1. A +/-2 needs a concrete, sourced, material development (policy decision, earnings shock, war, sanctions, default, regulatory change).

Rules:
- Every score needs at least 2 headlines with date, source name and URL, published inside the window. No URL, no score (use 0 with confidence "low").
- Prefer primary or top-tier sources (central banks, statistics agencies, Reuters, Bloomberg, FT, WSJ, CNBC, Nikkei, issuer press releases). Label opinion pieces as opinion.
- Separate facts from interpretation. Do not invent numbers.
- Note any fund-level red flag for a specific ETF (closure, merger, fee change, index change, suspension, large premium/discount, sanctions affecting holdings).

Output: write a JSON file at the path you are given, exactly this shape:
{
  "pillar_id": "J0x",
  "pillar_name": "...",
  "week": "<week>",
  "window": "<YYYY-MM-DD..YYYY-MM-DD>",
  "bucket_scores": {
    "<bucket>": {"score": 0, "confidence": "low|medium|high", "rationale": "2-4 sentences", "headlines": [{"date": "YYYY-MM-DD", "title": "...", "source": "...", "url": "..."}]}
  },
  "regime_notes": "3-6 sentences on what matters most this week for your scope",
  "red_flags": [{"target": "ticker or bucket", "issue": "...", "url": "..."}],
  "upcoming_events": [{"date": "YYYY-MM-DD", "event": "...", "buckets": ["..."]}]
}
Then write a short markdown digest (under 400 words) next to it with the same name and a .md extension.
Valid bucket names are in /home/user/portofolio/etf-monitor/weekly/config/buckets.txt; use only those.
