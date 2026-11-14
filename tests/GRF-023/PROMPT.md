Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-023
name: graph-learning-split-leakage-audit
domain: Graph Engineering Foundations
subdomain: Graph learning information boundaries
version: 1.0
description: Audit supervision partitions and message-passing graph visibility for declared target-equivalent edges when preparing a graph link-prediction evaluation.
triggers: ["audit graph split leakage", "check message passing visibility", "find inverse edge target leakage", "separate link supervision from graph context", "review graph learning split boundaries"]
not_for: ["choosing a general validation split [TML-001]", "auditing target encoding alone [TFE-005]", "reconstructing historical graph snapshots [GRF-005]", "measuring model predictive accuracy"]
requires: []
risk_level: medium
---

# Graph Learning Split Leakage Audit

## Purpose
Produce an information-boundary ledger for a declared link-prediction experiment, separating target supervision from graph context visible during each phase. Detect target-equivalent edges that cross the permitted boundary through duplicates or declared inverse representations. A clean bounded edge check does not establish that features, sampling or the full training pipeline are leakage-free.

## Inputs to collect
1. **Prediction contract** — specify predicted relation, deployment population and evaluation phase. Why: visibility depends on what the model is supposed to predict. Default: unresolved; request the contract.
2. **Generalization regime** — specify transductive, inductive or temporal evaluation and its operational meaning. Why: shared nodes may be legitimate in one experiment and prohibited in another. Default: no assumed node-disjointness rule.
3. **Supervision partitions** — obtain training, tuning and final target records with stable source identities. Why: record-disjoint partitions can still contain equivalent target facts. Default: no completed partition verdict without the records.
4. **Visible graph inventories** — obtain actual adjacency or edge records used by each phase, including reverse-edge augmentation and cached neighborhoods. Why: the label table alone does not describe message-passing exposure. Default: pending visibility audit.
5. **Equivalence policy** — collect approved inverse and symmetric relations, duplicate semantics and context boundaries. Why: reversed spelling is not automatically the same target fact. Default: exact typed triples only, with undeclared equivalences listed as unresolved.
6. **Feature and timing provenance** — obtain fitting inputs, source availability times and preprocessing/cache revisions. Why: removing a target edge does not remove target-derived features. Default: feature and temporal checks pending.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze experiment, partition, graph and preprocessing revisions for the phase under review.
2. Describe the permitted information for that phase, including whether node identity, node features and training targets may be visible.
3. Map supervision records to target facts using only the supplied equivalence policy and matching context.
4. Check target-fact overlap across training, tuning and final partitions while retaining all originating record IDs.
5. Enumerate the actual graph records visible to message passing, including generated inverse edges and cached expansions.
6. ⚠️ Compare visible records against prohibited target facts by semantic key rather than record ID; a fresh ID for a reverse edge does not remove its information.
7. Inspect node overlap against the declared regime instead of imposing universal node separation.
8. Trace feature fitting, graph statistics, negative sampling and preprocessing caches to their permitted inputs and availability times.
9. Propose repairs that rebuild affected graph views and derived artifacts from the authorized inputs while retaining the original experiment evidence.
10. Rerun the boundary checks on the repaired artifacts before interpreting any new model score.
11. Deliver witnessed violations separately from untested paths and unresolved equivalence or availability policies.

This Python 3 reference checks exact triples and explicitly declared inverse-equivalent triples in one frozen context. It assumes prevalidated nonempty string IDs and four-field records `(record_ID, subject, predicate, object)`. The inverse map must be reciprocal; symmetric predicates can map to themselves. It does not infer equivalence from names, merge entities, handle time windows, test feature provenance or train a model. Record the interpreter version when executing.

```python
def leakage(supervision, visible, inverse):
    if any(inverse.get(q) != p for p, q in inverse.items()):
        raise ValueError("inverse policy must be reciprocal")
    def indexed(records):
        out = {}
        seen = set()
        for rid, s, p, o in records:
            if rid in seen:
                raise ValueError("duplicate record identity within ledger")
            seen.add(rid)
            key = (s, p, o)
            if p in inverse:
                key = min(key, (o, inverse[p], s))
            out.setdefault(key, []).append(rid)
        return out
    target = indexed(supervision)
    context = indexed(visible)
    return [(key, sorted(target[key]), sorted(context[key]))
            for key in sorted(target.keys() & context.keys())]

held_out = [("h1", "A", "owns", "B")]
visible = [("v1", "B", "owned_by", "A"),
           ("v2", "A", "owns", "B"),
           ("v3", "B", "visits", "A")]
policy = {"owns": "owned_by", "owned_by": "owns"}
found = leakage(held_out, visible, policy)
assert len(found) == 1
assert found[0][1:] == (["h1"], ["v1", "v2"])
assert leakage(held_out, visible[2:], policy) == []
assert leakage(held_out, visible[:1], {}) == []
print("declared inverse and duplicate target exposure checked")
```

The last assertion means an undeclared inverse was not evaluated, not that the real experiment is safe. Use the same key comparison between supervision partitions to detect equivalent targets crossing partitions. Before applying it to temporal or contextual records, select the appropriate context or implement and test a richer key; collapsing different times can create false overlaps. An empty target ledger checks nothing about an intended nonempty evaluation set.

## Decision rules
- IF target-equivalent facts appear in prohibited graph context THEN report their target and visible record IDs BECAUSE disjoint file rows do not establish an information boundary.
- IF nodes overlap under a declared transductive contract THEN judge their permitted features and edges BECAUSE node reuse alone is not the specified violation.
- IF deployment requires unseen nodes THEN test node visibility and all derived artifacts BECAUSE removing target edges alone cannot establish inductive isolation.
- IF temporal availability is unknown THEN leave the temporal verdict pending BECAUSE an event timestamp need not equal its availability to the system.
- IF an inverse policy is unresolved THEN report that unchecked route BECAUSE guessing equivalence can create either false alarms or missed exposure.

## Output template
```text
Contract: <phase, task, regime, revisions and permitted information; maximum 80 words>
Partitions: <target-fact overlap witnesses or checked scope>
Visibility: <target key | target records | visible records | violated rule>
Other channels: <nodes/features/sampling/time/caches | observed or pending evidence>
Repair: <proposed rebuild | owner | affected artifacts; maximum 6 rows>
Recheck: <executed artifact checks/results or pending>
Decision: <violates / passes bounded checks / unresolved; remaining limits>
```

## Quality checklist
- [ ] Supervision and visible graph inventories are separate inputs.
- [ ] The permitted information boundary identifies a phase and regime.
- [ ] Inverse and symmetric semantics come from an explicit policy.
- [ ] Witnesses retain both supervision and visible record identities.
- [ ] Node overlap is interpreted under the declared deployment contract.
- [ ] Feature fitting and graph-derived caches have separate review states.
- [ ] Temporal findings use availability evidence rather than guessed dates.
- [ ] Passing edge checks do not become whole-pipeline approval.

## Anti-patterns
- **Fresh-ID reassurance**: treat new edge IDs as new information. Fix: compare target-equivalent semantic keys.
- **Reverse-edge escape**: remove forward targets but retain generated inverses. Fix: audit augmented adjacency after construction.
- **Universal node split**: declare every shared node a leak. Fix: apply the explicit generalization contract.
- **Feature amnesia**: remove edges while retaining target-derived embeddings. Fix: trace and rebuild affected features and caches.
- **Score proves isolation**: use plausible accuracy as evidence of clean boundaries. Fix: inspect actual information flow before interpreting scores.

## Worked example
**Input:** Fictional experiment W predicts held-out owns links between known nodes. Its policy permits known-node identity but prohibits held-out target-equivalent edges in evaluation context. Use the snippet records and inverse policy. Feature fitting evidence is unavailable.

**Output:**
```text
Contract: W evaluation; known-node link prediction; transductive node reuse permitted; frozen fixture; held-out target equivalents prohibited.
Partitions: Only h1 supplied; cross-partition overlap review pending other ledgers.
Visibility: A/owns/B | h1 | v1,v2 | prohibited target-equivalent context.
Other channels: Node reuse permitted by contract; features/sampling/time/caches pending evidence.
Repair: Rebuild context without v1/v2 and inspect affected derived artifacts; experiment owner; no production change authorized.
Recheck: Reference fixture checks cleaned v3-only context; real artifact rebuild pending.
Decision: Original context violates; cleaned fixture passes bounded edge checks only; feature and partition review unresolved.
```

**Bad output:** “h1 and v1 have different IDs, so the test is clean.”
This ignores the supplied inverse equivalence and unreviewed information channels.

## Edge cases
- **Duplicate observations**: preserve each record but compare the target fact once; do not erase provenance.
- **Undirected target**: obtain a symmetric equivalence policy before normalizing endpoint order.
- **Temporal repeats**: use context-sensitive keys; do not collapse distinct prediction instants without an explicit policy.
- **Unknown negative labels**: audit sampling assumptions separately; absent edges do not automatically establish true negative relations.
- **Empty inventory**: state exactly which ledger is empty and withhold a broader isolation verdict.

## Test case
**Input:**
> Fictional held-out A owns B is absent as a forward edge, but visible B owned_by A remains under an approved inverse policy. Known nodes may be shared. Feature provenance is missing. Audit the split.

**Assertions:**
1. Identifies inverse target exposure despite different edge orientation.
2. Does not treat permitted known-node reuse alone as a violation.
3. Leaves feature provenance unresolved.
4. Requires a rebuilt context and recheck before a clean bounded-edge claim.
</skill>

<user_request>
Fictional held-out A owns B is absent as a forward edge, but visible B owned_by A remains under an approved inverse policy. Known nodes may be shared. Feature provenance is missing. Audit the split.
</user_request>
