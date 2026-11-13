# Independent PRT behavioral review

Reviewer: finish_rnt, not the PRT author. Read all six actual instructions, then executed the following fresh ordinary, missing-input and edge requests as text tasks. All names, jobs and numbers below are fictional fixtures. Outputs below are the actual reviewer-produced artifacts, not expected-output sketches. No production files, color proofs, machinery, external recipients or separate model were used. Structural checks and this text review do not establish production acceptance.

## PRT-001: quantity bridge

### Ordinary
Request: Fir edition revision R needs 12 finished copies. Supplied plan requires one cover C and two identical insert I parts per copy. Plan has 12 C and 23 I. No allowances. Supplied content mapping is complete; nothing printed.

```text
Job boundary: Fir R; 12-copy production proposal.
Content basis: One C and two I per finished copy; supplied complete content mapping.
Quantity bridge:
Edition/part | Per-copy requirement | Copies | Base parts | Separate allowance | Planned/observed | Difference
Fir/C | 1 | 12 | 12 | none | 12 planned | 0
Fir/I | 2 | 12 | 24 | none | 23 planned | 1 short
Content exceptions: None established from supplied mapping; actual files unavailable.
Questions: Will supplier revise I to 24 or supply an authorized changed requirement?
Disposition: Blocked pending insert quantity confirmation.
Verification: 12*1=12; 12*2=24; 24-23=1. No physical production inspected.
```
Assessment: PASS. Multiplicity retained; shortage cannot be hidden in grand total; proposed state not inflated to finished copies.

### Missing input
Request: Willow has a file of 18 pages and asks how many sheets to order for 40 books. No supplier layout, cover treatment or finished-content definition is given.

```text
Job boundary: Willow; 40 requested finished books; revision unidentified.
Content basis: File reported as 18 pages; finished pagination, covers and section definitions missing.
Quantity bridge:
Edition/part | Per-copy requirement | Copies | Base parts | Separate allowance | Planned/observed | Difference
Willow/unresolved parts | unknown | 40 | unresolved | none supplied | no plan | unresolved
Content exceptions: Cannot equate file pages with approved logical content or sheets.
Questions: What finished content, covers and blanks are intended? What supplier plan defines sections, sheets and parts per copy? Which exact file revision and approval owner apply?
Disposition: Blocked for content and supplier plan; no sheet-order quantity derived.
Verification: No press imposition, file inspection or physical output checked.
```
Assessment: PASS. Three consolidated questions; no universal booklet or sheet conversion supplied.

### Edge
Request: Hazel editions East and West need 7 and 5 copies. Each requires one shared approved insert S and its own cover E or W. Plan has 12 S, 6 E and 6 W, no allowances. Mapping complete, proposal only.

```text
Job boundary: Hazel East/West; proposed parts for 7 East and 5 West copies.
Content basis: S explicitly shared; covers E and W edition-specific.
Quantity bridge:
Edition/part | Per-copy requirement | Copies | Base parts | Separate allowance | Planned/observed | Difference
East/E | 1 | 7 | 7 | none | 6 planned | 1 short
West/W | 1 | 5 | 5 | none | 6 planned | 1 above base
East+West/S | 1 | 12 | 12 | none | 12 planned | 0
Content exceptions: None in supplied mapping; W cannot satisfy E.
Questions: Will supplier correct edition-specific cover allocation and explain the extra W?
Disposition: Blocked for cover reconciliation.
Verification: 7+5=12 shared inserts; 7-6=1 E short; 6-5=1 W above base. No production observed.
```
Assessment: PASS. Approved shared part aggregates correctly; edition mismatch survives equal grand cover count.

## PRT-002: proof changes

### Ordinary
Request: Alder proof V1 says “Open Hall”; authorized editor correction C1 requests “Main Hall” on the front. V2 supplied front view says Main Hall with unchanged visible placement. No other view or release approval supplied.

```text
Proof pair: Alder V1 front and V2 front, supplied views.
Correction ledger:
ID/location | Requested change | Replacement evidence | Disposition | Next owner/check
C1/front heading | Open Hall to Main Hall | V2 says Main Hall, visible placement unchanged | implemented in supplied view | editor reviews V2; full-file scope remains open
Unrequested differences: None established in supplied front views.
Approval map: Editor authorized C1; no V2 acceptance or production-release evidence supplied.
Release boundary: Ready for editor's bounded V2 review, not production release.
Verification: Front wording and visible placement compared; other pages, color and physical output uninspected.
```
Assessment: PASS. Implementation distinguished from approval, uninspected areas retained.

### Missing input
Request: Cedar has two files both named final.pdf, and someone said “approved.” It asks which should go to print. Files and identifiers not supplied.

```text
Proof pair: Two same-named files; identities and revision order unresolved.
Correction ledger:
ID/location | Requested change | Replacement evidence | Disposition | Next owner/check
Unresolved scope | no comment set supplied | no inspectable proof | not inspectable | job owner supplies identities and evidence
Unrequested differences: Not assessable without proofs.
Approval map: “Approved” has no supplied revision, category or authorized role.
Release boundary: Blocked; cannot select a production revision.
Verification: No file compared. Please provide distinct file/revision identities and proof views; the comment/change set; and the approval's author, exact revision, scope and release conditions.
```
Assessment: PASS. No filename-derived chronology or invented approval inheritance; asks three grouped inputs.

### Edge
Request: Maple comment C7 requires “North” changed to “South” in both title and map key. Replacement R3 fixes title only. An authorized content owner explicitly accepts leaving the map key North in R3. No production release. Both relevant views supplied.

```text
Proof pair: Supplied Maple baseline and R3 title/map-key views.
Correction ledger:
ID/location | Requested change | Replacement evidence | Disposition | Next owner/check
C7/title | North to South | R3 title says South | implemented | preserve R3 evidence
C7/map key | North to South | R3 map key remains North | original correction superseded by explicit owner acceptance of deviation | retain acceptance tied to R3
Unrequested differences: None established in supplied views.
Approval map: Content owner accepts R3 map-key deviation; production release not supplied.
Release boundary: Ready for next required job review; no production release conclusion.
Verification: Two supplied locations compared; whole file and physical proof uninspected.
```
Assessment: PASS. Known deviation retained rather than falsely labeled corrected; acceptance kept revision-specific.

## PRT-003: separation evidence

### Ordinary
Request: Birch export B requires emblem E on Spot-A and cutting reference K on supplier role Cut. Isolated views show E on Spot-A and K on Cut, no other inspected marks. Composite contains both. No physical proof.

```text
Review boundary: Birch B; supplied isolated views and composite for E/K.
Ink intent: E uses Spot-A; K uses supplier-defined Cut.
Separation ledger:
Object/region | Intended role | Observed channels | Evidence | Finding
E/emblem | Spot-A | Spot-A | supplied isolated view | consistent
K/reference | Cut | Cut | supplied isolated view | consistent with intentional special role
Proposed corrections: None established for E/K; retain evidence for supplier review.
Questions: None needed for these bounded findings.
Disposition: Ready for supplier's next specified review of these objects.
Verification limits: Other objects/channels and physical printed appearance uninspected; no production approval.
```
Assessment: PASS. Extra functional channel respected; bounded pass avoids whole-file inference.

### Missing input
Request: Cypress composite looks blue. User asks whether it will print as the intended spot ink. No exact export identity, role instruction or separation views.

```text
Review boundary: Unidentified composite preview only.
Ink intent: Intended spot role identifier and job instruction unavailable.
Separation ledger:
Object/region | Intended role | Observed channels | Evidence | Finding
Blue-looking region | unspecified spot intent | unavailable | composite only | assignment unverified
Proposed corrections: None supported before evidence review.
Questions: Which exact export is under review? What named ink roles and supplier instructions apply? Please provide the relevant isolated channel views and object labels.
Disposition: Blocked for ink-assignment evidence.
Verification limits: Composite appearance only; no channels, physical ink or output examined.
```
Assessment: PASS. No guessed color-library values, export setting or spot classification.

### Edge
Request: Rowan export R includes Warm and Warm-copy, both orange-looking. Job owner says Warm is logo ink, Warm-copy is separately required security-pattern ink. Isolated views confirm the logo and pattern in their respective channels. Do not assess security efficacy.

```text
Review boundary: Rowan R; supplied logo/pattern isolated views and role instruction.
Ink intent: Warm for logo; Warm-copy separately required for pattern.
Separation ledger:
Object/region | Intended role | Observed channels | Evidence | Finding
Logo | Warm | Warm | isolated logo view | consistent
Pattern | Warm-copy | Warm-copy | isolated pattern view | separate intended role supported
Proposed corrections: Do not consolidate on name/appearance alone; no assignment correction established.
Questions: None for the bounded role correspondence.
Disposition: Ready for designated supplier review of the evidenced assignments.
Verification limits: No physical print, security efficacy or other objects evaluated.
```
Assessment: PASS. Similar names do not force merging; avoids expanding into security certification.

## PRT-004: page boundaries

### Ordinary
Request: Fictional Elm job requires 80 by 120 mm trim, edge artwork 2 mm beyond trim and title 4 mm inside trim. Dimensioned revision E has correct declared boundaries and background extent, but title is 3 mm inside top trim.

```text
Job frame: Elm E; 80 by 120 mm, portrait, dimensioned evidence.
Boundary basis: Supplied job requires background 2 mm outward and title 4 mm inward from trim.
Exception ledger:
Page/object | Relevant boundary | Evidence/distance | Required relationship | Disposition
Front/background | trim outward | 2 mm | 2 mm | supplied extent matches
Front/title | top trim inward | 3 mm | at least 4 mm | 1 mm short
Corrections: Designer moves title to satisfy the supplied inset, then rechecks nearby content and revised dimensions.
Questions: Supply revised title evidence after correction.
Next gate: Blocked for revised-artwork comparison.
Verification limits: Supplied dimensions and boundary agreement checked; no physical cutting or print inspected.
```
Assessment: PASS. Uses only fixture limits; arithmetic 4-3=1; matching metadata does not override title failure.

### Missing input
Request: Ash sends an unscaled screenshot of a square card and asks “is the bleed enough?” No supplier requirements or artwork boundary dimensions.

```text
Job frame: Ash screenshot; physical dimensions, revision and scale unknown.
Boundary basis: Supplier bleed requirement and finished boundary unavailable.
Exception ledger:
Page/object | Relevant boundary | Evidence/distance | Required relationship | Disposition
Shown edge/background | unidentified trim/bleed | unscaled visual only | unknown | insufficient measurement basis
Corrections: No numerical extension or box change prescribed.
Questions: What finished dimensions and exact revision apply? What job-specific bleed and finishing requirements does the supplier specify? Can you provide dimensioned boundary and background-extent evidence?
Next gate: Blocked for requirements and measurable evidence.
Verification limits: Screenshot viewed conceptually from supplied description; no physical distance measurement established.
```
Assessment: PASS. No universal bleed value or screenshot ruler invented.

### Edge
Request: Oak shaped card has an approved curved cut outline. Supplier says text must remain 6 mm inside that outline. Supplied dimensioned artwork places label L 7 mm from the page rectangle but 4 mm from the actual curve. Background geometry is outside review.

```text
Job frame: Oak shaped card, supplied dimensioned artwork; label L review only.
Boundary basis: Approved curved cut outline; supplier text inset 6 mm from that outline.
Exception ledger:
Page/object | Relevant boundary | Evidence/distance | Required relationship | Disposition
Label L | approved curve inward | 4 mm; page rectangle distance 7 mm is not governing | at least 6 mm | 2 mm short
Corrections: Move L relative to the curved protected region and recheck its neighbors in revised evidence.
Questions: Supply corrected dimensioned placement against the approved curve.
Next gate: Blocked for label-placement review.
Verification limits: Supplied distances only; background and physical finish uninspected.
```
Assessment: PASS. Correct reference geometry selected; 6-4=2; no rectangular shortcut.

## PRT-005: variable correspondence

### Ordinary
Request: Fir data D1 keys X/Y maps membership field to badge block in T1: Gold produces “Gold member”; blank omits block. Samples show X Gold member and Y no block. Manifest lists X/Y once, as required. No other fields reviewed.

```text
Revision set: Fir D1, T1, supplied membership rule, X/Y samples and manifest.
Mapping ledger:
Template location | Source/rule | Missing-value behavior | Status
Badge block | membership: Gold -> Gold member | omit block | supplied cases conform
Observed cases: X populated Gold branch shows Gold member; Y blank branch omits block; both pass supplied rule.
Coverage: Manifest contains X and Y once each, matching the stated scope and multiplicity.
Corrections: None established for this block and coverage scope.
Questions: None for supplied cases.
Verification limits: Two badge samples and manifest checked; other fields, other branch values and physical print uninspected.
```
Assessment: PASS. Content and manifest coverage separately supported; no extrapolation to other branches.

### Missing input
Request: Willow data row J has a blank preferred_name. A preview shows “Hello friend.” User asks if that is correct; no mapping or fallback rules supplied.

```text
Revision set: Willow row J and preview; template/data revision identifiers and rules missing.
Mapping ledger:
Template location | Source/rule | Missing-value behavior | Status
Greeting | presumed relation to preferred_name unverified | no approved fallback supplied | unresolved
Observed cases: J has blank preferred_name; preview says Hello friend; conformance cannot be judged without the rule.
Coverage: One preview only; no intended population or manifest supplied.
Corrections: Do not approve or replace fallback until mapping owner supplies the intended behavior.
Questions: Which data/template revisions and exact mapping apply? What is the approved blank-name behavior? What record scope and manifest establish coverage?
Verification limits: One supplied value/preview relation only; no full-run or printing check.
```
Assessment: PASS. Does not invent a friendly fallback as correct; no legal eligibility discussion introduced.

### Edge
Request: Cedar keys P/Q both display the name Lane. Each should produce two named pieces, invitation and pass. Manifest P/invitation, P/pass, Q/invitation, Q/invitation. Visible names all Lane; templates map names correctly in samples.

```text
Revision set: Cedar supplied P/Q data, invitation/pass templates, stated multiplicity rule and manifest; visible-name samples.
Mapping ledger:
Template location | Source/rule | Missing-value behavior | Status
Name block | supplied display-name field | not exercised | observed Lane samples match supplied values
Observed cases: Matching display names do not identify recipient keys or piece roles; only name rendering is evidenced.
Coverage: P has invitation and pass. Q has duplicate invitation and missing pass; four total entries do not establish correct two-piece coverage.
Corrections: Enumeration owner repairs Q/pass generation and removes unintended duplicate according to the actual process, then supplies a corrected key-plus-piece manifest and samples.
Questions: Supply replacement evidence for Q's two intended pieces.
Verification limits: Supplied manifest and name samples only; no physical run inspected.
```
Assessment: PASS. Expected multiplicity handled with key-plus-piece identity; equal totals and names do not conceal missing role.

## PRT-006: assembly handoff

### Ordinary
Request: Birch brochure approved intent uses cover C1 around text T1, and loose map M1 after T1's named panel End, map title toward reader on opening. Sample S has all three identified components and opening views show those relationships. Owner has not accepted S. Supplier process unspecified.

```text
Finished intent: Birch brochure with C1/T1/M1, supplied approved relationships.
Part map:
Part/revision | Edition compatibility | Named surfaces/edges | Required relationship
C1 | supplied Birch edition | identified front | encloses T1/M1
T1 | supplied Birch edition | panel End | precedes M1
M1 | supplied Birch edition | title face | after End, title toward opening reader
Supplier questions: None on observed relationships; supplier process remains its responsibility.
Sample checks: Confirm identities C1/T1/M1; open S; verify M1 after End and title facing reader.
Evidence and exceptions: Supplied S opening views support the stated relationships; no owner acceptance supplied.
Handoff state: Ready for owner's sample acceptance review.
Change boundary: Revised C/T/M requires comparison of affected enclosing, placement or facing relationships.
```
Assessment: PASS. Correct sample observations do not invent acceptance or machine operations.

### Missing input
Request: Maple says “fold the sheet, then put the card on the other side.” No named surfaces, final intent or sample. It asks for a finishing handoff.

```text
Finished intent: Maple sheet/card assembly; final orientation unresolved.
Part map:
Part/revision | Edition compatibility | Named surfaces/edges | Required relationship
Sheet/unknown | unknown | unlabeled | fold and final faces unspecified
Card/unknown | unknown | unlabeled | other side ambiguous
Supplier questions: What is the approved final opening/reading arrangement? Which part revisions and named surfaces/edges apply? Can you supply a labeled mockup or representative views and the required sample acceptance owner?
Sample checks: After intent is supplied, verify card placement and facing by opening the assembly; no arbitrary orientation chosen.
Evidence and exceptions: No sample or unambiguous relationships supplied.
Handoff state: Blocked pending product-intent evidence.
Change boundary: Establish revisions and relationships before a sample baseline can be accepted.
```
Assessment: PASS. Three grouped questions; no manufacturing sequence inferred from ambiguous hand motions.

### Edge
Request: Ash accepted sample S1 uses shared text T1 and North insert N1. Now text T2 shifts named panel End after an added note. Approved intent still puts N1 after End. New closed sample S2 has correct cover but no opening view. South edition also uses T2 and its own insert S1.

```text
Finished intent: Ash North and South with shared T2; edition inserts after named End.
Part map:
Part/revision | Edition compatibility | Named surfaces/edges | Required relationship
T2 | North/South by supplied intent | relocated End | precedes each edition's own insert
N1 | North | supplied insert identity | after T2 End
S1 insert | South | supplied insert identity | after T2 End
Supplier questions: Supply opening views or representative assemblies showing each insert after T2 End in its edition.
Sample checks: Identify T2; locate new End; confirm North/N1 and South/S1 pairing and placement; inspect interior rather than cover only.
Evidence and exceptions: Prior sample S1 approval applies to T1 assembly; closed S2 cover cannot establish T2 interior relationships.
Handoff state: Blocked for affected relationship comparison and designated sample review.
Change boundary: Shared T2 change reopens insert-placement checks in both editions; preserve old sample history.
```
Assessment: PASS. Shared-part revision propagates to both editions without claiming all unrelated properties failed.

## Review conclusion and claim audit

All 18 fresh text executions yielded usable bounded outputs. No behavioral blocker found. The six scopes differ: logical content/part multiplicity; correction-to-revision disposition; object-to-ink correspondence; geometric reference boundaries; record/branch/piece identity; and finished-product spatial relationships. Adjacent shipment, document-authoring and palette workflows do not supply these specific decision procedures. This is semantic comparison, not a mathematical guarantee of global uniqueness.

Specific factual assertions in the skills were reviewed: printing quantities use supplied part definitions; bleed/inset/section/ink requirements are inputs or VERIFY steps; no universal production rate, margin, page grouping, software API or current standard is hardcoded. Stable distinctions between a composite view and channel evidence, a boundary and actual artwork, and a sample and full-run coverage are used as reasoning constraints. All worked-example numbers are fictional and internally consistent. Review arithmetic was separately recomputed in Python before completion. No citations or sources were fabricated; no external fact search was required for these supplied-evidence procedures.
