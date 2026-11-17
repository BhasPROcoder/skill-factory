# GRF-009 candidate and author evidence

2026-11-13. Draft weighted-route-cost-verification is ready for independent review; no registry, shared index or progress file was changed.

## Candidate comparison

Read AGENTS.md and SPEC.md in this session. Queried sf.py for SEQ-003 and lexical route/shortest matches. Read actual SEQ-003 and EXP-005 procedures; GRF-006 was read and independently reviewed earlier in this agent session.

- GRF-006 returns minimum-hop bounded reachability and frontier/exhaustion evidence. GRF-009 optimizes a supplied additive weight objective and verifies an edge-identity route against distance labels; a direct edge can lose to a two-edge route.
- SEQ-003 propagates task durations over a prerequisite DAG to obtain a longest completion baseline and total slack. GRF-009 computes a minimum source-to-target edge-cost route on a graph that may contain cycles and does not produce task schedules or slack.
- EXP-005 compares meaning available on exhibition routes. It neither computes route costs nor establishes a weighted optimum. Other route search hits concern administrative or messaging routes and are not computational neighbors.

The candidate fills the approved G09 card with a coherent nonnegative additive-cost implementation. Solver selection rejects nonadditive or negative-weight input rather than silently transforming it. It does not claim to implement negative-edge or negative-cycle solving, time-dependent routing, multiple objectives or safety-critical navigation. No external source code or skill content was copied; no external attribution or license claim is introduced.

## Specific-claim review before saving

Reviewed the nonnegative settlement precondition, equal-weight versus varying-weight distinction, strict-improvement parent rule, zero-cost loops, tie handling, edge-identity continuity and optimality certificate. For every reachable edge, distance[target] <= distance[source] + edge cost supplies a lower-bound argument along any source path, while a witnessed path attaining the target label supplies the matching feasible cost. The zero source label anchors that argument. The code computes all reachable labels, not an early-stopped partial label set. String identifiers and tuple shapes remain an explicit prevalidation boundary.

The fictional example has A-C-D cost 1+4=5, A-B-D cost 2+3=5 and direct A-D cost 8. The deterministic implementation settles C before B and keeps its first equal-cost target witness. The test case has cost 2+3=5 versus direct 9. No current API, external statistic, changing platform rule or production threshold is asserted. Python 3 identifies reference syntax; installed interpreter version below records observation rather than a current release recommendation.

## Actual executions

Direct tools.sf.validate_text returned errors=[] and warnings=[]. Body whitespace word count: 1706.

Extracted and executed the exact code fence using Python 3.14.6. Terminal output:

```text
cost, tie witness, zero-loop, unreachable and source-equals-target passed
test-case, parallel, zero-cycle, reverse-unreachable, nonmutation and 10 rejection fixtures passed
bounded independent relaxation comparisons passed: 6561
direct validation [] []
```

Additional assertions checked the published s/a/t test, unequal parallel edges, a two-node zero-cost cycle, reverse-direction unreachability and input nonmutation. Six invalid weights were rejected: negative integer, fractional value, Boolean, NaN, infinity and None. Four other rejected fixtures covered duplicate inventory IDs, unknown target, unknown edge endpoint and duplicate edge identity.

A bounded independent oracle enumerated all 729 assignments of absent/zero/two cost to the six non-self directed edges on three nodes. For each source, repeated bounded relaxation independently calculated reachable labels, then all three targets were compared with the reference: 729 * 3 * 3 = 6561 comparisons. Every distance map and target cost matched. Self-loops and zero cycles were tested separately. These tests support the finite reference contract, not general malformed-input parsing, production scaling, external graph completeness or real-world route availability.

Independent reviewer ordinary, missing-input and edge applications remain required before acceptance. This author evidence is not an audited registry status.
