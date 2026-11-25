# Candidate GRF-059: optional graph edge-pattern row contract

Status: discovery card only. No skill or registry entry. ID provisional.

## Problem and distinct artifact

Specify and verify a one-edge **optional** directed graph-pattern result for a fixed seed-node inventory. Every qualifying identified edge yields one row. A seed with no qualifying edge yields exactly one row with an explicit unbound edge/target marker. The artifact is an expected row multiset and a filter-placement comparison that exposes when a predicate applied after optional matching silently drops unmatched seeds. Do not assume a particular graph query language's syntax or null behavior; this neutral contract must be translated only after checking that implementation's current official documentation.

Actual nearby procedures inspected: GRF-015 `graph-query-plan-equivalence` checks an inner two-hop SQL walk multiset and plan changes under fixed graph data; it does not specify optional row preservation or predicate placement. GRF-006 `bounded-graph-traversal-contract` reports minimum-hop reached nodes, not one row per edge plus an unmatched row. GRF-020 `knowledge-graph-constraint-witness-review` treats missing values as a completeness question, not query outer-match row semantics. TDQ-008 `dataset-join-multiplication-diagnosis` is a generic tabular join diagnostic; the proposed skill must add graph-specific edge identity, direction, parallel-edge multiplicity and optional-filter placement rather than restating generic outer joins. sf.py searches for “optional graph” and “outer join” found no graph optional-pattern procedure.

## Neutral contract and fixture

Inputs: frozen node inventory and edge records `(edge_id, source, target, label)`; unique edge IDs and known endpoints; explicitly selected seeds; direction `out` or `in`; relation filter applied **inside** the optional pattern; and any target predicate whose placement is being compared. Preserve parallel edge IDs. Use a distinguished unbound marker in the reference that cannot collide with a node ID; never treat it as a graph node or a negative fact. A seed with matching edges has no extra unbound row. A seed with none has one unbound row, regardless of how many nonmatching relations exist.

Fictional nodes A,B,C,I; edges p1:A→B link, p2:A→B link, loop:B→B link, note:C→B note. Query all A/B/C/I seeds for optional outgoing `link` edge. Expected rows are `(A,p1,B)`, `(A,p2,B)`, `(B,loop,B)`, `(C,unbound,unbound)`, `(I,unbound,unbound)`: five rows. C's note edge does not match link, so it receives one unbound row; B's self-loop is one matching edge; parallel A/B IDs create two rows. An after-optional condition requiring edge label `link` removes both unbound rows under the explicitly modeled three-valued/undefined filtering rule, leaving three rows. That is a different result contract. An inside-optional target condition that excludes B would instead yield one unbound row for each seed, not zero rows; this isolates predicate placement.

Executable acceptance: a Python 3 reference builds expected per-seed rows directly from source edge IDs and separately simulates a filter applied after optional matching. Compare exact row multisets and preserve original seed coverage. Test incoming direction, parallel edges, loop, relation mismatch, isolated seed, no seeds, malformed/duplicate edge ID, ambiguous unbound sentinel, and a proposed engine adapter that drops unmatched rows. The independent verifier may reconstruct rows by a second per-edge grouping method. Report that neutral undefined-filter behavior is a declared fixture assumption, not a universal platform rule.

## Gate before authoring

Recheck actual GRF-015/006/020 and TDQ-008. If the procedure becomes merely a generic left join explanation, reject it. A full skill needs a distinct graph row contract, runnable fixture, explicit missing-input behavior, source-identity tests and independent ordinary/adversarial review before registry acceptance.
