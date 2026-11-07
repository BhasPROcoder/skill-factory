---
id: ARC-001
name: accession-lot-inventory-reconciliation
domain: Collection Description Operations
subdomain: Accession reconciliation
version: 1.0
description: Reconcile a collection transfer list with received containers and their observed contents when an accession's scope or completeness is uncertain.
triggers: ["check what arrived in this collection transfer", "reconcile an accession list", "missing items in archive boxes", "match received containers to donor inventory", "document an incomplete collection delivery"]
not_for: ["warehouse movement balance reconciliation [WHS-001]", "determining legal ownership or donation validity", "designing a collection hierarchy [ARC-002]"]
requires: []
risk_level: medium
---

# Accession lot inventory reconciliation

## Purpose
Create a defensible receiving record that distinguishes what a transfer list promised from what was actually observed. Preserve original identifiers and uncertainty so later cataloging does not turn a container count into an unsupported claim about item completeness or ownership.

## Inputs to collect
1. **Transfer boundary:** Obtain the lot identifier, sender's inventory and expected delivery stages. Required; without a list, describe observed material but do not infer a missing balance.
2. **Receiving evidence:** Collect receipt notes, container labels and inspected contents. Required for reconciliation; a delivery confirmation alone establishes neither internal content nor condition.
3. **Counting units:** Identify whether each stated quantity means boxes, folders, volumes, leaves or digital files. Default: preserve the source wording and mark unit relationships unknown.
4. **Prior identifiers:** Request former shelf marks, labels, inventory numbers and any supplied crosswalk. Default: retain every visible label without treating similar names as identical.
5. **Inspection limits:** State which containers can be opened and what evidence may be recorded. Default: use supplied records only and propose further inspection; do not handle fragile or restricted material.
6. **Decision authority:** Identify who may resolve discrepancies or accept a partial transfer. Default: unresolved differences remain pending rather than silently waived.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Define the accession event being reconciled, separating this delivery from earlier or anticipated later deliveries. Use the sender's identifiers even when a local identifier will eventually be assigned.
2. Transcribe the expected list into rows that preserve the original counting unit. Record ranges as ranges unless the source establishes which members exist.
3. Create a received-container list using actual receiving evidence. Include sealed, unopened or inaccessible states; do not convert receipt into an inspected-content assertion.
4. Match containers to expected rows through explicit labels or supplied correspondence. Keep tentative matches visible when several containers carry the same broad label.
5. ⚠️ Reconcile at the same level of description. Three received boxes cannot prove that three promised volumes arrived, and one folder can contain several listed documents.
6. Record inspected content under its container while preserving source order and labels. Separate an observed item from a catalog description inferred from its appearance.
7. Compare expected and observed members only where identity and units are sufficiently clear. Classify matched, not yet inspected, unexpected, apparently missing or ambiguous, with the evidence behind each classification.
8. Investigate discrepancies through targeted questions: whether an item travels separately, whether a list uses another identifier, or whether a container has a supplied subinventory. Do not presume loss, misrepresentation or theft from an unmatched row.
9. ⚠️ Preserve both versions when a sender corrects an inventory. Link the correction to its author and scope instead of rewriting the receiving record as if the original discrepancy never existed.
10. Produce a bounded accession handoff with unresolved rows and their next evidence check. State separately that custody observations do not determine legal title, permission to reproduce, appraisal value or authenticity.

For any formal accession requirements, check the current collection policy and responsible repository instructions. Use [VERIFY: required receiving fields and acceptance authority in the repository's current accession procedure] rather than inventing a mandatory form or retention rule.

## Decision rules
- IF a container is sealed or uninspected THEN mark its content unresolved BECAUSE evidence of arrival does not identify everything inside.
- IF expected and received quantities use different units THEN withhold a numerical shortage BECAUSE subtraction requires comparable units.
- IF one object has several former labels THEN retain a crosswalk and source evidence BECAUSE deleting older labels can break provenance links.
- IF an unmatched item is discovered THEN isolate its description from confirmed matches BECAUSE assigning it to the nearest title may hide a genuine discrepancy.
- IF a partial transfer is accepted THEN preserve the outstanding list and accepting authority BECAUSE acceptance does not mean completeness.

## Output template
```text
Transfer: <lot, delivery and source evidence; up to three lines>
Container register: <up to eight rows; attach continuation for larger lots>
Container | Labels | Observed state | Content evidence
Reconciliation: <one row per expected member or unresolved group>
Expected reference and unit | Received reference | Finding | Evidence
Identifier links: <confirmed and tentative crosswalks; up to six lines>
Open checks: <up to three grouped questions and responsible role>
Disposition: <inspection scope, unresolved coverage and unperformed actions>
```

## Quality checklist
- [ ] The delivery boundary is separated from other transfer stages.
- [ ] Every numerical comparison uses the same counting unit.
- [ ] Container arrival and content inspection have different evidence fields.
- [ ] Original labels survive local identifier assignment.
- [ ] Tentative matches remain distinguishable from confirmed identity.
- [ ] Inventory corrections retain their source and previous state.
- [ ] Custody, completeness and legal title are not conflated.

## Anti-patterns
- **Box equality:** equal box counts imply complete contents. Fix: reconcile the promised description level against inspected members.
- **Nearest-title matching:** an unfamiliar item is forced into the closest expected title. Fix: keep an unresolved identity row.
- **Cleaned history:** a revised inventory erases a discrepancy. Fix: retain the superseded statement and correction evidence.
- **Ownership by receipt:** possession is called proof of title. Fix: report physical receipt and route ownership evidence separately.
- **False shortage:** volumes are subtracted from cartons. Fix: obtain the missing unit relationship before arithmetic.

## Worked example
**Input:** Fictional repository Willow expects Lot Cedar containing three labeled volumes V1, V2 and V3. The sender predicts two boxes. Receiving notes confirm two boxes: A was opened and contains V1 and V2; B arrived sealed and has not been inspected. No information establishes B's contents. No acceptance decision has been supplied.

**Output:**
```text
Transfer: Willow Lot Cedar, current delivery; sender list and receiving notes supplied.
Container register:
Container | Labels | Observed state | Content evidence
A | A | Opened | V1 and V2 observed
B | B | Sealed | Contents not inspected
Reconciliation:
Expected reference and unit | Received reference | Finding | Evidence
V1 volume | A/V1 | Matched | Receiving notes
V2 volume | A/V2 | Matched | Receiving notes
V3 volume | Unknown | Not yet established, not proven missing | B uninspected
Identifier links: V1 and V2 retained as sender references; no new local identifiers assigned.
Open checks: Authorized receiving staff should inspect or obtain an itemized record for B and establish whether V3 is present.
Disposition: Two expected boxes received; two of three listed volumes observed. One volume's presence remains unresolved. No acceptance or ownership conclusion.
```

**Bad output:** “Two boxes arrived, so all three volumes are complete and owned by Willow.”
This converts container receipt into unsupported item completeness and ownership.

## Edge cases
- Several deliveries share a label: use receipt-event identifiers and distinguish repeated packaging labels from duplicate contents.
- A container cannot safely be opened: record the constraint and route inspection to the responsible trained handler; do not improvise handling instructions.
- Digital files accompany physical objects: maintain a separate file inventory and link supplied correspondence without equating file count to object count.
- The sender's list has uncertain ranges: preserve the uncertainty and request member-level evidence before marking omissions.

## Test case
**Input:**
> Fictional archive Juniper receives one carton against a transfer list saying five folders. The carton is unopened and a courier receipt says delivered. Prepare the receiving handoff.

**Assertions:**
1. Records one received carton without subtracting it from five folders.
2. Keeps folder identities and completeness unresolved.
3. Requests authorized content evidence.
4. Makes no claim of ownership or formal acceptance.
