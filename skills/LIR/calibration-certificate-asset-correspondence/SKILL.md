---
id: LIR-001
name: calibration-certificate-asset-correspondence
domain: Laboratory Instrument Records
subdomain: Certificate correspondence
version: 1.0
description: Match calibration documents to instrument identity and requested record scope when certificates may refer to similar or replacement assets.
triggers: ["match a certificate to an instrument", "check asset serial on calibration record", "reconcile calibration certificate identity", "find certificate-to-equipment mismatch", "prepare instrument certificate evidence"]
not_for: ["performing a calibration", "deciding whether an instrument is fit for use"]
requires: []
risk_level: medium
---

# Certificate correspondence

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
3. Apply the following procedure to this task: Collect the instrument register row, the complete supplied certificate and its revision or issue identity, and the request scope. Preserve each source as received. Extract manufacturer, model, serial or other stable asset key, certificate identifier, covered range or configuration only when present, and the document's stated dates without interpreting them as current validity. Compare identity fields independently; a matching model does not prove a matching instrument. ⚠️ Never merge certificate rows by model alone; retain conflicting serials and request owner resolution. Mark each comparison as exact, conflicting, absent or unreadable. Trace any alias through an owner-supplied crosswalk and preserve the link; never infer that a replaced serial belongs to the same asset. Record certificate scope and any listed accessories separately from the instrument identity. Reconcile document revision and supersession only from explicit source evidence. Ask the document owner to resolve identity conflicts, missing pages or illegible fields. Produce a correspondence table and a bounded disposition: matched for record linkage, unresolved, or conflict. This disposition is not an acceptance, calibration-validity, or fitness decision. Keep source references and exact excerpts needed to reproduce the match.
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
IF a stable asset key agrees across register and certificate THEN mark that field exact BECAUSE identity requires evidence tied to the physical or controlled asset.
- IF model agrees but serial conflicts THEN classify identity as conflict BECAUSE model-level similarity cannot resolve asset identity.
- IF a field is absent or unreadable THEN mark it unknown BECAUSE absence is not agreement.
- IF alias mapping lacks an owner-supplied source THEN request the mapping BECAUSE the agent cannot create asset lineage.

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
**Input:** Fictional Lab Cedar request: Fixture: fictional Lab Cedar register asset M7 model Q serial 44; certificate C9 shows Q/44, stated scope channel A, revision 2; another certificate C8 shows Q/45. Link C9 to M7 on model and serial, record channel A and revision 2 as stated, and flag C8 as serial conflict. Do not call C9 valid today or conclude M7 is fit for use. Arithmetic: none.

**Output:**
```text
Scope: Fictional Cedar register snapshot; asset M7, model Q, serial 44; certificate records C9 and C8.
Evidence: M7 register | Q/44 | register row M7; C9 | Q/44, channel A, revision 2 | certificate C9; C8 | Q/45 | certificate C8.
Reconciliation: C9 model and serial match M7; C8 model matches but serial conflicts. Two certificates reviewed; one linked, one conflicting.
Open questions: Asset owner to confirm whether C8 belongs to another asset or reflects an authorized identity change.
Handoff: Link C9 to M7 for record retrieval only; preserve C8 as unresolved conflict pending owner evidence.
Limits: No current calibration validity, instrument fitness, measurement validity, safety or release decision is made.
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
> Fixture: fictional Lab Cedar register asset M7 model Q serial 44; certificate C9 shows Q/44, stated scope channel A, revision 2; another certificate C8 shows Q/45. Link C9 to M7 on model and serial, record channel A and revision 2 as stated, and flag C8 as serial conflict. Do not call C9 valid today or conclude M7 is fit for use. Arithmetic: none.

**Assertions:**
1. Retains each source record identity and its provenance.
2. Marks missing or conflicting evidence explicitly rather than guessing.
3. Produces the requested administrative handoff in the exact template.
4. Makes no technical fitness or scientific result-validity determination.
