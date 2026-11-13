# Shipment Record Reconciliation (SHP)

Reconcile package identities, contents and shipment records without asserting physical handover or carrier acceptance.

Macro-area: Operations & Supply Chain

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| SHP-001 | [shipment-package-contents-reconciliation](shipment-package-contents-reconciliation/SKILL.md) | Reconcile order-line quantities and package assignments when a shipment is split, consolidated or repacked. | reconcile parcels with order lines; check a packing list; trace a repacked shipment | validated |
| SHP-002 | [lot-trace-scope-reconciliation](lot-trace-scope-reconciliation/SKILL.md) | Trace a specified product lot through supplied inventory, transformation, shipment, and return records to prepare a bounded affected-stock and destination handoff. | trace where this product lot went; prepare a lot traceability record; identify shipments linked to an affected batch | validated |
