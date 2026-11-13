# GRF-012 independent review

Reviewed 2026-11-14 by rank_review. Decision: accept for coordinator ingestion and validation; no blocking finding. Only this review log was changed. These are reviewer applications and executed fixtures, not a separately measured model benchmark.

## Scope and selected-neighbor comparison

Read AGENTS.md, SPEC.md, the full GRF-012 draft, and actual input/procedure/rule sections of TAN-008, BST-004 and GRF-007 after sf.py metadata lookup. TAN-008 varies generic scenario inputs and reports a decision boundary. BST-004 compares strategic criteria and stakeholder weights. GRF-007 computes weak connectivity and filter explanations. None supplies the restart-walk transition model, dangling-row handling, residual error certificate or certified ordering-reversal artifact of GRF-012. This is a targeted substantive comparison, not an exhaustive global uniqueness proof.

## Mathematical and claim audit

The reference normalizes positive outgoing-weight rows and replaces zero-total rows with the supplied prior. Each resulting row is a probability distribution. If P denotes that row-stochastic transition matrix, then the update is T(x)=(1-a)p+a*xP. For any two vectors, the triangle inequality and row sums give ||(x-y)P||_1 <= ||x-y||_1. Thus T is a contraction with factor at most a for 0 <= a < 1. The simplex is preserved, and the unique fixed point x* satisfies ||x-x*||_1 <= ||T(x)-x||_1 + a||x-x*||_1. Rearrangement proves the stated residual/(1-a) bound.

The code returns x after the requested number of updates, separately computes following=T(x), and uses their difference. Its certificate therefore bounds the returned x, exactly as the prose says. It does not accidentally attach a previous-iterate bound to another vector. Each coordinate error is at most the total-error bound, so a gap strictly greater than twice that bound certifies the sign. This is conservative but correct. Equality at the threshold stays unresolved. Equal approximate coordinates with nonzero error do not establish an exact tie; equal coordinates with zero residual do.

The code's exact rational arithmetic supports this certificate without floating-point rounding assumptions. The skill explicitly requires a separately justified certificate for floating-point adaptations. Nonnegative integer weights, fixed node universe, accepted dangling policy and supplied restart values are input contracts rather than platform defaults. Zero prior mass need not imply zero final score because incoming transitions can transfer mass. Scenario bundles do not isolate individual causal contributions. No unsupported influence, real-world importance, current platform behavior or universal perturbation threshold is asserted.

## Actual execution evidence

Extracted and executed the exact Python fence from the draft on Python 3.14.6. Observed output:

```text
certified reversal, dangling redistribution and budget uncertainty passed
closed-form dangling-cycle bound and relation cases 48
zero-prior receiving node ({'A': Fraction(3, 4), 'B': Fraction(1, 4)}, Fraction(1, 2))
zero-weight, equality-boundary and exact-tie checks passed
seven invalid-input cases rejected; inputs unchanged
runtime 3.14.6
validation ([], [])
```

The 48 independent cases used A-to-B with B dangling, prior concentrated at A, continuation values 0, 1/2, 3/4 and 9/10, and update counts zero through eleven. The independently derived fixed point is A=1/(1+a), B=a/(1+a). Every returned vector's actual total absolute error was no larger than its certificate; every certified ordering agreed with that fixed point. This tests the bound against an analytic solution rather than the author's comparison oracle.

Additional checks covered all-zero outgoing weights, exact ties, equality at the ordering-certification boundary and input nonmutation. Seven invalid cases rejected continuation one, negative continuation, a prior summing to two, negative edge weight, unknown endpoint, duplicate edge identity and a Boolean iteration budget. Tuple shapes/string-field prevalidation remains the documented caller responsibility. No production graph, floating-point implementation or large-scale runtime was tested.

## Ordinary procedural application

Input: the fictional Juniper two-node fixture, uniform restart, continuation one-half, baseline p:A->B and q:B->B, alternate p:A->A and q:B->A, one update per run, fixed node inventory.

```text
Scope: Juniper supplied two-node graph; fixed universe A/B; external coverage unverified.
Model: Directed unit weights; prior A=1/2,B=1/2; continuation 1/2; dangling redistribution follows prior.
Scenarios: base p:A->B,q:B->B; alternate p:A->A,q:B->A; both changes supplied as one bundle.
Scores: base A=1/4,B=3/4,total-error bound=0; alternate A=3/4,B=1/4,total-error bound=0.
Comparisons: A/B | below | above | certified reversal.
Checks: Exact snippet executed; nonnegative mass sums to one; residuals zero; sign checks passed.
Interpretation: The ordering reverses under the supplied two-edge bundle; no individual-edge causality or real importance established.
Next evidence: Supply isolated scenarios only if individual-change attribution is needed.
```

The fixture arithmetic is exact: each score pair sums to one and each gap has magnitude one-half, exceeding the zero error allowance.

## Missing-input application

Input: “Rank this graph robustly,” with a graph sketch but no score contract or scenarios.

Response: “What direction and weight meaning, restart distribution, continuation fraction and dangling policy define the intended walk? Which exact graph changes should be compared, and is the node universe fixed? What iteration budget and pairwise or selection decision should the comparison support?”

Three grouped questions in one message. No platform default or invented perturbation range is supplied. Computation and ranking remain pending until the required model is specified.

## Numerical and projection edge application

Input: fictional A/B, no edges, uniform prior and continuation one-half; then switch to the baseline fixture but permit zero updates, asking for a winner from the sorted output.

```text
Scope: Supplied fixed A/B universe only.
Model: Uniform restart, continuation 1/2, dangling rows redistribute to restart.
Scenarios: empty edges; baseline p:A->B,q:B->B with zero updates.
Scores: empty A=1/2,B=1/2,error=0; zero-update baseline A=1/2,B=1/2,error=1.
Comparisons: A/B | exact tie in empty graph | unresolved in zero-update baseline.
Checks: Embedded reference assertions executed; dangling mass preserved. Baseline residual is 1/2, so its bound is (1/2)/(1/2)=1.
Interpretation: Equal displayed scores have different certainty states. No winner follows from alphabetical sorting or the incomplete iterate.
Next evidence: Additional updates are decision-dependent; do not claim numerical uncertainty proves scenario sensitivity.
```

All published test assertions hold. Filtering all positive outgoing weight would likewise require rebuilding transitions and using the agreed dangling policy, not retaining stale denominators. Population changes remain a separate comparison-scope issue, not an inferred rank reversal.
