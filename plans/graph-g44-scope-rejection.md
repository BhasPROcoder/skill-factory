# GRF-044 proposal rejected before allocation

Candidate: graph query pagination snapshot-consistency certificate for a changing node/edge result set.

`sf.py search pagination` found TAP-003 `api-pagination-consistency-plan`. Its actual Procedure already specifies deterministic ordering with a unique tie-breaker, cursor/snapshot semantics, mutations between page requests, duplicate/omission behavior, and a tied-sort-value fixture checking complete identifier coverage. The proposed G44's duplicate/missing identities, cursor-order violations, version mixing and stable exact coverage are applications of those same checks to graph node/edge rows. Adding a graph-specific name and Python fixture would not create a distinct portable judgment method.

Also compared actual GRF-005 (effective/recorded-time graph reconstruction), GRF-015 (query-plan output equivalence) and GRF-026 (partition placement reconciliation). They address different graph questions but do not rescue the proposed G44 from overlap with TAP-003.

No GRF-044 skill or staging manifest was written or registered. A future graph-specific pagination skill would need a concrete graph-only invariant beyond row identity and snapshot coverage, with a fixture that TAP-003 cannot already guide. This proposal is not counted toward the expansion.
