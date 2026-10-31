# Query syntax per engine

| Engine | Boolean syntax | Phrase | Field restriction | Notes |
|---|---|---|---|---|
| semantic_scholar (bulk) | `+` AND, `\|` OR, `-` NOT, `( )` grouping | `"..."` | none (title+abstract) | Bulk endpoint is not relevance-ranked; if hits > limit the record set is arbitrary — narrow the query. Supports `--year 2015-2026`. |
| openalex | `AND`, `OR`, `NOT` (uppercase), `( )` | `"..."` | search covers title, abstract, fulltext | Free key required. Relevance-ranked. |
| arxiv | `AND`, `OR`, `ANDNOT`, `( )` | `"..."` (URL-encoded automatically) | `ti:`, `abs:`, `au:`, `cat:`, `all:` | 1 request / 3 s. Example: `abs:"overreliance" AND (cat:cs.HC OR cat:cs.AI)` |
| dblp | space = AND, `\|` OR | none | title words only | Good for CS venues coverage; no abstracts. |
| crossref | free text in `query.bibliographic` (no boolean) | — | — | Use for metadata validation and journals outside CS. |
| acl | same as semantic_scholar, restricted to ACL-family venues | | | Implemented via S2 venue filter (ACL, EMNLP, NAACL, EACL, COLING, TACL, CL, Findings, CoNLL, AACL, LREC). |
| github | GitHub search qualifiers: `topic:`, `language:`, `stars:>50`, `in:readme` | `"..."` | | Finds code artifacts, not papers; only for tool/benchmark work. |

## Writing a query set
1. One concept block per RQ concept, synonyms ORed inside the block, blocks ANDed.
2. Translate the same logical query into each engine's syntax; record the translation, not just the intent.
3. Test the broadest query on one engine first; if hits > 2,000, add a concept block or restrict fields before fanning out.
4. Year range in the plan, not inside query strings.
