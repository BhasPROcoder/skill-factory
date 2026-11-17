# GRF-006 independent review

Reviewer: g06_review_resume, 2026-11-13. Decision: accept for coordinator checks; no blocking finding. Only this review log was changed. No registry status or skill mutation was performed.

## Distinctness and scope

Read AGENTS.md, SPEC.md, the GRF-006 draft and author evidence. Queried sf.py metadata and read actual SEQ-001, GRF-004 and TDS-012 skills. SEQ-001 produces a cycle witness or ordering; GRF-004 checks explicit-root forest conformance; TDS-012 uses descendant evidence to plan authorized withdrawal actions. GRF-006 supplies a different artifact: minimum-hop bounded node reachability with predecessor witnesses and concrete boundary exits, explicitly separating bounded completion, exhaustion and interruption. The comparison supports a distinct operational procedure among these nearest neighbors, not exhaustive semantic uniqueness across every catalog entry.

The reference is explicitly limited to a fixed, finite filtered graph. Node exclusions, remote fetching, resource caps and path-dependent permissions require adaptation and are not falsely advertised as implemented. The procedure covers the reporting obligations when those features prevent a complete result. No public-source license or pinned-commit claim is made by the skill; the author's inspiration candidate remains separately unverified.

## Executed evidence

Extracted the exact Python fence from the draft and executed it with Python 3.14.6. Direct tools.sf.validate_text returned errors=[] and warnings=[]. This does not change registry status. Actual terminal output included:

```text
bounded, exhausted and zero-depth checks passed
ordinary depth 0 ({'P': 0}, {'P': None}, [('P', 'a', 'Q')])
ordinary depth 1 ({'P': 0, 'Q': 1}, {'P': None, 'Q': ('P', 'a')}, [('Q', 'c', 'R')])
ordinary depth 2 ({'P': 0, 'Q': 1, 'R': 2}, {'P': None, 'Q': ('P', 'a'), 'R': ('Q', 'c')}, [])
nonempty boundary with return only ({'A': 0, 'B': 1}, {'A': None, 'B': ('A', 'a')}, [])
minimum hops despite longer alternative ({'A': 0, 'B': 1, 'D': 1, 'C': 2, 'E': 2}, {'A': None, 'B': ('A', '1'), 'D': ('A', '4'), 'C': ('B', '2'), 'E': ('D', '5')}, [])
direction/filter/cycle/loop/parallel/minimum-hop/no-mutation and seven rejection cases passed
```

The ordinary fixture was the published P/Q/R test. Further assertions checked incoming traversal from R (R:0,Q:1,P:2), outgoing traversal from R (R only), either-direction traversal, an empty relation filter, a self-loop at zero depth, deterministic parallel-edge witness selection and unchanged input lists. A graph with A->B->C->D and A->D->E confirmed D at one hop and E at two, rather than retaining the longer first path. Seven expected rejection cases covered negative/Boolean/fractional depth, unknown seed, invalid direction, repeated edge identity and unknown endpoint. No remote pagination, interruption mechanism or production service was exercised.

## Independent procedural applications

These are reviewer-produced applications of the written skill, not a separately benchmarked model service.

### Ordinary bounded traversal and comparison

Input: fictional complete snapshot O1, nodes P/Q/R, link edges a:P->Q, b:Q->P, c:Q->R; seed P, outgoing link, depths one and two, one witness per node.

```text
Scope: O1 complete fictional fixture; seed P.
Contract: Outgoing link edges; no exclusions; compare bounds one and two; node witnesses only.
Reached: At bound one: P | 0 | none; Q | 1 | P/a. At bound two additionally R | 2 | Q/c.
Boundary: At one: Q, exit Q/c/R. At two: R, no exit to an unreached node.
Stopping: Both bounded complete; bound one depth-truncated, bound two exhausted within filtered O1.
Witness checks: Executed reference assertions verified distances and exits. P-a-Q-c-R uses two allowed outgoing edges; the return edge b does not repeat expansion.
Limits: One predecessor witness is not every route through the cycle. No live service or weighted-route claim.
```

All four published test assertions are satisfied. The result does not equate a finite witness with all possible paths.

### Required inputs missing

Input: "Find everything near the node called Cedar" with no snapshot, unique identity, direction, relation set or bound.

Response: "Please provide the graph snapshot and coverage statement, with the exact node ID meant by Cedar. Which direction and relation labels should traversal follow, and are any nodes excluded? What maximum edge count should bound the search, and is one witness per reached node sufficient?"

Three grouped questions are asked in one message. No seed is guessed from a label, no arbitrary hop limit is introduced, and execution remains unrun.

### Boundary is nonempty but reachability exhausted

Input: fictional complete E1 contains A/B and x edges a:A->B, b:B->A; seed A, outgoing x, depth one.

```text
Scope: Complete E1 fixture; seed A.
Contract: Outgoing x; no exclusions; one-hop bound; one node witness.
Reached: A | 0 | none; B | 1 | A/a.
Boundary: B; its only eligible step returns to already reached A, so no unseen-node exit.
Stopping: Bounded complete; exhausted within the filtered supplied graph.
Witness checks: Exact helper execution returned A:0, B:1 and an empty exit list.
Limits: Exhaustion does not enumerate all cyclic walks or establish real-world completeness outside E1.
```

This exercises the non-obvious stopping distinction rather than labeling every nonempty boundary truncated.

### Partial fetch and operational interruption

Input: fictional remote search from P with depth two has observed P->Q, but Q's adjacency page fails before completeness is established. No complete offline graph is available.

```text
Scope: Partial remote snapshot; seed P; Q adjacency unavailable.
Contract: Outgoing supplied link relation, depth two; one witness per node.
Reached: Observed P | 0 | none; Q | 1 | P/supplied-edge. Distances are observed-path lengths until missing adjacency is resolved, not certified global minima.
Boundary: Unavailable because required expansion is incomplete.
Stopping: Interrupted; exhaustion or depth truncation unknown.
Witness checks: Supplied P->Q witness is supported; full traversal and minimum-hop certification pending.
Limits: Cannot claim all nodes within two hops were examined. Resume the missing adjacency fetch or report the incomplete observed subset; no execution was simulated.
```

The reference has no remote budget implementation, so this is a procedural branch review only. The response correctly qualifies the template's minimum-hop field when complete expansion cannot be proved.

## Specific-claim audit

Breadth-first, first-discovery distances are minimum unweighted hop counts within the fixed adjacency. Every edge from a reached node below the limit is examined; therefore any exit from the reached set must come from the boundary after complete bounded execution. If the boundary has no unseen-node exit under full adjacency, no further reachable node exists in that filtered snapshot. These stable graph properties agree with the executed counterexamples. The worked distances, loop handling and deterministic parallel-edge choice are internally consistent. Interpreter version records observation, not a current-version recommendation. No changing law, price, API support assertion, invented citation or arbitrary production threshold appears.

Acceptance is limited to the skill's declared procedural and reference scope. No production graph, stateful permission model, remote budget implementation or complete-world reachability has been validated.
