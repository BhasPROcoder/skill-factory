---
id: RNT-002
name: rental-checkout-accessory-completeness
domain: Rental Asset Operations
subdomain: Checkout kits
version: 1.0
description: Reconcile required rental accessories with the actual checkout kit when base-unit presence does not establish complete fulfillment.
triggers: ["check this rental kit", "is the hire package complete", "reconcile checkout accessories", "missing part in a rental bundle", "verify the accessory handover"]
not_for: ["shipment package totals [SHP-001]", "rental serial allocation [RNT-001]", "equipment safety inspection"]
requires: []
risk_level: medium
---

# Rental checkout accessory completeness

## Purpose
Produce an itemized checkout decision for the accessories promised with a rental asset. Separate quantity, compatibility, observed presence and recipient acknowledgment so a checked box for the main unit cannot conceal an incomplete kit.

## Inputs to collect
1. **Reservation kit definition:** Collect the promised main unit, accessory types, quantities and permitted optional items. This establishes the actual obligation. Default: no universal kit list; the supplied reservation or approved kit definition is required.
2. **Selected physical unit:** Obtain its unique identity and the applicable accessory interface specification. This distinguishes matching parts from visually similar alternatives. Default: compatibility unverified if no specification is supplied.
3. **Observed checkout items:** Obtain item labels, quantities, serials where tracked, inspection time and observer. This anchors the comparison to a physical kit. Default: listed stock is not an observed checkout item.
4. **Substitution rules:** Collect approved substitutes and who may change the promised kit. This prevents an extra unrelated part from satisfying a missing requirement. Default: no substitution authority assumed.
5. **Handover evidence:** Obtain the recipient's itemized acknowledgment and any partial-handover agreement. This distinguishes prepared, presented and received items. Default: prepared only; no recipient receipt inferred.
6. **Exceptions:** Obtain waived items, separately supplied consumables and split deliveries. This keeps omissions visible. Default: no waiver or later delivery promised.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Fix the reservation, selected unit and kit-definition revision being checked. Keep the kit requirement associated with that actual unit rather than a generic product photo.
2. Expand bundles into the smallest independently accountable accessories. Preserve the parent bundle reference so a complete bag and its contents are not counted twice.
3. Assign each requirement a quantity, unit and compatibility basis. Distinguish a pair from a single piece and a reusable accessory from a supplied consumable.
4. Map observed items to requirements using their identities or supplied compatibility evidence. Leave unmatched items in an extras column instead of using them to offset a shortage.
5. ⚠️ Calculate missing quantities only within the same requirement and compatible item class. Two spare covers cannot compensate for an absent connector, even when the grand total of pieces is correct.
6. Mark each mapped item as observed, prepared, presented or acknowledged from the supplied evidence. A scan into a staging area establishes neither recipient possession nor successful operation.
7. Identify a specific remedy for every gap: retrieve the required part, verify a proposed substitute, document an authorized omission or defer the affected handover. Do not choose a customer-facing concession without authority.
8. ⚠️ Reopen the comparison after a main-unit substitution. Retain earlier observations as history, then check whether their accessory interfaces still match the replacement unit.
9. Prepare an itemized handover record showing the exact delivered kit and unresolved exceptions. Give each split-delivery item its own status so a later shipment cannot silently close an earlier gap.
10. State the limited disposition: complete on observed evidence, incomplete or unresolved. Keep safety inspection and technical function testing outside this count-and-identity conclusion.

## Decision rules
- IF a bag is sealed but its contents are unevidenced THEN mark internal completeness unverified BECAUSE the container's presence does not establish each promised accessory.
- IF a substitute has the right quantity but no compatibility basis THEN retain the original gap BECAUSE count equality does not establish interchangeability.
- IF the recipient accepts a partial kit under supplied authority THEN record the omitted requirement and agreement BECAUSE acceptance does not make the original kit complete.
- IF an item was observed before a later kit change THEN require a refreshed association BECAUSE an earlier check may refer to the displaced configuration.

## Output template
```text
Kit boundary: <reservation, main-unit identity, kit revision; up to three lines>
Accessory ledger:
Requirement | Required quantity/unit | Observed item/quantity | Compatibility basis | Handover state | Gap
<up to twelve rows; attach a full ledger for larger kits>
Extras: <unmatched items or none; up to five lines>
Remedies: <gap, action, owner and evidence needed; up to six lines>
Disposition: <complete on observed evidence / incomplete / unresolved; one explanation>
Receipt boundary: <what was acknowledged and what remains unreceived; up to three lines>
```

## Quality checklist
- [ ] The checked kit has a reservation and main-unit identity.
- [ ] Parent containers and contents are not counted twice.
- [ ] Every required item has an explicit quantity and unit.
- [ ] Compatibility has a supplied basis or an unresolved state.
- [ ] Extra items do not offset unrelated shortages.
- [ ] Prepared items are distinguished from received items.
- [ ] Every omission has a remedy or an authorized exception reference.
- [ ] The disposition does not certify safety or technical function.

## Anti-patterns
- **Bag-count shortcut:** one bag is declared a complete kit. Fix: reconcile the contents against the applicable list.
- **Piece-total balancing:** surplus accessories hide a missing type. Fix: calculate shortages by requirement.
- **Visual equivalence:** similar connectors are called interchangeable. Fix: obtain the supplied compatibility basis.
- **Receipt inflation:** a staging scan becomes recipient acceptance. Fix: label the evidence state explicitly.
- **Silent waiver:** an absent item disappears from the record. Fix: retain the requirement and its authorized exception.

## Worked example
**Input:** Fictional display-rental business Hazel promises stand D4 with two compatible shelf clips and one carry sleeve. Its approved D4 list requires clip type K. Checkout observer Mira records two K clips and no sleeve; an extra label pouch is present. Nothing has been handed over, and no waiver is authorized.

**Output:**
```text
Kit boundary: Hazel reservation H; stand D4; supplied approved D4 list.
Accessory ledger:
Requirement | Required quantity/unit | Observed item/quantity | Compatibility basis | Handover state | Gap
Shelf clips | 2 pieces | 2 K clips | supplied D4 list specifies K | observed only | none in count/type
Carry sleeve | 1 piece | 0 sleeves | required by D4 list | not presented | 1 sleeve
Extras: 1 label pouch; not a sleeve substitute.
Remedies: Checkout owner retrieves the sleeve and records a refreshed observation, or obtains an explicit authorized exception before the handover decision.
Disposition: Incomplete; the required sleeve is absent.
Receipt boundary: No recipient acknowledgment or handover evidenced.
```

**Bad output:** “Three accessories are present, so the three-piece kit is complete.”
It substitutes an unrelated pouch for the required sleeve and ignores item-specific matching.

## Edge cases
- A kit is delivered in separate trips: preserve a receipt state for each requirement and identify which trip supplied it.
- An accessory carries no serial: use the approved type and accountable quantity; do not fabricate an individual identifier.
- The recipient supplies a compatible item: record it as recipient-supplied and establish whether the rental obligation was formally changed.
- A disposable item is partly consumed: compare the supplied quantity basis, such as unopened units, rather than treating any remaining material as a full item.

## Test case
**Input:**
> Fictional depot Alder promises two type P feet for stand T. The checkout bag contains one P foot and one type Q foot. No substitution evidence or receipt is available.

**Assertions:**
1. Identifies one supported P foot and one missing P foot.
2. Lists Q as unmatched or compatibility-unverified rather than automatically accepted.
3. Requests the required part or a supported substitution decision.
4. Does not claim a completed handover.
