Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-043
name: directed-minimum-feedback-edge-certificate
domain: Graph Engineering Foundations
subdomain: Directed cycle-breaking analysis
version: 1.0
description: Find and verify a minimum-cardinality set of identified directed edges whose hypothetical removal makes a bounded graph acyclic.
triggers: ["find the fewest edges to break all cycles", "compute a directed feedback edge set", "certify minimum cycle-breaking edge count", "compare alternative cycle repairs", "check a proposed feedback edge removal"]
not_for: ["finding one cycle witness [SEQ-001]", "reachability-preserving reduction of an already acyclic graph [GRF-035]", "authorizing deletion of source relationships", "weighted or policy-constrained repair"]
requires: []
risk_level: medium
---

# Directed Minimum Feedback Edge Certificate

## Purpose
Find the smallest number of identified directed edges whose hypothetical removal leaves an acyclic graph. Return a complete optimum only after bounded exhaustive search reaches a feasible set in increasing cardinality order and an independent verifier checks it. Graph minimality does not determine which business relationships may actually be changed.

## Inputs to collect
1. **Snapshot** — obtain unique node IDs, unique edge IDs, source and target endpoints, and a revision, including isolates. Why: a missing edge or ID collision changes the cycle problem. Default: none.
2. **Direction and projection** — confirm included relationship types and arrow meaning. Why: an undirected or filtered graph has a different cycle definition. Default: no silent conversion.
3. **Removal unit** — confirm that one candidate removes exactly one edge ID, not all parallel records or one endpoint pair. Why: parallel edges can require distinct decisions. Default: one identified edge record.
4. **Search budget** — obtain a maximum number of candidate subsets to examine, with an execution environment. Why: exhaustive search may stop before proving a minimum. Default: ask; no unbounded production promise.
5. **Decision boundary** — identify who owns each edge and whether any records are protected or have unequal costs. Why: the reference minimizes count only. Default: structural hypothetical; if constraints matter, formulate a separate verified model before claiming an optimum for it.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the snapshot, selected directed projection and edge-ID removal unit.
2. Validate nonempty string node and edge IDs, unique identities, known endpoints and a positive integer candidate budget.
3. Check the original graph for a directed cycle using a complete acyclicity test; include self-loops and parallel records.
4. Enumerate edge-ID subsets by increasing size, and within a size by deterministic ID order.
5. For each subset, remove exactly those IDs from a hypothetical copy and run the complete acyclicity test; increment the budget counter once per candidate tested.
6. Stop at the first acyclic candidate. All smaller subsets have already failed, so its count is minimum within the supplied graph. Ties may exist; the returned set is one deterministic optimum, not the only one.
7. ⚠️ If the budget is exhausted before a feasible candidate is tested, report `unknown`, the number examined and the next untested candidate; do not call the best observed cyclic set an optimum.
8. Independently test the residual graph for absence of cycles using a second method and test every smaller edge-ID subset for remaining cyclicity before accepting a `complete minimum` certificate.
9. Preserve original edge records and any cycle evidence in the output. Escalate proposed removals to the relevant owners; neither cardinality nor deterministic tie-breaking supplies repair authority.
10. Report the chosen ID set, count, search completeness, verification and limits. If source data or constraints change, rerun from the new frozen scenario.

The Python 3 reference below accepts finite lists of nodes and `(edge_id, source, target)` triples. It counts candidate subsets, not wall-clock time. Run it on the available interpreter and record the observed version. This is a small-graph exact method; a larger graph needs a separate solver and a certificate whose current interfaces are checked from its official documentation.

```python
from itertools import combinations

def check(nodes, edges, limit):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    if any(type(e) not in (tuple, list) or len(e) != 3 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b in edges):
        raise ValueError("unknown endpoint")
    if type(limit) is not int or limit < 1:
        raise ValueError("positive integer candidate budget required")

def dag_kahn(nodes, edges):
    indegree = {n: 0 for n in nodes}
    outgoing = {n: [] for n in nodes}
    for _, a, b in edges:
        indegree[b] += 1
        outgoing[a].append(b)
    queue = [n for n in nodes if indegree[n] == 0]
    visited = 0
    for node in queue:
        visited += 1
        for nxt in outgoing[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return visited == len(nodes)

def dag_dfs(nodes, edges):
    adj = {n: [] for n in nodes}
    for _, a, b in edges:
        adj[a].append(b)
    state = {n: 0 for n in nodes}
    def visit(node):
        state[node] = 1
        for nxt in adj[node]:
            if state[nxt] == 1 or (state[nxt] == 0 and not visit(nxt)):
                return False
        state[node] = 2
        return True
    return all(state[n] != 0 or visit(n) for n in nodes)

def solve(nodes, edges, limit):
    check(nodes, edges, limit)
    ids, examined = sorted(e[0] for e in edges), 0
    for size in range(len(ids)+1):
        for chosen in combinations(ids, size):
            if examined == limit:
                return {"status": "unknown", "examined": examined,
                        "next": chosen}
            examined += 1
            removed = set(chosen)
            kept = [e for e in edges if e[0] not in removed]
            if dag_kahn(nodes, kept):
                assert dag_dfs(nodes, kept)
                for smaller in range(size):
                    for other in combinations(ids, smaller):
                        assert not dag_dfs(nodes, [e for e in edges
                                                 if e[0] not in other])
                return {"status": "complete minimum", "removed": chosen,
                        "count": size, "examined": examined}
    raise AssertionError("removing every edge must leave an acyclic graph")

nodes = ["A", "B", "C", "I"]
edges = [("ab", "A", "B"), ("ba", "B", "A"),
         ("loop", "C", "C")]
result = solve(nodes, edges, 20)
assert result == {"status": "complete minimum",
                  "removed": ("ab", "loop"), "count": 2, "examined": 6}
assert solve(nodes, edges, 2)["status"] == "unknown"
assert solve(["I"], [], 1)["removed"] == ()
print("minimum feedback set, cutoff and independent DAG checks passed")
```

The independent depth-first check evaluates the residual graph and every smaller removal set after a complete result. A self-loop must be removed to achieve acyclicity. Two parallel A→B records with one B→A record can be broken by removing the single B→A record; deleting only one A→B record leaves a cycle. The reference does not optimize costs, protected edges, or operational consequences.

## Decision rules
- IF the baseline is already acyclic THEN return the empty set as a complete minimum BECAUSE zero removals suffice.
- IF a self-loop remains THEN reject the candidate BECAUSE a one-edge directed cycle remains.
- IF a parallel edge survives a proposed cut THEN test the actual residual IDs BECAUSE removing one identity does not erase its peers.
- IF the candidate budget ends before a feasible set THEN report unknown completeness BECAUSE untested subsets may contain the first solution.
- IF owners forbid an edge's removal THEN rerun a constrained model BECAUSE the unconstrained minimum may be inadmissible.

## Output template
```text
Scope: <revision, directed projection and complete inventory; maximum 70 words>
Search: <candidate budget, examined count, deterministic ID order>
Status: <complete minimum / unknown>
Proposed removed IDs: <one set with count, or unresolved>
Residual evidence: <acyclic verification or pending; original records retained>
Minimum proof: <all smaller subsets checked, or not established>
Limits: <coverage, constraints and decision authority; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Node and edge identities are checked before search.
- [ ] Every candidate removes exact edge IDs.
- [ ] Subsets are tested by ascending cardinality.
- [ ] Cutoff is reported as unknown, never as minimum.
- [ ] Residual acyclicity is independently verified.
- [ ] Every smaller subset is checked before a minimum claim.
- [ ] Self-loops and parallel records retain their identities.
- [ ] Owner approval is separated from hypothetical graph analysis.

## Anti-patterns
- **One-cycle cure**: remove one witness edge and declare the whole graph repaired. Fix: test the complete residual graph.
- **Unbounded optimum claim**: stop at a budget and say minimum. Fix: label completeness unknown.
- **Parallel collapse**: remove an endpoint pair instead of an ID. Fix: filter by exact edge identity.
- **Count without proof**: report two deletions while an untested one-edge solution exists. Fix: exhaust all smaller subsets.
- **Automatic source edit**: delete chosen records. Fix: present a hypothetical proposal to their owners.

## Worked example
**Input:** Fictional Team Rowan supplies A↔B as ab and ba, a C self-loop named loop, and isolated I. All links are directed. Search at most 20 candidates, minimizing removed edge count.

**Output:**
```text
Scope: Rowan exercise R1; nodes A/B/C/I and directed records ab,ba,loop; supplied inventory complete for this exercise.
Search: Budget 20 subsets; 6 examined; edge IDs sorted ab,ba,loop.
Status: Complete minimum.
Proposed removed IDs: ab, loop; count 2.
Residual evidence: ba remains, I isolated; independent DAG check executed and passed; original records retained.
Minimum proof: Empty set and all three one-edge subsets were tested and remained cyclic.
Limits: One of multiple possible two-edge choices; count-only structural result, no owner approval to delete.
Next action: Relationship owners review edge meanings and constraints before considering a separate correction.
```

**Bad output:** “Remove ab; the A/B loop is gone, so all cycles are fixed and the repair is approved.”
The C self-loop remains, and the graph algorithm cannot authorize a source edit.

## Edge cases
- **Acyclic or empty graph**: return the empty removal set after testing it.
- **Self-loop**: every acyclic candidate must remove that edge ID.
- **Parallel directed edges**: treat each ID independently; the opposite-direction edge may be the cheapest count cut.
- **Disconnected cycles**: the returned set must break every component's cycle.
- **Cutoff before solution**: return unknown with examined count and next candidate.

## Test case
**Input:**
> Fictional directed graph has A→B, B→A, C→C and isolated I. Find the minimum number of identified edges to remove; also explain a search that stops after two candidates.

**Assertions:**
1. Reports a complete minimum count of two only after checking all smaller subsets.
2. Includes the C self-loop ID in the chosen removal set.
3. Verifies the residual graph is acyclic and retains I.
4. Labels the two-candidate cutoff unknown rather than optimal.
5. Does not authorize deleting a real source edge.
</skill>

<user_request>
Fictional directed graph has A→B, B→A, C→C and isolated I. Find the minimum number of identified edges to remove; also explain a search that stops after two candidates.
</user_request>
