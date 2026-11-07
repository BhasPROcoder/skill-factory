---
id: ARC-002
name: archival-description-hierarchy-design
domain: Collection Description Operations
subdomain: Description hierarchy
version: 1.0
description: Design a collection description hierarchy that preserves provenance and parent scope when organizing supplied groups, folders and items.
triggers: ["organize a collection finding aid", "design archive description levels", "keep collection provenance visible", "map folders into a collection hierarchy", "separate physical boxes from intellectual groups"]
not_for: ["reconciling received material [ARC-001]", "generic dataset provenance mapping [TDS-002]", "claiming compliance with an archival standard"]
requires: []
risk_level: low
---

# Archival description hierarchy design

## Purpose
Create a proposed description tree that explains how supplied collection material relates without inventing creators or rearranging physical objects. Separate intellectual grouping from storage location so moving a folder between boxes does not silently change its provenance or descriptive parent.

## Inputs to collect
1. **Collection boundary:** Obtain the material included and excluded from the proposed description. Required; do not absorb adjacent material because names or subjects resemble each other.
2. **Provenance evidence:** Collect known creators, activities, custody notes and original labels. Default: preserve uncertainty and label inferred relationships as proposals.
3. **Existing order:** Request current sequences, groupings and explanations of prior arrangement. Default: record supplied order without asserting it is original.
4. **Description needs:** Identify intended users and what relationships they need to navigate. Default: explain parent-child relationships and distinguish storage references.
5. **Repository conventions:** Obtain the local level vocabulary, identifier rules and descriptive policy. Default: use explicitly provisional labels rather than claim a standard has been followed.
6. **Physical locations:** Collect container references separately from descriptive groups. Default: unknown locations remain unknown.
7. **Editing authority:** Establish whether a proposed hierarchy or an actual catalog update is requested. Default: proposal only; do not rearrange holdings or overwrite records.

If required inputs lack safe defaults, ask in one message with at most three questions.

## Procedure
1. Inventory the supplied descriptive units and preserve their existing identifiers. Mark a group that has only a supplied title differently from an inspected item with observed content.
2. Separate evidence of common provenance from similarity of subject. Two creators can discuss the same topic without their papers forming a single originating body of records.
3. Describe the collection-level scope in terms of what is actually included. Name limits such as incomplete date coverage or unidentified contributors instead of filling gaps with plausible history.
4. Propose intermediate groups only where they explain evidenced activity, source organization or a supplied arrangement decision. Avoid creating empty levels merely to make every branch equally deep.
5. Assign each descriptive unit one primary parent in the proposed tree. Use explicit related-material links for additional associations rather than duplicating the item as though two physical originals exist.
6. ⚠️ Verify that a child's description stays within its parent's stated scope. If a folder contradicts the proposed group definition, revise the group, relocate the proposal or retain a flagged unresolved placement.
7. Keep storage location in a separate field. A box can hold parts of several intellectual groups, and one group can span boxes; describe that relationship without treating the container as the creator.
8. State which descriptive facts are shared at a parent level and which are specific to a child. Never silently inherit a date, creator or access condition where the evidence says the child differs.
9. Review titles for unsupported claims. Use supplied labels with explanation when necessary; distinguish a historical title from a new descriptive title created for navigation.
10. ⚠️ Check references and identifiers after every proposed merge or move. A changed parent must not orphan a child, introduce a cycle or make an earlier citation point to a different unit.
11. Produce the hierarchy and a decision log explaining uncertain placements. Preserve the prior arrangement as a reference and identify the curator or description owner whose approval is needed before changes.

Check current repository rules or any explicitly requested descriptive standard in its authoritative documentation before claiming compliance. The task can produce a useful provisional tree even when that verification remains pending, provided it is labeled accordingly.

## Decision rules
- IF two units share a topic but have different evidenced creators THEN retain their provenance distinction BECAUSE subject similarity does not prove common origin.
- IF one item relates to several groups THEN choose an evidenced primary parent and add related links BECAUSE duplicate tree entries can imply duplicate holdings.
- IF a parent fact does not apply to every child THEN state the exception at the appropriate child BECAUSE unqualified inheritance hides differences.
- IF physical boxes span intellectual groups THEN keep both mappings BECAUSE storage and description serve different functions.
- IF the source of an existing order is unknown THEN call it current order BECAUSE labeling it original would invent history.

## Output template
```text
Scope: <collection boundary and evidence limits; up to three lines>
Proposed tree: <indented identifiers and titles; attach continuation if over twelve units>
Unit details:
ID | Parent | Scope or provenance | Storage | Uncertainty
Related links: <cross-references with relationship, or none supplied>
Decision log: <up to six placement decisions with evidence>
Verification: <reference checks performed or pending; up to four lines>
Approval boundary: <proposed versus applied and responsible role>
```

## Quality checklist
- [ ] Collection scope does not absorb unsupplied material.
- [ ] Provenance and topic grouping are distinguished.
- [ ] Each unit has a stable identifier and one primary parent.
- [ ] Storage references are separate from descriptive ancestry.
- [ ] Parent statements do not silently override child exceptions.
- [ ] Cross-references do not imply duplicate physical items.
- [ ] Current order is not mislabeled original without evidence.
- [ ] Proposed changes remain separate from applied catalog edits.

## Anti-patterns
- **Topic takeover:** all records about a topic are merged despite distinct creators. Fix: preserve origin and add related links.
- **Box genealogy:** physical containers become descriptive ancestors without reason. Fix: maintain a separate location mapping.
- **Symmetry padding:** every branch gets identical empty levels. Fix: introduce levels only for meaningful evidenced grouping.
- **Inherited certainty:** one parent's date or creator is applied to every child. Fix: retain specific evidence and exceptions.
- **Citation drift:** a reused identifier now means a different item. Fix: preserve identity and record superseded relationships.

## Worked example
**Input:** Fictional archive Fern holds writer Ivo's correspondence group L, containing folders L-A and L-B. L-A contains incoming letters; L-B contains outgoing copies. The supplied arrangement groups both under Ivo correspondence. Both folders are in box Cedar. An unrelated folder N, also in Cedar, contains illustrator Nera's notes. No evidence links Nera's papers to Ivo's creation of correspondence. All identifiers are supplied. No catalog editing is authorized.

**Output:**
```text
Scope: Describe supplied L, L-A, L-B and N; shared storage does not establish shared provenance.
Proposed tree:
Collection proposal
  L — Ivo correspondence
    L-A — Incoming letters
    L-B — Outgoing copies
  N — Nera notes, separate provenance branch
Unit details:
ID | Parent | Scope or provenance | Storage | Uncertainty
L | Collection proposal | Ivo correspondence, supplied arrangement | Cedar partly | Collection boundary needs owner confirmation
L-A | L | Incoming letters | Cedar | Dates not supplied
L-B | L | Outgoing copies | Cedar | Dates not supplied
N | Collection proposal | Nera notes | Cedar | Whether a separate collection record is required
Related links: None evidenced between N and L; common storage recorded separately.
Decision log: Preserve L's supplied grouping. Keep N's provenance distinct. Do not make Cedar a descriptive creator or parent.
Verification: Identifiers are distinct and each listed child has one parent; repository-level conventions remain pending.
Approval boundary: Proposal only. Description owner confirms collection boundary before catalog changes.
```

**Bad output:** “Cedar is the Ivo collection; put Nera under his outgoing correspondence.”
The output turns a storage container into provenance and invents an unsupported relationship.

## Edge cases
- An item has several creators: describe the supplied roles and use a primary placement justified by arrangement evidence; do not erase joint creation.
- A former catalog grouped material differently: retain old identifiers and a mapping to the proposed arrangement so earlier citations remain interpretable.
- A description spans material not yet inspected: state its source and limit; do not call it verified item-level description.
- A digital object has several representations: keep identity separate from file versions and link representations to the descriptive unit.

## Test case
**Input:**
> Fictional archive Ash stores two unrelated creators' diaries in one box. A request asks for one creator-based group because there is only one box. Prepare a hierarchy proposal.

**Assertions:**
1. Preserves the two creator identities.
2. Uses the box as storage information rather than proof of one provenance group.
3. Keeps unknown dates and repository conventions unresolved.
4. Does not claim that catalog records or holdings were rearranged.
