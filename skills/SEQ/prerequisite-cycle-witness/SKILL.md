---
id: SEQ-001
name: prerequisite-cycle-witness
domain: Dependency Schedule Computation
subdomain: Graph consistency
version: 1.0
description: Produce an explicit closed dependency path when a prerequisite graph cannot support a completion order.
triggers: ["find the exact dependency cycle", "show why these tasks cannot be ordered", "validate a prerequisite graph", "return a circular dependency witness", "check a proposed dependency repair"]
not_for: ["negotiating initiative scope [BPL-002]", "choosing resource capacity", "checking pipeline artifact completion [TDE-008]"]
requires: []
risk_level: medium
---

# Prerequisite Cycle Witness

## Purpose
Turn a supplied prerequisite graph into either a complete prerequisite-first order or a concrete closed path explaining a cycle. Keep graph evidence separate from the business decision to remove an edge; detecting a contradiction does not establish which dependency is unnecessary.

## Inputs to collect
1. **Task identities** — obtain stable unique identifiers and the scoped graph revision. This prevents similarly named activities from being merged. Default: none; the task universe is required.
2. **Prerequisite edges** — collect direct prerequisite identifiers for each task. This defines the graph being checked. Default: no omitted list is interpreted as evidence of no prerequisites; obtain explicit empty lists for roots.
3. **Edge meaning** — confirm that each listed edge requires its predecessor to complete before the dependent task can complete. This distinguishes actual dependency from preference. Default: uncertain edges remain proposed and findings conditional.
4. **External dependencies** — establish whether external work is represented as explicit nodes or outside the model. Default: reject unknown identifiers rather than silently inserting finished tasks.
5. **Repair authority** — identify who can change an edge and what evidence supports a correction. Default: read-only diagnosis; no deletion or schedule commitment.

If a required input is missing and has no safe default, ask in one message with at most three questions. Group task scope, edge semantics and external-node handling into those requests.

## Procedure
1. Freeze the task and edge snapshot with a declared direction convention: each task lists its prerequisites. In the returned witness, each next item is a prerequisite of the preceding item.
2. Validate that every referenced identifier exists in the declared task universe. ⚠️ An unknown prerequisite is an input gap, not a root that can be assumed complete.
3. Separate hard prerequisites from uncertain or preferred ordering edges. Run different explicitly labeled scenarios if their inclusion changes the question; do not quietly discard inconvenient edges.
4. Traverse the graph while tracking the currently active path and the fully finished nodes. Revisiting an active node identifies a closed path; revisiting a finished node does not by itself establish a cycle.
5. Extract a witness beginning and ending at the same identifier. Check every consecutive pair against the supplied adjacency relation before reporting the result.
6. If no cycle is found, return a prerequisite-first order covering every task exactly once. Verify each prerequisite appears before its dependent task; independent tasks may have several valid orders.
7. Route the witness to the edge owners with the originating evidence. Ask whether a task split, intermediate artifact or incorrectly modeled edge resolves the contradiction; do not prescribe an unsupported removal.
8. Re-run the whole scoped graph after any approved correction. A single removed cycle does not prove another disconnected cycle is absent.

This Python 3 reference uses dictionaries of string identifiers to sets of prerequisite identifiers. It returns one deterministic witness rather than enumerating every cycle. Its recursive traversal is suitable for small supplied graphs; very deep graphs require an iterative implementation or a graph tool with tested traversal behavior, not arbitrary recursion-limit changes. Run the complete snippet and record the actual interpreter used.

```python
def diagnose(pred):
    if any(p not in pred for ps in pred.values() for p in ps):
        raise ValueError("unknown prerequisite")
    active, finished, order = [], set(), []

    def visit(task):
        if task in active:
            return active[active.index(task):] + [task]
        if task in finished:
            return None
        active.append(task)
        for prerequisite in sorted(pred[task]):
            witness = visit(prerequisite)
            if witness:
                return witness
        active.pop()
        finished.add(task)
        order.append(task)
        return None

    for task in sorted(pred):
        witness = visit(task)
        if witness:
            assert all(b in pred[a] for a, b in zip(witness, witness[1:]))
            return {"cycle": witness, "order": None}
    positions = {task: i for i, task in enumerate(order)}
    assert all(positions[p] < positions[t] for t in pred for p in pred[t])
    return {"cycle": None, "order": order}

graph = {"A": {"B"}, "B": {"C"}, "C": {"A"}, "D": set()}
assert diagnose(graph) == {"cycle": ["A", "B", "C", "A"], "order": None}
fixed = {"A": {"B"}, "B": {"C"}, "C": set(), "D": set()}
assert diagnose(fixed)["order"] == ["C", "B", "A", "D"]
assert diagnose({"A": {"A"}})["cycle"] == ["A", "A"]
assert diagnose({}) == {"cycle": None, "order": []}
try:
    diagnose({"A": {"missing"}})
except ValueError:
    pass
else:
    raise AssertionError("unknown prerequisite accepted")
print("cycle witness checks passed")
```

## Decision rules
- IF a reference names an undeclared task THEN stop the graph verdict and request its scope BECAUSE silently inserting a node changes the model.
- IF traversal revisits a currently active node THEN return the closed path BECAUSE those edges provide a checkable circular prerequisite witness.
- IF a node was already fully processed THEN reuse its finished state BECAUSE shared prerequisites are not necessarily cycles.
- IF one witness is repaired THEN check the full graph again BECAUSE other cycles may remain outside that witness.
- IF the graph is acyclic THEN describe the result as structural orderability BECAUSE resource availability and actual completion evidence remain separate.

## Output template
```text
Graph scope: <revision, nodes and edge meaning; up to three lines>
Input exceptions: <up to five missing or uncertain items, or None>
Result: <cycle found / acyclic / unresolved input>
Witness or order: <exact identifiers; attach full list if longer than twelve>
Edge evidence: <one line per witness edge with supplied source, or order checks>
Repair handoff: <up to three owner decisions; no unauthorized edge deletion>
Verification limit: <executed graph checks and untested operational conditions; two sentences>
```

## Quality checklist
- [ ] Task identifiers are unique within the declared scope.
- [ ] Every prerequisite refers to a declared node.
- [ ] Edge direction is explained for the returned path.
- [ ] A cycle witness repeats its starting node at the end.
- [ ] Every witness step exists in the input relation.
- [ ] An acyclic order contains every node exactly once.
- [ ] Proposed repairs retain their required owner decision.
- [ ] Graph success is not described as capacity or delivery assurance.

## Anti-patterns
- **Unknown means finished**: an absent node is inserted as a completed prerequisite. Fix: resolve the graph boundary first.
- **Shared ancestor panic**: repeated reachability is called a cycle. Fix: distinguish active and finished traversal states.
- **Broken witness**: a list of suspicious tasks has no verified closing edge. Fix: check each consecutive relation and closure.
- **Convenient edge deletion**: the algorithm drops whichever edge reveals the loop. Fix: preserve the evidence and ask the authorized owner to resolve meaning.

## Worked example
**Input:**
> Fictional workshop Elm supplies graph G: A needs B, B needs C, C needs A, and D has no prerequisites. All are confirmed completion prerequisites. Owners have not approved any changes. Execute the reference diagnosis.

**Output:**
```text
Graph scope: Elm G; A, B, C and D; each adjacency entry lists completion prerequisites.
Input exceptions: None.
Result: cycle found.
Witness or order: A -> B -> C -> A; each arrow means needs, not chronological execution.
Edge evidence: G lists B for A, C for B and A for C; all witness edges verified.
Repair handoff: Owners of A/B/C must resolve a prerequisite or staged deliverable; D has no part in this witness. No edge removed.
Verification limit: Reference graph checks executed for G. Resource capacity, durations and real task completion were not checked.
```

**Bad output:** “Delete C needs A and schedule everything; the algorithm found the bad dependency.”
This chooses a business correction without evidence and confuses finding a cycle with identifying an invalid edge.

## Edge cases
- **Self-dependency**: return the two-item closed witness and ask whether the node represents multiple stages that need separate identities.
- **Disconnected components**: inspect all components; an acyclic first component cannot justify a whole-graph verdict.
- **Duplicate listed edges**: normalize exact duplicates for traversal while retaining their source records for review.
- **Uncertain dependency**: label the scenario containing it as conditional and compare it with an explicitly authorized alternative graph.

## Test case
**Input:**
> Fictional graph has A needing C and B needing C, with C needing nothing. A separate X needs Y and Y needs X. Return a witness without blaming the shared C prerequisite.

**Assertions:**
1. Returns X -> Y -> X or its rotated equivalent.
2. Verifies each edge in the closed witness.
3. Does not label the shared C prerequisite cyclic.
4. Does not remove an edge or claim an operational schedule is approved.
