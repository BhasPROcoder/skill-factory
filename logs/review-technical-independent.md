# Independent technical and media skill review

Reviewer: marketing_business agent, independent of the original T-domain author.

## Scope

Reviewed all 150 authored task records in `tools/build_data_technical.py`: the inputs, four task-specific procedure actions, branch condition, fictional fixture, finding, recommended action, verification condition, and available offline snippet. Reviewed the shared renderer and output contract. The review covers these 15 domains: TRP, TAM, TVE, TDV, TSC, TAP, TST, TKG, THK, TML, TFE, TDE, TAN, TDS, and TDQ.

Inspected the rendered substantive sections of at least one actual skill per domain, rather than relying only on the records. Deep-read IDs: TRP-007, TAM-009, TVE-003, TDV-001, TSC-002, TAP-007, TST-009, TKG-002, THK-003, TML-003, TFE-008, TDE-005, TAN-004, TDS-004, and TDQ-010. Inspection emphasized procedures, worked examples, output requirements, decisions, and test assertions; repeated shared boilerplate was reviewed in the renderer.

## Findings and repairs

1. The original examples frequently named a deliverable but returned only advice to create it. Added an `Artifact` field to the exact output template and every worked example. Added 150 independently authored concrete artifacts in `tools/review_technical_artifacts.py`: interface payloads, permission matrices, comparison calculations, source inventories, routing rules, script lines, and bounded plans. Procedure and test assertion now require actual task output. For example, THK-003 includes a proposed success payload and failure shape; TSC-002 includes read/delete decisions for the reporting role; TDS-004 contains field-level meanings and missing-value treatment; TKG-002 states the actual metric calculation.
2. Descriptions contained the ungrammatical construction `task is to <noun phrase>` and some triggers contained `review my a`. Replaced them with grammatical deliverable-based descriptions and article-free possessive triggers. Existing IDs and names are unchanged.
3. Subdomains were assigned by cyclic position. Replaced the modulo assignment with an explicit content-based mapping to existing subdomain names. For example, stem handoff belongs to Delivery, backup restoration to Recovery, permission review to Access review, and submission schema checking to Submissions.
4. TAP-007 could imply that older webhook events can always be ignored. Limited the worked fixture to complete state snapshots and explicitly distinguished delta events, which may need every event or reconciliation. The artifact does not prescribe newest-version replacement for deltas.
5. TFE-008 treated incomplete follow-up too broadly. The example now explicitly has no observed qualifying event, and the procedure/artifact preserve an already observed qualifying positive. An incomplete no-event record is not treated as a confirmed negative.
6. TKG-007 said models predicted the same probability although its numeric fixture differed. Corrected the fixture wording to the same target and rows, with potentially different predictions. The aligned combination is an example, not a claim of better ensemble performance.
7. TAN-008 unnecessarily used financial break-even language for a general sensitivity method. Replaced it with a user-supplied operational acceptance threshold; the values remain fictional inputs rather than a universal threshold.
8. Added task-specific caveats where concise fixtures could otherwise be overgeneralized: a sequential deduplication illustration does not establish concurrent atomicity; checkpoint ordering requires replay-safe coordination; stable pagination tie-breakers do not settle all mutation semantics; illustrative digest labels are not a specified algorithm's outputs; a reduced dataset view is not an anonymity guarantee.
9. Added a direct `__main__` call to the existing `finish()` workflow so running the authoring script actually emits its planned staging manifest and invokes `sf.py` validation. Previously a direct run rendered files but did not call that finish function.
10. Revised skill frontmatter versions to 1.1. The regenerated staging manifest keeps `planned` statuses for coordinator-controlled metadata integration. This reviewer did not update registry statuses or mark any skill audited.

## Verification evidence

The completed `python tools/build_data_technical.py` run invoked `sf.py validate --file` across all 150 owned skill paths. The observed `sf.py` output contained PASS for every path and no warnings or failures. The builder also executed its existing offline Python fixture assertions before saving. Its pre-save body-length checks remained within the repository's 700–1,800-word range.

The coordinator must synchronize description and subdomain metadata for all T-domain rows from the regenerated files, then run combined registry, quality, routing, and package checks. `staging/data_technical.json` contains the corresponding planned records. The shared registry was not mutated by this review.

## Limits

This is an independent substantive source-and-example review plus structural validation. It is not a cross-model behavioral evaluation, execution against live production systems, a security penetration test, a competition-rule certification, or verification of current platform requirements. Those changing requirements remain explicit inputs or official-source verification steps. Not every skill was exercised against a fresh unseen task. The simple offline snippets verify their small fictional invariants; they do not establish the correctness of a user's real implementation. No claim of universal expert approval or automatic audited status is made.
