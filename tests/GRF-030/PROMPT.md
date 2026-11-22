Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-030
name: relation-sequence-graph-path-search
domain: Graph Engineering Foundations
subdomain: Stateful relation path matching
version: 1.0
description: Find endpoint witnesses accepted by a supplied relation-state contract when relationship order determines whether a graph walk qualifies.
triggers: ["find paths matching relation order", "search graph with relation states", "allow node revisit at another rule state", "explain accepted graph path witnesses", "check cyclic relation pattern termination"]
not_for: ["plain bounded reachability [GRF-006]", "query plan optimization [GRF-015]", "enumerating every accepted walk", "simple-path matching without repeated nodes", "parsing an arbitrary regular expression"]
requires: []
risk_level: medium
---

# Relation Sequence Graph Path Search

## Purpose
Find endpoints reached by walks whose relation labels follow an explicit finite transition contract. Return one reproducible edge witness for each accepted endpoint and expose the rule states that make it valid. This establishes acceptance in the supplied graph and rule system, not a new domain fact implied by connectivity.

## Inputs to collect
1. **Graph snapshot** — obtain node inventory, unique edge IDs, directed endpoints and relation labels. Why: witnesses must identify actual edges in one snapshot. Default: supplied snapshot only; external completeness unknown.
2. **Seed identity** — obtain the exact starting node. Why: an ambiguous label can initiate the wrong search. Default: ask; never select a name match silently.
3. **Finite rule contract** — obtain named states, start state, accepting states and transitions keyed by state and relation. Why: allowed labels alone do not encode order. Default: missing rules block execution; no invented pattern.
4. **Walk meaning** — confirm that repeated nodes and edges are permitted and that each transition consumes one outgoing edge. Why: product-state search does not enforce simple paths. Default: propose these semantics for approval, without claiming execution.
5. **Depth and operational bounds** — obtain a nonnegative maximum edge count and any execution budget. Why: a truncated search cannot prove unrestricted absence. Default: ask for depth; interrupted runs remain incomplete.
6. **Evidence requirement** — clarify endpoint existence versus all walks and rule-state variants. Why: a finite visited table suppresses redundant walks. Default: one witness per accepted endpoint, with complete reached state-pair evidence.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the graph revision and approved transition contract together.
2. Validate graph identities and endpoints before building outgoing adjacency.
3. Validate every transition's source and destination state and reject conflicting transitions for the same state/label key.
4. Initialize the search at the pair consisting of the seed node and start rule state with an empty witness.
5. Inspect outgoing graph edges against transitions enabled in the current rule state.
6. ⚠️ Record discovery by node-and-rule-state pair rather than node alone, preserving revisits that have different future acceptance possibilities.
7. Process newly reached pairs in increasing edge count and retain their predecessor pair and edge ID.
8. Stop expanding pairs at the approved depth while preserving evidence of enabled exits into undiscovered pairs.
9. Select accepting reached pairs and reconstruct one minimum-edge witness per endpoint with deterministic tie handling.
10. Replay each witness through both the graph and transition contract, checking endpoint continuity and final acceptance.
11. Report bounded completion separately from exhausted product-state reachability and operational interruption.
12. Deliver accepted endpoints and rejection boundaries without interpreting omitted or unobserved edges as global impossibility.

This Python 3 reference uses finite in-memory inputs, outgoing edges and deterministic transitions supplied as rows `(state, label, next_state)`. Every transition consumes exactly one graph edge; there are no empty transitions. Repeated graph nodes and edges are allowed. Prevalidate string IDs and tuple shapes. Execute the complete snippet and record the interpreter version. A separate operational interruption requires an incomplete status even if the configured depth is known.

```python
from collections import deque

def match(nodes, edges, seed, states, start, accept, rules, depth):
    if type(depth) is not int or depth < 0:
        raise ValueError("explicit nonnegative depth required")
    if len(set(nodes)) != len(nodes) or seed not in nodes:
        raise ValueError("invalid inventory or seed")
    if len(set(states)) != len(states) or start not in states or not set(accept) <= set(states):
        raise ValueError("invalid rule states")
    transition = {}
    for state, label, nxt in rules:
        if state not in states or nxt not in states or (state, label) in transition:
            raise ValueError("invalid or duplicate transition key")
        transition[state, label] = nxt
    adj = {n: [] for n in nodes}
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    for eid, s, o, label in sorted(edges):
        if s not in adj or o not in adj:
            raise ValueError("unknown endpoint")
        adj[s].append((eid, o, label))
    initial = (seed, start)
    distance, paths = {initial: 0}, {initial: ()}
    queue = deque([initial])
    while queue:
        node, state = queue.popleft()
        if distance[node, state] == depth:
            continue
        for eid, target, label in adj[node]:
            if (state, label) not in transition:
                continue
            pair = (target, transition[state, label])
            if pair not in distance:
                distance[pair] = distance[node, state] + 1
                paths[pair] = paths[node, state] + (eid,)
                queue.append(pair)
    accepted = {}
    for pair in sorted(distance, key=lambda k: (distance[k], k)):
        node, state = pair
        if state in accept:
            accepted.setdefault(node, (state, paths[pair]))
    exits = []
    for (node, state), d in sorted(distance.items()):
        if d == depth:
            for eid, target, label in adj[node]:
                if (state, label) in transition:
                    pair = (target, transition[state, label])
                    if pair not in distance:
                        exits.append(((node, state), eid, pair))
    return distance, accepted, exits

nodes = ["A", "B", "C"]
edges = [("e1", "A", "B", "out"), ("e2", "B", "A", "back"),
         ("e3", "A", "C", "finish")]
states = ["s0", "s1", "s2", "done"]
rules = [("s0", "out", "s1"), ("s1", "back", "s2"),
         ("s2", "finish", "done")]
d, accepted, exits = match(nodes, edges, "A", states, "s0", {"done"}, rules, 3)
assert accepted == {"C": ("done", ("e1", "e2", "e3"))}
assert ("A", "s0") in d and ("A", "s2") in d
assert exits == []
assert match(nodes, edges, "A", states, "s0", {"done"}, rules, 1)[1] == {}
assert match(nodes, edges, "A", states, "s0", {"s0"}, rules, 0)[1] == {"A": ("s0", ())}
print("ordered relation witness and distinct-state revisit checked")
```

Finite node/state pairs bound the visited inventory, so cycles cannot cause unlimited expansion in this reference. Discovering a pair by a longer walk cannot add a new acceptance possibility under this history-independent transition contract and maximum-depth rule. This reasoning does not extend to exact-length queries, path uniqueness constraints or rules depending on unrecorded history. A boundary exit proves another product state is omitted, not that an additional accepted endpoint necessarily exists.

## Decision rules
- IF the same graph node appears in a different rule state THEN explore it separately BECAUSE enabled transitions and acceptance can differ.
- IF the start state accepts THEN include the seed's empty witness BECAUSE zero consumed edges satisfy that supplied contract.
- IF a relation lacks an enabled transition THEN reject that step BECAUSE label membership elsewhere in the rule graph does not authorize it here.
- IF a boundary exit exists THEN report depth-limited state exploration BECAUSE further rule-state pairs remain reachable, without claiming they accept.
- IF the request requires simple paths or exact length THEN stop and redesign the state model BECAUSE this existence search merges histories that those requirements distinguish.

## Output template
```text
Scope: <snapshot, seed, coverage; maximum 60 words>
Rule contract: <states, start, accepting states, transitions, walk meaning and depth>
Accepted: <endpoint | final state | edge witness; complete table or none>
State evidence: <reached node/state pairs with minimum depth>
Boundary: <enabled unseen-pair exits or none; completion/interruption>
Verification: <witness replay and reference checks executed/pending>
Limits: <coverage, unsupported semantics and inference limits; maximum 80 words>
```

## Quality checklist
- [ ] Transitions specify order rather than only allowed labels.
- [ ] Visited keys contain graph node and rule state.
- [ ] Every accepted witness ends in an accepting state.
- [ ] Empty-walk acceptance follows the supplied start state.
- [ ] Graph edge direction and rule transitions both replay correctly.
- [ ] Depth boundaries are separated from operational interruptions.
- [ ] One-witness output is not described as every accepted walk.
- [ ] Global absence and domain inference claims remain bounded.

## Anti-patterns
- **Node-only visited set**: suppress a valid return in another state. Fix: use product-state discovery.
- **Any-order labels**: accept finish before out/back. Fix: replay transitions in order.
- **Cycle prohibition**: reject all repeated nodes despite walk semantics. Fix: distinguish node revisits from repeated product-state expansion.
- **All-path inflation**: present one witness as an exhaustive path list. Fix: state endpoint-existence scope.
- **Boundary optimism**: infer an accepting result beyond the limit. Fix: report only the witnessed unseen-state exit.

## Worked example
**Input:** Fictional graph and rule rows from the snippet; seed A; outgoing walks may repeat nodes; maximum three edges; one endpoint witness requested.

**Output:**
```text
Scope: Fictional F1; seed A; complete supplied fixture only.
Rule contract: s0,out->s1; s1,back->s2; s2,finish->done; start s0; accept done; outgoing walks; depth 3.
Accepted: C | done | e1,e2,e3.
State evidence: A/s0=0; B/s1=1; A/s2=2; C/done=3.
Boundary: No enabled unseen-pair exits; reference can exhaust this product-state region when executed.
Verification: Replay A-e1-B-e2-A-e3-C and s0-s1-s2-done; reference assertions supplied, execution must be recorded separately.
Limits: Direct e3 at s0 is rejected; one witness per endpoint, no all-walk enumeration or real-world inference.
```

**Bad output:** “A was visited initially, so stop when e2 returns to A; no match exists.”
This discards A/s2 and loses its enabled finish transition.

## Edge cases
- **Accepting seed with no edges**: return the empty witness when the start state accepts.
- **Rule cycle and graph cycle**: expand each product pair once and retain finite witness evidence.
- **Parallel edges**: preserve IDs; deterministic selection returns one witness, not multiplicity.
- **Unknown seed or state**: reject invalid input before reporting no matches.
- **Partial adjacency**: report observed matches but withhold exhaustive absence claims.

## Test case
**Input:**
> Fictional A-out-B-back-A-finish-C must match out,back,finish in order. A is revisited, and a direct finish edge also exists. Explain acceptance under depth three.

**Assertions:**
1. Retains A at its initial and post-back rule states.
2. Returns e1/e2/e3 or the supplied equivalent edge-ID witness ending at C.
3. Rejects direct finish from the initial state.
4. Does not claim every accepted walk was enumerated.
</skill>

<user_request>
Fictional A-out-B-back-A-finish-C must match out,back,finish in order. A is revisited, and a direct finish edge also exists. Explain acceptance under depth three.
</user_request>
