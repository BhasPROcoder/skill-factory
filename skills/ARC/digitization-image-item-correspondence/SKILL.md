---
id: ARC-003
name: digitization-image-item-correspondence
domain: Collection Description Operations
subdomain: Capture correspondence
version: 1.0
description: Reconcile digitization captures with their physical items, leaves and sides when missing views, retakes or derivative files could distort coverage.
triggers: ["map scans to original pages", "check digitization coverage", "identify retakes in an image batch", "missing front or back scan", "link image derivatives to physical items"]
not_for: ["3D scan restoration [SDR-002]", "designing collection hierarchy [ARC-002]", "judging image resolution against an unspecified standard"]
requires: []
risk_level: medium
---

# Digitization image and item correspondence

## Purpose
Build a capture-to-source map that explains which physical units and views are represented by each image. Distinguish original captures, retakes and derivatives so a large file count cannot hide missing pages or create a false claim of complete digitization.

## Inputs to collect
1. **Source inventory:** Obtain item identifiers and the expected leaves, surfaces or views for each item. Required; without it, report the supplied images but withhold completeness.
2. **Capture manifest:** Request filenames or file identifiers, recorded source references, sequence and capture notes. Required; a folder's order alone is not a source identity.
3. **View policy:** Collect which sides, blanks, covers or inserts should be captured. Default: unknown; do not infer that blank surfaces may be skipped.
4. **Retake evidence:** Identify superseded captures and the reasons for replacements. Default: retain both candidates as unresolved instead of choosing by filename or modification date.
5. **Derivative lineage:** Obtain links from master captures to display, thumbnail or edited versions. Default: mark lineage absent and do not count derivatives as additional source coverage.
6. **Inspection capability:** Establish whether actual images and originals can be inspected. Default: manifest-only reconciliation; proposed visual checks remain unperformed.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Define a source-view key from supplied identifiers, such as item plus leaf plus side. Preserve qualifiers that distinguish foldouts, loose inserts or multiple photographs of one surface.
2. Build the expected-view list from the supplied capture policy. If the policy is ambiguous, record competing interpretations rather than inventing an expected total.
3. Map every file to its claimed source-view key and role. Label unassigned files explicitly; do not silently discard them as clutter or assign them to the nearest sequence number.
4. ⚠️ Collapse derivatives under their parent capture for coverage counting. A master, preview and thumbnail can all represent one view, not three photographed pages.
5. Compare expected keys with mapped capture keys. Separate no mapped capture, several candidates, known excluded view and mapped but uninspected view.
6. Inspect available images for visible identity clues such as page labels, headings or matching edges. Keep uncertain correspondence explicit when image appearance cannot distinguish repeated blank surfaces.
7. Trace retake decisions to supplied evidence. Select a preferred capture only when an authorized decision or explicit quality criterion supports it; retain the replaced capture's identity and replacement relationship.
8. ⚠️ Review sequence without using it as sole identity proof. A missing file, rescanned insert or sorting change can shift every subsequent filename while the physical order remains unchanged.
9. Check that assembled viewing sequences use the selected captures in the intended order. Record covers, backs and inserts separately where the policy requires them, instead of flattening them into guessed page numbers.
10. Produce a correspondence ledger and focused exception list. State whether source identity, expected coverage, visual quality and assembled sequence have each been checked; passing one does not establish the others.

Check current repository digitization policy and any requested technical specification in its authoritative documentation before stating compliance. This skill does not prescribe resolution, color targets, compression or preservation formats. Those requirements belong in the supplied verification criteria.

## Decision rules
- IF several files derive from one capture THEN count one source view BECAUSE file multiplicity does not increase coverage.
- IF two captures claim the same view THEN retain both until the retake relationship is resolved BECAUSE newest file time is not proof of preferred quality.
- IF an expected back side lacks a capture THEN mark the coverage gap even if it may be blank BECAUSE exclusion requires the supplied policy.
- IF image identity contradicts the manifest THEN flag both records for reconciliation BECAUSE neither filename nor appearance should silently overwrite the other.
- IF the source inventory is incomplete THEN qualify the coverage conclusion BECAUSE complete coverage of a partial list is not complete coverage of the collection.

## Output template
```text
Scope: <items, view policy and inspection boundary; up to four lines>
Expected coverage: <source-view keys or attached list>
Correspondence: <up to ten representative rows; attach full ledger when larger>
Source-view key | Capture | Role and lineage | Selection | Evidence state
Exceptions: <missing, duplicate, unassigned or contradictory entries>
Sequence checks: <ordered selection and unresolved placement; up to five lines>
Disposition: <coverage conclusion, quality limits and next evidence check>
```

## Quality checklist
- [ ] Expected coverage is based on supplied source inventory and view policy.
- [ ] Every file has a source-view key or an explicit unassigned state.
- [ ] Derivatives do not inflate covered-view totals.
- [ ] Retake selection preserves replaced capture identifiers.
- [ ] Missing views and uncertain identities are separate findings.
- [ ] Filename order is not the sole source-order evidence.
- [ ] Manifest review and visual inspection are reported separately.
- [ ] Coverage does not imply image-quality or standards compliance.

## Anti-patterns
- **File-count completion:** many files imply all pages are captured. Fix: compare unique source-view keys.
- **Newest wins:** a recent file replaces a capture automatically. Fix: require an evidenced selection decision.
- **Blank erasure:** blank backs are omitted without policy. Fix: record the expected view and approved exclusion separately.
- **Sequence cascade:** a filename gap shifts all later page assignments. Fix: verify item identity and inserts before renumbering.
- **Derivative confusion:** thumbnails become independent captures. Fix: preserve their parent lineage and role.

## Worked example
**Input:** Fictional archive Alder requires both sides of leaves L1 and L2 from item Book-P. Its manifest has capture C1 for L1/front, preview D1 derived from C1, C2 for L1/back, C3 and retake C4 for L2/front. The operator's recorded decision selects C4 and marks C3 replaced. No L2/back capture is listed. No images can be opened in this exercise.

**Output:**
```text
Scope: Book-P, L1 and L2, front and back required; manifest-only review.
Expected coverage: L1/front; L1/back; L2/front; L2/back.
Correspondence:
Source-view key | Capture | Role and lineage | Selection | Evidence state
L1/front | C1 | Capture; D1 preview derives from it | C1 | Manifest mapped, visually uninspected
L1/back | C2 | Capture | C2 | Manifest mapped, visually uninspected
L2/front | C3 | Replaced capture | Not selected | Operator decision links replacement C4
L2/front | C4 | Retake | C4 | Operator-selected, visually uninspected
L2/back | None | Expected view | Missing | No mapped capture
Exceptions: L2/back missing. D1 is a derivative, not an additional covered view.
Sequence checks: Proposed selected order C1, C2, C4, unresolved L2/back; actual display assembly untested.
Disposition: Three of four required views are mapped to selected captures. Five listed files do not establish four-view coverage. Image quality remains uninspected; obtain or capture the missing view under authority.
```

**Bad output:** “Five files for four sides means the book is fully digitized.”
This counts a derivative and a replaced capture as new source coverage.

## Edge cases
- A foldout needs several views: use the supplied view policy and link the views to one source unit instead of creating invented leaves.
- A capture contains several physical pages: record the covered regions and whether each meets the supplied policy; one file need not mean one view.
- Original pagination is wrong or repeated: preserve printed labels alongside local disambiguating keys, without silently correcting the source.
- A file is unreadable: retain its manifest relationship but mark usable coverage unconfirmed until an authorized replacement is available.

## Test case
**Input:**
> Fictional collection Birch requires front and back for card K. A master and two previews all show K/front. No back is listed. The operator asks whether three files satisfy two required views.

**Assertions:**
1. Counts only one represented source view.
2. Identifies K/back as a coverage gap.
3. Preserves preview-to-master lineage.
4. Does not claim visual or technical quality verification.
