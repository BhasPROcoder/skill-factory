# GRF-016 independent review

Reviewer: community_review, 2026-11-14. The draft was treated as unverified because author execution had been interrupted. Decision: accept for coordinator checks; no blocking finding. Only this review log was changed for G16. No registry, commit or push action performed.

## Completeness and distinctness

Read the complete draft against AGENTS.md and SPEC.md. All required sections, worked example and test assertions are present. Direct tools.sf.validate_text returned errors=[] and warnings=[]; whitespace body count 1615.

Used sf.py metadata and read actual inputs/procedures for TAP-005, TDE-001, GRF-003 and GRF-005. TAP-005 defines API request-key/payload behavior; TDE-001 defines logical-event deduplication and atomic target-write handling. GRF-003 reconciles an initial edge-list import, and GRF-005 selects historical assertions by two clocks. G16's distinct artifact is an executable ordered node/edge patch transition with a whole-graph expected version, explicit incident-edge deletion order, copy-isolated late-failure rejection and replay retaining newer state. Shared idempotency principles are appropriate prerequisites to that different operational deliverable. This is a bounded neighbor comparison, not a universal uniqueness claim.

## Executed evidence

Extracted the exact Python fence and executed on Python 3.14.6. Embedded output: `ordered deletion, exact replay and whole-batch rejection passed`.

Independent executions used base version 4, nodes X/Y and edge e:X-to-Y:

- The published test, node+ Z then node- Y, rejected because Y remained referenced. Deep equality confirmed original nodes, edge, version and receipt ledger unchanged; Z was absent and no success receipt existed.
- Ordered edge- e then node- Y accepted at version 5, leaving X and no edges. The version-4 base remained unchanged.
- Exact repeat returned replay and unchanged version-5 state.
- A later accepted patch added Z and edge z:X-to-Z at version 6. Replaying the earlier delete envelope returned this current version-6 state unchanged, rather than restoring its old result.
- Reusing the accepted event with reversed operation order raised payload conflict. Reusing it with a changed expected version also raised payload conflict.
- A new event with obsolete expected version raised stale-version rejection.
- Reversing the original deletion order rejected the referenced node.
- Adding Z before an edge with an unknown endpoint rejected the entire candidate; deep equality confirmed no partial node addition.
- Adding Z before reusing existing edge ID e rejected the candidate, preserving the base.
- Deleting an unknown edge and submitting an empty patch each rejected.
- Adding a separately identified parallel X-to-Y edge and Y self-loop accepted with all three edge identities retained, under the explicitly permitted reference policy.

Nine negative fixtures printed their expected rejection messages. Deep-copy comparisons guarded state nonmutation for each rejection, and successful-preview checks confirmed the original base remained intact. The helper requires prevalidated tuple shapes/string identities and trusted consistent input state, as stated; it is not a malformed-input parser. No storage engine, concurrency, persistence, cryptographic signing or external system was tested.

## Independent procedural scenarios

These are reviewer applications, not a separate model-service benchmark.

### Ordinary accepted preview and retry

Input: fictional revision 4 with X/Y and e:X-to-Y; authorized offline proposal has event removeY, expected 4, operations edge- e then node- Y. Retained receipt history is empty and trusted.

```text
Scope: Fictional version 4; explicit edge deletion required before referenced-node removal; offline preview.
Envelope: removeY | expected 4 | edge- e, then node- Y | supplied operation records.
Preconditions: Trusted empty receipt ledger; expected version equals base; e is Y's only incident edge.
Candidate: Remove e and Y; retain X.
Outcome: Accepted preview at version 5. Identical repeat is replay with version 5 unchanged.
Verification: Executed equivalent fixture; complete graph/version/receipt comparisons pass. Original version-4 input unchanged.
Next action: Retry has no new effect under retained receipt evidence; production implementation remains separate.
Limits: In-memory copy only; no crash durability, multiple-writer coordination or unimplemented domain invariant certified.
```

### Missing evidence

Input: "Retry that graph update" without a snapshot, original envelope or receipt history.

Response: "Please supply the current graph snapshot and trusted revision. What is the original logical batch ID, expected version and exact ordered operation envelope? Which accepted receipts and retention history are available, and what mutation policy applies?"

The response uses three grouped questions, performs no patch and does not assume that an absent receipt proves nonexecution. Outcome remains incomplete, with no invented version or replacement event ID.

### Late failure and corrected proposal

Input: published version-4 fixture asks node+ Z then node- Y while e:X-to-Y remains. No cascade policy exists.

```text
Scope: Fictional version 4; explicit deletion policy; offline transition review.
Envelope: new batch | expected 4 | node+ Z; node- Y.
Preconditions: Fresh event and matching base; Y is referenced by e.
Candidate: Reject at node- Y; discard preceding candidate addition Z.
Outcome: Rejected; current version remains 4.
Verification: Executed fixture preserves X/Y, e, version 4 and empty receipt ledger; no success receipt created.
Next action: Obtain an explicitly corrected operation envelope and recheck the actual current version. No implicit cascade or automatic rebase.
Limits: No live deletion or durable receipt guarantee established.
```

All published assertions hold. Since a failed event has no accepted receipt in this reference, an explicit corrected submission is evaluated as a fresh transition against its supplied expected version; no assertion of successful prior execution is made.

## Specific-claim and boundary audit

Event equality binds expected version and operation order. Receipt lookup preceding fresh-write version checking is necessary here to recognize an old successful event after newer updates; returning a copy of current state avoids rollback-by-replay. Candidate copying prevents the stated in-memory partial-write problem, but it does not establish durable atomicity or concurrent compare-and-swap. The text requires one actual atomic conditional commit for live storage and qualifies receipt-retention limitations. Integer versions advance once on acceptance, not on replay or rejection, as executed. Incident-edge references, loops and parallel identities follow the declared fixture contract; lifecycle/tombstone/property constraints are explicitly unimplemented. No invented source, law, changing API guarantee or unexplained numeric threshold appears. No blocking finding.
