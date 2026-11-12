# Independent GRF-002 review

Reviewed 2026-11-12 by review_graph02. This is an independent reviewer application of the draft, not a separate model benchmark or live database test. No registry status was changed.

## Scope and uniqueness

Read the full GRF-002 draft, AGENTS.md, SPEC.md, and selected comparison skills returned by sf.py: TDQ-001 and MSL-008. TDQ-001 diagnoses row-key uniqueness and legitimate repeated observations. MSL-008 distinguishes duplicate business listings from co-located businesses and prepares owner/platform cases. Neither provides transitive cannot-link adjudication, canonical endpoint rewriting, newly created self-loop disposition, or reversible graph merge impact. GRF-002 has a substantively distinct artifact and procedure. A lexical `sf.py search merge` returned no catalog matches; this is supporting discovery, not proof of global uniqueness.

## Executed code checks

Extracted and executed the Python fence directly from the draft using Python 3.14.6. Observed output:

```text
conflicting_pairs=1 preserved_edges=3 new_self_loops=1
transitive conflict: block A-B-C; A-C cannot-link remains true
no supported pairs: preserve 3 separate nodes
duplicate reciprocal proposals: terminates and yields one group
```

The first line is the supplied fixture after its assertions passed. Additional reviewer assertions checked that A-B and B-C produce a common group containing A/C, no pairs preserve three groups, and reciprocal duplicate proposals terminate with one final group. `tools.sf.validate_text` returned empty errors and warnings. This is direct draft validation, not registry acceptance. The helper is a small fixture and does not implement property arbitration, reachability queries, mutation, or recovery.

## Ordinary scenario applied

Fictional input: snapshot S1 has organization nodes a,b,x; supplied record R establishes a/b identity; owner selects a; no conflicting properties. Complete incident list e1:a->x and e2:b->x represents two distinct events. Policy allows parallel events, forbids self-loops, and places no degree cap. Requested query is outgoing event count of the combined identity. Source snapshot and reverse mapping are available; execution is not requested.

```text
Scope: S1; organization identities; supplied complete incident-edge fixture.
Identity decisions: a/b | record R | same; x separate, no merge proposed.
Mapping: a->a; b->a; x->x | supplied owner choice; proposal only.
Properties: No conflicts in supplied fixture; retain original records.
Edges: e1 a->x becomes a->x, retain event; e2 b->x becomes a->x, retain distinct event.
Checks: event IDs 2->2, pass; new self-loops 0, pass; combined outgoing events 2->2, pass by direct fixture enumeration; degree cap not required by supplied policy.
Recovery: S1 and original endpoint records retained; reverse mapping a->{a,b}, x->{x} supplied.
Decision: Ready for owner approval within supplied fixture; execution not performed.
```

Checks: did not collapse repeated events, rewrote both endpoints, preserved recovery references, and separated a ready proposal from execution. Arithmetic was recomputed by enumeration: two old edge identities remain two.

## Missing-input scenario applied

Fictional input: user supplies two same-name nodes and asks for a merge; no entity definition, identity evidence, or incident relationships are supplied.

Reviewer response:

```text
What does each node represent, including source namespace and time/version scope?
What evidence establishes the same entity or requires them to remain distinct?
Can you supply the snapshot with incident edges and the canonical-ID, property, and relationship policies?

Scope: Supplied name-only suggestion; entity meaning and graph coverage unknown.
Identity decisions: proposed pair | matching label only | unresolved.
Mapping: No canonical selection; preserve both original IDs.
Properties: Not supplied; reconciliation unrun.
Edges: Not supplied; endpoint preview unrun.
Checks: Identity, relationship constraints, and queries unrun.
Recovery: Snapshot and recovery evidence unavailable.
Decision: Incomplete; retain separate nodes pending the requested evidence.
```

Checks: three questions, no invented sameness, no arbitrary canonical selection, and unperformed checks remain unrun.

## Conflicting-chain edge scenario applied

Fictional input: same-entity proposals A-B and B-C conflict with supplied authoritative distinctness record D for A-C. Each has one event edge to X. User requests merging and collapsing shared endpoints.

```text
Scope: Supplied A/B/C/X fixture; proposed identity chain; no live changes.
Identity decisions: {A,B,C} | A-B and B-C proposals contradict A-C record D | unresolved conflicting group; A-C distinct.
Mapping: Blocked for A/B/C; retain original IDs.
Properties: Not supplied; arbitration unrun.
Edges: Preserve all three original event identities and endpoints; no consolidation justified by shared X.
Checks: Cannot-link within proposed group fails; code group check confirms A and C would share a group; downstream query checks unrun.
Recovery: Original fixture retained; production snapshot/recovery evidence not supplied.
Decision: Blocked; owner must adjudicate contradictory identity evidence before any merge preview is approved.
```

Checks: blocked the entire group, did not greedily accept a pair, preserved original edges, and did not promote similarity or user preference over contradictory evidence.

## Specific-claim review and decision

Reviewed numerical example claims (three retained edges and one new self-loop), group transitivity, coincident-edge versus event-identity distinction, and recovery limitations. Fixture execution and explicit enumeration support the counts. These are stable algorithmic/procedural claims, with no current platform rules, fabricated citations, or changing external constants. The snippet records the installed interpreter instead of asserting a current release.

Decision: No blocking finding. Accept for coordinator checks. This review supports the stated fixture behavior and selected-neighbor uniqueness; it does not prove universal correctness, full-library uniqueness, real graph completeness, or successful database execution. For larger reviews, preserve complete mappings outside the bounded summary rather than silently omitting records; the draft already requires original IDs and edges to remain recoverable.
