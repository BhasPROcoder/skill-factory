---
id: PRT-006
name: print-finishing-assembly-handoff
domain: Print Production Handoffs
subdomain: Finishing correspondence
version: 1.0
description: Translate approved multi-part print intent into an evidence-based finishing and assembly handoff when part order, orientation or edition matching could be confused.
triggers: ["prepare a print assembly handoff", "check booklet insert order", "reconcile finishing instructions", "prevent mixed-edition assembly", "review folded piece orientation"]
not_for: ["calculating print quantities [PRT-001]", "operating or adjusting finishing machinery", "certifying production safety"]
requires: []
risk_level: medium
---

# Print finishing and assembly handoff

## Purpose
Create a reproducible description of how approved printed parts form the intended finished piece. Resolve ambiguous order, orientation and edition pairing through labeled evidence, while leaving machinery settings and production process choices to the responsible supplier.

## Inputs to collect
1. **Finished intent:** Obtain the approved reading sequence, opening direction and placement of covers, inserts or attachments. Required; a pile of printed parts does not establish assembly intent.
2. **Part identities:** Collect named parts, revisions, editions and visible distinguishing features. Required; generic labels such as “the blue sheet” are inadequate when several parts look alike.
3. **Orientation evidence:** Request labeled front/back views, top edges, fold references and a sample or mockup if available. Default: unresolved orientation where text alone permits multiple interpretations.
4. **Supplier process proposal:** Collect the proposed finishing sequence and any dependencies the supplier identifies. Default: handoff describes product relationships only, without inventing machine operations.
5. **Acceptance evidence:** Identify the checks and owner required for a representative assembled sample. Default: prepare a review checklist, not a production release.
6. **Variant scope:** List editions and exceptions, including interchangeable shared parts where explicitly approved. Default: keep different editions separate until compatibility is established.

If required inputs lack safe defaults, ask in one message with at most three questions.

## Procedure
1. Define the finished piece and its revision boundary. Keep the customer-approved product description separate from the supplier's proposed manufacturing sequence.
2. Assign a stable part label to each required component. Preserve edition and revision in the label or adjacent field so a common visual design does not make different parts interchangeable.
3. Describe the intended reading or opening sequence from the user's viewpoint. Use named surfaces and direction references rather than “flip it” or “put it behind,” which depend on how an observer holds the part.
4. ⚠️ Map each physical relationship explicitly: before/after in the reading order, inside/outside, facing direction and attachment location where supplied. If two arrangements remain plausible, request labeled visual evidence instead of guessing.
5. Create an edition compatibility table for parts. Allow shared components only where the supplied specification establishes interchangeability, and retain the relationship back to each finished edition.
6. Compare the supplier's proposed process with the intended relationships. Flag a dependency or conflict for supplier resolution rather than prescribing an unsupported machine sequence or equipment setting.
7. Define a representative assembly check using the actual variants and ambiguous relationships. Include opening and reading the piece, not only inspecting its closed exterior, so reversed interiors or misplaced inserts can be observed.
8. Reconcile the sample against the approved relationships and record each discrepancy at the part or surface involved. A correct cover cannot compensate for a wrong insert or inverted inner panel.
9. Record the accepted sample identity and any remaining exceptions with the approving role. If a part revision changes afterward, identify which relationships and variants require renewed comparison.
10. Deliver a finishing handoff that separates confirmed intent, supplier questions and sample evidence. State whether the handoff is ready for a mockup, sample review or the next authorized gate, without claiming unobserved assembly occurred.

Check [VERIFY: the supplier's current job instructions, approved finishing proposal and sample acceptance process] before using external production constraints. Do not supply universal fold allowances, adhesive specifications, machine setup values or equipment-operation instructions.

## Decision rules
- IF an orientation instruction depends on how a person holds the part THEN replace it with labeled surface and edge references BECAUSE relative words can describe several physical arrangements.
- IF editions use visually similar components THEN retain explicit compatibility labels BECAUSE appearance alone does not establish correct pairing.
- IF a proposed process conflicts with the finished intent THEN return the conflict to the supplier BECAUSE product relationships do not determine a safe machine sequence.
- IF only the closed sample is shown THEN leave interior relationships unverified BECAUSE correct exterior appearance does not prove reading order.
- IF an accepted component changes THEN recheck affected relationships BECAUSE a prior sample may no longer represent the production revision.

## Output template
```text
Finished intent: <piece, edition and revision; up to three lines>
Part map: <up to ten rows; attach continuation if larger>
Part/revision | Edition compatibility | Named surfaces/edges | Required relationship
Supplier questions: <up to three grouped ambiguities or process conflicts>
Sample checks: <up to eight observable checks tied to relationships>
Evidence and exceptions: <sample identity, observations and unresolved findings>
Handoff state: <ready for named next gate / blocked; owner>
Change boundary: <which revisions or relationships require renewed comparison>
```

## Quality checklist
- [ ] Every part has an identity and revision boundary.
- [ ] Reading sequence is expressed from the intended user's viewpoint.
- [ ] Orientation references identify surfaces or edges.
- [ ] Edition compatibility comes from supplied evidence.
- [ ] Supplier process questions are separate from product intent.
- [ ] Sample checks include relevant interior relationships.
- [ ] Acceptance claims identify the exact observed sample and role.
- [ ] Changed parts have a stated recheck boundary.

## Anti-patterns
- **Hand-motion instruction:** “turn it over and put it behind” substitutes for orientation evidence. Fix: name the surfaces, edges and final relationship.
- **Cover-only acceptance:** a closed piece is declared fully correct. Fix: inspect opening sequence and required interior placement.
- **Edition pooling:** similar parts are mixed without compatibility evidence. Fix: preserve edition labels and approved shared-part relationships.
- **Machine inference:** an assembly diagram becomes equipment instructions. Fix: ask the supplier to resolve manufacturing dependencies.
- **Sample drift:** an accepted mockup is reused after parts change. Fix: identify affected relationships and compare the replacement revision.

## Worked example
**Input:** Fictional publisher Reed has editions North and South. Both use shared approved text part T, but covers CN and CS and map inserts IN and IS are edition-specific. The approved intent places each map after named text panel End, with the map title facing the reader on opening. A supplied North sample contains CN, T and IS. Its closed cover looks correct; its interior photo clearly identifies IS.

**Output:**
```text
Finished intent: North and South editions using supplied approved component revisions.
Part map:
Part/revision | Edition compatibility | Named surfaces/edges | Required relationship
T/current approved | North and South | named panel End | precedes edition-specific map
CN/current approved | North only | identified cover front | encloses North assembly
CS/current approved | South only | identified cover front | encloses South assembly
IN/current approved | North only | map title face | after End, title toward reader on opening
IS/current approved | South only | map title face | after End, title toward reader on opening
Supplier questions: Please correct the North sample's insert pairing and supply interior evidence of its replacement.
Sample checks: Verify cover-to-insert edition pairing; locate map after End; observe title orientation on opening.
Evidence and exceptions: Supplied North sample has correct CN cover but wrong IS insert; replacement orientation remains unverified.
Handoff state: Blocked for corrected North sample review by publication owner.
Change boundary: Recheck insert identity, placement and facing in the replacement; any revised shared T requires comparison in both editions.
```

**Bad output:** “The North cover matches, so the sample is accepted.”
It ignores the visible wrong-edition insert and treats exterior identity as proof of the whole assembly.

## Edge cases
- A loose insert has no fixed orientation requirement: preserve that explicit freedom instead of inventing a constraint.
- A part's visible label disappears after folding: identify a pre-assembly check or another supplied traceability feature rather than assuming final visibility.
- The mockup uses placeholder artwork: distinguish relationships it can demonstrate from edition or revision content it cannot verify.
- A supplier proposes an equivalent assembly approach: compare the resulting product relationships and route the process decision to its owner.

## Test case
**Input:**
> Fictional supplier instructions say “put the insert behind the folded sheet.” No surface labels or opening view are provided, and two orientations satisfy that sentence.

**Assertions:**
1. Identifies the orientation ambiguity explicitly.
2. Requests labeled surfaces or a representative opening view.
3. Does not choose an arbitrary arrangement or machine sequence.
4. Marks the relevant relationship unresolved until evidence distinguishes the alternatives.
