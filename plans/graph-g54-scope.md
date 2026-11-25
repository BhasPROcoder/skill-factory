# Candidate GRF-054: graph change-feed coverage reconciliation

Status: discovery card only. No skill or registry entry. Recheck ID and overlap before authoring.

## User problem and distinct artifact

A graph source reports committed mutation envelopes for a bounded revision interval, while a downstream change feed exposes delivery records and a consumer checkpoint. Reconcile whether every committed node/edge mutation identity has a corresponding feed record at the intended source revision, whether a feed record is duplicated or foreign, and whether the consumer checkpoint claims progress beyond complete delivery. Return a source-to-feed coverage ledger with exact envelope/operation witnesses and a safe replay interval proposal. Do not apply mutations, assert distributed exactly-once delivery, or infer graph state merely from feed counts.

The key distinction is **delivery coverage between two artifacts**. GRF-016 `versioned-graph-patch-replay` validates and applies one ordered patch with a payload-bound receipt; it does not compare a separately emitted feed against the complete set of committed source envelopes. GRF-024 `graph-service-restore-reconciliation` verifies a restored graph and query views at a backup/log boundary; it does not reconcile source commit identities to feed deliveries. GRF-047 `graph-adjacency-index-freshness-audit` compares materialized edge-ID buckets with primary records, not change events. TDE-005 `pipeline-checkpoint-recovery-review` is a generic pipeline recovery plan; a graph-specific card must preserve node/edge operation identities and endpoint dependencies, rather than repeat generic checkpoint advice.

## Contract and failure decisions

Inputs: independently retained source commit manifest for a finite contiguous source-revision interval; each envelope ID, revision and ordered operation IDs/payload digest; feed records with source envelope ID, source revision, operation ID, payload digest and delivery offset; consumer checkpoint offset and declared ack semantics; complete node/edge operation meanings and graph epoch. No current platform API or offset convention is hardcoded. A repeated delivery with identical payload may be a retry, while repeated logical operation IDs with conflicting payloads are a conflict. A missing feed record is a gap, not proof the source operation never committed. Out-of-order delivery may be tolerable only when consumer dependency rules are explicitly supplied; an edge addition before its endpoint node additions is a concrete ordering hazard under a consumer that requires endpoint presence.

The procedure should compare multisets and exact identities, retain source and delivery order separately, classify missing/extra/duplicate/conflicting records, and compute the greatest **complete contiguous source revision** represented by the feed. A consumer checkpoint beyond the last fully covered delivery boundary is suspicious; an offset alone cannot prove applied graph state. Source manifest gaps or unavailable feed pages make completeness unresolved rather than pass. No automatic replay should be issued; produce the bounded interval and owner checks.

## Executable fictional fixture

Fictional source commits:

- revision 1, envelope E1: operation nA adds node A, operation nB adds node B;
- revision 2, envelope E2: operation e1 adds edge p from A to B;
- revision 3, envelope E3: operation e2 adds parallel edge q from A to B.

Feed contains nA and nB at source revision 1, e1 at revision 2, and two identical delivery attempts for e1; it lacks e2. The exact coverage result is revisions 1–2 complete, revision 3 incomplete, duplicate delivery of e1, and missing e2. An ack/checkpoint claiming revision 3 complete must be flagged for reconciliation; do not call q nonexistent or collapse it with p because endpoints match. An adversarial record for e1 with a different payload digest must be classified as conflict, not harmless retry. If feed order places e1 before nA/nB, report the endpoint-order hazard under the stated consumer contract even though all three operation IDs eventually appear.

Executable reference acceptance: build a finite source operation map keyed by (revision, envelope ID, operation ID), a feed multiset keyed by the same logical identity plus digest, classify exact mismatches, and scan revisions in order until the first incomplete revision. Independently verify the result by reconstructing each revision's expected-vs-observed identity set. Test empty declared interval, missing source revision, parallel edge IDs, duplicate identical delivery, conflicting duplicate, foreign feed record, out-of-order endpoint dependency and unavailable feed page.

## Gate before a full skill

Inspect actual GRF-016/024/047 and TDE-005 procedures again, then decide if the final method goes beyond a renamed generic CDC checklist. An author must supply a runnable bounded Python 3 implementation, fictional ordinary/missing/adversarial outputs, claim audit and exact no-invented-source handling. Independent review is required before registry acceptance.
