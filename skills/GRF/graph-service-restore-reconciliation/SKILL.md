---
id: GRF-024
name: graph-service-restore-reconciliation
domain: Graph Engineering Foundations
subdomain: Graph recovery evidence
version: 1.0
description: Reconcile a restored graph and its query views against a declared recovery boundary when deciding whether an isolated graph service restoration is ready for owner review.
triggers: ["verify restored graph service", "reconcile graph backup recovery", "find stale graph indexes after restore", "check restored relationship evidence", "validate graph recovery boundary"]
not_for: ["generic restore rehearsal planning [TDV-004]", "implementing graph storage [GRF-014]", "applying graph patches [GRF-016]", "production cutover execution", "claiming distributed crash durability"]
requires: []
risk_level: medium
---

# Graph Service Restore Reconciliation

## Purpose
Determine whether a recovered graph represents the declared snapshot and applied-log boundary and whether its query views expose that same state. Produce a discrepancy ledger with graph identities, properties and query witnesses, plus the remaining operational readiness checks. A successful offline comparison does not establish production recovery or durable distributed behavior.

## Inputs to collect
1. **Recovery boundary** — obtain backup identity, snapshot revision and intended applied-log position. Why: matching data from different boundaries can hide lost or repeated changes. Default: unresolved; no readiness verdict without a declared target.
2. **Expected graph evidence** — obtain an independently retained manifest of node and edge identities, endpoints, properties and representative query results at that boundary. Why: restored state cannot certify itself. Default: counts alone support only count checks; missing detailed evidence stays unverified.
3. **Restored artifacts** — collect isolated service identity, observed snapshot/log markers, node and edge extracts, query outputs and derived-view revisions. Why: each can recover to a different point. Default: no restoration or query execution claimed without observations.
4. **Recovery objectives** — obtain owner-approved data-loss and recovery-time targets, measurement origins and service acceptance checks. Why: semantic equality alone cannot establish operational readiness. Default: report measurements only; target compliance unresolved.
5. **Dependency and index inventory** — list query indexes, caches, derived relationships, consumers and rebuild dependencies. Why: visible answers can lag correct primary records. Default: unknown dependencies remain unchecked, not implicitly healthy.
6. **Execution authority** — obtain isolated destination, approved commands, stop conditions and decision owner. Why: diagnosis must not accidentally replace a live graph. Default: offline reconciliation of supplied evidence; production actions remain a separate owner decision.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the target recovery boundary and the independent expected manifest before inspecting restored results.
2. Record the authorized isolated destination and restoration start observation, with the owner's measurement convention.
3. Restore the selected snapshot and apply the authorized log range using the environment's verified recovery procedure; record this step as pending if only extracts are supplied.
4. Compare observed snapshot and applied-log markers with the target boundary before interpreting equality findings.
5. Reconcile node identities and complete agreed properties, preserving missing, unexpected and changed records separately.
6. Reconcile edge identities, endpoints and properties; explicitly test endpoint existence and parallel-edge preservation.
7. ⚠️ Execute the selected application queries against both primary-state expectations and recovered query views; expose stale or incomplete views instead of inferring readiness from matching record counts.
8. Rebuild only the authorized stale derived artifacts in dependency order, retaining the original failure evidence and the resulting build revision.
9. Rerun affected queries and graph invariants after rebuilding, recording remaining differences rather than replacing the original report with a pass label.
10. Compare measured recovery duration and observed loss boundary against owner targets, preserving uncertainty when a marker cannot be translated into elapsed time or lost business events.
11. Deliver a readiness decision with explicit unchecked dependencies, consumer probes and the owner's next action.

This Python 3 reference reconciles prevalidated dictionary extracts, a scalar recovery boundary and a complete outgoing-edge-ID view for every node. Nodes map IDs to property dictionaries; edges map IDs to `(source, target, properties)`. Record the interpreter version when running it. This checks supplied artifacts, not live storage, log continuity, index configuration, authorization, latency or source truth. Extract adapters must reject duplicate IDs before constructing dictionaries; silently overwritten duplicates cannot be detected afterward.

```python
from copy import deepcopy

def outgoing(nodes, edges):
    return {n: sorted(e for e, (s, t, props) in edges.items() if s == n)
            for n in nodes}

def reconcile(expected, restored, observed_view):
    issues = []
    if expected['boundary'] != restored['boundary']:
        issues.append(('boundary', restored['boundary']))
    for kind in ('nodes', 'edges'):
        want, got = expected[kind], restored[kind]
        for key in sorted(set(want) | set(got)):
            if key not in got:
                issues.append((kind, key, 'missing'))
            elif key not in want:
                issues.append((kind, key, 'unexpected'))
            elif want[key] != got[key]:
                issues.append((kind, key, 'changed'))
    for eid, (source, target, props) in restored['edges'].items():
        if source not in restored['nodes'] or target not in restored['nodes']:
            issues.append(('dangling', eid))
    computed = outgoing(restored['nodes'], restored['edges'])
    if observed_view != computed:
        issues.append(('view', 'differs from restored primary graph'))
    if observed_view != outgoing(expected['nodes'], expected['edges']):
        issues.append(('query', 'differs from target boundary'))
    return issues

expected = dict(boundary=('snapshot-S', 4),
                nodes={'A': {'label': 'alpha'}, 'B': {'label': 'beta'}},
                edges={'e1': ('A', 'B', {'kind': 'links'}),
                       'e2': ('A', 'B', {'kind': 'links'})})
restored = deepcopy(expected)
view = {'A': ['e1'], 'B': []}
assert reconcile(expected, restored, view) == [
    ('view', 'differs from restored primary graph'),
    ('query', 'differs from target boundary')]
assert reconcile(expected, restored, outgoing(restored['nodes'], restored['edges'])) == []
broken = deepcopy(restored)
del broken['nodes']['B']
assert ('dangling', 'e1') in reconcile(expected, broken, view)
print('primary equality, stale view and dangling edge checks passed')
```

Use full identity/property equality only when the manifest covers the complete intended scope. For large graphs, label sampled checks as sampled and report the inspected population; matching a sample does not certify all relationships. More application queries may be required than this outgoing-edge fixture, especially queries involving derived relationships, filters or access-dependent views.

## Decision rules
- IF markers disagree THEN withhold boundary readiness BECAUSE matching some records cannot identify the intended recovered revision.
- IF node and edge counts match but identities or properties differ THEN report semantic discrepancies BECAUSE counts discard relationship meaning.
- IF primary records match while query views differ THEN isolate the affected derived artifact BECAUSE correct stored edges do not guarantee correct visible answers.
- IF evidence lacks complete identities THEN limit the verdict to inspected checks BECAUSE unavailable records have not passed reconciliation.
- IF duration or loss targets are absent THEN leave operational target compliance unresolved BECAUSE no universal recovery objective applies.

## Output template
```text
Boundary: <target and observed snapshot/log markers; maximum 60 words>
Evidence: <manifest scope, restore observation, query-view revisions>
Reconciliation: <identity/property/endpoint/query check | result | record witnesses>
Repair rehearsal: <authorized action | observed result or pending>
Objectives: <owner targets | measured duration/loss | unresolved conversion>
Readiness: <ready for owner review / blocked | unchecked dependencies>
Next action: <owner | action | required completion evidence; maximum 70 words>
```

## Quality checklist
- [ ] Expected evidence is independent of the restored extracts.
- [ ] Snapshot and applied-log markers name the same intended boundary.
- [ ] Identities and properties are compared beyond counts.
- [ ] Endpoint integrity and parallel-edge identities are checked.
- [ ] Query views are compared with primary and target state.
- [ ] Repairs preserve prior discrepancy evidence.
- [ ] Duration and loss conclusions use supplied measurement conventions.
- [ ] Operational and untested scope remain explicit.

## Anti-patterns
- **Self-certified restore**: derive expectations from restored data. Fix: retain independent boundary evidence.
- **Count-only approval**: equal totals imply correct graph. Fix: compare identities, properties and application queries.
- **Stale-view blindness**: primary rows pass so all queries pass. Fix: inspect actual query outputs and derived revisions.
- **Marker arithmetic**: subtract log positions and call it elapsed downtime. Fix: use the declared time and loss measurement conventions.
- **Unobserved recovery claim**: a fixture becomes proof of live recovery. Fix: label offline and operational evidence separately.

## Worked example
**Input:** Fictional service Birch supplies the snippet target and identical restored primary graph at snapshot-S position 4. Its observed outgoing view omits e2. Only offline extracts are available; recovery objectives and live restoration timing are absent.

**Output:**
```text
Boundary: Target snapshot-S/4; supplied restored marker snapshot-S/4.
Evidence: Complete fictional manifest; identical node/edge extracts; supplied outgoing query view, build revision unavailable; live restoration unobserved.
Reconciliation: Identities/properties/endpoints match supplied target; A query returns e1 instead of e1,e2; primary and target view comparisons fail.
Repair rehearsal: Recompute outgoing view in isolated fixture; rerun available snippet to confirm equality; service index rebuild pending.
Objectives: Owner targets and duration/loss measurements absent; compliance unresolved.
Readiness: Blocked; stale query view, actual index rebuild and consumer probes unverified.
Next action: Service owner identifies stale view dependency, authorizes isolated rebuild and supplies matching query results plus objective measurements.
```

**Bad output:** “Two nodes and two edges restored, so recovery succeeded.”
This ignores the missing query-visible edge and the absent operational evidence.

## Edge cases
- **Extra recovered log range**: treat a newer marker as a boundary mismatch; request owner disposition rather than silently accepting it.
- **Property normalization differences**: agree comparison semantics before reconciliation; retain original values and conversion evidence.
- **Empty intended graph**: require a manifest explicitly declaring emptiness; missing extraction output is not an empty graph.
- **Consumer-specific query views**: test each declared access context separately without copying its credentials into the report.
- **Failed rebuild**: preserve primary data and failure evidence; report blocked readiness rather than deleting relationships to match the stale view.

## Test case
**Input:**
> Fictional restore has expected edge count, but e7 points to absent node Z and the query cache still exposes deleted edge e8. The target log boundary is unavailable. Produce a readiness report.

**Assertions:**
1. Reports e7 as a dangling-edge witness and e8 as a query-view discrepancy.
2. Does not infer success from matching edge counts.
3. Blocks boundary readiness pending a declared target.
4. Distinguishes proposed isolated repair from performed recovery.
