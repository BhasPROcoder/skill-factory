# Candidate GRF-051: bounded graph query cache invalidation ledger

Status: discovery card only. No skill or registry entry exists. The ID is provisional and must be rechecked before authoring.

## User problem and proposed artifact

A graph service has cached answers for several declared bounded traversal queries. One identified source edge is added or removed. Determine which cached answers may be retained, which must be invalidated, and which need recomputation, using complete before/after query results under the same projection and bound. Return a ledger keyed by cache key, query parameters, old source revision, candidate new revision, old answer, new answer, changed-answer witness and disposition. The decision concerns cache validity and version binding; it does not edit the source graph or assume a cache backend.

Each cache key must encode seed, direction, relation filter, hop bound, answer semantics and source revision. A stale revision marker is an invalidation finding even when answer contents happen to match; content equality is useful diagnostic evidence but does not make the old key a valid representation of the new revision. A cache entry without its full query contract is unresolved rather than retained.

## Nearest procedures inspected

- GRF-006 `bounded-graph-traversal-contract` computes one bounded answer and stopping evidence. It does not maintain a portfolio of versioned cached answers or decide per-key invalidation after a mutation.
- GRF-039 `directed-edge-addition-reachability-delta` compares all ordered pairs after one insertion, without hop bounds, relation filters, cached answers or deletion cases. Its pair delta is not sufficient to decide bounded-query cache validity: a shorter path can change a minimum-hop answer without changing reachability.
- GRF-047 `graph-adjacency-index-freshness-audit` reconciles primary edge IDs with outgoing/incoming index buckets and epoch, not cached traversal result contracts.
- GRF-015 `graph-query-plan-equivalence` compares a query's result multiset while changing its plan/index, with frozen data. It does not analyze a data mutation across multiple cached queries.

The new skill must remain an operations decision ledger. A generic “rerun a bounded traversal” recipe would duplicate GRF-006, and an unbounded all-pair insertion delta would duplicate GRF-039.

## Acceptance fixture

Use fictional nodes A, B, C, D, I. Baseline directed link edges: ab:A→B, bc:B→C, cd:C→D; I isolated. Cache three complete results at revision r1:

1. Key Q1: outgoing `link` from A, bound 2, answer includes minimum hop and reached IDs. Baseline A0,B1,C2.
2. Key Q2: outgoing `link` from D, bound 2. Baseline D0.
3. Key Q3: incoming `link` from C, bound 1. Baseline C0,B1.

Propose a new edge ad:A→D at revision r2. Recompute the same contracts: Q1 adds D1 and retains A0,B1,C2; Q2 and Q3 contents stay equal. The ledger must mark Q1 changed and all r1 keys revision-stale, then offer new r2 entries only after full recomputation and validation. It may separate “content unchanged” from “old key cannot serve r2.” A separate deletion fixture removes bc: Q1 loses C at bound 2 and Q3 loses B; Q2 remains content-equal. An alternative path fixture adds ac:A→C, changing C's minimum hop from 2 to 1 while unbounded A→C reachability was already true.

Adversarial checks: a relation-filtered edge must not change a query that excludes that relation; a cache key missing its filter or bound must be unresolved; an incomplete traversal cannot certify content unchanged; an edge-ID mutation must use the declared before/after inventories, not silently drop parallel records; all source revisions and query keys must be preserved in the audit.

## Gate before drafting

Author must compare actual closest procedures again, define one exact answer contract and a portable reference implementation, and demonstrate independent result verification for changed and unchanged cache entries. Independent reviewer must test ordinary, missing-input and adversarial cases. No count changes until registry ingestion and validation after that review.
