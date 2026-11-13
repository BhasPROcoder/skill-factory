# GRF-010 author evidence

2026-11-13; author g07_review_resume. Candidate is unaccepted pending independent review; no registry changes.

## Distinctness before authoring

Read SPEC and creation-order G10. Queried sf.py searches for flow/capacity and SEQ-003 metadata. Read task-specific input/procedure/rule sections of BPL-003, MOP-008 and SEQ-003. BPL-003 negotiates work versus specialist availability; MOP-008 translates request mixes into role workloads; SEQ-003 propagates dependency durations. None provides per-edge flow bounds, per-node conservation, signed residual cancellation or a matching cut certificate. Earlier actual GRF-004/006/007 review established forest/traversal/component scopes; none certifies transfer feasibility or maximum value. The artifact is a proposed-flow certificate, not a renamed workload or reachability report. This is bounded selected-neighbor comparison, not an exhaustive library claim.

## Claim self-audit before save

Reviewed capacity bounds, internal conservation, net source outflow, backward residual cancellation, feasible-flow upper bound by any separating cut, and equality as optimality proof. These are stable mathematical claims under the explicit single-commodity directed edge-capacity model. Every residual arc retains original edge ID and sign, avoiding antiparallel ambiguity. Self-loops cancel in node balance and never cross a cut. Unknown units, loss/storage, node capacities, lower bounds and multiple commodities are model inputs or explicit exclusions, never silently certified. Exact integer arithmetic is the example contract, not a universal numeric requirement. No current product behavior, platform/API/version claim or external factual attribution is included. Source/destination tuple identity validation is declared prevalidation.

Fictional example recomputation: initial net value 2+1=3; internal balances at a/b are zero; residual sb/bt availability one; proposed values 2+2=4. Cut source-side {s,a} has at capacity two and sb capacity two, total four. Summing all initial edge assignments gives six but double-counts each transferred unit, explicitly identified as the bad example. No physical-system suitability or live execution is asserted. Code and prose are original; no external skill content copied.

## Actual executed checks

Direct tools.sf.validate_text returned errors=[] and warnings=[]; whitespace body count 1730. Python 3.14.6 executed the extracted fence and printed `feasible improvement and matching cut checks passed`. This is draft checking, not registry validation status.

Additional actual checks:

- Parallel p/q each capacity two, assignments two/zero: feasible value two, residual path q forward, amount two.
- Cancellation fixture with s->a->b->t carrying one and unused s->b/a->t: residual path sb forward, ab backward, at forward, amount one. A distinct zero-capacity b->a original edge remained separate from ab's backward residual arc.
- Disconnected source/sink with no edges: maximum value zero.
- Over-capacity assignment raised capacity violation with original edge ID.
- Internal imbalance raised conservation violation with all node balances.
- A self-loop capacity three/flow two plus saturated source-to-sink capacity one: maximum value one; loop contributes no cut capacity.
- Completed parallel assignment p=q=2: maximum value four, cut retains both p/q IDs and capacities.

An exhaustive bounded test enumerated all 729 assignments of (capacity,flow) in {(0,0),(1,0),(1,1)} to the six distinct directed non-self edges on s/a/t. Infeasible assignments were rejected. For each of the 219 feasible assignments, independently enumerated both possible separating cuts and checked maximum status exactly when flow value equaled the minimum cut total. Each improvable result was applied to a separate tuple list using signed original-edge deltas, then re-certified; its value increased by the returned amount. Observed terminal output: `feasible assignments checked against enumerated cuts 219`. This verifies only the bounded fixture family, not production scale or alternative model constraints.

Independent ordinary/missing/edge procedural review remains required. The skill deliberately checks a proposed flow and one improvement rather than claiming to implement a complete optimizer. No live operations, throughput or safety validation occurred.
