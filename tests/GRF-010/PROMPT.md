Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-010
name: flow-feasibility-cut-certificate
domain: Graph Engineering Foundations
subdomain: Flow and capacity certificates
version: 1.0
description: Validate a proposed directed network flow and produce either a residual improvement witness or a matching cut certificate when capacity and conservation claims need evidence.
triggers: ["check this network flow is feasible", "prove this flow is maximum", "find residual flow improvements", "verify a capacity cut certificate", "explain why saturated edges do not prove optimality"]
not_for: ["business workload tradeoffs [BPL-003]", "service staffing capacity estimates [MOP-008]", "dependency duration and slack [SEQ-003]", "minimum-cost flow, multiple commodities or physical safety certification"]
requires: []
risk_level: medium
---

# Flow Feasibility Cut Certificate

## Purpose
Turn a proposed single-commodity flow into independently checkable capacity, conservation and optimality evidence. Separate an invalid assignment, a feasible but improvable flow, and a feasible flow whose value matches a separating cut. The certificate concerns the supplied mathematical model, not actual throughput or safe operation of a physical system.

## Inputs to collect
1. **Network snapshot** — obtain all node IDs and uniquely identified directed edges with source records. Why: parallel and opposite-direction relationships must remain distinguishable. Default: supplied snapshot only, with wider completeness unverified.
2. **Source and sink** — obtain distinct terminal IDs and what transfer they represent. Why: internal nodes conserve flow while terminals define the measured value. Default: none; do not infer terminals from a diagram.
3. **Capacities and units** — obtain nonnegative edge limits in the same units and planning interval. Why: incompatible quantities cannot share a conservation equation. Default: unknown values block certification; never substitute unlimited capacity.
4. **Proposed flow** — obtain a nonnegative assignment for every edge. Why: feasibility is a property of an explicit assignment. Default: request missing assignments; zero may be used only as an explicitly proposed starting assignment, not observed operation.
5. **Model restrictions** — identify losses, storage, lower bounds, node capacities, multiple commodities or coupled limits. Why: these need additional modeling and invalidate a plain edge-capacity certificate if ignored. Default: no such restriction assumed absent without confirmation.
6. **Arithmetic contract** — obtain exact integer/scaled units or an evidenced numeric tolerance. Why: near-equality is not an exact certificate. Default: the reference uses nonnegative integers; other arithmetic requires a documented adaptation.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the model revision, common units, terminals and assumptions; state whether this is an assignment review or a request to construct an improved flow.
2. Validate unique node/edge identities, known endpoints and complete capacities/assignments before calculating totals.
3. Check every edge against zero and its capacity; preserve offending edge IDs rather than clipping invalid values.
4. Compute incoming minus outgoing flow at every node; require zero at internal nodes and equal opposite terminal balances with nonnegative source net outflow.
5. Stop optimality analysis if feasibility fails, returning the violated bounds or node balances as the repair evidence.
6. Build residual arcs for each original edge: forward availability is capacity minus flow, and backward availability is flow. Preserve edge ID and direction sign on both arcs.
7. Search from the source through positive residual availability, retaining predecessor arcs and the full reachable set.
8. If the sink is reached, reconstruct one simple residual path and compute its smallest availability. Present the signed original-edge changes as an improvement proposal; backward arcs decrease an existing assignment rather than create an actual reverse relationship.
9. If the sink is unreachable, take the source-reachable set as one side of a cut. Sum capacities of original edges leaving that set and compare with the feasible net source flow.
10. ⚠️ Claim maximum only when feasibility and a matching separating-cut value are both established. Saturating a few edges or failing to find a path in an interrupted search is insufficient.
11. Recheck all bounds and balances after any approved change to a separate assignment, and label any search interruption or incomplete model evidence explicitly.

This Python 3 reference uses exact integer units and tuples `(edge ID, source, target, capacity, flow)`. Validate tuple shapes and nonempty string identities before calling it. It supports parallel, antiparallel and self-loop edges through separate IDs; it checks a supplied flow rather than running a full optimizer. Execute the snippet and record the installed interpreter version.

```python
from collections import deque

def certify(nodes, edges, source, sink):
    known = set(nodes)
    if len(known) != len(nodes) or source not in known or sink not in known or source == sink:
        raise ValueError("unique inventory and distinct known terminals required")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("unique edge IDs required")
    balance = {n: 0 for n in nodes}
    residual = {n: [] for n in nodes}
    for eid, u, v, cap, flow in edges:
        if u not in known or v not in known:
            raise ValueError("unknown endpoint")
        if type(cap) is not int or type(flow) is not int or not 0 <= flow <= cap:
            raise ValueError(("capacity violation", eid))
        balance[u] -= flow
        balance[v] += flow
        if cap > flow:
            residual[u].append((v, eid, 1, cap-flow))
        if flow:
            residual[v].append((u, eid, -1, flow))
    value = -balance[source]
    if value < 0 or balance[sink] != value or any(
            b != 0 for n, b in balance.items() if n not in (source, sink)):
        raise ValueError(("conservation violation", balance))
    parent, queue = {source: None}, deque([source])
    while queue:
        u = queue.popleft()
        for v, eid, sign, available in residual[u]:
            if v not in parent:
                parent[v] = (u, eid, sign, available)
                queue.append(v)
    if sink in parent:
        path, v = [], sink
        while v != source:
            u, eid, sign, available = parent[v]
            path.append((eid, sign, available))
            v = u
        path.reverse()
        return {"state": "improvable", "value": value,
                "path": path, "amount": min(a for _, _, a in path)}
    side = set(parent)
    cut = [(eid, cap) for eid, u, v, cap, flow in edges if u in side and v not in side]
    assert sum(cap for _, cap in cut) == value
    return {"state": "maximum", "value": value,
            "source_side": sorted(side), "cut": cut}

nodes = ["s", "a", "b", "t"]
edges = [("sa", "s", "a", 3, 2), ("at", "a", "t", 2, 2),
         ("sb", "s", "b", 2, 1), ("bt", "b", "t", 2, 1)]
result = certify(nodes, edges, "s", "t")
assert result["value"] == 3 and result["amount"] == 1
assert [p[0] for p in result["path"]] == ["sb", "bt"]
fixed = edges[:2] + [("sb", "s", "b", 2, 2), ("bt", "b", "t", 2, 2)]
final = certify(nodes, fixed, "s", "t")
assert final == {"state": "maximum", "value": 4,
                 "source_side": ["a", "s"], "cut": [("at", 2), ("sb", 2)]}
print("feasible improvement and matching cut checks passed")
```

## Decision rules
- IF any capacity or conservation check fails THEN withhold a maximum-flow claim BECAUSE optimality certificates require a feasible assignment.
- IF a positive residual source-to-sink path exists THEN report an improvement amount and signed edge changes BECAUSE every path arc permits that adjustment.
- IF the feasible value equals a separating cut's capacity THEN certify maximum within the model BECAUSE every feasible transfer is bounded by that cut.
- IF an original reverse edge and a backward residual arc coexist THEN preserve both IDs and signs BECAUSE they represent different permitted changes.
- IF capacities describe different time windows or units THEN reconcile them first BECAUSE conservation across incomparable quantities is meaningless.

## Output template
```text
Model: <revision, units, terminals, restrictions; maximum 80 words>
Assignment: <edge ID | capacity | flow; complete table or attachment>
Feasibility: <bound violations and node balances, or exact pass evidence>
Residual evidence: <signed improvement path and amount, or complete reachable set>
Cut evidence: <source-side nodes, crossing original edge IDs/capacities and total; or not certified>
Decision: <invalid / feasible improvable / maximum certified / incomplete; reason>
Next check: <proposed adjustment or missing evidence; maximum 80 words>
Limits: <model assumptions, arithmetic and execution scope; maximum 60 words>
```

## Quality checklist
- [ ] Terminals, units and model restrictions are explicit.
- [ ] Every original edge retains its identity and assignment.
- [ ] Capacity bounds and internal conservation are independently checked.
- [ ] Flow value is net source outflow, not the sum of all edge assignments.
- [ ] Residual reverse arcs identify the original edge to decrease.
- [ ] A cut separates source from sink and counts only forward crossing capacities.
- [ ] Optimality is distinguished from feasibility and interrupted search.
- [ ] Proposed changes are not reported as live operations.

## Anti-patterns
- **Saturation proof**: call a flow maximum because one edge is full. Fix: produce a matching cut or residual result.
- **Total-edge counting**: count the same transferred units at every stage. Fix: measure terminal net flow.
- **Reverse-edge confusion**: treat cancellation as a physical reverse link. Fix: carry original ID and residual sign.
- **Silent clipping**: replace over-capacity values with limits. Fix: return the original violation for correction.
- **Model laundering**: ignore storage, loss or coupled constraints. Fix: revise the model before using its certificate.

## Worked example
**Input:** Fictional workshop Elm supplies the snippet's integer-unit network for one planning period, with no losses, storage or coupled limits. Review the initial assignment; no live changes requested.

**Output:**
```text
Model: Elm supplied fixture; integer units per period; source s, sink t; single commodity, edge limits only.
Assignment: sa|3|2; at|2|2; sb|2|1; bt|2|1.
Feasibility: Bounds pass; a and b balances zero; s=-3, t=3.
Residual evidence: sb(+1), bt(+1); increase both by one unit; bottleneck availability one.
Cut evidence: Not certified for the initial assignment.
Decision: Feasible improvable; current value three is not maximum.
Next check: Proposed separate assignment sb=2, bt=2; recheck all balances. Reference preview has value four and cut {s,a} with at=2 plus sb=2, certifying four when executed.
Limits: Fictional exact model; no actual throughput, physical safety or live mutation established.
```

**Bad output:** “at is saturated, so three is the maximum; total edge flow is six.”
The first claim ignores residual capacity via b, and the second double-counts transferred units.

## Edge cases
- **Disconnected sink**: a feasible zero flow may be maximum; show the zero-capacity separating cut rather than calling the model invalid.
- **Circulation**: preserve a feasible cycle flow; it contributes no net terminal value and may expose cancellation opportunities.
- **Parallel or antiparallel edges**: retain each original capacity and signed residual identity; never merge by endpoint pair silently.
- **Lower bounds or multiple sources**: obtain an explicitly validated transformed model; the reference cannot certify the unmodified problem.
- **Approximate arithmetic**: document tolerances and residual decisions; do not describe numerical near-equality as the exact integer certificate shown here.

## Test case
**Input:**
> Fictional source S and sink T have two parallel edges p and q, each capacity two; flows are p=2 and q=0. Single commodity, exact units, no other constraints. Review optimality without changing the graph.

**Assertions:**
1. Reports a feasible value of two and an improvement of two through q.
2. Does not treat saturated p as proof of maximum.
3. Retains both edge IDs and proposes q=2 rather than changing capacity.
4. Identifies the completed assignment's cut capacity four if that preview is actually checked.
5. Makes no live-operation or physical-safety claim.
</skill>

<user_request>
Fictional source S and sink T have two parallel edges p and q, each capacity two; flows are p=2 and q=0. Single commodity, exact units, no other constraints. Review optimality without changing the graph.
</user_request>
