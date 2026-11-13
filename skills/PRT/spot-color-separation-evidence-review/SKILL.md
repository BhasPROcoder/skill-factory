---
id: PRT-003
name: spot-color-separation-evidence-review
domain: Print Production Handoffs
subdomain: Separation evidence
version: 1.0
description: Compare intended ink roles with supplied separation evidence when a print file may contain duplicate spot definitions, unexpected process conversion or missing marks.
triggers: ["review spot color separations", "why are extra inks listed", "check spot ink export", "compare ink intent with separations", "find a missing spot object"]
not_for: ["choosing a visual palette [MVA-003]", "operating a printing press", "certifying printed color from a screen"]
requires: []
risk_level: medium
---

# Spot color separation evidence review

## Purpose
Produce an object-to-ink evidence ledger for a particular print revision. Separate the intended production roles from what the supplied separation views actually show, so similar screen colors do not conceal additional inks or missing content.

## Inputs to collect
1. **Ink intent:** Collect the job's intended process and spot ink roles, including any non-color production marks. Required; an attractive composite preview does not define the intended ink set.
2. **File identity:** Obtain the exact exported production revision and its relationship to the design source. Required; reviewing another export cannot establish this file's state.
3. **Separation evidence:** Request the named output channels and isolated views of relevant objects. Default: evidence unavailable, with no assertion that file channels were inspected.
4. **Object map:** Identify logos, backgrounds, text and production marks whose ink assignment matters. Default: review supplied named objects only and disclose limited coverage.
5. **Supplier instructions:** Collect the job-specific treatment of spot inks, aliases, transparency and specialized marks. Default: unresolved; no assumed conversion or channel merging.
6. **Decision owner:** Identify who can change ink intent or approve export corrections. Default: prepare findings for review without modifying production files.

If required inputs lack safe defaults, ask in one message with at most three questions.

## Procedure
1. Record the revision and the exact evidence available. Distinguish native-file properties, exported-file channels, screenshots and physical proof observations rather than treating them as equivalent.
2. List the intended ink roles using supplied identifiers. Preserve the original spelling alongside any proposed alias; a similar name does not prove two definitions should be merged.
3. Inventory the channels reported in the production evidence. Classify each as expected, unexpected or unresolved against the job specification, without assuming every extra channel is an error.
4. Map each critical object to the channel or channels in which it appears. Record the inspected region so a global channel list is not mistaken for proof that a particular object exists there.
5. ⚠️ Compare isolated evidence with the composite view. An object visible in the composite but absent from its intended channel needs investigation; do not conclude that matching screen appearance establishes correct ink assignment.
6. Identify possible duplicate definitions by both their intended role and actual object use. Keep the proposed consolidation conditional on supplier confirmation because differently named channels may have deliberately separate production purposes.
7. Trace unexpected process-channel content back to the named object where evidence permits. Report the observation without inventing which export setting caused it; unresolved cause and observed result are different fields.
8. Check the declared treatment of overlapping objects or special production marks against supplied output evidence. If the necessary views are missing, request them rather than prescribing a universal setting.
9. Prepare the smallest proposed correction and its recheck boundary. A corrected ink definition requires inspection of the new export, including objects sharing that definition, rather than just a renamed swatch in the source.
10. Deliver an ink ledger with unresolved questions and the next review owner. State whether any physical proof or supplier output was examined and keep production approval separate from this evidence review.

For changing software behavior and production requirements use [VERIFY: the current export application's documentation and the supplier's approved job instructions]. No particular menu command, ink library value or conversion setting is assumed by this workflow.

## Decision rules
- IF two channels have similar names THEN compare their intended roles and object assignments before merging BECAUSE naming resemblance does not establish production equivalence.
- IF a composite object has no evidence on its intended channel THEN flag an assignment gap BECAUSE composite visibility does not prove separation placement.
- IF a special mark uses an extra channel THEN check the supplier specification BECAUSE an additional channel may be intentional.
- IF the export changes THEN review the new output evidence BECAUSE a source-file correction alone does not establish the delivered result.

## Output template
```text
Review boundary: <revision and evidence type; up to three lines>
Ink intent: <declared roles and unresolved instructions>
Separation ledger: <up to ten rows; attach remaining rows>
Object/region | Intended role | Observed channels | Evidence | Finding
Proposed corrections: <up to five; owner and recheck scope for each>
Questions: <up to three consolidated questions>
Disposition: <ready for named next check / blocked>
Verification limits: <uninspected channels, objects or physical output>
```

## Quality checklist
- [ ] File identity matches the evidence under review.
- [ ] Intended ink roles come from supplied instructions.
- [ ] Each finding identifies an object or explicitly remains channel-level.
- [ ] Similar channel names are not automatically merged.
- [ ] Composite appearance is separate from channel assignment.
- [ ] Proposed changes include a new-export recheck.
- [ ] Special production channels receive a documented disposition.
- [ ] Physical color approval is not inferred from screen evidence.

## Anti-patterns
- **Palette substitution:** a pleasant appearance is treated as production correctness. Fix: compare intended roles with isolated output evidence.
- **Name-only merge:** every similar spot name is consolidated. Fix: establish role and supplier approval first.
- **Cause invention:** an unexpected channel proves a particular export setting was wrong. Fix: report the observed assignment and investigate the cause separately.
- **Source-only closure:** renaming a source swatch closes the finding. Fix: examine the replacement production export.
- **Universal knockout advice:** one overlap setting is prescribed for all marks. Fix: use the supplied object-specific production requirement.

## Worked example
**Input:** Fictional studio Larch supplies export E. Its job instruction assigns logo L to spot role Brand and crop guide G to a separate supplier-defined Guide role. Isolated evidence shows L only on process channels, while G appears on Guide. The composite shows both. No physical proof is supplied.

**Output:**
```text
Review boundary: Export E; supplied isolated and composite views of L and G.
Ink intent: L uses Brand; G uses the separate Guide role under supplied instructions.
Separation ledger:
Object/region | Intended role | Observed channels | Evidence | Finding
L/logo | Brand | process channels only | supplied isolated views | intended assignment not evidenced
G/guide | Guide | Guide | supplied isolated view | consistent with supplied role
Proposed corrections: Export owner to investigate L assignment and provide replacement export evidence for L and other objects sharing its definition.
Questions: Which source assignment and export treatment produced L on the process channels?
Disposition: Blocked for L assignment review; Guide is not an unexplained extra ink.
Verification limits: Supplied regions only; no physical proof or printed color inspected.
```

**Bad output:** “The composite looks right; delete Guide because it is an extra color.”
This ignores the documented Guide role and substitutes appearance for the missing Brand assignment.

## Edge cases
- A channel name is truncated in a screenshot: request its full identifier before proposing an alias or deletion.
- Only a channel list exists: report inventory findings but leave object placement unverified.
- A spot role is intentionally converted for a particular edition: retain the edition-specific approval instead of declaring every conversion wrong.
- An object is absent in both composite and isolated views: investigate omission or view coverage before diagnosing ink assignment.

## Test case
**Input:**
> Fictional export F lists Brand and Brand-copy. Both appear orange on screen, but no isolated views or supplier alias instructions are available.

**Assertions:**
1. Records both channel identifiers without merging them.
2. Requests object assignment evidence and intended ink roles.
3. Does not certify the export from matching screen colors.
4. Gives a conditional review disposition rather than a production approval.
