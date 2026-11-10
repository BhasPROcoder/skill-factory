---
id: LIR-003
name: out-of-tolerance-affected-record-inventory
domain: Laboratory Instrument Records
subdomain: Affected-record inventory
version: 1.0
description: Build a traceable candidate inventory after an instrument status notice identifies an out-of-tolerance condition, when run records may need owner review.
triggers: ["identify records after an instrument notice", "trace runs to affected instrument status", "prepare out of tolerance impact inventory", "find candidate samples from instrument logs", "handoff instrument incident records"]
not_for: ["determining whether results must be invalidated", "calculating measurement uncertainty", "making patient or product disposition decisions"]
requires: []
risk_level: medium
---

# Affected-record inventory

## Purpose
Create an evidence-linked administrative record that another reviewer can reproduce from the supplied source documents. Keep source facts, interpretation rules and unresolved questions distinct so the result cannot be mistaken for a technical instrument determination.

## Inputs to collect
1. **Instrument identity** — obtain the controlled asset key and relevant aliases. This anchors records to one instrument. Default: no identity inference from model name alone.
2. **Source records** — obtain the complete supplied register, notice, certificate or run-log scope. This bounds the inventory. Default: use only provided records.
3. **Time and revision basis** — collect timestamps, zones, document revisions and effective-time policy when relevant. This controls ordering. Default: preserve raw forms and mark incomparable values unresolved.
4. **Decision boundary** — ask what record or handoff is needed. This keeps the output administrative. Default: evidence reconciliation only; no technical disposition.
5. **Handling constraints** — collect permitted identifiers and sharing limits. This protects source context. Default: minimize personal or sensitive sample details.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the supplied source snapshot and list every included artifact with its identifier and revision.
2. Extract the fields relevant to this workflow without normalizing away their original wording.
3. Apply the following procedure to this task: Collect the notice as received, affected asset identifiers, condition description, stated discovery and effective times, stated scope limitations, run records, and owner-approved inclusion rules. ⚠️ Do not reinterpret technical tolerance criteria; copy the notice's terminology and source references. Resolve asset aliases only through controlled mappings. ⚠️ Build a candidate universe from run records in the requested period, retaining row identity and source snapshot; do not infer onset from discovery time. Apply the supplied inclusion rule transparently to each run: match, exclude with reason, or unresolved. Keep discovery time distinct from any asserted onset or effective time. Do not infer that all runs after discovery are affected or that earlier runs are unaffected. Join sample, batch or downstream record identifiers only from explicit run links; expose missing links rather than fuzzy matching names. Reconcile candidate counts against input records and preserve duplicate run rows as separate source observations until their identity is resolved. Produce an evidence inventory with a review queue and exact unresolved fields. The qualified technical owner decides whether results, products or decisions require action. The inventory itself makes no scientific, safety, regulatory or release determination. Before sharing, follow the user's authorized data-handling boundary and minimize sensitive sample details.
4. Label each conclusion as exact match, conflict, absent, unreadable, or unresolved, as appropriate.
5. Preserve a source reference for every extracted fact and every disposition.
6. Reconcile the output row identities against the input universe and report excluded records with reasons.
7. Ask the record owner to resolve conflicts that require institutional knowledge.
8. Prepare the bounded handoff using the output template; make the limitation visible in the first section.

## Decision rules
- IF the evidence supports only an administrative linkage THEN report that limited linkage BECAUSE records do not establish technical fitness.
- IF source fields conflict THEN preserve both values and request owner resolution BECAUSE silently selecting one would alter evidence.
- IF a governing time or status rule is missing THEN mark the conclusion unresolved BECAUSE no default rule is authorized.
- IF a record is absent from the supplied scope THEN say it was not supplied BECAUSE absence from this packet does not establish nonexistence.
- IF the requester asks for technical validity or disposition THEN route the evidence to the responsible qualified owner BECAUSE this workflow does not make that determination.
IF the notice gives only a discovery time and no effective interval THEN do not invent the onset BECAUSE discovery does not establish when the condition began.
- IF a run identity links to the asset but not to a sample THEN retain it as a candidate with missing downstream link BECAUSE absent linkage is not proof of no impact.
- IF the inclusion policy is absent THEN prepare source inventory only and request policy BECAUSE the candidate boundary is undefined.
- IF duplicate run identifiers conflict THEN preserve both source rows and flag identity resolution BECAUSE deduplication could erase evidence.

## Output template
```text
Scope: <asset identity, source snapshot and record boundary; up to 3 lines>
Evidence: <record ID | extracted fields | source reference; up to 12 rows then continuation>
Reconciliation: <matched, conflicting, absent, unreadable and unresolved counts; up to 3 lines>
Open questions: <owner decisions needed, or None; up to 5 items>
Handoff: <bounded administrative result and next owner; up to 3 lines>
Limits: <what this inventory does not establish; up to 2 sentences>
```

## Quality checklist
- [ ] Asset identity is tied to a supplied stable key or clearly unresolved.
- [ ] Source snapshot and revisions are named.
- [ ] Original timestamps and source wording are retained where material.
- [ ] Each row traces to a supplied record reference.
- [ ] Conflicts and missing fields remain explicit.
- [ ] Output coverage reconciles to the input universe.
- [ ] No current interval, tolerance or standard was invented.
- [ ] No technical fitness or result-validity conclusion is implied.

## Anti-patterns
- **Model-name match**: treating similar models as the same asset. Fix: compare stable identifiers.
- **Timestamp collapse**: replacing event time with entry time. Fix: retain each clock field separately.
- **Gap as proof**: treating absent records as proof an event did not happen. Fix: mark the source gap.
- **Silent conflict resolution**: picking the most convenient record. Fix: preserve both and route to owner.
- **Administrative overclaim**: converting a record match into technical approval. Fix: state the precise boundary.

## Worked example
**Input:** Fictional Lab Cedar request: Fixture: fictional Lab Cedar notice N2 names instrument M7, discovered at 14:00, with no effective start. Runs R1 at 09:00 and R2 at 15:00 link to M7; sample link for R2 is absent. Under an owner-supplied “inventory all runs on M7 for this shift” rule, list both as candidates, retain missing sample link for R2, and state onset unresolved. Do not invalidate either result. Arithmetic: 09:00 precedes discovery; 15:00 follows it.

**Output:**
```text
Scope: Fictional Cedar snapshot; asset M7; all M7 runs in the owner-defined shift inventory; notice N2.
Evidence: N2 | discovery 14:00, onset absent | notice N2; R1 | 09:00, linked M7 | run log R1; R2 | 15:00, linked M7, sample link absent | run log R2.
Reconciliation: Two in-scope runs, two candidate rows. R1 retained despite preceding discovery because owner rule includes all shift runs; R2 retained with missing sample link. Onset remains unresolved.
Open questions: Qualified owner to determine the notice effective interval and whether either result requires action; record owner to supply R2 sample link if available.
Handoff: Send both candidate rows and source references for owner review. No run is invalidated or excluded by this inventory.
Limits: Discovery time does not establish onset. This inventory makes no scientific, safety, regulatory, product or release determination.
```

**Bad output:** “The instrument is certified and every result is safe to use.”
This claims technical conclusions that the supplied administrative evidence and workflow do not establish.

## Edge cases
- **Illegible record**: mark the field unreadable and request a clearer controlled copy.
- **Conflicting asset aliases**: preserve both source identifiers and obtain an approved crosswalk.
- **Incomplete time basis**: retain raw timestamps and withhold ordering.
- **Duplicate source rows**: keep separate row references until an owner resolves identity.

## Test case
**Input:**
> Fixture: fictional Lab Cedar notice N2 names instrument M7, discovered at 14:00, with no effective start. Runs R1 at 09:00 and R2 at 15:00 link to M7; sample link for R2 is absent. Under an owner-supplied “inventory all runs on M7 for this shift” rule, list both as candidates, retain missing sample link for R2, and state onset unresolved. Do not invalidate either result. Arithmetic: 09:00 precedes discovery; 15:00 follows it.

**Assertions:**
1. Retains each source record identity and its provenance.
2. Marks missing or conflicting evidence explicitly rather than guessing.
3. Produces the requested administrative handoff in the exact template.
4. Makes no technical fitness or scientific result-validity determination.
