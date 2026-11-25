# GRF-024 independent review
Reviewer g23_reviewer, 2026-11-14; registry untouched.
Read complete candidate and author evidence, AGENTS/SPEC already read in this reviewer session. Inspected actual GRF-014 schema/reopen procedure, GRF-016 versioned replay procedure and TDV-004 isolated restoration procedure. G24 adds reconciliation against an independent snapshot/log boundary plus identity/property/query-visible state disagreement. It does not implement replay or database durability. Distinct within these selected neighbors; no full-catalog uniqueness guarantee.

Executed embedded snippet under Python 3.14.6. Independently checked wrong snapshot identity, wrong applied-log position, changed node property, changed edge property, equal-count edge identity replacement (e2 missing/e9 unexpected), dangling e7 endpoint Z and stale query e8. All assertions passed. Original stale parallel-edge fixture also passed. Prevalidated extracts and complete manifest assumptions remain explicit. The reference does not check log continuity, source truth or live index configuration.

## Ordinary scenario
Input: fictional complete independent S/4 manifest and identical primary restore, outgoing view omits parallel edge e2; operational timings unavailable.
```text
Boundary: Target S/4 and observed S/4 agree.
Evidence: Complete fictional identity/property manifest; supplied isolated extracts; outgoing view revision unknown; no live restore observed.
Reconciliation: Nodes/edges/properties/endpoints match; A view contains e1 but expected e1,e2; view differs from primary and target.
Repair rehearsal: Fixture recomputation executed and equality confirmed; actual service index rebuild pending authorization and observation.
Objectives: Targets and duration/loss measures absent; compliance unresolved.
Readiness: Blocked; stale service view and consumer probes unresolved.
Next action: Service owner identifies derived-view dependency and supplies isolated rebuild results plus timing/loss evidence.
```

## Missing-input scenario
Input: a graph extract is called restored but no expected boundary or independent manifest is provided.
```text
Boundary: Target snapshot/log boundary unavailable; no boundary readiness verdict.
Evidence: Supplied extract only; independent target manifest and restore observation absent.
Reconciliation: No target equality established; self-consistency checks cannot certify recovery.
Repair rehearsal: Pending defined recovery target and authorized procedure.
Objectives: Unknown targets and measurements; no compliance claim.
Readiness: Blocked; boundary, expected evidence and operational checks missing.
Next action: Owner supplies target snapshot/log markers, independent manifest and objective/authority evidence; ask these together before dependent recovery claims.
```

## Adverse scenario
Input: fictional expected edge count matches, restored e7 points to absent Z, cache exposes deleted e8, target log boundary absent.
```text
Boundary: Target log boundary unavailable; observed marker cannot establish intended recovery.
Evidence: Supplied graph/cache observations and equal edge count; independent complete target reconciliation unavailable.
Reconciliation: Endpoint check fails for e7->Z; query cache contains e8 absent from restored primary; matching counts do not establish identities or properties.
Repair rehearsal: Proposed isolated source/edge reconciliation and cache rebuild; neither performed on the service.
Objectives: Loss/time targets and measurements unavailable; compliance unresolved.
Readiness: Blocked; target boundary, dangling relationship and stale query view remain unresolved.
Next action: Owner provides target boundary and expected manifest, adjudicates e7 source correction, then authorizes isolated rebuild and captures query/endpoint recheck evidence.
```

All four Test case assertions satisfied. Every example output field is present. Fictional edge counts, parallel identity distinctions and references are consistent. Claims remain stable equality and explicit recovery-procedure choices, with changing environment behavior delegated to verified environment procedures; no fabricated sources or operational thresholds. Scope excludes production cutover and distributed durability. No required repairs found; recommend acceptance within declared reconciliation scope.
