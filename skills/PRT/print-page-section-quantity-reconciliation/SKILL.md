---
id: PRT-001
name: print-page-section-quantity-reconciliation
domain: Print Production Handoffs
subdomain: Quantity reconciliation
version: 1.0
description: Reconcile logical pages, printer-supplied sections and finished-copy quantities when a print order mixes covers, blanks or different editions.
triggers: ["check booklet page counts","reconcile print sections and copies","why do printed quantities disagree","separate cover and text quantities","verify a mixed-edition print quantity brief"]
not_for: ["shipment package reconciliation [SHP-001]","designing press imposition","pricing or approving a production order"]
requires: []
risk_level: medium
---

# Print page and section quantity reconciliation

## Purpose
Build a quantity bridge between the publication the customer expects and the production units the supplier proposes. Keep logical pages, physical parts, section plans and finished copies separate so an apparently correct total does not hide a missing cover, duplicate blank or wrong edition.

## Inputs to collect
1. **Publication inventory:** Obtain edition identifiers, intended logical pages and the treatment of covers, inserts and intentional blanks. Required; a file's page count alone does not establish the finished product.
2. **Finished demand:** Collect the required number of finished copies for each edition and any separately stated spare parts. Required; do not invent an overrun allowance.
3. **Supplier plan:** Request the actual section grouping, parts per copy, binding approach and the supplier's definitions of its counting units. Default: unresolved; do not derive a press layout from familiar booklet conventions.
4. **File evidence:** Obtain file revision identifiers and ordered page lists. Default: document-only reconciliation; no file inspection is claimed.
5. **Quantity status:** Distinguish requested, planned, printed, accepted and delivered amounts. Default: supplied quantities are proposals unless evidence establishes completion.
6. **Approval boundary:** Identify the person allowed to accept changes to pagination, blanks or copy quantity. Default: prepare a discrepancy handoff only.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Name the exact edition and revision being compared. Keep different language, regional or personalized editions in separate rows even when their page counts happen to match.
2. List the finished parts that make one complete copy. Record whether the cover is a separate part or included in the text count according to the supplied plan, not according to terminology alone.
3. Translate each source's count into its declared unit. A logical page, file page, leaf, supplier section and finished copy are not interchangeable labels; unresolved definitions remain questions.
4. ⚠️ Reconcile the ordered logical content before multiplying quantities. Identify intentionally blank positions, missing positions and duplicated content without assuming every blank is waste or every file page is required.
5. Map each logical range to the supplier's stated section or part. Flag overlaps, uncovered ranges and assignments that cross editions; do not repair the section plan by inventing an imposition rule.
6. Calculate required part quantities from copies and the supplied number of each part per copy. Keep separately requested spares outside the base demand so they are not counted twice.
7. Compare each calculated requirement with the corresponding supplied plan. Distinguish a numerical shortfall from an unverified production allowance or a unit mismatch.
8. Check whether the quantities describe the same production stage. Printed sheets do not establish accepted finished books; damaged parts or unassembled work require their own evidence.
9. Prepare targeted questions for the supplier or publication owner. If changing a blank or section could alter page order, binding or content, state the dependency rather than treating it as a harmless arithmetic correction.
10. Deliver a quantity ledger and a release boundary. State which calculations were checked and which physical, file or supplier confirmations remain outstanding.

For any actual section constraints, allowable pagination or production allowance use [VERIFY: the supplier's current job specification and approved section plan]. This skill does not prescribe how many pages a section must contain or what amount of spoilage to add.

## Decision rules
- IF the cover is counted separately in one source but included in another THEN normalize the counting basis before comparing BECAUSE unequal labels can describe the same publication.
- IF an edition has its own content THEN retain its quantity separately BECAUSE matching page totals do not make parts interchangeable.
- IF a supplier allowance is not documented THEN keep it outside confirmed demand BECAUSE an assumed overrun changes the order.
- IF logical ranges overlap THEN flag the duplicate assignment BECAUSE a correct grand total can still repeat some content and omit other content.
- IF only planned quantities exist THEN report planned coverage BECAUSE arithmetic is not evidence that usable copies were produced.

## Output template
```text
Job boundary: <edition, revision and quantity stage; up to three lines>
Content basis: <pages, blanks, covers and supplied section definitions>
Quantity bridge: <up to ten rows; attach complete ledger when larger>
Edition/part | Per-copy requirement | Copies | Base parts | Separate allowance | Planned/observed | Difference
Content exceptions: <uncovered, repeated or ambiguous content positions>
Questions: <up to three consolidated supplier/owner questions>
Disposition: <ready for stated check / blocked / revision proposed>
Verification: <arithmetic and actual inspections performed, with limits>
```

## Quality checklist
- [ ] Each quantity has a unit and production stage.
- [ ] Edition identities remain attached to content and parts.
- [ ] Cover, insert and blank treatment follows supplied evidence.
- [ ] Per-copy requirements are established before multiplication.
- [ ] Allowances are separate from base demand.
- [ ] Section mappings expose gaps and overlaps.
- [ ] Accepted finished copies are not inferred from planned parts.
- [ ] Open decisions identify the needed evidence and responsible role.

## Anti-patterns
- **File count equals book count:** file pages automatically define the physical product. Fix: reconcile the finished specification and supplied page sequence.
- **Universal section rule:** a familiar grouping is imposed on every job. Fix: use the supplier's actual section plan and identify missing constraints.
- **Grand-total comfort:** equal totals conceal repeated content. Fix: compare named logical ranges as well as quantities.
- **Allowance laundering:** extra production is silently added to the customer order. Fix: identify the source and approval of each allowance.
- **Stage mixing:** printed pieces are called completed books. Fix: separate production, acceptance and assembly evidence.

## Worked example
**Input:** Fictional publisher Alder requests 30 copies of edition Pine. Its approved supplier plan requires one separate cover and two named text sections, A and B, per copy. No spare parts are authorized. The production proposal lists 30 covers, 30 A sections and 28 B sections. The page mapping shows A and B cover the approved logical text without overlap. Nothing has been printed.

**Output:**
```text
Job boundary: Pine edition, supplied approved plan; production proposal only.
Content basis: Separate cover; one A and one B section per finished copy. Supplied mapping has no text gap or overlap.
Quantity bridge:
Edition/part | Per-copy requirement | Copies | Base parts | Separate allowance | Planned/observed | Difference
Pine cover | one | 30 | 30 | none | 30 planned | zero
Pine A | one | 30 | 30 | none | 30 planned | zero
Pine B | one | 30 | 30 | none | 28 planned | two short
Content exceptions: None in the supplied mapping; actual files uninspected.
Questions: Will the supplier revise B to the required 30 parts, or is a different approved requirement missing?
Disposition: Blocked for quantity confirmation; the proposal cannot establish 30 complete copies.
Verification: 30 × one checked for each part; no printing, acceptance or assembly observed.
```

**Bad output:** “There are 88 parts, so the 30-copy order is essentially complete.”
The total hides a shortage in a part required by every copy and invents completion.

## Edge cases
- An insert is supplied by a different vendor: retain its revision, quantity and arrival state separately; do not assume the printer's total includes it.
- Several editions share a genuinely identical part: aggregate only after supplied interchangeability is confirmed and keep the allocation back to each edition.
- The page list changes after the quote: compare the new content basis with the earlier section plan before reusing quantities.
- The supplier reports only sheets: ask for the evidenced relationship to accepted parts and copies; do not invent a conversion.

## Test case
**Input:**
> Fictional editions Birch and Cedar each need ten books. Their covers differ, but the proposal offers twenty unspecified covers and says the grand total is right.

**Assertions:**
1. Keeps the cover demand split by edition.
2. Marks allocation and cover identity unresolved despite the total of twenty.
3. Requests the edition-specific production evidence.
4. Does not claim copies were produced or accepted.
