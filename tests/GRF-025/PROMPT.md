Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-025
name: graph-negative-example-construction
domain: Graph Engineering Foundations
subdomain: Link example construction
version: 1.0
description: Construct reproducible unobserved link candidates under typed eligibility and positive-exclusion policies when preparing negative examples for a declared graph-learning phase.
triggers: ["construct graph negative examples", "sample unobserved graph links", "exclude inverse positive edges", "handle exhausted negative candidate pools", "audit graph negative sampling policy"]
not_for: ["auditing supervision visibility [GRF-023]", "choosing validation partitions [TML-001]", "target encoding leakage checks [TFE-005]", "proving that absent relationships are false"]
requires: []
risk_level: medium
---

# Graph Negative Example Construction

## Purpose
Construct a finite, reproducible selection of eligible unobserved relationship candidates, retaining why other candidates were excluded. Distinguish a negative training designation from verified real-world falsity. The deliverable makes candidate eligibility, available evidence and exhausted-pool behavior inspectable before model fitting or evaluation.

## Inputs to collect
1. **Prediction phase and task** — identify the relation, training or evaluation phase, and what examples represent. Why: a training sampler and a filtered evaluation protocol may access different evidence. Default: unresolved; do not construct labels without a phase policy.
2. **Typed node inventory** — obtain scoped IDs, endpoint types and allowed source/target populations. Why: arbitrary pairs can be meaningless for the target relation. Default: no invented nodes or endpoint types.
3. **Eligible universe** — obtain permitted relation, self-pair rule and any domain exclusions. Why: sample interpretation depends on the population it represents. Default: exact supplied source-by-target population, with self-pairs excluded unless explicitly permitted.
4. **Authorized positive ledger** — collect positive triples, snapshot and availability boundary for this phase. Why: known positives must not become negative examples, while forbidden future labels must not silently influence sampling. Default: construction pending without the authorized exclusion view.
5. **Equivalence policy** — obtain reciprocal inverse relations and symmetric-relation declarations. Why: different triples can encode the same known positive fact. Default: exact triples only; undeclared equivalences remain unresolved.
6. **Selection contract** — obtain requested count, ordering or randomization method, reproducibility inputs and replacement policy. Why: these determine which eligible examples are selected and how repeats are interpreted. Default: deterministic lexical selection without replacement, disclosed as nonrandom; request the count.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the phase, inventory, positive-view revision and selection policy before generating examples.
2. Validate scoped node IDs and declared endpoint classes against the supplied inventory.
3. Enumerate the candidate universe from the explicit relation and permitted endpoint populations.
4. Expand the authorized positive exclusions using only declared reciprocal inverse or symmetric equivalences.
5. Classify each candidate as prohibited self-pair, known positive, or eligible unobserved link, retaining its identity and reason.
6. ⚠️ Apply other eligibility restrictions before selection; do not generate a target count first and then hide invalid examples by dropping them.
7. Select without replacement under the disclosed ordering or tested randomization contract.
8. Reconcile requested count, selected count and finite eligible population, explicitly reporting any shortfall.
9. Label selected rows as constructed negatives under the experiment policy while retaining their unobserved-world status.
10. Verify selected uniqueness, endpoint eligibility and disjointness from authorized positive equivalence classes.
11. Deliver selected IDs, exclusions, universe scope and unresolved evidence boundaries; rerun construction when its frozen inputs change.

This Python 3 reference enumerates one typed directed relation and selects the lexical prefix of eligible triples. It is deterministic selection, not uniform random sampling or hard-negative mining. Use only prevalidated nonempty string IDs, class labels and relation names; positive records are three-field tuples. The caller must first select the authorized positive view and context. Record the interpreter version and actual execution result.

```python
def construct(types, relation, source_type, target_type, positives,
              inverse, count, allow_self=False):
    if type(count) is not int or count < 0 or type(allow_self) is not bool:
        raise ValueError("invalid selection policy")
    if any(inverse.get(q) != p for p, q in inverse.items()):
        raise ValueError("inverse policy must be reciprocal")
    blocked = set()
    for s, p, o in positives:
        if s not in types or o not in types:
            raise ValueError("unknown positive endpoint")
        blocked.add((s, p, o))
        if p in inverse:
            blocked.add((o, inverse[p], s))
    eligible, rejected = [], []
    for s in sorted(types):
        if types[s] != source_type:
            continue
        for o in sorted(types):
            if types[o] != target_type:
                continue
            triple = (s, relation, o)
            reason = "self-pair" if s == o and not allow_self else "known positive" if triple in blocked else None
            if reason:
                rejected.append((triple, reason))
            else:
                eligible.append(triple)
    selected = eligible[:count]
    return selected, rejected, len(eligible), max(0, count-len(selected))

types = {"A": "Unit", "B": "Unit", "C": "Unit"}
positives = [("B", "inside", "A")]
policy = {"contains": "inside", "inside": "contains"}
selected, rejected, pool, shortfall = construct(
    types, "contains", "Unit", "Unit", positives, policy, 6)
assert pool == 5 and len(selected) == 5 and shortfall == 1
assert ("A", "contains", "B") not in selected
assert len(rejected) == 4
assert len(set(selected)) == len(selected)
print("typed universe, inverse exclusion and finite shortfall checked")
```

The reference keeps the selected triple as its stable candidate identity; preserve the original positive ledger separately. An empty eligible population is a legitimate result under the supplied restrictions. For large inventories, replace exhaustive enumeration with an explicitly tested generator and track its stopping condition: a search limit does not prove the eligible pool is exhausted. If using randomization, retain the generator implementation and state plus population ordering; do not claim reproducibility from a seed alone across unspecified implementations.

## Decision rules
- IF a candidate matches an authorized positive or declared inverse THEN exclude it BECAUSE changing representation does not change the known fact.
- IF a candidate is absent from the positive view THEN call it unobserved BECAUSE absence does not establish falsity.
- IF the finite eligible pool is smaller than requested THEN return the shortfall BECAUSE duplicating rows would violate sampling without replacement.
- IF exclusion requires forbidden future labels THEN stop that dependent construction BECAUSE the sampler must obey the experiment's information boundary.
- IF a generation budget stops enumeration THEN report incomplete search BECAUSE an unvisited candidate is not evidence of pool exhaustion.

## Output template
```text
Contract: <phase, snapshots, relation, endpoint populations, equivalence policy; maximum 90 words>
Universe: <enumeration scope, self-pair policy, eligible count or unknown>
Selection: <candidate triples, ordering/randomization, replacement policy; ledger attachment if large>
Exclusions: <candidate | reason; complete ledger or attachment>
Reconciliation: <requested, selected, eligible, shortfall; stopping condition>
Checks: <executed results versus pending checks; maximum 80 words>
Interpretation: <negative designation, truth limits, information-boundary gaps; maximum 80 words>
```

## Quality checklist
- [ ] Phase and authorized positive-view revision are explicit.
- [ ] Endpoint populations and relation direction are defined.
- [ ] Equivalence exclusions use declared rules only.
- [ ] Selected candidates preserve stable identities.
- [ ] Without-replacement output has no duplicates.
- [ ] Shortfall distinguishes exhaustion from interrupted search.
- [ ] Negative designation does not assert real-world falsity.
- [ ] Reproducibility inputs and selection bias are disclosed.

## Anti-patterns
- **Absent means false**: present unobserved pairs as verified nonrelations. Fix: retain constructed-label status.
- **Inverse loophole**: exclude only the exact positive spelling. Fix: apply the declared equivalence policy.
- **Future-label filtering**: silently consult later outcomes. Fix: use the phase-authorized evidence view.
- **Fill by repetition**: duplicate candidates to meet a quota. Fix: report the finite shortfall.
- **Randomness claim**: call a lexical prefix representative random sampling. Fix: name the actual selection mechanism and limitations.

## Worked example
**Input:** Fictional training view F contains the snippet's three Unit nodes and B inside A. The reciprocal inverse policy is supplied. Request six contains candidates without replacement, excluding self-pairs and using lexical order.

**Output:**
```text
Contract: Training F; Unit-to-Unit contains; contains/inside reciprocal; only F positives authorized.
Universe: All nine ordered Unit pairs; self-pairs excluded; five eligible unobserved links.
Selection: A contains C; B contains A; B contains C; C contains A; C contains B; lexical order without replacement.
Exclusions: A contains A | self-pair; A contains B | known positive via B inside A; B contains B | self-pair; C contains C | self-pair.
Reconciliation: Requested 6; selected 5; eligible 5; shortfall 1; finite enumeration exhausted.
Checks: Reference assertions verify counts and inverse exclusion when executed; no live training performed.
Interpretation: Constructed negatives under F only; their real-world falsity is unknown. Selection is nonrandom and no later evidence was consulted.
```

**Bad output:** “Six false relationships found; repeat C contains B to fill the batch.”
This invents truth and violates the declared replacement policy.

## Edge cases
- **No nodes of an allowed type**: return empty selection and the requested shortfall; ask whether the inventory is complete.
- **Symmetric relation**: map the predicate to itself only when explicitly declared; exclude reversed positives accordingly.
- **Multiple contexts**: partition construction by the approved context before equivalence checks; do not combine incompatible facts.
- **Known positive outside target endpoint classes**: retain it in the source ledger; it need not belong to this candidate universe.
- **Domain-specific exclusions**: require their explicit predicate and provenance; the reference implements only type, self and positive exclusions.

## Test case
**Input:**
> Fictional Unit A and B have authorized positive A parent B and declared inverse child. Request two child candidates without replacement, no self-pairs. Later labels exist but are forbidden for this phase.

**Assertions:**
1. Excludes B child A through the declared inverse policy.
2. Returns only A child B with shortfall one.
3. Does not access later labels or claim the selected link is truly false.
4. Reports the finite universe and actual selection mechanism.
</skill>

<user_request>
Fictional Unit A and B have authorized positive A parent B and declared inverse child. Request two child candidates without replacement, no self-pairs. Later labels exist but are forbidden for this phase.
</user_request>
