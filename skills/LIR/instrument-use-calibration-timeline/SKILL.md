---
id: LIR-002
name: instrument-use-calibration-timeline
domain: Laboratory Instrument Records
subdomain: Use-to-calibration timeline
version: 1.0
description: Reconstruct instrument-use and calibration-status chronology from supplied records when a later status change may affect review of earlier runs.
triggers: ["trace instrument status at run time", "build calibration chronology", "check which runs precede a status change", "link runs to instrument calibration records", "reconstruct calibration event sequence"]
not_for: ["deciding scientific result validity", "setting calibration intervals", "performing retrospective legal compliance review"]
requires: []
risk_level: medium
---

# Use-to-calibration timeline

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
3. Apply the following procedure to this task: Collect instrument identity, dated use/run records, calibration or service events, status-change records, and the owner-provided rule for interpreting effective times. Preserve original timestamps, zones and source identifiers. ⚠️ Do not infer instrument fitness or run validity from administrative chronology; route technical disposition to its qualified owner. Separate event occurrence time, record creation time and any explicitly stated effective time. Normalize only when the source supplies enough zone information; otherwise retain raw timestamps and mark ordering uncertain. ⚠️ Sort events only when their time basis is comparable. For each run, identify the nearest preceding relevant status event under the supplied policy and show the source link. Do not interpolate status across missing periods or assume a certificate's issue date equals an effective date. Represent overlapping, contradictory or undated events as unresolved branches. Distinguish an administrative status label from a technical judgment about measurement validity. Reconcile the set of runs in scope against the source list so omitted records remain visible. Ask for the minimum missing timezone, effective-time policy or identity link needed to order records. Output a row per run with raw time, linked events, chronology confidence and unresolved questions. This supports review routing only; a qualified owner determines technical consequences.
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
IF timestamps lack a common zone or explicit ordering rule THEN retain raw values and mark ordering unresolved BECAUSE apparent sequence may be false.
- IF a run has no preceding status record THEN report no supplied prior status BECAUSE a gap is not evidence of an expired or acceptable state.
- IF event and entry times differ THEN preserve both BECAUSE late recording can change the apparent sequence.
- IF a status boundary overlaps a run time THEN escalate the event-time interpretation BECAUSE the supplied data do not establish which state applied.

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
**Input:** Fictional Lab Cedar request: Fixture: fictional Lab Cedar run R12 raw time 10:15Z; status event E3 effective 09:00Z and entered 11:00Z; event E4 effective 12:00Z. Under supplied UTC effective-time policy, link E3 as preceding R12 while retaining that it was recorded later. Do not judge the run result or assert instrument fitness. Arithmetic: 10:15 follows 09:00 and precedes 12:00.

**Output:**
```text
Scope: Fictional Cedar snapshot; asset M7; runs in supplied log R12 only; UTC effective-time rule supplied.
Evidence: R12 | run 10:15Z | log row R12; E3 | effective 09:00Z, entered 11:00Z | status event E3; E4 | effective 12:00Z | status event E4.
Reconciliation: R12 falls after E3 effective time and before E4 effective time. E3 was entered after the run, but its supplied effective time governs this administrative chronology.
Open questions: None for ordering under the stated UTC effective-time rule. Any technical consequence requires the responsible owner.
Handoff: Route R12 with E3 and E4 source references for qualified review; preserve the late entry timestamp.
Limits: This chronology does not establish instrument fitness, measurement validity or whether the run result should be used.
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
> Fixture: fictional Lab Cedar run R12 raw time 10:15Z; status event E3 effective 09:00Z and entered 11:00Z; event E4 effective 12:00Z. Under supplied UTC effective-time policy, link E3 as preceding R12 while retaining that it was recorded later. Do not judge the run result or assert instrument fitness. Arithmetic: 10:15 follows 09:00 and precedes 12:00.

**Assertions:**
1. Retains each source record identity and its provenance.
2. Marks missing or conflicting evidence explicitly rather than guessing.
3. Produces the requested administrative handoff in the exact template.
4. Makes no technical fitness or scientific result-validity determination.
