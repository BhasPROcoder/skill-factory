---
id: GRF-012
name: restart-walk-rank-sensitivity
domain: Graph Engineering Foundations
subdomain: Ranking sensitivity
version: 1.0
description: Compare graph restart-walk rankings across explicit scenarios while separating certified ordering changes from numerical uncertainty and unsupported importance claims.
triggers: ["test graph rank sensitivity", "check whether graph rankings really reverse", "explain dangling node ranking policy", "separate convergence error from rank changes", "compare graph ranking assumptions"]
not_for: ["generic sensitivity scenario tables [TAN-008]", "strategic option scoring [BST-004]", "weak component diagnosis [GRF-007]", "causal influence estimation or consequential decisions about people"]
requires: []
risk_level: medium
---

# Restart Walk Rank Sensitivity

## Purpose
Compare a baseline graph ranking with explicitly supplied edge, weight or restart-policy scenarios. Produce score evidence and certified pairwise ordering changes without mistaking iteration error, arbitrary tie-breaking or graph coverage changes for meaningful rank instability. Scores describe the declared walk model, not real-world importance or causal influence.

## Inputs to collect
1. **Directed snapshot** — obtain complete scoped node IDs and identified weighted edges. Why: direction and omitted nodes change how score mass moves. Default: supplied graph only; no external completeness claim.
2. **Score contract** — obtain the meaning of weights, restart distribution and continuation fraction. Why: a ranking is conditional on these choices. Default: none; do not borrow a platform's numerical defaults.
3. **Dangling policy** — specify where mass goes from nodes with zero total outgoing weight. Why: deleting that mass breaks the probability model. Default: reference redistributes it through the supplied restart distribution only when explicitly accepted.
4. **Scenario ledger** — obtain exact changed edge IDs, weights, filters or policy values and their evidential basis. Why: several simultaneous changes cannot isolate one cause. Default: no invented perturbation range; retain the baseline unchanged.
5. **Comparison universe** — obtain node identity mapping and requested pairwise or selection decisions. Why: changing the candidate population changes ranks independently of scores. Default: same node inventory across scenarios; label any changed universe separately.
6. **Execution budget** — obtain iteration budget and required certainty for the decision. Why: close scores may need further computation. Default: unresolved ordering when the available error certificate overlaps; no universal tolerance.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the baseline and enumerate each scenario's changes with source evidence, preserving original edge IDs and values.
2. Validate nonnegative finite weights, known endpoints and a nonnegative restart distribution summing to one. Require continuation fraction at least zero and strictly below one.
3. Normalize each positive outgoing-weight row into transition probabilities. Replace a zero-total row using the declared dangling policy; retain zero-weight edges as source evidence rather than pretending they transfer mass.
4. Start from the restart distribution and repeatedly distribute the continuation share through transitions, adding the restart share at each step.
5. Compute an error certificate for the resulting vector before comparing ranks. In the exact reference, the sum of absolute one-step changes divided by one minus the continuation fraction bounds total absolute error from the fixed point.
6. ⚠️ Certify one node above another only when their score gap exceeds twice that error bound. Otherwise label their ordering unresolved; an alphabetical display order is not evidence of a winner.
7. Repeat the same computation and certificate checks for each supplied scenario, preserving its precise transition and restart policy.
8. Compare certified pairwise relations across scenarios. Report a reversal only when both opposite orderings are certified; distinguish an exact tie from an unresolved comparison.
9. Attribute differences to the declared scenario bundle. When several inputs changed, request isolated variants before attributing the reversal to one edge or parameter.
10. Deliver the scenario matrix, uncertainty and interpretation limits. Do not promote stability across a few tested variants into robustness against all missing edges or policies.

The Python 3 reference uses exact rational arithmetic, integer edge weights and a small fixed node inventory. Tuples are `(edge ID, source, target, weight)`; prevalidate tuple shape and string identity fields. Run the entire snippet and record the interpreter version. This transparent finite fixture is not a scalable implementation or a floating-point error certificate.

For returned vector x, let T(x) be one further update and let a be the continuation fraction. Normalized transitions contract absolute-error sum by at most a. Thus distance from x to the fixed point is at most residual plus a times that distance, giving residual/(1-a). The certificate bounds x, not the unreturned T(x). Each coordinate error is no larger than this total bound, so a gap exceeding twice the bound certifies its sign.

```python
from fractions import Fraction as F

def rank(nodes, edges, prior, alpha, steps):
    known = set(nodes)
    if not nodes or len(known) != len(nodes) or set(prior) != known:
        raise ValueError("unique nonempty inventory and complete prior required")
    if any(type(v) is not F or v < 0 for v in prior.values()):
        raise ValueError("nonnegative rational prior required")
    if sum(prior.values()) != 1 or type(alpha) is not F or not 0 <= alpha < 1:
        raise ValueError("normalized prior and continuation in [0,1) required")
    if type(steps) is not int or steps < 0:
        raise ValueError("nonnegative iteration budget required")
    adj = {n: [] for n in nodes}
    ids = set()
    for eid, a, b, w in edges:
        if eid in ids or a not in known or b not in known:
            raise ValueError("duplicate edge or unknown endpoint")
        if type(w) is not int or w < 0:
            raise ValueError("nonnegative integer weight required")
        ids.add(eid)
        adj[a].append((b, w))
    totals = {n: sum(w for b, w in adj[n]) for n in nodes}
    def advance(x):
        y = {n: (1-alpha)*prior[n] for n in nodes}
        for a in nodes:
            if totals[a]:
                for b, w in adj[a]:
                    y[b] += alpha*x[a]*F(w, totals[a])
            else:
                for b in nodes:
                    y[b] += alpha*x[a]*prior[b]
        assert sum(y.values()) == 1 and min(y.values()) >= 0
        return y
    x = dict(prior)
    for _ in range(steps):
        x = advance(x)
    following = advance(x)
    error = sum(abs(following[n]-x[n]) for n in nodes)/(1-alpha)
    return x, error

def relation(scores, error, a, b):
    gap = scores[a]-scores[b]
    if gap > 2*error:
        return "above"
    if gap < -2*error:
        return "below"
    return "tie" if gap == 0 and error == 0 else "unresolved"

nodes = ["A", "B"]
prior = {"A": F(1, 2), "B": F(1, 2)}
base = [("p", "A", "B", 1), ("q", "B", "B", 1)]
alternate = [("p", "A", "A", 1), ("q", "B", "A", 1)]
x, e = rank(nodes, base, prior, F(1, 2), 1)
y, f = rank(nodes, alternate, prior, F(1, 2), 1)
assert (x, e) == ({"A": F(1, 4), "B": F(3, 4)}, 0)
assert (y, f) == ({"A": F(3, 4), "B": F(1, 4)}, 0)
assert relation(x, e, "A", "B") == "below"
assert relation(y, f, "A", "B") == "above"
assert rank(nodes, [], prior, F(1, 2), 1) == (prior, 0)
assert relation(*rank(nodes, base, prior, F(1, 2), 0), "A", "B") == "unresolved"
print("certified reversal, dangling redistribution and budget uncertainty passed")
```

## Decision rules
- IF a score gap overlaps its error allowance THEN withhold the ordering BECAUSE numerical approximation can explain the apparent difference.
- IF the same pair reverses with certified order in both scenarios THEN report scenario-sensitive ordering BECAUSE the change exceeds the computation uncertainty.
- IF filtering removes outgoing mass THEN rebuild normalized transitions and apply the dangling policy BECAUSE retaining stale denominators changes the declared walk.
- IF node populations differ THEN separate population changes from score changes BECAUSE rank positions are not directly comparable across different universes.
- IF several inputs change together THEN attribute the result to the bundle BECAUSE the run does not isolate an individual cause.

## Output template
```text
Scope: <snapshot, node universe and evidence coverage; maximum 70 words>
Model: <direction, weights, restart, continuation and dangling policy>
Scenarios: <ID | exact changes | evidence; complete change ledger>
Scores: <scenario | node | score | total-error bound; full table>
Comparisons: <pair | baseline relation | variant relation | certified/unresolved>
Checks: <mass, residual, execution and input checks; maximum 80 words>
Interpretation: <supported sensitivity and attribution limits; maximum 90 words>
Next evidence: <missing scenarios, precision or coverage; maximum 60 words>
```

## Quality checklist
- [ ] Every scenario preserves or explicitly changes the node universe.
- [ ] Outgoing weights and zero-total rows follow the declared model.
- [ ] Restart probabilities sum to one and continuation is below one.
- [ ] Score mass and nonnegativity were checked.
- [ ] Every reported ordering includes its numerical-certainty status.
- [ ] Exact ties differ from overlapping uncertainty.
- [ ] Edge identities and scenario changes remain recoverable.
- [ ] No importance, causality or universal robustness claim follows from score alone.

## Anti-patterns
- **Default by habit**: reuse an unexplained continuation value. Fix: obtain the intended model.
- **Dangling mass loss**: discard score at zero-outdegree nodes. Fix: apply the declared redistribution.
- **Sorted means certain**: rank tiny differences without error checks. Fix: certify gaps or mark unresolved.
- **Filter without renormalization**: remove edges but retain old probabilities. Fix: rebuild each scenario's transitions.
- **Score becomes influence**: treat stationary mass as causal impact. Fix: state its model-specific meaning.

## Worked example
**Input:** Fictional sandbox Juniper supplies the snippet's two scenarios, uniform restart and continuation one-half. Both edge endpoints change in the alternate. Compare A/B after one update; the node population is fixed.

**Output:**
```text
Scope: Juniper supplied two-node fixture; no external graph coverage claim.
Model: Directed integer weights; uniform restart; continuation 1/2; dangling mass follows restart.
Scenarios: base | p A->B, q B->B | supplied; alternate | p A->A, q B->A | supplied.
Scores: base A=1/4,B=3/4,error=0; alternate A=3/4,B=1/4,error=0.
Comparisons: A/B | below | above | certified reversal.
Checks: Reference verifies mass, fixed-point residual and relations when executed.
Interpretation: Ordering depends on the supplied two-edge change bundle. Neither individual-edge causality nor real importance is established.
Next evidence: Isolate individual changes if that attribution is needed; no additional precision needed for these exact fixtures.
```

**Bad output:** “A became influential because edge p changed; the sorted output proves it.”
This ignores the second changed edge and substitutes causal meaning for a model score.

## Edge cases
- **All weights zero**: every row is dangling; use the accepted redistribution policy, not division by zero.
- **Zero restart mass on some nodes**: retain those nodes; zero prior does not itself prove zero final score.
- **Budget exhausted with overlapping bounds**: report unresolved comparisons and request more computation only if decision-relevant.
- **Floating-point implementation**: obtain a justified numerical certificate; the exact-arithmetic bound alone omits rounding error.
- **Changed population**: report added/removed IDs and align a declared common universe before interpreting rank movements.

## Test case
**Input:**
> Fictional nodes A/B have no edges, uniform restart and continuation one-half. Compare A/B. Then replace the graph with the snippet baseline but allow zero updates. Explain numerical certainty without inventing a winner.

**Assertions:**
1. The empty-edge graph retains both nodes through dangling redistribution.
2. It reports equal half scores with an exact tie for that fixed point.
3. The zero-update baseline comparison is unresolved rather than an exact tie or a certified winner.
4. It makes no influence or external completeness claim.
