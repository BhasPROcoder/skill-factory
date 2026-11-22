---
id: GRF-058
name: knowledge-rule-negation-stratification-audit
domain: Graph Engineering Foundations
subdomain: Rule-program admission
version: 1.1
description: Check variable binding and signed predicate dependencies before evaluating a bounded neutral knowledge-rule program with negation.
triggers: ["check knowledge rule stratification", "find a negation dependency cycle", "audit unbound negative variables", "assign rule predicate strata", "review recursive graph rules before execution"]
not_for: ["choosing relation meanings [GRF-018]", "retracting transitive facts [GRF-048]", "diagnosing value constraints [GRF-020]", "executing a specific rule-engine language"]
requires: []
risk_level: medium
---

# Knowledge Rule Negation Stratification Audit

## Purpose
Check whether a supplied finite rule program has positively bound head and negative-atom variables, then determine whether its predicate dependencies admit strata. Return an assignment or a concrete negative-edge cycle witness. This is admission under the declared neutral rule notation, not evaluation of derived facts or a claim about any external rule engine.

## Inputs to collect
1. **Rule inventory** — obtain unique rule IDs and complete head/body atoms. Why: a missing rule can remove a negation cycle. Default: none.
2. **Neutral syntax contract** — declare predicate names, variable tokens, positive/negative body polarity and no function symbols, aggregates or existential heads. Why: other languages may have different semantics. Default: this limited reference only; obtain current authoritative language documentation before adapting.
3. **Predicate inventory** — obtain all base and derived predicate names, including those with no rules. Why: dependency coverage should not invent or omit a symbol. Default: derive names from supplied atoms for the reference; report external predicates as unverified.
4. **Binding policy** — confirm that every head or negative-atom variable must occur in a positive body atom of the same rule. Why: otherwise the rule can range over an unspecified population. Default: this reference policy.
5. **Use and completeness** — establish whether the rule set is complete and who decides release. Why: a passing subset cannot certify a larger program. Default: inspected rules only; no production deployment.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the rule set and its neutral syntax before analysis.
2. Validate unique rule IDs and nonempty predicate/variable tokens; reject malformed atom shapes instead of guessing a parser interpretation.
3. For each rule, collect variables in positive body atoms and separately collect head and negative-atom variables.
4. Report an unsafe-variable witness whenever a head or negative variable lacks positive binding. Stop admission, but retain any independent dependency findings as diagnostics.
5. Add a directed dependency from each head predicate to every body predicate, marked positive or negative with its rule ID.
6. Compute mutually reachable predicate groups in the dependency graph. A negative edge inside one group is a concrete obstruction: return it plus a path from its target back to its source.
7. If no obstruction exists, assign nonnegative integer strata satisfying head≥body for positive edges and head>body for negative edges. A positive recursive group may share one stratum.
8. ⚠️ Do not call a program stratified merely because one negative edge appears acyclic by itself; check its return path through all rules.
9. Independently verify every assigned inequality. For a small fixture, enumerate candidate stratum maps to confirm both accepted and rejected outcomes; report that exhaustive check as bounded evidence.
10. Deliver safety findings, signed dependency witnesses, stratum assignment or rejection, rule-set coverage and release handoff. Do not derive facts or claim engine compatibility from this audit.

The Python 3 reference uses rules `(rule_id, head_predicate, head_variables, body_atoms)`; each body atom is `(sign, predicate, variables)` where sign is `+` or `-`. Variable lists and body lists are tuples. This notation has no constants or function symbols. Run the complete snippet and record the observed interpreter version.

```python
from itertools import product

def inspect(rules):
    ids, predicates, dependencies, unsafe = set(), set(), [], []
    for row in rules:
        if type(row) not in (tuple, list) or len(row) != 4:
            raise ValueError("invalid rule shape")
        rid, head, hvars, body = row
        if (type(rid) is not str or not rid or rid in ids or
            type(head) is not str or not head or
            type(hvars) is not tuple or type(body) is not tuple):
            raise ValueError("invalid rule identity or fields")
        ids.add(rid)
        predicates.add(head)
        if any(type(v) is not str or not v for v in hvars):
            raise ValueError("invalid head variable")
        positive, needed = set(), set(hvars)
        for atom in body:
            if type(atom) not in (tuple, list) or len(atom) != 3:
                raise ValueError("invalid atom shape")
            sign, pred, variables = atom
            if (sign not in ("+", "-") or type(pred) is not str or not pred or
                type(variables) is not tuple or
                any(type(v) is not str or not v for v in variables)):
                raise ValueError("invalid atom fields")
            predicates.add(pred)
            dependencies.append((head, pred, sign, rid))
            if sign == "+":
                positive.update(variables)
            else:
                needed.update(variables)
        for variable in sorted(needed - positive):
            unsafe.append((rid, variable))
    adjacency = {p: [] for p in predicates}
    for head, body, sign, rid in dependencies:
        adjacency[head].append((body, sign, rid))

    def route(start, target):
        queue = [(start, ())]
        seen = {start}
        for node, path in queue:
            if node == target:
                return path
            for nxt, sign, rid in adjacency[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, path + ((node, nxt, sign, rid),)))
        return None

    witness = None
    for head, body, sign, rid in dependencies:
        if sign == "-":
            back = route(body, head)
            if back is not None:
                witness = ((head, body, sign, rid),) + back
                break
    strata = {p: 0 for p in predicates}
    if witness is None:
        for _ in range(len(predicates)):
            changed = False
            for head, body, sign, _ in dependencies:
                required = strata[body] + int(sign == "-")
                if strata[head] < required:
                    strata[head], changed = required, True
            if not changed:
                break
        if not all(strata[h] >= strata[b] + int(s == "-")
                   for h, b, s, _ in dependencies):
            raise ValueError("stratum constraints not satisfied")
    return unsafe, witness, strata if witness is None else None, dependencies

def brute_possible(predicates, dependencies):
    names = sorted(predicates)
    for values in product(range(len(names)+1), repeat=len(names)):
        ranks = dict(zip(names, values))
        if all(ranks[h] >= ranks[b] + int(s == "-")
               for h, b, s, _ in dependencies):
            return True
    return False

rules = (
    ("r1", "reach", ("X", "Y"),
     (("+", "edge", ("X", "Y")),)),
    ("r2", "reach", ("X", "Z"),
     (("+", "reach", ("X", "Y")),
      ("+", "edge", ("Y", "Z")))),
    ("r3", "allowed", ("X", "Y"),
     (("+", "reach", ("X", "Y")),
      ("-", "blocked", ("X", "Y")))),
)
unsafe, witness, strata, deps = inspect(rules)
assert unsafe == [] and witness is None
assert strata["allowed"] > strata["blocked"]
assert brute_possible({x for h, b, _, _ in deps for x in (h, b)}, deps)
bad = rules + (("r4", "blocked", ("X", "Y"),
                (("+", "allowed", ("X", "Y")),)),)
_, cycle, ranks, bad_deps = inspect(bad)
assert cycle and ranks is None
assert not brute_possible({x for h, b, _, _ in bad_deps
                           for x in (h, b)}, bad_deps)
assert ("r3", "X") in inspect((("r3", "allowed", ("X", "Y"),
                             (("-", "blocked", ("X", "Y")),)),))[0]
print("safe recursion, signed cycle and independent strata checks passed")
```

The dependency arrow points from a rule head to a body predicate. An internal negative edge plus a return path makes the strict inequalities impossible. The brute-force verifier is practical only for small fixtures; it does not evaluate facts. A valid stratum assignment says nothing about the truth of source assertions or permission to publish the rule.

## Decision rules
- IF a head or negative variable lacks positive binding THEN reject admission BECAUSE its population is unbound under this notation.
- IF a negative dependency lies on a cycle THEN reject stratification BECAUSE strict rank increase around a cycle is impossible.
- IF recursion uses only positive dependencies THEN permit equal strata BECAUSE no strict step is required.
- IF rule coverage is incomplete THEN qualify the outcome BECAUSE an omitted rule may close a negative cycle.
- IF an external language has different semantics THEN verify its current authoritative specification BECAUSE this neutral contract may not apply.

## Output template
```text
Scope: <rule revision, neutral notation and completeness; maximum 70 words>
Safety: <rule ID | unbound variable, or None>
Dependencies: <head | sign | body | rule ID; complete ledger>
Stratification: <accepted with predicate ranks / rejected / unresolved>
Witness: <negative dependency and return path with rule IDs, or None>
Verification: <inequality and bounded independent check executed/pending>
Limits: <language, execution and source-truth limits; maximum 80 words>
Next action: <rule owner and bounded review; maximum 40 words>
```

## Quality checklist
- [ ] Rule IDs and atom shapes are validated.
- [ ] Head and negative variables are positively bound.
- [ ] Every body predicate creates a signed dependency.
- [ ] Negative-cycle witness closes through actual rule IDs.
- [ ] Accepted ranks satisfy every signed inequality.
- [ ] Positive recursion is not rejected as negative recursion.
- [ ] Bounded independent verification is labeled accurately.
- [ ] No derived-fact or engine-conformance claim is made.

## Anti-patterns
- **Name-based meaning**: infer a rule is safe from its predicate label. Fix: inspect variable occurrence and dependency polarity.
- **One-edge glance**: miss a return path to a negative edge. Fix: search the full dependency graph.
- **Positive-cycle panic**: reject harmless positive recursion. Fix: require a negative edge on the cycle.
- **Unbound negative query**: accept variables only in a negated atom. Fix: require positive binding.
- **Engine claim**: equate neutral admission with platform support. Fix: verify the actual language contract separately.

## Worked example
**Input:** Fictional Team Cedar supplies rules r1–r3 in the snippet under the neutral notation. It wants a pre-execution admission check, not derived facts.

**Output:**
```text
Scope: Cedar exercise C1; complete r1–r3 neutral rule set; no external rule engine assumed.
Safety: None; X/Y/Z in heads and negative atoms have positive body binding.
Dependencies: reach | + | edge | r1; reach | + | reach | r2; reach | + | edge | r2; allowed | + | reach | r3; allowed | - | blocked | r3.
Stratification: Accepted; edge=0, blocked=0, reach=0, allowed=1.
Witness: None.
Verification: Signed inequalities and bounded independent rank enumeration executed for C1.
Limits: Rule syntax only; no source facts evaluated or engine compatibility established.
Next action: Rule owner reviews intended relation meanings before a separate execution test.
```

**Bad output:** “The recursive reach rule makes the program invalid, so remove it.”
Positive recursion has no negative dependency cycle in this fixture.

## Edge cases
- **Negative cycle**: return the negative edge and actual return path; do not assign ranks.
- **Unbound negative variables**: reject safety even if dependency ranks exist.
- **Duplicate rule ID**: reject before a map overwrites one rule.
- **Malformed atom**: reject rather than guessing missing sign or variable tuple.
- **Empty rule set**: return empty dependency ledger and assignment under an explicitly empty scope.

## Test case
**Input:**
> Fictional rules define reach from edge, recursively extend reach, and define allowed from reach and not blocked. Then add blocked from allowed. Audit safety and stratification without deriving facts.

**Assertions:**
1. Accepts the original positive recursion and safe negation with allowed above blocked.
2. Rejects the added program with a negative-edge cycle witness involving allowed and blocked.
3. States which rule IDs establish both directions of the cycle.
4. Does not claim an external engine executed or approved the rules.
