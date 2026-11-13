---
id: GRF-016
name: versioned-graph-patch-replay
domain: Graph Engineering Foundations
subdomain: Incremental graph updates
version: 1.0
description: Apply an ordered graph patch to a versioned snapshot with payload-bound replay receipts and whole-batch reference checks when retries or stale writers could corrupt node-edge consistency.
triggers: ["replay a graph update safely", "apply an atomic graph patch", "reject stale graph changes", "delete nodes without dangling edges", "detect conflicting graph event reuse"]
not_for: ["generic API idempotency contracts [TAP-005]", "pipeline write design [TDE-001]", "initial edge-list reconciliation [GRF-003]", "historical assertion reconstruction [GRF-005]", "distributed consensus or live database deployment"]
requires: []
risk_level: medium
---

# Versioned Graph Patch Replay

## Purpose
Produce a new graph snapshot only when an entire ordered patch satisfies its version and relationship preconditions. Bind a stable batch-event identity to the exact patch so an identical retry has no new effect while conflicting reuse is rejected. The reference demonstrates an in-memory transition contract, not durable or concurrent exactly-once execution.

## Inputs to collect
1. **Snapshot and version** — obtain node IDs, edge IDs/endpoints and a trusted revision token. Why: a patch must name the state it expects. Default: no guessed latest version; request the actual snapshot.
2. **Batch identity and ordered operations** — obtain a stable logical event ID, expected version and exact operation sequence. Why: retry identity differs from a processing attempt. Default: no fresh ID on retry and no implicit operation reordering.
3. **Graph mutation policy** — confirm permitted loops, parallel relationships, node/edge deletion, identity reuse and property constraints. Why: reference consistency alone cannot validate domain meaning. Default: preserve edge identities and reject referenced-node deletion; other policies require explicit agreement.
4. **Receipt evidence** — obtain the previously accepted event IDs and payload binding, including retention limits. Why: forgotten receipts cannot prove a request was never applied. Default: missing receipt history means replay guarantees are unresolved.
5. **Commit environment** — identify whether this is an offline preview or a live transaction implementation. Why: copying data in memory does not coordinate concurrent writers or survive a crash. Default: preview only; verify current official storage documentation before implementation.
6. **Failure and retry handling** — obtain owner decisions for stale versions, conflicting payloads and rejected changes. Why: blindly rebasing may alter graph meaning. Default: return a conflict and preserve the original graph for explicit reconciliation.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the base snapshot, version and complete ordered operation envelope, retaining source evidence for each operation.
2. Validate envelope types and bind the event ID to its expected version and exact operations; preserve the canonical representation used for equality.
3. Inspect existing receipts before evaluating a fresh-write version condition. An identical retained receipt means replay without a new graph effect; a different envelope under the same ID is a conflict.
4. For an unseen event, compare its expected version with the current snapshot. Reject a mismatch without silently moving the patch to a newer base.
5. Copy the graph into an isolated candidate and apply operations in their declared order, checking each operation's identity and endpoint preconditions.
6. ⚠️ Reject node deletion while any candidate edge still references it. Require explicit preceding edge deletions instead of silently cascading away relationship evidence.
7. Validate the entire candidate against endpoint integrity and every supplied graph invariant. A failure at any position rejects the entire batch, including earlier candidate changes.
8. Publish graph, next version and receipt together only after all checks pass. In a live implementation, require one atomic conditional commit covering all three; otherwise report that guarantee unimplemented.
9. Replay the same envelope, try changed payload reuse, inject a late failure and submit an obsolete expected version. Compare full graph, version and receipts after every case.
10. Deliver the transition and conflict evidence, distinguishing accepted preview, replay, rejected batch and unperformed durable execution.

This Python 3 reference uses trusted internally consistent state, nonempty string identities and immutable operation tuples. Prevalidate tuple shapes and string fields. Operations are node+/node- with an ID, edge+ with ID/source/target, and edge- with ID. It models whole-graph integer versions, permits loops/parallel edges and stores receipts indefinitely in memory; it does not implement properties, tombstones, persistence or concurrency. Execute the snippet and record the installed interpreter version.

```python
from copy import deepcopy

def apply_patch(state, event, expected, operations):
    if type(expected) is not int or expected < 0 or not operations:
        raise ValueError("expected version and nonempty patch required")
    envelope = (expected, tuple(operations))
    if event in state["receipts"]:
        if state["receipts"][event] != envelope:
            raise ValueError("event payload conflict")
        return deepcopy(state), "replay"
    if expected != state["version"]:
        raise ValueError("stale version")
    candidate = deepcopy(state)
    nodes, edges = candidate["nodes"], candidate["edges"]
    for operation in operations:
        kind, key, *args = operation
        if kind == "node+":
            if key in nodes:
                raise ValueError("node already exists")
            nodes.add(key)
        elif kind == "edge+":
            source, target = args
            if key in edges or source not in nodes or target not in nodes:
                raise ValueError("edge identity or endpoint conflict")
            edges[key] = (source, target)
        elif kind == "edge-":
            if key not in edges:
                raise ValueError("unknown edge")
            del edges[key]
        elif kind == "node-":
            if key not in nodes or any(key in pair for pair in edges.values()):
                raise ValueError("unknown or referenced node")
            nodes.remove(key)
        else:
            raise ValueError("unknown operation")
    assert all(a in nodes and b in nodes for a, b in edges.values())
    candidate["version"] += 1
    candidate["receipts"][event] = envelope
    return candidate, "accepted"

base = {"version": 0, "nodes": {"A", "B"},
        "edges": {"p": ("A", "B")}, "receipts": {}}
operations = (("edge-", "p"), ("node-", "B"))
updated, status = apply_patch(base, "batch1", 0, operations)
assert status == "accepted" and updated["version"] == 1
assert updated["nodes"] == {"A"} and updated["edges"] == {}
assert apply_patch(updated, "batch1", 0, operations) == (updated, "replay")
try:
    apply_patch(base, "bad", 0, (("node+", "C"), ("node-", "B")))
except ValueError:
    pass
else:
    raise AssertionError("referenced deletion accepted")
assert base == {"version": 0, "nodes": {"A", "B"},
                "edges": {"p": ("A", "B")}, "receipts": {}}
print("ordered deletion, exact replay and whole-batch rejection passed")
```

## Decision rules
- IF an accepted event ID returns with an identical envelope THEN leave the current graph unchanged BECAUSE a transport retry is not a new logical patch.
- IF that ID carries changed operations or expected version THEN reject it BECAUSE receipt identity must not authorize a different transition.
- IF an unseen event expects an obsolete version THEN request reconciliation BECAUSE its preconditions were established against another graph.
- IF a node still has incident edges THEN reject deletion BECAUSE automatic cleanup would conceal relationship removals.
- IF any candidate operation fails THEN discard all candidate changes and its receipt BECAUSE partial acceptance violates the batch contract.
- IF receipt retention or atomic persistence is unavailable THEN qualify replay guarantees BECAUSE an in-memory demonstration does not establish crash-safe execution.

## Output template
```text
Scope: <snapshot/version, policy and execution boundary; maximum 70 words>
Envelope: <event ID, expected version, ordered operations and source references>
Preconditions: <receipt comparison, version and graph-policy evidence>
Candidate: <node/edge additions and removals, or rejected operation/witness>
Outcome: <accepted preview / replay / rejected / incomplete; resulting version>
Verification: <graph, version and receipt comparisons; executed/pending>
Next action: <reconcile, authorize implementation or no new effect; maximum 70 words>
Limits: <receipt retention, durability, concurrency and domain checks; maximum 70 words>
```

## Quality checklist
- [ ] Event identity is stable across retries and distinct from attempt identity.
- [ ] Payload comparison includes expected version and operation order.
- [ ] Fresh writes require the observed base version.
- [ ] Every added edge has valid candidate endpoints.
- [ ] Node removals identify and explicitly remove incident edges first.
- [ ] Failed batches preserve graph, version and receipt ledger.
- [ ] Identical replay does not increment the version or restore an old snapshot.
- [ ] In-memory atomicity is separated from durable concurrent commit evidence.

## Anti-patterns
- **Fresh retry ID**: duplicate attempts become new patches. Fix: retain the logical batch identity.
- **Auto-rebase**: replace a stale expected version silently. Fix: revalidate meaning against the new snapshot.
- **Receipt before commit**: record success before graph changes finish. Fix: commit graph, version and receipt together.
- **Hidden cascade**: remove incident edges as a side effect. Fix: require explicit ordered edge operations.
- **Old snapshot replay**: restore the original result after later updates. Fix: report replay with current state unchanged.

## Worked example
**Input:** Fictional team Birch supplies the snippet base and batch1: delete p, then delete B, expected version zero. Its policy permits these explicitly evidenced removals; this is an offline preview.

**Output:**
```text
Scope: Birch base version 0; directed identified edges; offline copy only.
Envelope: batch1 | expected 0 | edge- p; node- B | supplied operation records.
Preconditions: No prior receipt; version matches; deleting p removes B's only incident edge.
Candidate: Remove p and B; retain A.
Outcome: Accepted preview, version 1. Exact repeat is replay at version 1.
Verification: Reference assertions compare graph, version and receipt behavior when executed; base remains unchanged.
Next action: No additional graph effect for the retry; durable implementation remains separate.
Limits: In-memory retained receipts only; no concurrent writer, crash recovery or live deletion tested.
```

**Bad output:** “Delete B first, cascade p, and assign a new event ID whenever the request repeats.”
This invents an unlisted relationship removal and destroys logical replay identity.

## Edge cases
- **Replay after newer updates**: recognize its retained identical receipt before version checks; preserve the newer current state.
- **Unknown receipt history**: do not assume an absent receipt proves nonexecution; reconcile against retained records before retrying.
- **Multiple writers**: use storage-supported atomic version comparison with the graph/receipt commit; the reference offers no concurrency guarantee.
- **Node identity reuse**: require the supplied lifecycle/tombstone policy before accepting recreation; the reference's membership checks do not establish identity continuity.
- **Property or temporal updates**: define their preconditions and invariants separately; do not infer them from endpoint-only validation.

## Test case
**Input:**
> Fictional graph version 4 has edge e:X->Y. An unseen batch expects version 4 and requests node+ Z followed by node- Y without deleting e. Explain result, receipt and retry handling.

**Assertions:**
1. Rejects the batch because e still references Y.
2. Leaves Z absent and preserves e, Y and version 4.
3. Does not create a success receipt for the rejected batch.
4. Requires an explicitly corrected envelope and version check rather than silently cascading e.
