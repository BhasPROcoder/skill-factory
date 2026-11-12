# GRF-004 independent review

Reviewer: review_graph01. Decision: accept for coordinator ingestion and validation; no blocking change identified. No registry or skill mutation performed.

## Scope and substantive distinctness

Read draft, author evidence and actual GRF-003 and ARC-002 procedures, with sf.py metadata lookup; GRF-001 and SEQ-001 actual procedures were already inspected in this review session. GRF-001 chooses representations from questions and role semantics. GRF-003 reconciles imported identities and rows. ARC-002 chooses provenance-respecting descriptive placements and merely calls for structural checks. SEQ-001 finds a cycle or prerequisite order. GRF-004 provides a different artifact: explicit-root forest conformance, full incoming-edge witnesses and unreachable inventory, with an evidence-bound repair preview. It does not repeat cycle enumeration or select archival parents. This is a targeted neighbor comparison, not an exhaustive library uniqueness proof.

## Mathematical claim review

For the stated finite directed parent relation, roots with indegree zero, every other node with indegree one, and reachability from declared roots are sufficient for a rooted forest. A reachable directed cycle would require either a root on the cycle (violating its zero indegree) or an entry from outside the cycle (giving the entry node a second incoming edge). Thus cycles cannot survive all checks. Indegree at most one also prevents two rooted paths from merging at a non-root. Each reachable component therefore has its unique declared root. Requiring one tree additionally requires one root; step 3 explicitly supplies that condition. The helper intentionally checks a forest, not that separate one-tree requirement.

Parallel identified edges count separately under this contract, even with the same endpoints. Empty snapshots require a separate declared policy and are rejected by the example helper. Non-string fields and malformed tuple shapes are caller-prevalidation requirements, not claimed helper capabilities. Structural validity is expressly distinguished from truthful parent assignment and deployment.

## Executed evidence

Executed the exact Python fence with Python 3.14.6. tools.sf.validate_text returned errors=[], warnings=[]. Additional terminal observations:

```text
disconnected-cycle, repaired-preview and multiple-parent checks passed
multi-parent all-reachable {'parent_violations': {'A': ['p', 't']}, 'unreachable': []}
root-parent {'parent_violations': {'r': ['z'], 'a': []}, 'unreachable': ['a']}
parallel {'parent_violations': {'a': ['p', 'q']}, 'unreachable': []}
orphan {'parent_violations': {'a': []}, 'unreachable': ['a']}
self-loop {'parent_violations': {}, 'unreachable': ['a']}
singleton {'parent_violations': {}, 'unreachable': []}
two-roots {'parent_violations': {}, 'unreachable': []}
rejected nonempty unique node inventory required
rejected nonempty unique node inventory required
rejected explicit unique known roots required
rejected explicit unique known roots required
rejected unknown endpoint
rejected edge identities must be unique
independent input and no-mutation checks passed
```

The six rejected fixtures were empty inventory, repeated node ID, no roots, unknown root, unknown endpoint and repeated edge ID. An assertion confirmed the R/S/A/B input lists were unchanged by the function. The two-root output is a valid forest only; it does not pass a single-tree contract. No production graph was accessed or changed.

## Independent procedural scenarios

These outputs were produced by this reviewer applying the skill, not by a separately measured model benchmark.

### Ordinary complete snapshot

Input: fictional revision F1, complete inventory R/S/A/B, roots R/S, forest allowed, parent edges p:R->A, q:S->B, t:B->A, no evidence selecting p or t.

```text
Scope: F1 complete fictional snapshot; parent-to-child relation only.
Contract: Roots R and S; forest allowed; nonempty snapshot.
Input exceptions: None.
Local witnesses: A | expected 1 | observed p,t.
Global witnesses: None; all inventory nodes reachable.
Verdict: Fail for complete F1 because A has two parent edges.
Repair proposal: No approved edge change; owner must supply parent evidence to adjudicate p/t. Preserve both records.
Rerun: F1 executed; A violates incoming count and unreachable list is empty. Repaired snapshot unrun; no supported alternative supplied.
Limits: No semantic parent selection, live mutation or deployment established.
```

Result: satisfies all published test assertions without interpreting reachability alone as a pass.

### Required contract missing

Input: "Check this hierarchy" with a few edge pairs but no node inventory, root policy or direction/completeness statement.

Output: "Please provide the complete node inventory and snapshot revision. Which relation direction and roots define the contract, and is one tree or a forest required? Is the supplied node/edge snapshot complete for that scope?"

Result: a single message with three questions; no invented roots, implied node inventory, or full-graph verdict.

### Partial orphan extract

Input: fictional extract P1 has inventory r/a, root r, no edges, declared partial coverage; parent-to-child tree intended and no correction evidence.

```text
Scope: P1 fictional partial extract; parent-to-child relation.
Contract: Root r; one tree intended; nonempty snapshot.
Input exceptions: None within supplied inventory; parent-edge completeness unresolved.
Local witnesses: a | expected 1 | observed no incoming edge IDs.
Global witnesses: a.
Verdict: Fail for the supplied extract; full-snapshot status unresolved because missing extraction data may explain the apparent orphan.
Repair proposal: No edge addition inferred. Source owner must supply the missing coverage or complete record before adjudicating a's parent.
Rerun: P1 executed; a has zero incoming edges and is unreachable. Full snapshot and repaired preview unrun.
Limits: No full-domain orphan claim, semantic parent selection or live change established.
```

Result: preserves extract evidence while refusing to conclude that the real parent is absent.

### Single-tree policy beyond helper

Input: fictional complete inventory r/s, both declared roots, no edges, but exactly one tree is required.

Output: local witnesses none; unreachable none; contract failure because two declared roots conflict with the supplied one-tree requirement. The executed helper's empty findings apply to a forest; step 3's additional root-count rule rejects this request. No root or node deleted to force a pass. Owner must reconcile the conflicting policy.

## Claim and boundary review

The four-node/three-edge example arithmetic is correct and its disconnected cycle invalidates a tree despite the aggregate total. Root/self-loop and isolated-root cases agree with the executed fixtures. No external law, price, standard, API currency or invented citation appears. Repair operations are proposals until evidence and authorization exist; approved changes apply to a separate preview followed by full rechecking. No blocking finding. Structural registry status remains the coordinator's responsibility.
