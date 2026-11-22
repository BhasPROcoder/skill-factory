# Candidate G48: derived-fact support after assertion retraction

## Decision

Pursue a bounded, source-ID-aware truth-maintenance procedure for a licensed transitive knowledge-graph predicate. Given one frozen assertion ledger and one proposed source-record retraction, recompute the derived view, classify each previously visible fact as retained or lost, and provide a currently valid source-ID derivation for every retained fact that depended on the retracted record's earlier witness. Do not allocate a registry ID or count a skill until a full draft, execution evidence and independent review pass.

## Distinct mechanism and overlap checks

- GRF-018 (`knowledge-relation-inference-contract`), whose actual procedure and reference were inspected, defines a vocabulary and computes inverse/transitive consequences. Its reference stores only the first derivation witness per triple, while separately retaining multiple source assertions; it does not perform source-record retraction or prove alternate support after a witness disappears. G48 freezes an already approved rule and evaluates a retraction against *all* surviving direct records and paths. Do not repeat vocabulary governance or claim general inference-rule coverage.
- GRF-005 reconstructs an active edge view from effective and recorded time revisions, including explicit retractions. It does not compute the licensed transitive closure or distinguish a lost derivation witness from a still-supported derived fact.
- GRF-016 checks atomic, payload-bound graph patch replay. It does not decide which rule-derived facts survive a source assertion removal.
- GRF-039 computes gained reachability pairs after one hypothetical edge addition. G48 is not a generic opposite-direction reachability delta: it tracks individually identified assertion support, duplicate direct records, an approved transitive rule, and witness replacement for surviving derived facts. If the eventual draft merely computes `before_paths - after_paths`, reject it as a renamed G39 variant.
- GRF-020 validates declared value-count constraints on an already selected assertion view; it does not maintain derivation support.

## Contract and procedure

Input a finite node inventory; unique source-record IDs each asserting `(subject, predicate, object)`; one predicate whose transitive rule is explicitly approved for this scoped exercise; a frozen snapshot/rule revision; and one existing source ID proposed for retraction. Preserve all original records in an evidence ledger. Treat equal triples with different source IDs as separate supports. The after view omits only the proposed record. Compute the nonempty-path closure before and after from the permitted predicate records; a fact may be both directly asserted and derived. For each visible fact, retain at least one exact source-ID path whose every record exists in the corresponding view. Partition facts into lost, retained with unchanged selected witness, and retained with replacement witness. For each lost fact, show the before witness and independently verify that no after path remains. For each replacement, show the before and after source-ID paths and verify both end at the same fact. Cyclic self-facts require a nonempty closed path; an empty path must never prove `(A,A)`.

Use a finite in-memory reference and an independent closure or path oracle. Report unknown rather than a global loss claim if the source inventory or licensed rule revision is incomplete. This skill does not establish source truth, authorize a deletion, handle arbitrary rule languages, or promise production-scale incremental maintenance. Avoid current platform APIs or standards claims.

## Executable acceptance fixture

Fictional nodes A, B, C, D, E with approved transitive predicate `contains` and distinct source records: `r1: A→B`, `r2: B→D`, `r3: A→C`, `r4: C→D`, `r5: D→E`, `r6: A→B` (duplicate triple, separate source identity). Retract only `r2`.

- Before, `(A,D)` has paths `[r1,r2]`, `[r6,r2]` and `[r3,r4]`. After, it remains visible via `[r3,r4]`; do not classify it lost because the first stored witness used `r2`.
- Before, `(A,E)` has an `r2`-dependent path `[r1,r2,r5]` and an alternate `[r3,r4,r5]`. After, it remains visible via `[r3,r4,r5]`.
- `(B,D)` and `(B,E)` are lost after `r2` is removed. `(A,B)` remains directly supported by both `r1` and `r6`; removing only `r1` in a separate fixture must retain it via `r6`.
- All source IDs in after witnesses must exist in the after ledger; inject a forged after witness containing `r2` and require rejection. Inject an omitted alternate `r3` or `r4` and require the corresponding derived fact to become lost when no other support exists.
- Add a two-record directed cycle fixture and check that a self-fact survives only while a nonempty cycle remains. Reject unknown retraction ID, duplicate source ID, unknown endpoint, malformed string-shaped record and unapproved transitive predicate.

The acceptance comparison should use exact fact sets, not only counts, and recalculate each displayed source-ID path against the frozen assertion inventory. The examples above are fictional and contain no changing external facts.
