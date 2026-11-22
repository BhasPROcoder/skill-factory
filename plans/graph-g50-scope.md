# GRF-050 candidate: node retirement referential preview

Status: discovery card only. No ID allocation, skill, manifest or registry entry. Author must still inspect the full neighboring procedures and demonstrate a distinct executable result before writing.

## Decision to pursue

Given a versioned directed graph with identified nodes and edges, a named node proposed for retirement, and an explicit relation-by-relation deletion policy, construct a **referential disposition preview**. Return every incident edge identity, its direction and policy result: retain and block the retirement, remove with the node under an authorized cascade policy, or unresolved pending owner decision. Produce the hypothetical surviving node/edge inventory and independently check that no retained edge references the retired node and no unrelated edge identity disappeared. Preserve parallel edges and self-loops as separate records; a self-loop appears once in the disposition ledger even though both endpoints match.

The preview does not execute deletion or infer permission to erase records. Relation types may have different owners, so a blanket cascade is not a safe default. The method asks the responsible owner for a policy when one is missing; it does not invent retention rules.

## Neighbor comparison

- GRF-029's actual Procedure removes a vertex plus incident edges hypothetically to measure **new loss of connectivity among surviving nodes** in an undirected graph. It does not decide referential disposition per directed relation, block a retirement, or reconcile the exact surviving record inventory.
- GRF-014's actual Procedure tests **database constraint enforcement**, including one deletion rejection under `ON DELETE RESTRICT`. It does not build a per-edge policy preview or compare pre/post graph identities across a proposed retirement.
- GRF-017's actual Procedure transforms identities reversibly for a migration, retaining all edges. It does not retire a node.
- GRF-024's actual Procedure checks a restored graph against a recovery manifest, including dangling references. It does not determine the proposed retirement closure from a relation policy.
- `sf.py search 'node deletion'`, `cascade` and `dangling` found no direct candidate. A later author must also check adjacent non-GRF administrative deletion workflows before acceptance.

The unique artifact is the policy-indexed incident-edge disposition and exact hypothetical inventory, not a reachability report, database DDL, or generic deletion advice. If further comparison shows an existing skill already performs that artifact, reject this candidate rather than renaming it.

## Executable acceptance fixture

Fictional complete snapshot S: nodes A, B, C, I. Directed edges `e1: A→B` and `e2: A→B` are separate parallel `link` records; `e3: B→C` is `owned`; `e4: B→B` is a loop of type `link`; `e5: C→A` is an unrelated `link`. Proposed retirement: B.

1. With `link=cascade`, `owned=restrict`, return **blocked**, with `e3` as the blocking witness. Do not claim a post-retirement inventory exists.
2. With both types explicitly set to `cascade`, show one node B and exactly `e1,e2,e3,e4` in the removal preview; `e4` appears once. Surviving graph has nodes A,C,I and only `e5: C→A`.
3. With no `owned` policy, return unresolved; do not silently cascade `e3`.
4. Inject an unknown endpoint, duplicate edge ID, or stale snapshot identifier; reject or require a re-freeze before computing a definitive preview.
5. Independently compare the surviving edge-ID set with `original IDs − incident IDs` and replay each surviving endpoint against surviving nodes. This checks referential closure and collateral loss, not operational authorization.

Potential Python 3 reference: validate exact string IDs and row shapes, group incident records by edge ID, apply explicit per-type policy, then build a copy-on-write preview only when no `restrict` or unresolved dispositions remain. Keep a source-locator ledger for owner review. Do not write source-state mutations in the skill's executable fixture.

```python
def preview(nodes, edges, retired, policy, observed, expected):
    if observed != expected:
        raise ValueError("snapshot changed")
    if len(set(nodes)) != len(nodes) or retired not in nodes:
        raise ValueError("invalid node inventory")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")
    incident = {eid: (a, b, kind) for eid, a, b, kind in edges
                if retired in (a, b)}
    unresolved = sorted(eid for eid, (_, _, kind) in incident.items()
                        if kind not in policy)
    blocked = sorted(eid for eid, (_, _, kind) in incident.items()
                     if policy.get(kind) == "restrict")
    if any(value not in {"cascade", "restrict"} for value in policy.values()):
        raise ValueError("unknown policy")
    if unresolved:
        return "unresolved", unresolved, None
    if blocked:
        return "blocked", blocked, None
    survivors = [n for n in nodes if n != retired]
    kept = [e for e in edges if e[0] not in incident]
    assert {e[0] for e in kept} == {e[0] for e in edges} - set(incident)
    assert all(a in survivors and b in survivors for _, a, b, _ in kept)
    return "preview", sorted(incident), (survivors, kept)

nodes = ["A", "B", "C", "I"]
edges = [("e1", "A", "B", "link"), ("e2", "A", "B", "link"),
         ("e3", "B", "C", "owned"), ("e4", "B", "B", "link"),
         ("e5", "C", "A", "link")]
assert preview(nodes, edges, "B", {"link": "cascade", "owned": "restrict"},
               "S", "S")[:2] == ("blocked", ["e3"])
assert preview(nodes, edges, "B", {"link": "cascade"},
               "S", "S")[:2] == ("unresolved", ["e3"])
result = preview(nodes, edges, "B",
                 {"link": "cascade", "owned": "cascade"}, "S", "S")
assert result[1] == ["e1", "e2", "e3", "e4"]
assert result[2] == (["A", "C", "I"], [("e5", "C", "A", "link")])
for bad in [edges + [("e1", "C", "A", "link")],
            edges + [("x", "Z", "A", "link")]]:
    try:
        preview(nodes, bad, "B", {"link": "cascade", "owned": "cascade"}, "S", "S")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid inventory accepted")
try:
    preview(nodes, edges, "B", {}, "S2", "S")
except ValueError:
    pass
else:
    raise AssertionError("stale snapshot accepted")
print("retirement disposition, exact closure and invalid-input checks passed")
```

## Accuracy and boundaries

All example IDs and policies are fictional. No current database cascade semantics, legal retention rule, product API, performance statistic or external documentation claim is hardcoded. Any real storage engine's delete behavior is `[VERIFY: inspect the installed engine's official constraint and transaction documentation plus a disposable execution test]`. The graph preview's correctness requires a complete eligible edge inventory for the named snapshot; a partial extract can identify known incident edges but cannot certify that no others exist.
