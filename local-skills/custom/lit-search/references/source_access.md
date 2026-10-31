# Source Access Table


Checked 2026-10-28. Rate limits change; every collector reads response headers and obeys them over these numbers.

| Source | Access method | Cost | Rate limit | Key | Fallback |
|---|---|---|---|---|---|
| Semantic Scholar | Academic Graph REST | free | keyless: shared pool, throttled under load; key: 1 req/s introductory | `S2_API_KEY` (recommended) | OpenAlex |
| OpenAlex | REST | free daily budget with key; usage-billed beyond | key mandatory since Feb 2026; daily budget metered per call type; ≤100 req/s; check `/rate-limit` | `OPENALEX_API_KEY` (required) | S2; CC0 snapshot on S3 for bulk |
| arXiv | Atom query API; OAI-PMH for bulk | free | 1 request per 3 s, single connection | none | S2/OpenAlex by arXiv ID |
| Crossref | REST, polite pool via `mailto` | free | polite: 10/s single DOI, 3/s list queries, concurrency 3 | `CROSSREF_MAILTO` | OpenAlex DOI filter (100 DOIs per call) |
| Crossref (retractions) | `update-to` / Retraction Watch data in REST | free | as above | as above | OpenAlex `is_retracted` |
| Unpaywall | REST | free | ~100k/day | `UNPAYWALL_EMAIL` | OpenAlex `best_oa_location` |
| DBLP | search API + XML dump | free | unpublished; self-throttle 1 req/s, obey 429 Retry-After | none | monthly XML dump |
| ACL Anthology | Semantic Scholar bulk search restricted to ACL-family venues (no ACL search API) | free | as Semantic Scholar | as Semantic Scholar | DBLP |
| GitHub | REST + search | free | 5,000/h with token; search 30/min | `GITHUB_TOKEN` | none needed |
| Google Scholar | **manual-assist**: skill writes queries, you run them and paste/export | free | n/a | none | S2 + OpenAlex |
| IEEE Xplore | metadata API if approved key; else Crossref metadata | free metadata, paywalled text | per key terms | `IEEE_API_KEY` (optional) | Crossref + OA copy; ask you for PDFs |
| ACM DL | no public API; metadata via Crossref (prefix 10.1145) | metadata free; check OA status per paper | via Crossref | none | OpenAlex OA location; ask you for PDFs |
| Hacker News | Algolia search API | free | ~10,000 req/h per IP | none | official Firebase API |
| Stack Exchange | API v2.3 | free | 10,000/day with key, 300 without; obey `backoff` field | `STACKEXCHANGE_KEY` | quarterly data dump (CC BY-SA) |
| Bluesky | AT Protocol public AppView | free | per-IP limits (~3,000 / 5 min) | optional app password | Jetstream |
| Mastodon | per-instance REST | free | instance-specific (default 300 / 5 min) | `MASTODON_ACCESS_TOKEN` | other instances; **respect `noindex` and instance research policies** |
| YouTube | Data API v3 | free quota | 10,000 units/day; `search.list` = 100 units | `YOUTUBE_API_KEY` | reduce scope |
| Reddit | official API **after approval only** | free if approved | ~100 QPM OAuth | `REDDIT_CLIENT_ID/SECRET` | **FLAGGED**: requires Reddit for Researchers approval recorded in state; else source excluded and limitation written |
| X | API v2 pay-per-use | ~$0.005 per post read, billed per resource returned; no free reads | 2M reads/month cap | `X_BEARER_TOKEN` + `X_MONTHLY_BUDGET_USD` | **FLAGGED**: refuses without a budget decision in state |

claude.ai fallback: the sandbox cannot reach these APIs. Every source module exposes `available()`; when false, the skill says "API unreachable in this runtime, using web search/fetch — counts and coverage are not reproducible" and tags the affected records `retrieval: web_fallback`.

