Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-054
name: graph-change-feed-coverage-reconciliation
domain: Graph Engineering Foundations
subdomain: Graph change delivery evidence
version: 1.0
description: Reconcile committed graph node and edge operations with emitted feed records and a consumer checkpoint when delivery gaps or duplicate attempts need exact witnesses.
triggers: ["audit graph change feed coverage", "find missing graph change events", "compare source commits with graph feed", "check duplicate graph delivery attempts", "verify consumer checkpoint against graph events"]
not_for: ["applying a graph patch [GRF-016]", "restoring a graph service [GRF-024]", "auditing adjacency buckets [GRF-047]", "generic checkpoint failure rehearsal [TDE-005]", "claiming exactly-once delivery"]
requires: []
risk_level: medium
---

# Graph Change-Feed Coverage Reconciliation

## Purpose
Compare committed graph operations with feed deliveries and checkpoint claims over a contiguous revision interval. Delivery does not prove consumer application.

## Inputs to collect
1. **Source interval** — obtain start/end revisions and an independent complete commit manifest. Why: a feed cannot certify itself. Default: none.
2. **Operation records** — obtain revision, envelope/operation IDs, action, object ID, edge endpoints and payload digest. Why: endpoint pairs collapse parallel identities. Default: no invented fields.
3. **Feed extract** — obtain delivery offset, source revision, envelope/operation IDs, payload digest and page completeness. Why: a missing page is not empty. Default: incomplete coverage unresolved.
4. **Checkpoint meaning** — obtain claimed last complete revision and acknowledgment semantics. Why: an offset may not prove persistence. Default: target state unverified.
5. **Dependency policy** — establish node-before-edge requirements and replay owner. Why: delivery order can matter. Default: report observed order only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source manifest, interval, feed extract, completeness flag and checkpoint observation.
2. Validate contiguous source revision coverage, unique source operation keys and nonempty identities before comparing delivery. Reject conflicting source identities instead of taking the last row.
3. Define the logical key as source revision, envelope ID and operation ID. Keep object ID and full source payload separately so two parallel edge additions remain distinct.
4. Group feed deliveries by logical key while preserving delivery offset and digest for every attempt.
5. For each source operation, report no matching feed record as missing; one matching digest as covered; repeated matching digests as duplicate attempts; any different digest as conflict. ⚠️ Do not treat a conflicting digest as a harmless retry.
6. Report feed keys absent from the source manifest as foreign; qualify incomplete extracts.
7. Scan source revisions in order and stop at the first revision lacking conflict-free coverage of every operation. That gives the greatest contiguous **observed covered** revision; do not skip a gap because later revisions arrived.
8. Independently reconstruct expected and observed logical-key sets for each revision and compare with the scan result. Preserve exact missing and conflicting witnesses.
9. With complete feed and a nodes-first policy, compare edge and endpoint-addition offsets; flag earlier edge delivery as a hazard.
10. Compare the claimed checkpoint revision with the contiguous covered revision. A claim beyond it needs reconciliation; a claim behind it may be conservative. An offset or acknowledgment does not by itself prove durable target graph state.
11. Deliver coverage and replay-boundary evidence without automatic mutation or exactly-once claims.

The Python 3 reference uses finite lists. Source rows are `(revision, envelope, operation, kind, object, source, target, digest)`; node additions have `None` endpoints. Feed rows are `(offset, revision, envelope, operation, digest)`. Set `nodes_first` from the consumer policy. Run it and record the interpreter version.

```python
from collections import Counter, defaultdict

def reconcile(source, feed, start, end, checkpoint, pages_complete,
              nodes_first):
    if any(type(x) is not int for x in (start, end, checkpoint)):
        raise ValueError("integer fixture revisions required")
    if start > end or type(pages_complete) is not bool or type(nodes_first) is not bool:
        raise ValueError("invalid interval or completeness flag")
    if any(type(row) not in (tuple, list) or len(row) != 8 for row in source):
        raise ValueError("invalid source record")
    if any(type(row) not in (tuple, list) or len(row) != 5 for row in feed):
        raise ValueError("invalid feed record")
    expected = {}
    node_add = {}
    for rev, env, op, kind, obj, a, b, digest in source:
        if (type(rev) is not int or
            any(type(x) is not str or not x for x in (env, op, kind, obj, digest)) or
            kind not in ("node+", "edge+") or rev < start or rev > end):
            raise ValueError("invalid source fields")
        if kind == "edge+" and any(type(x) is not str or not x for x in (a, b)):
            raise ValueError("edge endpoints required")
        if kind == "node+" and (a is not None or b is not None):
            raise ValueError("node endpoints must be absent")
        key = (rev, env, op)
        if key in expected:
            raise ValueError("duplicate source operation key")
        expected[key] = (kind, obj, a, b, digest)
        if kind == "node+":
            node_add[obj] = key
    revisions = {key[0] for key in expected}
    if revisions != set(range(start, end + 1)):
        raise ValueError("source revision gap")
    seen_offsets, delivered = set(), defaultdict(list)
    for offset, rev, env, op, digest in feed:
        if (type(offset) is not int or offset in seen_offsets or
            type(rev) is not int or
            any(type(x) is not str or not x for x in (env, op, digest))):
            raise ValueError("invalid feed identity or offset")
        seen_offsets.add(offset)
        delivered[rev, env, op].append((offset, digest))
    issues = []
    for key, (*_, digest) in sorted(expected.items()):
        attempts = delivered.get(key, [])
        if not attempts:
            issues.append((key, "missing" if pages_complete
                           else "unobserved; feed incomplete"))
        if len(attempts) > 1 and all(d == digest for _, d in attempts):
            issues.append((key, "duplicate attempt", len(attempts)))
        if any(d != digest for _, d in attempts):
            issues.append((key, "conflicting payload"))
    for key in sorted(set(delivered) - set(expected)):
        issues.append((key, "foreign"))
    for key, (kind, obj, a, b, _) in expected.items():
        if nodes_first and pages_complete and kind == "edge+" and key in delivered:
            edge_first = min(offset for offset, _ in delivered[key])
            for node in (a, b):
                nk = node_add.get(node)
                if nk in delivered and edge_first < min(o for o, _ in delivered[nk]):
                    issues.append((key, "endpoint order hazard", node))
    covered = start - 1
    if pages_complete:
        for rev in range(start, end + 1):
            keys = [k for k in expected if k[0] == rev]
            good = all(delivered.get(k) and
                       all(d == expected[k][-1] for _, d in delivered[k])
                       for k in keys)
            if not good:
                break
            covered = rev
        # Separate per-revision set reconstruction checks the scan.
        for rev in range(start, covered + 1):
            wanted = {k for k in expected if k[0] == rev}
            matched = {k for k in wanted if delivered.get(k) and
                       all(d == expected[k][-1] for _, d in delivered[k])}
            assert wanted == matched
    else:
        issues.append(("feed", "unavailable page; completeness unresolved"))
    if pages_complete and checkpoint > covered:
        issues.append(("checkpoint", checkpoint, "beyond covered", covered))
    return covered if pages_complete else None, issues

source = [(1, "E1", "nA", "node+", "A", None, None, "ha"),
          (1, "E1", "nB", "node+", "B", None, None, "hb"),
          (2, "E2", "e1", "edge+", "p", "A", "B", "hp"),
          (3, "E3", "e2", "edge+", "q", "A", "B", "hq")]
feed = [(10, 1, "E1", "nA", "ha"),
        (11, 1, "E1", "nB", "hb"),
        (12, 2, "E2", "e1", "hp"),
        (13, 2, "E2", "e1", "hp")]
covered, issues = reconcile(source, feed, 1, 3, 3, True, True)
assert covered == 2
assert ((3, "E3", "e2"), "missing") in issues
assert ((2, "E2", "e1"), "duplicate attempt", 2) in issues
assert ("checkpoint", 3, "beyond covered", 2) in issues
partial, partial_issues = reconcile(source, [], 1, 3, 3, False, True)
assert partial is None and all("missing" not in str(x)
                               for x in partial_issues)
print("source-to-feed coverage, retry and checkpoint checks passed")
```

The model cannot verify consumer persistence. Missing pages make coverage unresolved. Parallel object IDs remain separate.

## Decision rules
- IF an expected key has no feed record THEN report missing BECAUSE absence from complete delivery differs from an uncommitted source operation.
- IF attempts share a key and identical digest THEN report duplicate delivery BECAUSE repeated transport attempts are not distinct commits.
- IF a key has conflicting digests THEN flag conflict BECAUSE source identity cannot certify altered content.
- IF a revision is incomplete THEN stop the contiguous scan BECAUSE later deliveries cannot fill its gap.
- IF feed pages are unavailable THEN label missing and order findings provisional BECAUSE the extract is partial.

## Output template
```text
Scope: <source interval, feed extract, completeness and checkpoint meaning; maximum 70 words>
Coverage: <greatest contiguous observed covered revision, or unresolved>
Findings: <logical key | missing/duplicate/conflict/foreign/order hazard | witness; full ledger>
Checkpoint: <claim | comparison with coverage | target-state limit>
Checks: <source/observed per-revision identity comparison executed/pending>
Replay proposal: <bounded interval and owner review, or pending>
Limits: <unavailable pages, payload/consumer semantics; maximum 80 words>
```

## Quality checklist
- [ ] Source manifest is independent of the feed.
- [ ] Source revisions and logical operation keys are complete.
- [ ] Parallel edge object IDs remain distinct.
- [ ] Duplicate matching attempts differ from conflicting payloads.
- [ ] Missing and foreign records are separate findings.
- [ ] Contiguous coverage stops at the first incomplete revision.
- [ ] Missing feed pages block a complete pass.
- [ ] Checkpoint comparison is not called proof of applied graph state.

## Anti-patterns
- **Count parity**: duplicate and missing operations cancel. Fix: compare keys and digests.
- **Parallel collapse**: merge p and q because endpoints match. Fix: retain object and operation identities.
- **Later means complete**: accept a later revision despite a gap. Fix: scan contiguously.
- **Retry as conflict**: treat identical attempts as separate commits. Fix: compare key and payload.
- **Offset as state**: infer durable consumer graph from acknowledgment. Fix: require separate target-state evidence.

## Worked example
**Input:** Fictional source Team Fir supplies the snippet manifest and feed. The feed lacks e2 for parallel edge q; e1 appears twice with identical payload. Consumer checkpoint claims revision 3 complete.

**Output:**
```text
Scope: Fir exercise revisions 1–3; complete independent source and feed extracts; supplied checkpoint claims revision 3.
Coverage: Revisions 1–2 observed complete; first gap at revision 3.
Findings: (2,E2,e1) | duplicate attempt | offsets 12,13 identical hp; (3,E3,e2) | missing | q addition absent.
Checkpoint: Claim 3 exceeds observed coverage 2; consumer target graph remains unverified.
Checks: Per-revision source and feed keys compared; accepted attempts matched source digests through revision 2.
Replay proposal: Owner reviews bounded revision-3 delivery and consumer state before any replay.
Limits: Exercise records only; no live target-state, exactly-once or persistence claim.
```

**Bad output:** “The feed contains four rows for four source operations, so revision 3 is complete and q exists downstream.”
One row is a repeated e1 attempt; e2 is absent, and delivery alone does not prove target application.

## Edge cases
- **Unavailable feed page**: report completeness unresolved, not an empty delivery interval.
- **Conflicting retry**: mark the operation conflicted and stop coverage at that revision.
- **Foreign key**: report it separately from missing expected operations.
- **Edge before endpoint additions**: flag order hazard when the consumer requires nodes first.
- **Empty declared interval**: establish an explicit no-operations contract before claiming completeness; the reference requires at least one source revision.

## Test case
**Input:**
> Fictional source revisions 1–3 add nodes A/B, edge p:A→B, then parallel edge q:A→B. The feed has both nodes and two identical p attempts but no q; checkpoint claims revision 3 complete.

**Assertions:**
1. Reports revision 2 as the greatest contiguous observed covered revision.
2. Flags missing q and duplicate matching p deliveries by separate logical IDs.
3. Flags checkpoint claim 3 beyond coverage without claiming target state.
4. Preserves p and q as separate edge objects.
5. Proposes owner review rather than automatic replay.
</skill>

<user_request>
Fictional source revisions 1–3 add nodes A/B, edge p:A→B, then parallel edge q:A→B. The feed has both nodes and two identical p attempts but no q; checkpoint claims revision 3 complete.
</user_request>
