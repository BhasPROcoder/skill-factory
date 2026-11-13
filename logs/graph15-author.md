# GRF-015 candidate and author evidence

Candidate: graph-query-plan-equivalence. Own skill/manifest/log only; no registry changes or acceptance claim. User's latest instruction is local-only: no commit or push performed by this author.

## Comparison before authoring

Used sf.py metadata for TDQ-008 and GRF-014 (the latter was unregistered at lookup), and sf.py search for query. Read actual TDQ-008 input/procedure/rules and GRF-014 draft storage procedure. TDQ-008 diagnoses per-key join multiplication and chooses a data correction/aggregation based on row meaning. GRF-014 creates storage constraints, verifies transaction rollback and reopens stored data. Neither supplies a query/index experiment with independently enumerated graph edge sequences, exact before/after result multiplicities and observed plan evidence. G15's artifact is a correctness-preserving tuning proposal, not a renamed cardinality warning or schema implementation.

## Source and claim audit before saving

Consulted official [SQLite EXPLAIN QUERY PLAN documentation](https://www.sqlite.org/eqp.html) and [query-planning documentation](https://www.sqlite.org/queryplanner.html). Used these only to establish plan inspection and index experiments; source examples were not copied. The skill instructs readers to check current documentation and the installed environment. It does not freeze optimizer output, promise a chosen index, or assert timing gains. Plan output is treated as diagnostic evidence rather than a stable parsing interface.

Audited stable claims: parallel edge sequences are distinct when that is the stated row contract; two-step walks can repeat nodes and edges; unordered result multisets require multiplicity comparison; same counts alone do not prove equality; endpoint DISTINCT changes the provided walk contract. The eight-row fixture has two eligible first edges and four eligible second edges, giving eight sequences with destinations A/B/C. Fictional names and counts are explicit. No production throughput, law, external threshold or current release claim appears. Original Python/SQL code uses exact fixture fields and parameter binding.

## Actual executed checks

Direct tools.sf.validate_text returned errors=[] and warnings=[]; body whitespace word count 1565. Executed the exact Python code fence on Python 3.14.6 with SQLite 3.50.4. Observed:

```text
runtime 3.14.6 SQLite 3.50.4
rows 8 distinct destinations 3
baseline plan [(3, 0, 216, 'SCAN a'), (22, 0, 53, 'SEARCH b USING AUTOMATIC PARTIAL COVERING INDEX (relation=? AND source=?)')]
candidate plan [(3, 0, 56, 'SEARCH a USING COVERING INDEX hop_lookup (source=? AND relation=?)'), (11, 0, 56, 'SEARCH b USING COVERING INDEX hop_lookup (source=? AND relation=?)')]
```

This is an observed plan change for this environment only, not a speed measurement. Before/after result Counters equaled independent Python edge-pair enumeration. The empty Z lookup returned no matches; the skill distinguishes no matches from confirmed node presence.

Additional actual executions passed: empty graph, the published p/q parallel-first-hop fixture, a single self-loop reusing the same edge on both steps, and excluded first-hop relation. Exhaustively enumerated all sixteen directed edge subsets on A/B including loops, using both source IDs: 32 cases. Each baseline and indexed query matched independently enumerated edge sequences. No equality check relied on plan text or aggregate totals. Temporary database only; no real data or schema changed.

Independent review is still required before acceptance. No representative workload timings, write/storage overhead, query pagination, production deployment or complete arbitrary SQL equivalence proof were performed.
