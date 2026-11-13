# GRF-010 independent review

Reviewer: flow_review, 2026-11-13. Decision: accept for coordinator validation; no blocking finding. Reviewed the complete draft and author evidence, AGENTS.md and SPEC.md. Only this review log was changed; no registry or skill mutation.

## Selected-neighbor comparison

Used sf.py metadata for BPL-003 and MOP-008, then inspected their actual procedures, plus GRF-006 inputs/procedure. BPL-003 compares work against specialist capacity and exposes deferrals. MOP-008 translates service request stages into role workload. GRF-006 reports bounded reachability under a traversal contract. None delivers per-edge capacity bounds, internal-node conservation, signed residual cancellation and a separating cut matching the net terminal value. The proposed-flow certificate is a distinct artifact, not another generic capacity plan or seed traversal. This is selected-neighbor evidence, not exhaustive proof of library uniqueness.

## Mathematical and claim audit

All specific mathematical claims were reviewed under the declared directed, nonnegative edge-capacity, single-commodity model. Conservation makes net source flow equal net flow across any source/sink separating cut. The latter is forward crossing flow minus reverse crossing flow, so nonnegative assignments and capacity bounds give an upper bound equal to forward crossing capacity. If the residual reachable set excludes the sink, every forward crossing original edge is saturated and every reverse crossing original edge has zero flow; otherwise a positive residual arc would leave that set. Equality therefore certifies maximum value for a feasible assignment. A residual source-to-sink path permits a positive adjustment equal to the minimum residual availability while preserving internal conservation. Original edge identity and signs prevent confusion between cancellation and a distinct antiparallel edge.

Self-loops cancel in balances and do not cross a cut. Feasible circulations do not by themselves add net terminal value. These are stable mathematical claims, not assertions of physical capacity or current platform behavior. Unknown loss/storage, lower bounds, coupled constraints and multiple commodities remain outside the plain model until explicitly modeled. Numeric equality is exact only within the stated integer contract. The helper expects tuple shapes and string identities prevalidated, as expressly documented. No external rates, laws, runtime currency or invented citation appears.

The example arithmetic is internally consistent: initial net source value 2+1=3, proposed value 2+2=4, and the final forward cut capacities 2+2=4. The six-unit sum of initial edge assignments is deliberately identified as double-counting staged transfer, not throughput.

## Actual code executions

Extracted and executed the exact Python fence under Python 3.14.6. Embedded assertions passed with stdout `feasible improvement and matching cut checks passed`. Direct `tools.sf.validate_text` returned errors=[] and warnings=[]; this is draft validation, not accepted registry status.

Independent reviewer fixtures produced:

```text
parallel: improvable value=2, path=[(q,+1,2)], amount=2
parallel preview: maximum value=4, source_side=[s], cut=[(p,2),(q,2)]
cancel: improvable value=1, path=[(sb,+1,1),(ab,-1,1),(at,+1,1)], amount=1
cancel preview: maximum value=2, source_side=[s], cut=[(sa,1),(sb,1)]
circulation: maximum value=2, source_side=[a,s], cut=[(at,2)]
disconnected: maximum value=0, source_side=[s], cut=[]
```

The cancellation fixture had s->a->b->t carrying one, unused s->b and a->t, and a distinct unused b->a original edge with capacity one. The returned backward ab arc remained separate from ba. Signed adjustments were applied only to fresh tuple lists, and every returned improvement was re-certified with value increased by exactly its returned amount. The circulation fixture included s->a flow three, a->s flow one, a->t flow two, and an a self-loop carrying four; the net value remained two. For each maximum result, independently summed crossing capacities and checked source membership/sink exclusion. Assertions confirmed original input lists did not mutate.

Negative capacity, negative flow, over-capacity flow and Boolean capacity each raised the expected capacity violation. An s->a unit flow with no onward flow raised conservation violation with balances s=-1, a=1, t=0. Identical source/sink was rejected. No live network, physical system or production-scale graph was tested.

## Independent procedural applications

These are reviewer applications of the written skill, not a separate model benchmark.

### Ordinary supplied parallel flow

Input: fictional P1 has nodes S/T, directed edges p and q each capacity two, assignments p=2 and q=0; exact units for one period, single commodity, no additional constraints, review only.

```text
Model: P1 complete fictional model; units per period; S to T; edge bounds only.
Assignment: p|2|2; q|2|0.
Feasibility: Bounds pass; S=-2, T=2; no internal nodes.
Residual evidence: q(+1), availability two; proposed increase two.
Cut evidence: Initial assignment not maximum-certified. Separate preview p=q=2 has source side {S}, cut p=2 plus q=2, total four.
Decision: Feasible improvable; initial value two is below the independently checked preview value four.
Next check: Obtain approval before any operational change; preview recheck passed in the fictional fixture only.
Limits: Exact supplied mathematical model; no live operation, actual throughput or safety validation.
```

All published test assertions hold, including retaining both edge IDs and not treating p saturation as an optimality proof.

### Required inputs missing

Input: "Prove this flow is maximum" with a diagram and unlabeled numbers, but no terminal, unit or assignment definitions.

Reviewer response: "Which distinct nodes are source and sink, and what snapshot do the arrows represent? What capacities, flow assignments and common unit/period apply to every edge? Are there losses, storage, lower bounds, node limits or coupled constraints, and what exact arithmetic or tolerance is authorized?"

Three grouped questions in one message. Decision remains incomplete; no missing assignment is inferred as zero, no diagram number is silently classified as capacity, and no maximum claim is made.

### Cancellation with a distinct reverse relationship

Input: fictional C1 cancellation fixture from execution above, with no live changes requested.

```text
Model: C1; exact unit capacities; s to t; directed edge-capacity model.
Assignment: sa|1|1; ab|1|1; bt|1|1; sb|1|0; at|1|0; ba|1|0.
Feasibility: Bounds and internal balances pass; value one.
Residual evidence: sb forward, ab backward, at forward; amount one. Backward ab decreases ab, not an increase to ba.
Cut evidence: Separate preview has cut {s}, sa capacity one plus sb capacity one, total two.
Decision: Initial assignment feasible improvable; preview maximum value two.
Next check: Keep ba unchanged; propose sb=1, ab=0, at=1 and recheck all original edge identities. Executed preview passes.
Limits: Fictional assignment copies only; no physical reverse link or live mutation inferred.
```

### Invalid conservation boundary

Input: fictional s/a/t inventory with only s->a capacity one and flow one. Output decision invalid, bounds pass but internal a balance is +1, terminal values disagree; residual/optimality certification withheld. Request a corrected assignment or an explicitly different storage model. Do not clip the supplied flow or invent an a->t edge.

## Disposition

No blocking finding. Execution and scenario evidence support the stated finite reference contract and selected-neighbor distinction. No claim is made about general malformed-record parsing, real throughput, physical safety, universal numeric tolerances or completeness of unseen graphs.
