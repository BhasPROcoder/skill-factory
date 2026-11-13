---
id: BID-002
name: supplier-substitution-disposition
domain: Procurement Evidence Decisions
subdomain: Substitution evidence
version: 1.0
description: Prepare a traceable disposition for a supplier's proposed replacement when requirements, evidence and approval authority must be reconciled before release.
triggers: ["supplier proposes an alternate","review a substituted part","assess replacement evidence","document a substitution decision","scope a one-order deviation"]
not_for: ["normalizing quoted quantities [BID-001]","onboarding an approved vendor [MOP-005]"]
requires: []
risk_level: medium
---

# Supplier substitution disposition

## Purpose
Prepare a bounded decision record when a supplier offers a different item, revision or production method against an existing requirement. Distinguish a technical comparison, a request to waive a difference, and an actual release by an authorized person.

## Inputs to collect
1. Baseline identity: obtain the ordered identifier, revision, quantity and use. These identify what the replacement must satisfy. Without a confirmed baseline, hold the comparison.
2. Candidate identity: collect the proposed alternate identifier, revision, source and affected shipment or lot. These bound any later disposition. If unavailable, record the missing identity.
3. Requirements: collect mandatory attributes, allowed variations, interfaces and any fields that require separate approval. Use only the buyer's supplied priorities; do not infer acceptance criteria from marketing descriptions.
4. Evidence: obtain referenced drawings, test results, samples or declarations and the item each covers. If no supporting evidence is supplied, record the supplier's statement as a claim.
5. Authority: identify who can confirm technical fitness, waive a requirement, accept a temporary exception and release an order. Default to a recommendation only when no authority or signoff is shown.
6. Consequences: identify downstream labels, instructions, orders or assemblies affected by substitution. Default to an explicit unknown rather than assuming interchangeability.

If a required input is missing and has no safe default, ask in one message with at most three questions.

## Procedure
1. Pin the baseline and proposed item to their exact identifiers. Preserve the original order unchanged while preparing the comparison; similar family names are insufficient identity evidence.
2. Define the affected use and release boundary. Record whether the request concerns a sample, a single shipment, a bounded production run or a permanent change. Leave the boundary unresolved where unspecified.
3. Split the requirements into independently verifiable rows. Separate fit, intended function, appearance, traceability and downstream handling only when relevant to the stated use.
4. Attach the best available evidence to each requirement. Record what the evidence actually establishes, its revision and what remains unverified. ⚠️ Evidence for a related family member does not establish that the offered revision passed.
5. Classify each row as supported match, documented difference, unsupported claim, conflicting evidence or not applicable with a reason. Preserve units and test conditions when comparing observations.
6. Translate every material difference into an operational question. Identify what could stop working, which downstream artifact could become misleading, and the specific inspection or authority decision that would resolve it.
7. Choose a proposed disposition on the supplied evidence: hold for clarification, decline on this basis, recommend acceptance within scope, or request a documented exception. Do not turn a supplier promise into a waiver of a mandatory requirement.
8. Specify segregation and release handling where relevant. A sample sent for evaluation remains distinct from stock cleared for use. If a lot-specific deviation is considered, attach its lot limit and the condition that ends it.
9. Prepare the decision trail for the appropriate reviewer. State which decisions are proposed and which are already evidenced by an authorized record; leave an unverified approval field empty rather than inventing a signatory.

## Decision rules
- IF a mandatory requirement is contradicted THEN hold or recommend rejection on that basis BECAUSE only a valid change or authorized exception can alter the baseline.
- IF the proposed item is supported by a sample from another revision THEN request candidate-specific evidence BECAUSE similarity does not prove that the inspected item is the one offered.
- IF an authorized deviation is limited to one lot THEN retain that exact limit in receiving instructions BECAUSE the decision does not automatically change the standing order.
- IF acceptance evidence is complete but release authority is absent THEN recommend review without releasing BECAUSE technical support and authority to commit are different conditions.

## Output template
```text
Change boundary: <baseline, alternate, affected use and lot; up to three lines>
Requirements: <one row per decision-relevant requirement>
Requirement | Baseline | Candidate evidence | Finding | Open action
Downstream handling: <segregation, records and affected use; up to four lines>
Proposed disposition: <hold, decline, recommend acceptance, or request exception; give reason>
Release evidence: <actual authority and recorded decision, or none supplied>
Next gate: <evidence, responsible role if known, and scope of any future decision>
```

## Quality checklist
- [ ] Both identifiers and revisions are supplied or explicitly missing.
- [ ] The requested use and affected lot or order are bounded.
- [ ] Every requirement row compares the same attribute on both items.
- [ ] Supplier claims remain separate from inspected supporting evidence.
- [ ] Evidence gaps and demonstrated mismatches have different findings.
- [ ] Sample evaluation is distinguished from release for production.
- [ ] Proposed exceptions identify what baseline requirement would change.
- [ ] No unverified signature, approval or permanent change is implied.

## Anti-patterns
- **Family resemblance:** a similar product name is treated as interchangeability evidence. Fix: compare the exact offered revision against the actual requirement.
- **Approval by arrival:** physical receipt is treated as permission to use. Fix: specify the receiving hold and who can release it.
- **Single-property pass:** one matching dimension masks an unsupported interface or handling requirement. Fix: keep decision-critical rows separate.
- **Permanent drift:** a one-shipment concession becomes an informal default. Fix: preserve the boundary and route lasting changes through the owner's change process.
- **False expertise:** the comparison certifies safety or regulatory compliance from a supplier description. Fix: stop at evidence preparation and require the appropriate qualified review.

## Worked example
**Input:** Fictional archive studio Mora orders display sleeves Sleeve-A revision Clay for exhibit lot Pine. Its brief requires a clear viewing window and a blue identification tab. Supplier Venn proposes Sleeve-B revision Moss for Pine only. A photo explicitly labeled B/Moss shows a clear window and a green tab. Venn says green is acceptable. The studio's buyer can request a deviation but the curator must authorize a color change. No authorization was supplied.

**Output:**
```text
Change boundary: Sleeve-A/Clay to Sleeve-B/Moss for display sleeves in exhibit lot Pine only.
Requirements:
Requirement | Baseline | Candidate evidence | Finding | Open action
Viewing window | clear | supplied B/Moss photo shows clear window | supported visual match for depicted sample | confirm delivered lot identity if released
Identification tab | blue | supplied B/Moss photo shows green | documented difference | obtain curator decision on color deviation
Downstream handling: Keep candidate identified separately pending disposition. If an exception is granted, annotate Pine's receiving record and exhibit identification instructions; do not alter the standing baseline.
Proposed disposition: Hold; buyer may request a Pine-only color exception. Supplier preference does not waive the blue-tab requirement.
Release evidence: None supplied. Curator authorization is required for the color change; no release decision evidenced.
Next gate: Buyer presents the labeled photo and affected identification workflow to the curator. Document exact scope and receiving release authority before use.
```

**Bad output:** “Window matches; approve B for all exhibitions.”
The window does not resolve the tab mismatch, and the proposed scope exceeds both the request and the available authority.

## Edge cases
- A candidate is withdrawn and replaced mid-review: preserve the old record and repeat affected comparisons for the newly identified revision.
- Conflicting product sheets have no revision dates: record the conflict and request the controlling candidate-specific document; do not pick the favorable sheet.
- An approved substitute arrives in an unlisted lot: hold that lot pending a scope decision rather than extending the earlier exception.
- A claim concerns safety-critical or regulated use: route evidence to the qualified reviewer for the applicable context and current requirements; do not supply an independent certification.

## Test case
**Input:**
> A fictional supplier proposes a new label stock for one shipment. An earlier sample met the buyer's appearance requirement, but the supplier cannot confirm the offered stock has the same revision. No substitution authority is identified.

**Assertions:**
1. The earlier sample does not establish acceptance of the unidentified revision.
2. The record asks for candidate-specific identification and evidence.
3. The proposed scope stays limited to the requested shipment.
4. No approval, release or permanent baseline change is claimed.
