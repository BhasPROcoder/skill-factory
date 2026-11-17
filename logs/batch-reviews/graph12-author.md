# GRF-012 author evidence

2026-11-13. Candidate held for independent review; no registry mutation. Author owns the skill, graph_g12 manifest and this log only.

## Scope and comparison

Read AGENTS.md, SPEC.md and the ordered queue. Used sf.py searches for ranking, centrality, sensitivity and metrics. Read TAN-008 fully and the actual procedures of BST-004, MME-001 and GRF-007. TAN-008 varies generic scenario inputs and reports decision-boundary changes; BST-004 compares strategic criteria and weight choices; MME-001 defines comparable metrics; GRF-007 evaluates weak partitions under filtering. None constructs restart-walk probabilities, handles dangling-row score mass, certifies iterative rank comparisons or distinguishes approximation uncertainty from a graph ranking reversal.

The distinct artifact is a scenario-specific score matrix with an exact residual certificate and certified/unresolved pairwise ordering comparison. A weighted-degree sort was considered too close to a generic sensitivity table; this candidate instead exposes graph transition normalization and the numerical-certainty decisions required before reporting rank movement. Its boundaries exclude causal influence and consequential decisions about people.

## Primary-source verification and originality

Consulted the official [NetworkX PageRank documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html) for restart, damping, dangling redistribution and iteration concepts. No library code, default parameters or release/version claims are copied into the skill. The reference is original plain Python with exact Fraction arithmetic and an explicitly supplied model. The source's library stopping tolerance is not used as a mathematical certificate.

## Specific-claim audit before saving

Reviewed all score and error statements against the following argument. For a nonnegative normalized transition operator P and continuation a in [0,1), T(x)=(1-a)p+aP(x) contracts the L1 distance by at most a. For its unique fixed point z, triangle inequality gives ||x-z|| <= ||x-T(x)|| + a||x-z||. Thus residual/(1-a) bounds the returned x's total absolute error. Each coordinate's error is at most that bound; a pair gap strictly greater than twice the bound certifies its sign. Equality or overlap does not certify an order. If residual is exactly zero, equal coordinates are an exact tie. The implementation uses rational arithmetic, so floating-point roundoff is explicitly outside its certificate.

All weights and probabilities in examples are fictional, user-supplied fixture choices, not recommended defaults. Baseline transitions both lead to B, giving A=1/4,B=3/4 for uniform restart and continuation 1/2; the alternate transitions both lead to A and swaps those values. Both fixed points are reached after one update from the prior. All-zero rows redistribute via the prior. A zero-update baseline has equal tentative values but a nonzero residual certificate, so the relation is unresolved. No iteration count is claimed sufficient universally. No source/price/law/platform behavior is invented or hardcoded as current.

## Actual executions

Extracted the entire Python fence and executed it using Python 3.14.6. tools.sf.validate_text returned errors=[] and warnings=[] before the short derivation clarification; the final check is recorded below separately. Initial body count was 1663 words.

Observed stdout:

```text
certified reversal, dangling redistribution and budget uncertainty passed
exact two-node stationary oracle comparisons 2916
nonmutation and seven invalid-input fixtures passed
```

The independent oracle enumerated 81 assignments of weights 0/1/2 to the four possible directed edges on two nodes, four prior choices, three continuation values and three iteration budgets: 81*4*3*3=2916 cases. For first-node transition probabilities u from A and v from B, exact stationary first-node mass was solved algebraically as ((1-a)*p+a*v)/(1-a*(u-v)). Every returned L1 error lay inside its certificate, and every certified ordering/tie matched the exact solution. This includes self-loops, zero-total rows and priors with zero mass on a node. No library implementation served as the oracle.

Additional assertions confirmed nonmutation of node/edge/prior inputs. Seven rejected fixtures were continuation one, negative continuation, Boolean budget, negative weight, unknown endpoint, duplicate edge identity and non-normalized prior. All raised ValueError. String fields and tuple shape remain documented prevalidation requirements. These checks do not establish production scaling, real graph completeness or general floating-point convergence.

Independent ordinary, missing-input and edge-scenario review remains required before acceptance.

After adding the explicit contraction derivation and returned-iterate clarification, final tools.sf.validate_text again returned errors=[] and warnings=[]; final body word count1736. Reexecuting the unchanged complete snippet again passed its assertions and emitted the certified-reversal/dangling/budget message.
