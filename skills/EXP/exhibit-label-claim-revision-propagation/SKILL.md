---
id: EXP-001
name: exhibit-label-claim-revision-propagation
domain: Exhibition Interpretation Operations
subdomain: Label revision
version: 1.0
description: Trace a changed exhibit claim into every affected label and derivative when new source evidence alters published interpretation.
triggers: ["revise a museum label claim", "update labels after new evidence", "trace a changed attribution", "find outdated exhibit captions", "coordinate interpretive text corrections"]
not_for: ["classifying reconstruction geometry evidence [VEV-001]", "general art-direction handoff [MVA-009]", "authenticating an object or deciding legal ownership"]
requires: []
risk_level: medium
---

# Exhibit label claim revision propagation

## Purpose
Prepare a revision packet that connects a changed interpretive claim to the labels, audio scripts and reproductions that currently express it. The result makes the intellectual change and its publication consequences reviewable without treating a revised source as automatic permission to replace every label.

## Inputs to collect
1. **Changed evidence:** Obtain the supplied source record, its relevant passage and the stated reason for reconsideration. Required; a colleague's summary is a lead rather than a verified replacement claim.
2. **Current interpretation:** Obtain the exact published wording and its approved revision. Required for before-and-after comparison; do not reconstruct it from memory.
3. **Claim scope:** Identify the object, attribute and uncertainty affected, such as attribution, use or date description. Default: only the supplied claim, not a general reassessment of the exhibition.
4. **Publication inventory:** Collect physical labels, digital pages, audio, translations, guides and reusable image captions that may repeat the claim. Default: supplied instances only; disclose unknown derivative coverage.
5. **Editorial decisions:** Identify the role allowed to approve interpretation and the owner of each publication channel. Default: proposed edits awaiting approval.
6. **Display constraints:** Collect space, typography and installation requirements from the actual label system. Default: a textual revision packet rather than a fabricated print-ready file.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Give the claim a local reference and state what the existing label asserts. Separate maker, date, place, function and interpretation when the new evidence affects only one attribute.
2. Record what the new source directly supports and what remains an inference. Do not equate a changed catalog field with proof that every previous interpretation was false.
3. Write the narrow revision decision: retain, qualify, replace or remove the affected assertion. Explain why the supplied evidence supports that disposition and identify any unresolved editorial question.
4. Draft replacement wording that preserves the evidence's degree of certainty. Use observable editorial constraints: one clear subject, explicit uncertainty term where needed, and no unexplained specialist abbreviation.
5. ⚠️ Map the same claim across its actual publication instances. Search candidate wording and object identifiers, but inspect each occurrence before changing it; a quotation of the old interpretation may need contextual annotation rather than replacement.
6. Distinguish authoritative master text from exported derivatives. Updating the master does not establish that a printed label, cached page, recorded narration or borrowed exhibition kit has changed.
7. Build an instance-level change table identifying current revision, proposed wording or action, owner and verification evidence. For translations, retain the proposition and uncertainty change as a translator briefing rather than asserting bilingual correctness without review.
8. Specify how transitional inconsistency will be handled if channels cannot change together. A temporary explanatory note may be proposed, but its wording and installation still require the applicable owner decision.
9. ⚠️ Verify content and placement separately. A corrected proof can still be installed beside the wrong object; a screenshot can show new text while an older downloadable guide remains available.
10. Deliver the editorial decision and rollout packet with a release boundary. Report which sources and copies were inspected, which edits were made if any, and which channels still carry the previous claim.

## Decision rules
- IF new evidence changes only attribution THEN preserve independently supported date or material statements BECAUSE a local correction does not invalidate unrelated claims.
- IF the old wording is a historical quotation THEN propose context rather than silently modernizing it BECAUSE changing the quotation would misrepresent its source.
- IF derivative inventory is incomplete THEN qualify rollout coverage BECAUSE one corrected master cannot prove all public instances changed.
- IF an editorial decision is pending THEN keep proposed wording visibly provisional BECAUSE production readiness is different from interpretive approval.
- IF a channel cannot update with the others THEN identify its interim wording and owner BECAUSE contradictory simultaneous statements can conceal the revision's actual status.

## Output template
```text
Claim: <object, attribute and current assertion; up to three lines>
Evidence decision: <source support, uncertainty and proposed disposition; up to five lines>
Replacement wording: <one short paragraph or an explicit pending decision>
Instance ledger: <up to eight rows; attach remaining inventory>
Instance | Current wording/revision | Proposed action | Owner | Verification state
Transition: <temporary inconsistency and proposed handling; up to four lines>
Release boundary: <approved, changed, verified and still pending states>
```

## Quality checklist
- [ ] The affected claim is narrower than the entire object description.
- [ ] Source support is distinct from editorial inference.
- [ ] Replacement wording retains the supplied uncertainty.
- [ ] Each publication instance has its own revision or unknown-state record.
- [ ] Historical quotations are not silently rewritten.
- [ ] Translation and audio updates have explicit review needs.
- [ ] Content correctness and object placement have separate checks.
- [ ] The release statement does not infer publication from a proposal.

## Anti-patterns
- **Master-only completion:** one text file changes and the whole exhibit is declared corrected. Fix: track the physical and digital instances separately.
- **Certainty upgrade:** a possible attribution becomes a named maker. Fix: preserve the evidence's qualifying language.
- **Global word replacement:** every mention is edited, including quotations. Fix: classify each occurrence before changing it.
- **Unrelated erasure:** a disputed maker causes supported material facts to disappear. Fix: isolate the affected attribute.
- **Invisible transition:** old and new interpretations coexist without explanation. Fix: document the interval and owner-approved interim treatment.

## Worked example
**Input:** Fictional exhibit Reed labels object Jar-P “Made by artist Neri.” Supplied record S now supports only “possibly from Neri's workshop”; its material description remains supported. The same definite attribution appears on wall label W and web page D. Audio script A quotes an earlier curator saying the old attribution. No editorial approval or publication changes have occurred.

**Output:**
```text
Claim: Jar-P maker attribution currently names Neri as certain.
Evidence decision: S supports possible workshop association, not certain individual authorship. Propose qualification; retain the independently supported material description.
Replacement wording: Possibly from Neri's workshop. The object's material description remains as currently supported.
Instance ledger:
Instance | Current wording/revision | Proposed action | Owner | Verification state
W | definite attribution, revision unknown | replace attribution after approval | label editor role proposed | proof and installation pending
D | definite attribution, revision unknown | update claim and inspect public page | web editor role proposed | pending
A | historical curator quotation | retain quote and propose contextual note explaining revised evidence | audio editor role proposed | script decision pending
Transition: Coordinate W and D where feasible; if updates differ, obtain an approved explanatory note. Audio context requires editorial review.
Release boundary: Proposal only; no source beyond supplied S verified, no approval, print, website or audio update performed.
```

**Bad output:** “Neri did not make this; all labels are fixed.”
This overstates the negative conclusion and invents completed publication work.

## Edge cases
- The new record itself is disputed: preserve the dispute and propose qualified wording rather than selecting the more recent source automatically.
- A lender supplied mandatory wording: identify the conflict and route it to the responsible editorial relationship owner; do not invent permission to replace it.
- An image embeds the old caption: include the image asset as a distinct derivative, not only its surrounding page text.
- A removed object remains in a guide: record the guide's context and historical purpose before deciding whether to update or annotate it.

## Test case
**Input:**
> Fictional exhibit Ash changes “definitely ceremonial” to “function uncertain” for Cup-L. A printed leaflet, website and translated audio all repeat the old wording; only the website draft is available.

**Assertions:**
1. Produces qualified wording without inventing a new function.
2. Identifies all three channels while limiting inspection evidence to the supplied draft.
3. Leaves print and translated audio review pending.
4. Does not claim the public website or physical materials changed.
