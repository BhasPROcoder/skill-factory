---
id: GRF-040
name: bounded-maximum-clique-certificate
domain: Graph Engineering Foundations
subdomain: Clique search certificates
version: 1.0
description: Find a checked clique and distinguish proven maximum size from bounded-search uncertainty when a finite undirected graph needs a complete mutual-adjacency group.
triggers: ["find a maximum clique", "show fully connected node groups", "prove this clique is largest", "search for a clique with a budget", "check a claimed clique", "explain why a clique search is inconclusive"]
not_for: ["structural correspondence between graphs [GRF-027]", "bipartition or odd-cycle certificates [GRF-031]", "degree-threshold k-core peeling [GRF-037]", "inferring real-world group membership from links"]
requires: []
risk_level: medium
---

# Bounded Maximum Clique Certificate

## Purpose
Find a set of vertices in which every distinct pair is connected under a declared undirected projection. Return the set as a checked witness, and claim it is maximum only after a complete search or a separately verified upper bound. A clique can be structurally complete without representing a real social group, shared identity or collaboration.

## Inputs to collect
1. **Graph snapshot** — obtain a named revision, explicit node IDs including isolates, and uniquely identified edge records. Why: omitted vertices or links can change the maximum. Default: none; no whole-snapshot claim from an incomplete inventory.
2. **Projection policy** — confirm undirected interpretation, relation filters and time boundary. Why: direction or excluded relationships change adjacency. Default: ask before discarding arrows.
3. **Loop and parallel policy** — state whether self-loops and parallel records contribute to adjacency between distinct vertices. Why: a clique is defined here by distinct-pair adjacency. Default: ignore loops for clique membership and collapse parallel endpoint records to one adjacency, while preserving all source IDs in the ledger.
4. **Search budget** — obtain a positive integer count of candidate subsets that may be examined. Why: exact search may be expensive. Default: propose a small rehearsal, but do not execute until the owner supplies a limit.
5. **Claim purpose** — identify whether a witness, inclusion-maximal set or proven maximum is needed. Why: these are different claims. Default: return the best witnessed clique and an explicit completeness verdict.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the snapshot, projection and candidate-subset budget together.
2. Validate node and edge IDs, tuple shapes and endpoint membership before building adjacency; preserve rejected records as exceptions.
3. Build undirected distinct-pair adjacency sets; keep loop and parallel edge IDs in the source ledger without multiplying adjacency.
4. Enumerate node subsets in descending size and deterministic identifier order, counting every tested subset against the budget.
5. Test each subset by checking every distinct pair against the adjacency sets.
6. Retain the largest valid clique encountered, including the empty set as a valid lower-bound witness.
7. ⚠️ If the budget interrupts enumeration, report **unknown maximum** and the witnessed lower bound. Do not call a witnessed clique maximum merely because no larger one has yet appeared.
8. If every subset was tested, report the largest witnessed clique as a proven maximum within the supplied graph projection.
9. Independently check every pair of the reported witness against the original edge records. For a completed maximum claim, enumerate possible larger sets by a separate method or check an independently established upper bound.
10. Distinguish **inclusion-maximal** from **maximum**: an inclusion-maximal clique cannot add one outside vertex, while a maximum clique has the greatest possible size. Check the first property separately if the user asks for it.
11. Report tested count, completion status, witness, source policy and limits. Keep any business interpretation outside the structural result.

The Python 3 reference below uses small, already materialized finite graphs. Nodes are nonempty string IDs; edge records are tuple/list triples `(edge_id, endpoint_a, endpoint_b)` of nonempty strings. It checks those shapes before projection. Execute the complete snippet in an available Python 3 interpreter and record the observed version; no runtime-scale promise follows from this example.

```python
from itertools import combinations

def adjacency(nodes, edges):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    adj = {n: set() for n in nodes}
    seen = set()
    for e in edges:
        if type(e) not in (tuple, list) or len(e) != 3 or any(
                type(x) is not str or not x for x in e):
            raise ValueError("invalid edge record")
        eid, a, b = e
        if eid in seen or a not in adj or b not in adj:
            raise ValueError("duplicate edge ID or unknown endpoint")
        seen.add(eid)
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    return adj

def is_clique(group, adj):
    return all(b in adj[a] for a, b in combinations(group, 2))

def search(nodes, edges, budget):
    if type(budget) is not int or budget < 1:
        raise ValueError("positive integer budget required")
    adj = adjacency(nodes, edges)
    order = sorted(nodes)
    best, tested = (), 0
    for size in range(len(order), -1, -1):
        for group in combinations(order, size):
            if tested >= budget:
                return "unknown", best, tested
            tested += 1
            if is_clique(group, adj) and len(group) > len(best):
                best = group
    return "maximum", best, tested

def verify(nodes, edges, result):
    adj = adjacency(nodes, edges)
    verdict, best, tested = result
    n = len(nodes)
    if (verdict not in ("maximum", "unknown") or
            type(tested) is not int or tested < 1 or tested > 2**n or
            type(best) is not tuple or len(set(best)) != len(best) or
            any(v not in adj for v in best) or not is_clique(best, adj)):
        return False
    if verdict == "unknown":
        return tested < 2**n
    if tested != 2**n:
        return False
    order = sorted(nodes)
    return not any(is_clique(group, adj)
                   for size in range(len(best)+1, n+1)
                   for group in combinations(order, size))

nodes = ["A", "B", "C", "D", "I"]
edges = [("ab", "A", "B"), ("bc", "B", "C"),
         ("ca", "C", "A"), ("cd", "C", "D"),
         ("ab2", "A", "B"), ("loop", "I", "I")]
complete = search(nodes, edges, 32)
assert complete == ("maximum", ("A", "B", "C"), 32)
assert verify(nodes, edges, complete)
partial = search(nodes, edges, 1)
assert partial[0] == "unknown" and verify(nodes, edges, partial)
assert not verify(nodes, edges, ("maximum", ("C", "D"), 32))
assert search([], [], 1) == ("maximum", (), 1)
try:
    search(["A", "B"], ["xab"], 4)
except ValueError:
    pass
else:
    raise AssertionError("string edge record accepted")
print("bounded clique witness and completed maximum checked")
```

The verifier proves witness validity and, for a completed claim, absence of a larger clique by a separate larger-subset pass. It does not certify that an arbitrary `unknown` result faithfully represents the exact search prefix; it only checks the witness and that the reported count is incomplete. Preserve the execution trace if prefix fidelity matters. The completed pass is deliberately exhaustive and suitable only for a bounded inventory.

## Decision rules
- IF a returned witness lacks any distinct-pair edge THEN reject it BECAUSE the clique definition is violated.
- IF the search stops before all subsets are examined THEN report the maximum as unknown BECAUSE unseen subsets may be larger.
- IF a valid clique cannot add any outside vertex THEN it is inclusion-maximal, not necessarily maximum, BECAUSE another region may contain a larger clique.
- IF all subsets were checked and no larger clique exists THEN label the witness maximum for that frozen projection BECAUSE every candidate size has been covered.
- IF direction or scope is unresolved THEN request the contract BECAUSE a different projection changes the candidate groups.

## Output template
```text
Scope: <revision, undirected projection and coverage; maximum 70 words>
Adjacency policy: <parallel, loop and filter treatment>
Search: <candidate subsets tested, budget, complete or cutoff>
Verdict: <maximum proven / maximum unknown / unresolved>
Clique witness: <all node IDs and size; or pending>
Verification: <all-pair replay and larger-set check executed/pending>
Limits: <excluded records, semantics and scale; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Node inventory includes isolates and a frozen revision.
- [ ] Direction and relation projection are explicit.
- [ ] All edge IDs and endpoint records pass validation.
- [ ] Parallel and loop treatment is recorded.
- [ ] Every pair in the reported witness has a source-supported adjacency.
- [ ] The subset count and cutoff are recorded without exaggeration.
- [ ] A maximum label has a complete search or independent upper-bound proof.
- [ ] No structural clique is called a real-world social group without separate evidence.

## Anti-patterns
- **Largest seen equals maximum**: treat a partial search result as proven. Fix: state unknown until a complete exclusion argument exists.
- **Maximal equals maximum**: check only whether one node can be added. Fix: inspect larger sets elsewhere.
- **Parallel inflation**: count repeated A/B records as separate neighboring vertices. Fix: retain IDs but collapse pair adjacency under this policy.
- **Loop membership**: use an A/A loop to fill a missing A/B link. Fix: test distinct pairs only.
- **Count-only certificate**: accept a reported size without pair witnesses. Fix: replay all pairs against the source inventory.

## Worked example
**Input:** Fictional Cedar exercise C1 supplies nodes A/B/C/D/I, undirected edges ab,bc,ca,cd, a parallel A/B record ab2 and a loop at I. The inventory is complete for this exercise. Use the reference policy and budget 32 subsets.

**Output:**
```text
Scope: Fictional Cedar C1; five inventoried nodes; complete undirected exercise projection.
Adjacency policy: Parallel ab/ab2 yield one A/B adjacency; I loop contributes no distinct-pair adjacency.
Search: 32 candidate subsets tested of budget 32; complete.
Verdict: Maximum proven.
Clique witness: A,B,C; size 3.
Verification: Each of AB, AC and BC has an edge; independent larger-set check found no clique of size 4 or 5.
Limits: I is isolated for clique purposes; no real-world group or importance inference.
Next action: Graph owner checks source completeness before using this structural result elsewhere.
```

**Bad output:** “A,B,C is the largest possible because no fourth vertex can be attached to it after one check.”
That shows at most inclusion-maximality for this set; it does not rule out a larger clique elsewhere.

## Edge cases
- **Empty graph**: the empty set is a maximum clique of size zero after its single subset is tested.
- **Edgeless nonempty graph**: any singleton is a maximum clique; the deterministic order selects the first one.
- **Parallel edges**: retain each ID in the source ledger but count the endpoint pair once.
- **Self-loop**: ignore it for adjacency between distinct vertices; preserve its record.
- **Cutoff**: return the best valid witness as a lower bound and leave maximum unknown.
- **Partial snapshot**: limit the conclusion to inventoried nodes and selected records.

## Test case
**Input:**
> Fictional graph has triangle A/B/C, tail C/D, isolated I, a second A/B edge and a loop at I. Use the declared undirected policy. First search one subset, then allow all 32 subsets.

**Assertions:**
1. The one-subset run reports unknown maximum and does not claim the first witnessed group is maximum.
2. The complete run reports A/B/C as a size-three maximum clique.
3. The result counts parallel A/B as one adjacency and ignores I's loop for distinct-pair adjacency.
4. The completed certificate checks all witness pairs and rules out every larger group.
5. The response makes no claim that the clique is a real-world social group.
