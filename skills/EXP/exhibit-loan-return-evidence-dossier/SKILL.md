---
id: EXP-006
name: exhibit-loan-return-evidence-dossier
domain: Exhibition Interpretation Operations
subdomain: Loan return records
version: 1.0
description: Assemble a loan-return dossier linking exhibited objects, associated components, packing records, condition observations and custody acknowledgments when an exhibition closes.
triggers: ["prepare an exhibit loan return dossier", "reconcile borrowed objects before return", "link return packing and condition records", "check missing loan components", "separate dispatch from lender receipt"]
not_for: ["accessioning a new collection [ARC-001]", "ordinary shipment quantity reconciliation [SHP-001]", "conservation treatment or physical packing instructions", "deciding ownership, liability or insurance coverage"]
requires: []
risk_level: medium
---

# Exhibit loan return evidence dossier

## Purpose
Prepare a record package showing which borrowed objects and associated components are being returned, what observations accompany them and which custody events are evidenced. The dossier supports the responsible registrar's review without interpreting legal obligations, prescribing handling or treating a dispatch record as proof that the loan is closed.

## Inputs to collect
1. **Loan item schedule:** Obtain the agreed identifiers and return scope supplied by the registrar or responsible loan owner. Required; do not infer ownership or return obligations from an exhibition label.
2. **Associated components:** Obtain the schedule for frames, mounts, cases, accessories and lender-supplied packing materials. Default: unknown component scope, with explicit confirmation needed before declaring completeness.
3. **Return instructions:** Obtain the applicable lender-approved packing and documentation instructions as supplied for this return. Default: document missing instructions; provide no substitute physical packing method.
4. **Condition records:** Obtain relevant outgoing, installation and pre-return observations, with object identity and observation context. Default: no condition comparison where equivalent records are unavailable.
5. **Packing and custody evidence:** Collect package-object maps, seals or references if used, dispatch records and acknowledgments. Default: only supplied events are evidenced; no inference of receipt from a shipping label.
6. **Decision owners:** Identify the registrar, qualified conservator where needed and the receiving contact. Default: role placeholders, with closure decisions pending.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Establish the return boundary using the loan schedule revision, named return movement and responsible registrar. Separate items returning now from those retained under a supplied extension or transferred under another instruction.
2. Create an identity ledger connecting each loan item to its exhibition identifier and return record. Retain aliases as mappings; do not replace a lender identifier with a convenient local title.
3. Associate each component with its parent object or independent return obligation. A venue-owned display support and a lender-supplied frame may have different dispositions; follow the supplied schedule rather than visual proximity.
4. Reconcile the return scope against observed or recorded components. Classify missing, unidentified, substituted and intentionally retained items separately so an unexplained absence is not hidden as a packing exception.
5. ⚠️ Compare condition observations only where the object, region and viewing context correspond. Record a newly reported mark as an observation requiring qualified review, not as proof of when damage occurred or who caused it.
6. Link each item to the packing record specified for this movement. Record whether the supplied instructions and pack-out evidence are present; do not infer compliant physical packing from the existence of a crate photograph.
7. Trace custody events separately: ready for collection, handed over, in transit, received and acknowledged as complete if those states are used by the parties. Attach evidence to each claimed event rather than marking every later state complete after dispatch.
8. Identify unresolved exceptions that prevent a clear return record, such as an unpaired component, unreadable item identifier or unreviewed condition difference. Assign each to the responsible role and state the specific evidence or decision needed.
9. Assemble a concise dossier index with record references, revisions and missing attachments. Keep sensitive contact or contractual material in the authorized record location rather than reproducing it unnecessarily in a public summary.
10. Present a bounded handoff recommendation to the registrar. Distinguish documentation readiness from physical movement approval, lender receipt and formal loan closure; use the supplied closure process rather than inventing one.

## Decision rules
- IF a component's ownership or return disposition is unclear THEN leave it unresolved for the loan owner BECAUSE display proximity does not establish return scope.
- IF condition records show different views THEN request comparable evidence or qualified review BECAUSE an unseen area in an earlier image does not prove a later change.
- IF a dispatch record exists without recipient acknowledgment THEN report dispatch only BECAUSE movement evidence does not establish complete return receipt.
- IF an item is intentionally retained under a supplied instruction THEN record that instruction and exclude it from this movement BECAUSE an authorized split return differs from a missing item.
- IF physical packing instructions are absent or conflicting THEN flag the instruction gap for the registrar BECAUSE a record-preparation task cannot invent a safe packing method.

## Output template
```text
Return boundary: <loan schedule, movement and decision owner; up to three lines>
Identity and scope ledger: <up to ten rows; attach remainder>
Loan item/component | Local identity | Required disposition | Evidence | Exception
Condition comparison: <up to five observations, comparable evidence and review needs>
Packing record index: <item-to-package reference and instruction/evidence status; up to six rows>
Custody timeline: <one line per evidenced event; unknown later states explicit>
Resolution queue: <up to six owner, question and required-evidence entries>
Handoff boundary: <documentation readiness, movement authority and closure state; up to four lines>
```

## Quality checklist
- [ ] The return scope cites the supplied loan schedule or remains pending.
- [ ] Lender and local identities are linked without silent replacement.
- [ ] Associated components have explicit dispositions or unresolved scope.
- [ ] Condition differences distinguish observation from causation.
- [ ] Packing records are linked without claiming an unobserved packing method was followed.
- [ ] Each custody state has separate evidence.
- [ ] Missing attachments and unresolved decisions have responsible roles.
- [ ] Documentation readiness is not described as lender receipt or loan closure.

## Anti-patterns
- **Title-based return:** an object with a similar title fills the schedule row. Fix: reconcile the agreed identity references.
- **Component disappearance:** a frame is omitted because the main object is present. Fix: track the component's return disposition explicitly.
- **Damage attribution:** a newly noticed mark is blamed on the exhibition. Fix: preserve comparable observations and seek qualified assessment.
- **Crate-photo compliance:** a photograph is treated as proof of following every packing instruction. Fix: state exactly what the photograph establishes.
- **Dispatch equals closure:** a carrier handover is labeled complete loan return. Fix: preserve receipt and closure as distinct pending states.

## Worked example
**Input:** Fictional gallery Rowan returns lender item L-P, locally displayed as Panel-P, with lender frame F-P. Schedule R requires both. The pack-out record maps L-P to crate C-P but does not mention F-P. A pre-return note reports a corner mark; the earlier image does not show that corner. A signed dispatch handover exists, but no recipient acknowledgment is supplied.

**Output:**
```text
Return boundary: Schedule R, current Rowan return movement; registrar review required.
Identity and scope ledger:
Loan item/component | Local identity | Required disposition | Evidence | Exception
L-P | Panel-P | return | pack-out links L-P to C-P | none in identity mapping
F-P | lender frame | return | schedule R only | packing and location evidence missing
Condition comparison: Corner mark reported before return; earlier image omits that corner. Change and cause are unestablished; qualified review or comparable evidence needed.
Packing record index: L-P to C-P evidenced by pack-out record; F-P mapping missing. Instruction compliance not established by the supplied summary.
Custody timeline: Signed dispatch handover supplied; recipient receipt and completeness acknowledgment unknown.
Resolution queue: Registrar to locate F-P and reconcile its packing record; conservator role to assess the reported mark from appropriate evidence; receiving contact to supply receipt and scope acknowledgment when available.
Handoff boundary: Dossier incomplete for component scope and condition review. Dispatch is evidenced; no movement approval, lender acceptance or loan closure is inferred.
```

**Bad output:** “The panel shipped, so the loan is closed; the gallery caused the corner damage.”
This ignores the frame and missing receipt while asserting causation from incomparable observations.

## Edge cases
- Several loan items share a crate: retain separate item and component rows beneath the package reference so package receipt cannot conceal item-level exceptions.
- A lender agrees to a split return: attach the supplied instruction and record the retained subset without labeling it lost.
- A component has no independent identifier: use a local descriptive reference tied to the parent and request confirmation; do not fabricate a lender-issued number.
- The recipient acknowledges packages but has not checked contents: record package receipt and leave object completeness pending.

## Test case
**Input:**
> Fictional gallery Linden returns objects A and B in crate C. The receiver acknowledges C but says the contents are not yet checked. A mount associated with B appears in the exhibition inventory, but its owner and return disposition are unknown.

**Assertions:**
1. Distinguishes crate receipt from confirmation that A and B were received complete.
2. Leaves the mount's return disposition unresolved for the loan owner.
3. Does not declare the loan closed.
4. Provides no invented physical packing instructions or ownership conclusion.
