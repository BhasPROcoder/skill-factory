---
id: GRF-049
name: knowledge-assertion-polarity-conflict-ledger
domain: Graph Engineering Foundations
subdomain: Explicit assertion polarity
version: 1.0
description: Classify reviewed positive and negative knowledge-graph assertions by exact triple and context when conflicting evidence or missing support needs an auditable ledger.
triggers: ["find conflicting knowledge graph assertions", "compare positive and negative relationship records", "audit explicit negation in a graph", "show source IDs for both polarities", "distinguish no assertion from a negative assertion"]
not_for: ["extracting polarity from source passages [GRF-019]", "governing relation inference rules [GRF-018]", "checking value-count constraints [GRF-020]", "retraction support for transitive facts [GRF-048]"]
requires: []
risk_level: medium
---

# Knowledge Assertion Polarity Conflict Ledger

## Purpose
Classify reviewed assertion evidence for exact directed triples within one frozen graph context. Keep every positive and negative source ID visible, mark simultaneous support as a conflict for owner review, and treat absent evidence as unknown unless completeness is established. This procedure does not judge which source is true or infer new facts.

## Inputs to collect
1. **Selected context** — obtain its stable ID and snapshot boundary. Why: records from different contexts must not collide. Default: no context merger.
2. **Node and predicate contract** — obtain known node IDs, one directed predicate ID and its approved endpoint meaning. Why: an inverse-looking assertion is a different triple. Default: preserve stated direction; no inverse or transitive inference.
3. **Reviewed assertion ledger** — obtain unique record IDs and `(context, subject, predicate, object, polarity)` fields, with polarity explicitly `positive` or `negative`. Why: passage text, uncertainty and modality need separate semantic review. Default: hold unreviewed records outside this calculation.
4. **Queried triples** — obtain exact subject, predicate and object IDs to classify. Why: a broad graph summary can hide the particular conflict being asked about. Default: none; request the target set.
5. **Coverage statement** — obtain whether the selected-context record inventory is complete for the queried triples. Why: no observed record does not prove an explicit negative. Default: incomplete, so no conclusive neither result.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the context ID, snapshot, predicate, node inventory and queried triples; retain source-record IDs.
2. Check unique nonempty IDs, six-field record shapes, known endpoints, selected predicate and permitted polarity values. Reject a string-shaped row rather than reading its characters as fields.
3. Separate selected-context records from other-context records. Preserve excluded IDs in the output ledger; never silently merge contexts.
4. Group selected records by exact `(subject,predicate,object)` and polarity, preserving all IDs for an equal triple.
5. For each queried triple, classify **both** when both ID sets are nonempty; otherwise classify **positive-only** or **negative-only** when only that side is present and coverage is complete.
6. For a complete inventory with neither ID set, classify **neither**. ⚠️ Do not translate this into negative; it means no reviewed assertion of either polarity in this scoped inventory.
7. With incomplete coverage, label one-sided evidence `observed-positive` or `observed-negative`, two-sided evidence `observed-both`, and no evidence `unresolved`; do not present one-sided or absent evidence as final.
8. Independently replay every reported source ID against the frozen records, checking context, exact triple and polarity. Reject forged or swapped support.
9. Compare the complete output map with a second per-query scan of the original ledger; compare exact ID sets, not just counts.
10. Deliver the classification, excluded-context ledger and completeness limit. Route both-supported triples to the source owner without deleting either assertion or declaring a winner.

This Python 3 reference takes finite node IDs, reviewed six-field records and explicit query triples. It groups selected-context IDs, then verifies the result with an independent scan of the original records. Run the entire snippet and record the installed interpreter version. It does not read passages, determine semantic truth or implement a graph database.

```python
def check_input(nodes, records, context, predicate, queries, complete):
    if type(nodes) not in (list, tuple) or type(records) not in (list, tuple):
        raise ValueError("invalid inventory shape")
    if type(queries) not in (list, tuple) or type(complete) is not bool:
        raise ValueError("invalid query or coverage shape")
    if type(context) is not str or not context or type(predicate) is not str or not predicate:
        raise ValueError("missing context or predicate")
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid node inventory")
    known, ids = set(nodes), set()
    for row in records:
        if type(row) not in (list, tuple) or len(row) != 6:
            raise ValueError("invalid assertion record")
        rid, ctx, s, p, o, polarity = row
        if any(type(x) is not str or not x for x in row):
            raise ValueError("invalid assertion field")
        if rid in ids or s not in known or o not in known or p != predicate:
            raise ValueError("duplicate ID, endpoint or predicate mismatch")
        if polarity not in ("positive", "negative"):
            raise ValueError("unsupported polarity")
        ids.add(rid)
    if any(type(q) not in (tuple, list) or len(q) != 3 for q in queries):
        raise ValueError("invalid query triple")
    if any(type(x) is not str or not x for q in queries for x in q):
        raise ValueError("invalid query field")
    if any(s not in known or o not in known or p != predicate for s, p, o in queries):
        raise ValueError("unknown query endpoint or predicate")
    if len(set(map(tuple, queries))) != len(queries):
        raise ValueError("duplicate query triple")

def state(positive, negative, complete):
    if positive and negative:
        return "both" if complete else "observed-both"
    if positive:
        return "positive-only" if complete else "observed-positive"
    if negative:
        return "negative-only" if complete else "observed-negative"
    return "neither" if complete else "unresolved"

def classify(nodes, records, context, predicate, queries, complete):
    check_input(nodes, records, context, predicate, queries, complete)
    grouped = {}
    excluded = []
    for rid, ctx, s, p, o, polarity in records:
        if ctx != context:
            excluded.append(rid)
            continue
        bucket = grouped.setdefault((s, p, o), {"positive": [], "negative": []})
        bucket[polarity].append(rid)
    result = {}
    for q in map(tuple, queries):
        bucket = grouped.get(q, {"positive": [], "negative": []})
        pos, neg = tuple(sorted(bucket["positive"])), tuple(sorted(bucket["negative"]))
        result[q] = (state(pos, neg, complete), pos, neg)
    excluded = tuple(sorted(excluded))
    verify(records, context, queries, complete, result, excluded)
    return result, excluded

def verify(records, context, queries, complete, result, excluded):
    expected = {}
    for q in map(tuple, queries):
        pos = tuple(sorted(rid for rid, ctx, s, p, o, pol in records
                           if ctx == context and (s, p, o) == q and pol == "positive"))
        neg = tuple(sorted(rid for rid, ctx, s, p, o, pol in records
                           if ctx == context and (s, p, o) == q and pol == "negative"))
        expected[q] = (state(pos, neg, complete), pos, neg)
    other = tuple(sorted(rid for rid, ctx, *_ in records if ctx != context))
    if result != expected or excluded != other:
        raise ValueError("classification or source replay mismatch")
    return True

nodes = ["A", "B", "C"]
rows = [("p1", "C1", "A", "linked", "B", "positive"),
        ("p2", "C1", "A", "linked", "B", "positive"),
        ("n1", "C1", "A", "linked", "B", "negative"),
        ("p3", "C1", "B", "linked", "C", "positive"),
        ("n2", "C1", "C", "linked", "A", "negative"),
        ("q1", "C2", "B", "linked", "C", "negative")]
queries = [("A", "linked", "B"), ("B", "linked", "C"),
           ("C", "linked", "A"), ("A", "linked", "C")]
out, excluded = classify(nodes, rows, "C1", "linked", queries, True)
assert out[queries[0]] == ("both", ("p1", "p2"), ("n1",))
assert out[queries[1]] == ("positive-only", ("p3",), ())
assert out[queries[2]] == ("negative-only", (), ("n2",))
assert out[queries[3]] == ("neither", (), ()) and excluded == ("q1",)
partial, _ = classify(nodes, rows, "C1", "linked", queries, False)
assert partial[queries[3]][0] == "unresolved"
print("polarity, context isolation and incomplete coverage checked")
```

## Decision rules
- IF the same triple has reviewed IDs of both polarities in the selected context THEN report both sets as a conflict BECAUSE a source disagreement needs review.
- IF a negative ID is absent THEN never infer a negative assertion BECAUSE missing evidence and explicit negation differ.
- IF inventory coverage is incomplete THEN use observed or unresolved labels BECAUSE another eligible record could change a final classification.
- IF records belong to another context THEN exclude and list them BECAUSE equal triples across contexts need not conflict.
- IF polarity was inferred only from unreviewed text THEN hold the record for semantic review BECAUSE this calculation assumes approved annotations.

## Output template
```text
Scope: <context, snapshot, predicate and queried triples; max 60 words>
Coverage: <complete/incomplete and evidence>
Classification: <triple | status | positive IDs | negative IDs; one line per query>
Other-context IDs: <excluded IDs and contexts>
Replay: <exact ID/context/triple/polarity check passed, failed or pending>
Conflicts: <both-supported triples and owner review queue>
Limits: <semantic and completeness limits; max 60 words>
Next action: <review or missing-input request>
```

## Quality checklist
- [ ] Context and snapshot are fixed before grouping.
- [ ] Every source ID is unique and points to one exact reviewed assertion.
- [ ] Direction and predicate are preserved in each queried triple.
- [ ] Positive and negative IDs are listed separately, including duplicates of a triple.
- [ ] Other-context records are listed as excluded.
- [ ] Coverage flag controls one-sided and neither wording.
- [ ] Independent replay checks every displayed ID and status.
- [ ] No missing assertion is described as an explicit negative or a truth verdict.

## Anti-patterns
- **Context merge**: combining equal triples from separate contexts. Fix: filter by frozen context before grouping.
- **Closed-world leap**: calling an unrecorded triple false. Fix: use neither or unresolved support status.
- **Source winner**: deleting one side of a conflict. Fix: preserve both ID sets for owner review.
- **Path inference**: deriving A→C from positive A→B and B→C. Fix: classify only reviewed exact triples here.
- **Count-only output**: reporting two positive records without IDs. Fix: list and replay each source identity.

## Worked example
**Input:** Fictional contexts C1 and C2 have the six reviewed `linked` records and four queries in the Python reference. C1's inventory is declared complete for those queries.

**Output:**
```text
Scope: Fictional C1 snapshot S1; directed linked; queries A/B, B/C, C/A, A/C.
Coverage: Complete for the four queries under the supplied exercise inventory.
Classification: A,linked,B | both | p1,p2 | n1; B,linked,C | positive-only | p3 | none; C,linked,A | negative-only | none | n2; A,linked,C | neither | none | none.
Other-context IDs: q1 from C2 excluded.
Replay: Exact ID/context/triple/polarity check passed.
Conflicts: A,linked,B requires source-owner review.
Limits: Fictional reviewed assertions only; no source-truth or inferred-path claim.
Next action: Ask the C1 owner to review p1,p2 and n1 together.
```

**Bad output:** “A,linked,C is negative because no record asserts it.” This invents a negative assertion from absence and ignores the required explicit polarity ledger.

## Edge cases
- **Incomplete inventory**: use `unresolved` for absent A,linked,C; one-sided evidence receives an observed label.
- **Other context**: q1 must not turn C1's B,linked,C into a conflict.
- **Repeated triple**: p1 and p2 remain two positive source identities rather than one merged record.
- **Unknown or conditional polarity**: route upstream for review; never coerce it to positive or negative.
- **Malformed record**: reject string rows, reused IDs, unknown endpoints and unsupported polarity before grouping.

## Test case
**Input:**
> For fictional C1, classify the four queried linked triples using p1,p2,n1,p3,n2. Keep q1 in C2 separate. First use a complete C1 inventory, then mark C1 coverage incomplete.

**Assertions:**
1. Complete C1 labels A,linked,B both with p1,p2 versus n1, while B,linked,C is positive-only with p3.
2. Complete C1 labels C,linked,A negative-only with n2 and A,linked,C neither, without inferring A→C from two links.
3. q1 remains excluded as a C2 record and does not create a C1 conflict.
4. Incomplete C1 labels A,linked,C unresolved rather than a final neither verdict.
