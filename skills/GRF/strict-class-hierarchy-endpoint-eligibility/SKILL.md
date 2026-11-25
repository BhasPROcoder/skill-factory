---
id: GRF-053
name: strict-class-hierarchy-endpoint-eligibility
domain: Graph Engineering Foundations
subdomain: Inherited endpoint eligibility
version: 1.0
description: Check identified graph assertions against declared predicate endpoint classes through a strict subclass hierarchy, with subtype witnesses and completeness-aware findings.
triggers: ["validate inherited graph endpoint types", "check subclass eligibility for relationships", "explain why a graph assertion passes type rules", "audit an untyped graph endpoint", "find a class hierarchy cycle before validating edges"]
not_for: ["designing graph entity types [GRF-001]", "governing relation meanings or general inference [GRF-018]", "checking relationship value counts [GRF-020]", "task prerequisite ordering [SEQ-001]"]
requires: []
risk_level: medium
---

# Strict Class Hierarchy Endpoint Eligibility

## Purpose
Check assertion endpoints against an approved predicate contract with strict subclass inheritance. Show link-ID eligibility paths and distinguish invalid from incomplete typing. This structural check does not prove source truth or external ontology conformance.

## Inputs to collect
1. **Frozen contract** — obtain snapshot, vocabulary revision, classes and the owner's strict-specialization declaration. Why: other hierarchy meanings differ. Default: stop without this declaration.
2. **Class links** — obtain identified child/parent records. Why: inheritance needs replayable evidence. Default: no undeclared parent.
3. **Node types** — obtain each node's direct classes and type-inventory completeness. Why: incompatible means invalid only with complete typing. Default: incomplete.
4. **Predicate contract** — obtain one directed predicate and required endpoint classes. Why: roles differ. Default: no inferred inverse.
5. **Assertions** — obtain identified source/target nodes. Why: each edge needs a finding. Default: hold malformed IDs.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze class, node, predicate and edge inventories under one revision.
2. Validate IDs, classes, nodes and record shapes; reject string-shaped records.
3. Confirm strict specialization; stop with a link-ID witness on any class cycle.
4. Search upward from each direct endpoint type, including zero-link identity eligibility.
5. Retain one continuous link-ID path. ⚠️ Never invent a type to pass validation.
6. Mark unmatched endpoints invalid with complete typing, otherwise unresolved.
7. Mark edges valid when both endpoints qualify, invalid when either fails, otherwise unresolved.
8. Independently compute reflexive transitive subclass closure and compare endpoint states.
9. Replay path IDs for start, direction, continuity and required end class.
10. Deliver per-edge findings and coverage limits; leave source correction to owners.

This Python 3 in-memory reference uses directed `(link_ID, child, parent)` records, direct node types and one predicate. A separate closure verifier checks paths. Run it and record the interpreter version. It excludes equivalence, disjointness and storage writes.

```python
from collections import deque

def upward(start, target, links):
    if start == target:
        return ()
    adj = {}
    for rid, child, parent in links:
        adj.setdefault(child, []).append((rid, parent))
    seen, todo = {start}, deque([(start, ())])
    while todo:
        at, path = todo.popleft()
        for rid, parent in sorted(adj.get(at, [])):
            next_path = path + (rid,)
            if parent == target:
                return next_path
            if parent not in seen:
                seen.add(parent)
                todo.append((parent, next_path))
    return None

def check_input(classes, links, node_types, complete, predicate, domain, range_, edges):
    if any(type(x) not in (list, tuple) for x in (classes, links, edges)):
        raise ValueError("invalid inventory shape")
    if any(type(c) is not str or not c for c in classes) or len(set(classes)) != len(classes):
        raise ValueError("invalid classes")
    known, link_ids = set(classes), set()
    for row in links:
        if type(row) not in (list, tuple) or len(row) != 3:
            raise ValueError("invalid class link")
        rid, child, parent = row
        if any(type(x) is not str or not x for x in row):
            raise ValueError("invalid class field")
        if rid in link_ids or child not in known or parent not in known:
            raise ValueError("duplicate link ID or unknown class")
        link_ids.add(rid)
    if type(node_types) is not dict or type(complete) is not dict:
        raise ValueError("invalid node inventory")
    if set(node_types) != set(complete):
        raise ValueError("missing completeness flag")
    for node, direct in node_types.items():
        if type(node) is not str or not node or type(direct) not in (list, tuple):
            raise ValueError("invalid node type list")
        if any(type(t) is not str or t not in known for t in direct) or len(set(direct)) != len(direct):
            raise ValueError("invalid direct type")
        if type(complete[node]) is not bool:
            raise ValueError("invalid completeness flag")
    if any(type(x) is not str or x not in known for x in (domain, range_)):
        raise ValueError("unknown required class")
    if type(predicate) is not str or not predicate:
        raise ValueError("invalid predicate")
    edge_ids = set()
    for row in edges:
        if type(row) not in (list, tuple) or len(row) != 4:
            raise ValueError("invalid assertion record")
        rid, s, p, o = row
        if any(type(x) is not str or not x for x in row):
            raise ValueError("invalid assertion field")
        if rid in edge_ids or s not in node_types or o not in node_types or p != predicate:
            raise ValueError("duplicate edge ID, endpoint or predicate mismatch")
        edge_ids.add(rid)
    for rid, child, parent in links:
        path = upward(parent, child, links)
        if path is not None:
            raise ValueError("strict hierarchy cycle: " + ",".join((rid,) + path))

def endpoint(node, needed, links, node_types, complete):
    for direct in sorted(node_types[node]):
        path = upward(direct, needed, links)
        if path is not None:
            return ("eligible", direct, path)
    return ("invalid" if complete[node] else "unresolved", None, None)

def inspect(classes, links, node_types, complete, predicate, domain, range_, edges):
    check_input(classes, links, node_types, complete, predicate, domain, range_, edges)
    result = {}
    for rid, s, p, o in edges:
        left = endpoint(s, domain, links, node_types, complete)
        right = endpoint(o, range_, links, node_types, complete)
        status = ("valid" if left[0] == right[0] == "eligible" else
                  "invalid" if "invalid" in (left[0], right[0]) else "unresolved")
        result[rid] = (status, left, right)
    verify(classes, links, node_types, complete, domain, range_, edges, result)
    return result

def verify(classes, links, node_types, complete, domain, range_, edges, result):
    closure = {(c, c) for c in classes} | {(a, b) for _, a, b in links}
    while True:
        more = closure | {(a, d) for a, b in closure for c, d in closure if b == c}
        if more == closure:
            break
        closure = more
    by_id = {rid: (a, b) for rid, a, b in links}
    if set(result) != {rid for rid, _, _, _ in edges}:
        raise ValueError("missing assertion finding")
    for rid, s, p, o in edges:
        status, left, right = result[rid]
        for node, needed, finding in ((s, domain, left), (o, range_, right)):
            possible = any((t, needed) in closure for t in node_types[node])
            expected = "eligible" if possible else "invalid" if complete[node] else "unresolved"
            if finding[0] != expected:
                raise ValueError("endpoint state mismatch")
            if possible:
                _, direct, path = finding
                if direct not in node_types[node] or type(path) not in (tuple, list):
                    raise ValueError("invalid subtype witness")
                at = direct
                for link_id in path:
                    if link_id not in by_id or by_id[link_id][0] != at:
                        raise ValueError("broken subtype witness")
                    at = by_id[link_id][1]
                if at != needed:
                    raise ValueError("wrong subtype target")
            elif finding[1:] != (None, None):
                raise ValueError("unsupported witness")
        expected_status = ("valid" if left[0] == right[0] == "eligible" else
                           "invalid" if "invalid" in (left[0], right[0]) else "unresolved")
        if status != expected_status:
            raise ValueError("assertion status mismatch")
    return True

classes = ["Entity", "Person", "Employee", "Engineer", "Organization"]
links = [("h1", "Engineer", "Employee"), ("h2", "Employee", "Person"),
         ("h3", "Person", "Entity"), ("h4", "Organization", "Entity")]
types = {"Ada": ["Engineer"], "Bo": ["Employee"], "Co": ["Organization"], "Lee": []}
complete = {"Ada": True, "Bo": True, "Co": True, "Lee": False}
edges = [("e1", "Ada", "mentors", "Bo"),
         ("e2", "Co", "mentors", "Bo"), ("e3", "Ada", "mentors", "Lee")]
out = inspect(classes, links, types, complete, "mentors", "Person", "Person", edges)
assert [out[e][0] for e in ("e1", "e2", "e3")] == ["valid", "invalid", "unresolved"]
assert out["e1"][1] == ("eligible", "Engineer", ("h1", "h2"))
assert out["e1"][2] == ("eligible", "Employee", ("h2",))
assert out["e2"][1][0] == "invalid" and out["e3"][2][0] == "unresolved"
print("subtype paths, invalid and unresolved endpoints checked")
```

## Decision rules
- IF strict specialization is undeclared THEN stop BECAUSE hierarchy semantics may differ.
- IF strict links cycle THEN show the link-ID cycle and stop BECAUSE the DAG contract fails.
- IF an endpoint has a replayable subtype path THEN mark eligible BECAUSE its direct type reaches the requirement.
- IF no path exists and typing is complete THEN mark invalid BECAUSE declared types cannot qualify.
- IF no path exists and typing is incomplete THEN mark unresolved BECAUSE another type may qualify.

## Output template
```text
Scope: <snapshot, vocabulary revision, strict-hierarchy declaration; max 60 words>
Hierarchy: <valid DAG or cycle class/link-ID witness>
Predicate contract: <predicate | subject class | object class>
Assertions: <edge ID | status | subject state/type/path | object state/type/path>
Independent checks: <closure parity and path replay, or pending>
Coverage: <per-node type-completeness exceptions>
Limits: <source and semantic limits; max 60 words>
Next action: <owner review or missing-input request>
```

## Quality checklist
- [ ] Strict-specialization meaning and revision are explicit.
- [ ] Class-link IDs, node IDs and assertion IDs are validated.
- [ ] A cycle blocks classification with an exact link-ID witness.
- [ ] Every eligible endpoint has a continuous subtype path or zero-link identity witness.
- [ ] Invalidity uses that node's complete type inventory.
- [ ] Unresolved endpoints are not silently assigned a required class.
- [ ] Independent closure agrees with each endpoint state.

## Anti-patterns
- **Exact-type-only check**: rejecting Engineer because the requirement says Person. Fix: search the approved subclass links upward.
- **Invented type**: assigning Person to an untyped node. Fix: report unresolved when coverage is incomplete.
- **Cycle acceptance**: treating a strict subclass cycle as harmless equivalence. Fix: stop with its edge-ID witness.
- **Path without IDs**: saying an endpoint inherits eligibility with no replayable links. Fix: list and check class-link IDs.

## Worked example
**Input:** Fictional C1 contains the reference's five classes, four links, four nodes and three `mentors` assertions. Both roles require Person. Ada, Bo and Co have complete types; Lee does not.

**Output:**
```text
Scope: Fictional C1; approved strict subclass links h1–h4; fixed vocabulary revision for this exercise.
Hierarchy: Valid DAG; no cycle in supplied links.
Predicate contract: mentors | Person | Person.
Assertions: e1 | valid | Ada eligible Engineer h1,h2 | Bo eligible Employee h2; e2 | invalid | Co invalid Organization no Person path | Bo eligible Employee h2; e3 | unresolved | Ada eligible Engineer h1,h2 | Lee unresolved no supplied type.
Independent checks: Closure parity and subtype path replay passed.
Coverage: Lee incomplete; Ada, Bo, Co complete.
Limits: Fictional supplied types only; no source truth or external ontology claim.
Next action: Owner reviews e2 and requests Lee's type evidence before deciding e3.
```

**Bad output:** “Co is a Person because Organization is an Entity, so e2 is valid.” Entity is an ancestor of both branches; that does not provide an Organization-to-Person path.

## Edge cases
- **Identity subtype**: a directly asserted Person satisfies a Person requirement with an empty class-link path.
- **Multiple inheritance**: any one valid upward path proves eligibility; preserve the selected link IDs.
- **Incomplete direct types**: no observed path remains unresolved, not invalid.
- **Strict hierarchy cycle**: reject and show the closing class-link IDs before evaluating assertions.

## Test case
**Input:**
> In fictional C1, assess e1, e2 and e3 under the supplied strict class links and Person/Person mentors contract. Then add Person→Engineer as a new strict link, and separately test a forged subtype witness using h4 for Ada.

**Assertions:**
1. e1 is valid with Ada's h1,h2 path and Bo's h2 path.
2. e2 is invalid because Co's complete Organization typing has no path to Person; e3 is unresolved because Lee's typing is incomplete.
3. The added Person→Engineer link is rejected as a strict cycle with link IDs.
4. A forged h4 path for Ada is rejected by independent replay.
