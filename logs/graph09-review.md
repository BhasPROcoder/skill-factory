# GRF-009 independent coordinator review

Reviewed 2026-11-13. Decision: accept for serial ingestion and structural checks; no blocking finding. This is an independent application by the coordinator, not a separate model-service benchmark.

## Distinctness and claims

Read the full draft and the relevant procedures of SEQ-003 and EXP-005 after sf.py metadata lookup. GRF-006 was previously read in full. GRF-006 returns bounded minimum-hop reachability; SEQ-003 propagates task durations through an acyclic dependency graph to obtain completion/slack; EXP-005 compares interpretation on exhibit routes. GRF-009 computes one minimum additive-cost route, retains original weighted-edge identities and verifies distance inequalities. Its artifact and solver preconditions are distinct from those selected neighbors. This comparison is not an exhaustive uniqueness proof across the library.

Reviewed nonnegative settlement, strict-improvement predecessor handling, tie limits, zero cycles, source-equals-target, unreachable reporting and exact integer units. The proof obligation is appropriately bounded: source distance zero and edge inequalities imply a target label no greater than any source-to-target route sum; an actual continuous witness with that sum establishes equality. Edges leaving a reachable node must also lead to a labeled node after completed exploration, as checked by the reference. Negative and nonadditive cases are not silently transformed. No current API, platform release, price, law or unsupported operational safety claim is required.

## Actual executed checks

Extracted the Python fence directly and executed it on Python 3.14.6. Observed its embedded output:

```text
cost, tie witness, zero-loop, unreachable and source-equals-target passed
review: ordinary=5 via sa,at; reverse unreachable; identity=0; zero-cycle/parallel=1; eight rejections; nonmutation PASS
runtime 3.14.6
validation ([], [])
```

Extra assertions used s/a/t/x with direct s-to-t cost 9, s-to-a cost 2, a-to-t cost 3 and a self-loop cost 0. Returned cost 5 and edge IDs sa/at. Reverse t-to-s was unreachable; s-to-s returned zero and an empty path. A separate zero-cost s/a cycle plus parallel s-to-t edges of costs 5 and 1 returned edge fast at cost 1. Input lists were unchanged. Six invalid weights (negative, Boolean, missing, fraction, infinity, NaN), an unknown endpoint and a repeated edge identity raised ValueError. Tuple shape/string-field prevalidation remains an explicit caller responsibility. No production-scale implementation or external graph was tested.

## Ordinary procedural application

Input: the complete fictional s/a/t/x fixture described above, exact additive effort ticks, directed edges, one witness requested.

```text
Scenario: Reviewer fixture; s to t; complete supplied directed graph; no filters.
Cost contract: Exact nonnegative integer effort ticks; additive; every supplied edge has a cost.
Method: Executed small-graph label settlement after checking all scoped weights.
Result: Minimum cost 5 ticks within the supplied graph.
Witness: sa | s->a | 2; at | a->t | 3.
Verification: Executed cost/continuity/distance assertions; independently summed 2+3=5. Input records unchanged.
Alternatives: One witness only; direct edge costs 9, uniqueness beyond tested alternatives not claimed.
Limits: No real route availability, safety, capacity or live-system claim.
```

The published test assertions are satisfied. The zero loop did not enter the witness.

## Missing-input application

Input: “Find the cheapest route” with labels but no reliable costs, direction or unique source/target IDs.

Response: “Please supply the graph snapshot with unique node and edge IDs and its direction. Which exact source and target IDs should be used? What does each edge cost mean, in which exact unit, and are costs additive?”

Result remains unresolved; no missing weight becomes zero, no label is chosen by convenience and no execution is claimed. These are three grouped questions in one message.

## Edge application

Input: a fictional graph contains one negative edge, including on an otherwise disconnected branch, and the user asks to replace its sign so the reference runs.

Response: retain the original costs; the supplied reference rejects the scoped graph. Mark method selection unresolved pending a separately verified negative-weight method and its relevant cycle handling, or an explicitly justified change to the problem scope. Do not return an optimum for an altered objective. No path or finite cost is reported from this rejected run.

The executable negative-weight probe raised ValueError. Separately, completed reverse-direction unreachability in the ordinary fixture is limited to that graph, while an interrupted run would remain incomplete. Author oracle claims were read but not used as a substitute for these independent checks.
