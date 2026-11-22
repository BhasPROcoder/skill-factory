# Graph discovery after G24

Discovery only. No IDs reserved, registry changed, skill authored or acceptance established. Catalog queried with sf.py; selected procedures inspected where noted. These are proposed next actions, not proof of whole-catalog uniqueness. No external source text or code was used; public-source discovery remains a later gate if these become authoring candidates.

## Proposed order

### 1. Constrained graph negative-example construction — pursue after G23 review

Nearest actual entries: GRQ-004 sampling-plan-rationale (catalog metadata); GRF-023 graph-learning-split-leakage-audit (pending file inspected, absent from registry at inspection). G23 audits supervision/context visibility and traces sampling provenance but does not construct eligible negative candidates.

Deliverable: reproducible sampled candidate pairs with eligibility/rejection ledger, population definition, collision policy, exhausted-pool handling and explicit unknown-label status. Decide whether to corrupt source or target, enforce endpoint classes and relation direction, exclude known positive facts under the declared evidence boundary, and disclose that unobserved edges are not proven false. Keep training-only sampling and evaluation filtering policies separate: access to held-out positives must follow the declared experiment contract rather than silently leaking labels into fitting.

Failure decisions: reject disallowed self-pairs, known positives and declared inverse-equivalent positives; distinguish pool exhaustion from a sampling bug; report duplicates and seed/order provenance; never fabricate extra negatives to reach a requested count.

Executable acceptance fixture: small fictional typed node inventory whose admissible pair set is enumerated independently; known positive and inverse representation removed; requested sample exceeds finite pool; verify returned unique candidates plus shortfall and deterministic rerun. Include empty eligible class and policy prohibiting access to evaluation labels. Author must compare actual feature/sampling neighbors before committing scope.

### 2. Partition boundary ownership reconciliation — pursue after G24 review

Nearest entries: GRF-013 graph-community-partition-sensitivity (procedure inspected), GRF-007 weak-component-scope-diagnosis and GRF-008 strong-component-condensation-analysis (metadata), GRF-014 relational-graph-storage-implementation and pending G24 recovery (later substantive comparison required).

Deliverable: shard owner/replica manifest and cross-boundary edge reconciliation. A community label or connected component is an analytical partition; this task establishes which storage owner must retain each logical entity/edge and which replica copies are expected. Define owner function and epoch, enumerate boundary endpoints, reconcile missing and duplicate logical edges, then compare reconstructed global query results against a frozen reference. Do not claim distributed atomicity from an offline manifest check.

Failure decisions: classify legitimate replica copies separately from conflicting owner claims; preserve parallel edge IDs; reject mixed partition epochs; identify dangling remote references without inventing nodes.

Executable fixture: split a directed multigraph containing isolated nodes, parallel edges and one cross-shard edge; reconstruct by logical IDs; inject a missing boundary replica, duplicate ownership and stale epoch; each must yield its own witness. Query/count parity alone cannot prove full record parity.

### 3. Property graph serialization roundtrip — reject broad proposal

Nearest entries: GRF-003 graph-edge-list-import-reconciliation and GRF-017 reversible-graph-identity-migration, both selected procedures inspected. G03 already explicitly round-trips destination exports and preserves IDs, direction, properties and parallel edges. G17 checks full mapped records and inverse reconstruction. A new skill simply exporting, importing and comparing the same graph would repeat existing procedures.

Do not allocate an ID. A future narrower interoperability task would need a genuinely different mechanism, such as a documented typed-value encoding contract with exact null/missing and numeric-type semantics. Reopen only with a concrete format interoperability problem and verified current primary format documentation. Its fixture would need to demonstrate a failure the current generic roundtrip cannot diagnose; adding more test values alone is insufficient uniqueness.

### 4. Graph similarity alignment — hold; avoid identity/matching duplication

Nearest entries: GRF-002 graph-entity-merge-impact-review (procedure inspected), GRF-011 bipartite-matching-certificate (metadata), GRF-013 community comparison (procedure inspected), GRF-017 reversible migration (procedure inspected).

A label-based node match followed by merge or one-to-one assignment repeats G02/G11; partition-label alignment repeats G13; supplied identity-map transformation repeats G17. Reject these versions.

Potential distinct scope: structural graph alignment under explicitly supplied node/edge compatibility with symmetry ambiguity, returning a set of admissible mappings or a bounded search result rather than inferred entity identity. Deliverable must report unmatched nodes, edge-preservation witnesses and equivalent mappings, with semantic identity left unresolved. Distinguish exact isomorphism from approximate optimization and never claim optimality after a search cutoff.

Executable acceptance fixture if reopened: two small graphs with permuted labels and symmetric nodes yielding multiple valid mappings; another pair with identical degree counts but incompatible edges; incomplete search must report unknown completeness. Requires substantive G11 comparison and algorithm-specific accuracy review before authoring. Lower priority than the two clearer operational gaps above.

## Admission rules

No discovery card increases accepted counts. Complete missing neighbor comparisons and public-source provenance where used, then author a single bounded procedure with actual fixtures, claim audit and independent review. G23/G24 current work takes precedence. Do not use the remaining graph allocation to justify renamed variants.
