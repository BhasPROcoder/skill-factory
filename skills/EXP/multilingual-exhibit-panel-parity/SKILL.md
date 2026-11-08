---
id: EXP-002
name: multilingual-exhibit-panel-parity
domain: Exhibition Interpretation Operations
subdomain: Multilingual panels
version: 1.0
description: Plan equivalent interpretive content and reading paths across language versions when exhibit panels face unequal text lengths and space constraints.
triggers: ["fit multilingual exhibit text", "compare language versions of a panel", "preserve meaning while shortening labels", "plan translated panel space", "check multilingual visitor reading paths"]
not_for: ["general translation brief [GLA-001]", "standalone negation and modality review [GLA-003]", "claiming accessibility certification"]
requires: []
risk_level: medium
---

# Multilingual exhibit panel parity

## Purpose
Build a panel comparison that preserves the same essential interpretation across language versions while respecting the actual display space. Treat semantic review, layout review and visitor navigation as separate decisions rather than declaring equivalence because the versions have similar word counts.

## Inputs to collect
1. **Approved propositions:** Obtain the statements, qualifications and visitor actions that every language version must preserve. Required; if the master is unapproved, label all panel copy provisional.
2. **Language drafts:** Request each actual draft and any supplied back-translation or reviewer notes. Default: no claim of translation accuracy for a language that cannot be competently reviewed.
3. **Panel geometry:** Obtain usable text areas, type conventions, line spacing and viewing context from the design owner. Default: layout allocation proposal only, with no fabricated fit result.
4. **Reading sequence:** Identify headings, object references, captions and optional deeper layers. Default: preserve the supplied hierarchy rather than forcing every language into identical line breaks.
5. **Review roles:** Identify bilingual reviewers and the person deciding interpretive priorities. Default: reviewer roles proposed; no implied approval.
6. **Alternate delivery options:** Collect permitted companion cards, audio, expandable displays or adjacent panels. Default: do not assume a digital channel or extra physical surface exists.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Segment the approved interpretation into propositions, marking essential facts, uncertainty, attribution and optional supporting detail. Keep the hierarchy visible so shortening decisions are deliberate.
2. Align each proposition with its actual expression in each draft. A missing qualification and an omitted decorative phrase have different consequences even if both reduce length.
3. Record confidence in the language review. Use supplied bilingual evidence where available and identify unresolved meaning checks instead of pretending to understand an unsupported language.
4. ⚠️ Compare reading paths as well as sentences. A language version whose caveat sits on another panel may give a different default interpretation even when the caveat technically exists somewhere.
5. Map each language's text blocks into the supplied display regions. Record expected overflow and truncation risks as predictions until a real rendering or proof is inspected.
6. Try editorial compression against the proposition list before changing the physical text treatment. Remove redundant wording or move genuinely optional detail only with interpretive approval; do not silently discard uncertainty to fit a box.
7. Propose layout changes that preserve a legible hierarchy under the actual design criteria. Equal nominal font size or equal word count alone does not prove equivalent access; the relevant proof must be inspected.
8. If space remains insufficient, propose an authorized alternate delivery route and state which essential information stays in the default view. Never make one language's core meaning available only through an unavailable device.
9. Review names, quantities, references and directional instructions across versions. These affect how a visitor connects the panel to an object and can remain wrong despite fluent prose.
10. Produce the parity matrix, layout action list and explicit sign-off sequence. Track language approval and rendered-fit approval separately so one cannot stand in for the other.

For current accessibility or venue specifications, use [VERIFY: applicable panel typography, viewing and alternate-format criteria in the venue's approved design requirements]. This procedure does not supply universal text sizes, expansion ratios or reading-speed estimates.

## Decision rules
- IF a shorter version loses a qualifying phrase THEN restore that meaning or obtain an explicit interpretation decision BECAUSE space pressure does not justify increased certainty.
- IF a version fits only after reducing text below supplied design criteria THEN redesign the allocation BECAUSE nominal content presence does not establish usable presentation.
- IF a bilingual review is unavailable THEN leave semantic parity pending BECAUSE layout inspection cannot verify translation.
- IF supporting material moves to another channel THEN preserve its navigation and essential caveats BECAUSE information location changes the visitor's reading path.
- IF language versions use different object references THEN reconcile those references before release BECAUSE a correct sentence beside the wrong object misleads.

## Output template
```text
Panel boundary: <panel, languages and available proof evidence; up to three lines>
Parity matrix: <up to eight proposition rows; attach remainder>
Proposition | Required level | Version coverage | Meaning check | Display action
Reading paths: <one short sequence per language>
Space decisions: <up to five edits or allocation changes with authority needs>
Review gates: <language, interpretation and rendered-fit states>
Delivery limit: <what was actually reviewed and what remains untested>
```

## Quality checklist
- [ ] Essential facts and caveats are identified before shortening.
- [ ] Each language is mapped to the same proposition set.
- [ ] Missing language-review competence is disclosed.
- [ ] Default reading paths retain essential qualifications.
- [ ] Fit conclusions cite a supplied proof or remain proposed.
- [ ] Object references and visitor actions are reconciled.
- [ ] Alternate channels are supported by actual capabilities.
- [ ] Approval states distinguish meaning from layout.

## Anti-patterns
- **Word-count equality:** equal lengths are treated as equivalent meaning. Fix: align propositions rather than counts.
- **Caveat trimming:** uncertainty is removed to save space. Fix: preserve the qualifier and revise less important wording.
- **Language shrinkage:** one version becomes unreadably dense. Fix: reconsider block allocation using supplied design criteria.
- **Hidden core content:** a required interpretation moves to an inaccessible extra channel. Fix: retain essential meaning in the default route.
- **Fluency certification:** a visually polished draft is called accurate. Fix: obtain competent language review and record its scope.

## Worked example
**Input:** Fictional gallery Cedar has one approved interpretation: Vessel-A may have stored seeds; its exact use is uncertain. Language draft North includes both propositions. A supplied bilingual reviewer says draft South states definite seed storage and omits uncertainty. The designer reports South overflows its box, but no proof or typography criteria are provided. A second panel is not available.

**Output:**
```text
Panel boundary: Vessel-A panel, drafts North and South; reviewer note supplied, no inspectable layout proof.
Parity matrix:
Proposition | Required level | Version coverage | Meaning check | Display action
Possible seed storage | essential | North qualified; South definite | South changes certainty per reviewer | revise South to preserve possibility
Exact use uncertain | essential | North present; South absent | South omission established by supplied review | restore caveat before fitting
Reading paths: North: object reference, possible use, uncertainty. South proposed: same interpretive sequence after qualified revision.
Space decisions: Obtain proof and design criteria. Compress redundant wording while retaining both essential propositions. Reallocate existing panel blocks if permitted; no second-panel assumption.
Review gates: South bilingual revision pending; interpretive essentials established; rendered fit untested.
Delivery limit: Reviewer evidence and draft descriptions analyzed only; no translation authored, layout rendered or panel installed.
```

**Bad output:** “Delete ‘uncertain’ from both versions so the labels match.”
This creates shared inaccuracy instead of parity.

## Edge cases
- A language reads in a different direction: obtain its actual layout requirements and verify object arrows and ordering rather than mirroring the panel mechanically.
- A proper name has several accepted forms: retain the selected editorial convention and make the object link unambiguous; do not invent a preferred spelling.
- One version includes extra community context: assess whether it changes the core interpretation and whether equivalent context should be offered elsewhere, without erasing it automatically.
- Audio is the only permitted overflow route: state what is available without audio and keep essential interpretation visible according to the approved access design.

## Test case
**Input:**
> Fictional panel Birch has two language drafts. The shorter draft retains facts but moves a necessary uncertainty note into a QR-linked page. The venue has not confirmed network access.

**Assertions:**
1. Flags the changed default reading path.
2. Keeps essential uncertainty on the panel or leaves redesign pending.
3. Does not assume the linked page is accessible in the venue.
4. Separates bilingual review from proof-fit verification.
