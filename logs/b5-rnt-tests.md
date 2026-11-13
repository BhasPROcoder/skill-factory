# RNT independent forward tests

Evaluator: finish_exp, separate from RNT author finish_rnt. Read all six supplied skills and applied them to the fresh fictional requests below. Each fenced block is the evaluator's actual text output, not an intended answer supplied by the author. These are desk exercises; no rental systems, equipment, customer contact, qualified inspections or other models were exercised. Missing-required-input cases intentionally stop at the prescribed questions.

Specific-claim review: no changing rates, technical thresholds, law or equipment specifications supplied by the evaluator. All named businesses, assets and scenarios are fictional. Counter arithmetic was recomputed with Python before saving: 61.75-60.25=1.5; 7-2=5; sum=6.5; 18-12=6; 9-4=5; sum=11. Accessory shortage 3-2=1 was also checked. Operational evidence is hypothetical input, not observed real-world fact.

## RNT-001 — ordinary

Request: Fictional company Bramble has simultaneous reservations D for exact display unit U2 and E for any blue unit. U1 and U2 are distinct, ready, blue units at the depot. D is provisionally U1; E is provisionally U2. No handover occurred. Only propose a correction.

```text
Boundary: Bramble supplied snapshot, D and E in the same handover window; proposal only.
Unit identity: U1 and U2 are distinct ready blue units at the depot.
Assignment ledger:
Reservation | Promise | Current unit/status | Eligible alternatives | Conflict
D | exact U2 | U1, provisional | U2 only | current assignment violates promise
E | any blue unit | U2, provisional | U1 or U2 | occupies D's only eligible unit
Proposed mapping: D->U2 and E->U1 together; each distinct unit used once.
Dependencies: Allocation owner confirms current status and authorizes the paired correction before handover.
Disposition: Feasible on supplied evidence as a proposed mapping; present mapping remains incorrect.
Execution note: No allocation changed, unit handed over or customer notified.
```

Observed checks: preserved the exact-unit promise; tested the paired mapping; did not treat a proposal as execution. No blocker.

## RNT-001 — missing required input

Request: Fictional company Bramble says “We have enough blue stands; assign one to every booking,” but supplies no unit register or reservation list.

```text
Please provide, in one reply:
1. The reservations, quantities and whether any promises name exact units.
2. The physical-unit register showing unique identities, class membership and any aliases.
3. Current assignments, readiness/location evidence and relevant handover window.
Without those records I cannot distinguish distinct available units from duplicate labels or test a supported assignment.
```

Observed checks: three focused questions; no invented inventory, eligibility or mapping. No blocker.

## RNT-001 — edge

Request: Fictional company Heath has class-level reservations J and K in one window. Ready asset Q has two labels, old Q0 and new Q1, explicitly mapped to the same object. J claims Q0 and K claims Q1. Another unit V is only expected back before handover; no return or readiness observation exists.

```text
Boundary: Heath J/K allocation snapshot; same handover window.
Unit identity: Q0 and Q1 are aliases of one physical unit Q. V is a distinct expected return, not an observed ready unit.
Assignment ledger:
Reservation | Promise | Current unit/status | Eligible alternatives | Conflict
J | class-level unit | Q0, provisional | Q supported; V conditional | competing physical Q claim
K | class-level unit | Q1, provisional | Q supported; V conditional | competing physical Q claim
Proposed mapping: No complete supported mapping; Q can satisfy only one simultaneous handover. Allocation owner must resolve priority and the remaining gap.
Dependencies: Confirm V's actual return, readiness and reservation eligibility before adding it as an available candidate.
Disposition: Blocked on current evidence; an expected return does not close the gap.
Execution note: No assignment changed or handover confirmed.
```

Observed checks: one object despite aliases; return dependency preserved; no arbitrary cancellation. No blocker.

## RNT-002 — ordinary

Request: Fictional company Sedge's approved kit K for stand S requires three type A clips and one cover. The staged kit contains two A clips, one unrelated display card and one cover. The supplied list establishes compatibility. No acknowledgment or waiver exists.

```text
Kit boundary: Sedge reservation K, stand S, supplied approved kit list.
Accessory ledger:
Requirement | Required quantity/unit | Observed item/quantity | Compatibility basis | Handover state | Gap
A clips | 3 pieces | 2 A clips | supplied S list | staged only | 1 A clip
Cover | 1 piece | 1 cover | supplied S list | staged only | none in count/type
Extras: 1 display card; not a clip substitute.
Remedies: Checkout owner retrieves and records the missing A clip or obtains a documented authorized exception; recipient receipt remains a later event.
Disposition: Incomplete; one promised clip is missing.
Receipt boundary: No recipient acknowledgment or waiver supplied.
```

Observed checks: shortage calculated by item type; unrelated extra not credited; staging distinguished from receipt. No blocker.

## RNT-002 — missing required input

Request: Fictional company Sedge asks whether a photographed bag beside a stand is a complete hire kit. Neither reservation kit definition nor content inventory is supplied.

```text
Please provide the reservation's approved accessory list and the selected stand's identity, plus an itemized observation of the bag contents. If a proposed substitute is present, include its compatibility basis or approval. A bag's presence alone cannot establish completeness against an unknown kit definition.
```

Observed checks: required list requested without a universal kit assumption; no completeness or safety claim. No blocker.

## RNT-002 — edge

Request: Fictional company Hazelwood prepared base U with two type P feet and acknowledged them in staging. Before checkout U was replaced by V, whose supplied approved list requires two type R feet. The original P feet are still in the bag. No substitution permission exists.

```text
Kit boundary: Hazelwood current unit V; supplied V list supersedes the prepared U association for this checkout.
Accessory ledger:
Requirement | Required quantity/unit | Observed item/quantity | Compatibility basis | Handover state | Gap
R feet | 2 pieces | 0 R feet | supplied V list requires R | not presented | 2 R feet
Extras: 2 P feet prepared for U; not supported as V substitutes.
Remedies: Checkout owner obtains the required R feet or verified authorized substitution, then refreshes the V kit observation.
Disposition: Incomplete for V; the earlier U staging acknowledgment does not establish the replacement kit.
Receipt boundary: Staging acknowledgment is not recipient receipt; no V handover evidenced.
```

Observed checks: reopened after main-unit swap; incompatible prior evidence not reused. No blocker.

## RNT-003 — ordinary

Request: Fictional company Briar supplies checkout image A and return image B for uniquely identified panel T. Both show the same labeled front corner at comparable scale and lighting. A shows an unmarked corner; B shows a visible short dark line there. Observation times establish checkout before return; custody between them is unknown.

```text
Comparison scope: Briar panel T, supplied checkout A and return B; visible front corner only.
Source register: A—checkout observation, T identity supplied. B—later return observation, same T identity. Exact clock times not supplied.
Findings:
Region | Checkout evidence | Return evidence | Comparability | Observation classification
Labeled front corner | A shows no visible line | B shows short dark line | comparable supplied views | visible difference between observations
Unresolved history: Intervening custody and cause of the visible difference are unknown.
Follow-up: Responsible condition reviewer assesses the physical observation if needed; preserve A/B originals and any annotated copies separately.
Conclusion boundary: A visible line differs between supplied comparable views. No conclusion about depth, cause, liability, repair, fee or safe use.
```

Observed checks: reported an evidenced difference without overstating its mechanism. No blocker.

## RNT-003 — missing required input

Request: Fictional company Briar sends unlabeled before and after photographs of visually similar cases and asks which scratches appeared during the rental. No asset or rental identity is supplied.

```text
Please provide the rental's unit identifier and the evidence connecting each photograph to that same unit. Also identify which image is the checkout observation and which is the return observation, using observation times rather than upload order. Until identity is established, these remain unmatched observations and cannot support a same-asset change conclusion.
```

Observed checks: stopped at identity gap; no similarity-based comparison. No blocker.

## RNT-003 — edge

Request: Fictional company Moor has unit M. Checkout note N says “rear mark present.” Checkout photo P shows only the front. Return photo R clearly shows a rear mark. P was uploaded after R, though P's observation record establishes checkout before return. The requester calls the rear mark new because it is absent from P.

```text
Comparison scope: Moor unit M; supplied N/P checkout and R return records.
Source register: N—checkout note, M identity supplied; P—checkout front view uploaded later; R—return rear view, M identity supplied.
Findings:
Region | Checkout evidence | Return evidence | Comparability | Observation classification
Rear | N records a mark; P does not show region | R shows rear mark | note supports prior presence but no matching image details | rear mark documented at both stages; sameness of detailed appearance unresolved
Unresolved history: No complete intervening record; later upload of P does not alter its checkout observation time.
Follow-up: Records owner seeks any original checkout rear view if detailed change comparison is required; retain N alongside the images.
Conclusion boundary: Newness is not established. P's missing region does not negate N, and no cause or charge conclusion follows.
```

Observed checks: reconciled note/photo scope, did not confuse upload order with observation order. No blocker.

## RNT-004 — ordinary

Request: Fictional company Woodrush has unit A, counter M measured in hours. It reads 60.25 at checkout and 61.75 before documented replacement. New counter N reads 2.0 on installation and 7.0 at return. The event record establishes no unmeasured operating span between counters. No billing requested.

```text
Scope: Woodrush A; M then N; supplied checkout-to-return measurement chain in hours.
Reading ledger:
Source | Observation time | Counter | Reading/unit | Continuity event or uncertainty
Checkout | checkout | M | 60.25 hours | start
Replacement | before replacement | M | 61.75 hours | segment end
Installation | installation | N | 2.0 hours | new baseline
Return | return | N | 7.0 hours | segment end
Calculations: M: 61.75 - 60.25 = 1.5 hours. N: 7.0 - 2.0 = 5.0 hours. Sum: 1.5 + 5.0 = 6.5 hours.
Result: Complete supported total across the supplied measurement chain: 6.5 hours.
Gaps: No unmeasured operating span in the supplied event record; exact clock times not supplied.
Attribution boundary: No responsibility allocation or fee calculation.
Next check: Records owner confirms the applicable counter/event references before downstream use.
```

Observed checks: no cross-counter subtraction; nonzero replacement baseline respected; arithmetic independently recomputed. No blocker.

## RNT-004 — missing required input

Request: Fictional company Woodrush provides numbers 40 and 44 with no asset, counter, units or observation times and requests exact rental usage.

```text
Please identify the rented asset and counter, the measurement units, and which dated observations produced 40 and 44. Include any reset, replacement or swap between them. I cannot report the arithmetic difference as rental usage until the readings belong to the same supported measurement interval.
```

Observed checks: no invented measurement meaning or usage total. No blocker.

## RNT-004 — edge

Request: Fictional company Rush records one hour counter from 12 to 18 before removal, then another from 4 to 9 after installation. The machine operated during an unmetered interval between them. The requester asks for the entire hire usage and suggests treating the gap as zero.

```text
Scope: Rush unit and replacement counters as supplied; documented segments plus unmetered intervening operation, in hours.
Reading ledger:
Source | Observation time | Counter | Reading/unit | Continuity event or uncertainty
Old start | before removal | old | 12 hours | supported segment start
Old end | removal | old | 18 hours | supported segment end
Gap record | between counters | none | unknown | unmetered operation
New start | installation | new | 4 hours | supported segment start
New end | return | new | 9 hours | supported segment end
Calculations: Old: 18 - 12 = 6 hours. New: 9 - 4 = 5 hours. Supported subtotal: 6 + 5 = 11 hours.
Result: Subtotal of documented segments: 11 hours; full hire usage unresolved.
Gaps: Unmetered operating span cannot be assumed zero and prevents a complete total.
Attribution boundary: No allocation or charge; subtotal is not all rental usage.
Next check: Records owner seeks independent evidence for the missing span; absent evidence, retain the unknown interval.
```

Observed checks: subtotal not promoted to complete; unsupported zero rejected. No blocker.

## RNT-005 — ordinary

Request: Fictional company Fen has unit F due at the depot Friday 14:00 in the same supplied local-time basis. Signed receiving record R places F at the depot Friday 13:20. R was entered Saturday and the overdue flag persists. No customer contact was authorized.

```text
Scope and due basis: Fen F, Saturday snapshot; agreed Friday 14:00 depot receipt in the supplied local-time basis.
Timeline:
Event time | Posting time | Unit | Event and source | Evidence state
Friday 13:20 | Saturday | F | signed receiving record R | depot receipt evidenced
Custody conclusion: F received at depot before the due event; return processing remains open.
Classification: Administrative posting gap, not evidenced customer nonreturn.
Next action: Depot operations reconciles R with the open transaction and sets a review checkpoint; authorized correction remains pending.
Draft inquiry: Internal draft only: Please reconcile F's open return transaction with signed receiving record R and confirm the resulting state. No renter inquiry needed on supplied evidence.
Execution note: Analysis and draft only; no contact sent or record changed.
```

Observed checks: event/posting times separated; internal evidence holder selected. No blocker.

## RNT-005 — missing required input

Request: Fictional company Fen says “Morgan has overdue equipment; send a warning,” but supplies no rental reference, asset identity or due agreement.

```text
Please provide the rental and unit identifiers, the applicable due agreement including approved changes, and the last checkout/collection/receipt evidence. A person's name and a dashboard flag do not establish which unit remains out or which return event is due. I have not sent a warning; a targeted draft can follow the reconciliation.
```

Observed checks: no identity or due-time fabrication; no unsupported accusation or tool sending. No blocker.

## RNT-005 — edge

Request: Fictional company Marsh rents units A and B. The agreement requires carrier pickup by Monday noon, local time. The pickup receipt identifies only A at Monday 11:30. B appears on a scheduled pickup list, but the renter says the driver also took B. Depot receipt is not yet recorded for either unit.

```text
Scope and due basis: Marsh A/B; supplied agreement requires carrier pickup by Monday noon, local time.
Timeline:
Event time | Posting time | Unit | Event and source | Evidence state
Monday 11:30 | not supplied | A | signed pickup receipt | collection evidenced
scheduled Monday | not supplied | B | pickup list | plan only
time unconfirmed | not supplied | B | renter reports collection | statement, transfer not confirmed
Custody conclusion: A collection supported; depot receipt unknown. B custody unresolved between prior rental possession and reported collection.
Classification: A's required pickup event is evidenced before due time. B has an unresolved custody transfer, not established nonreturn.
Next action: Pickup operator supplies the actual B transfer record; internal rental owner sets the review checkpoint and preserves separate unit statuses.
Draft inquiry: Please check whether the driver collected unit B with A. The receipt identifies A only, while the renter reports both were collected. Please provide B's collection acknowledgment or clarify the recorded transfer.
Execution note: Draft only; no message sent or return state changed.
```

Observed checks: applied supplied pickup definition; split assets instead of closing whole rental; targeted disputed transfer evidence. No blocker.

## RNT-006 — ordinary

Request: Fictional company Reedbed provides unit Z's current return-cycle procedure P: clean, check configuration and obtain manager release. Cleaning and configuration results are accepted for Z; manager release R explicitly covers this cycle and intended display use. The stock flag is still unavailable. No system mutation requested.

```text
Readiness boundary: Reedbed Z, current return cycle, procedure P, supplied display use.
Task grid:
Task | Applicability/dependency | Evidence/result | Acceptance state | Remaining action
Cleaning | required | current-cycle accepted record | accepted | none supplied
Configuration check | required | current-cycle accepted result | accepted | none supplied
Manager release | after task acceptance | R covers cycle and intended use | release evidenced | none in release record
Holds: None supplied; unavailable stock flag requires administrative reconciliation, not an invented technical hold.
Remaining package: Operations confirms the flag's basis and performs any authorized update using R; no update is assumed.
Recommendation: Released on supplied evidence for the stated display use.
Handoff: Operations receives P/task records/R; do not generalize to another configuration or use.
Execution state: Release record supplied; review performed; availability update not performed.
```

Observed checks: bounded affirmative conclusion where release actually supplied; stock state distinct. No blocker.

## RNT-006 — missing required input

Request: Fictional company Reedbed says unit Z has returned and asks for a release decision. No applicable turnaround procedure or authority is provided.

```text
Please provide the applicable turnaround requirement revision for Z and the intended next use, the task results and open holds for this return cycle, and the role/evidence required to authorize release. Physical return establishes possession, not completion of an unknown procedure; I cannot invent the checks or release authority.
```

Observed checks: no generic technical procedure invented; no returned-equals-ready conclusion. No blocker.

## RNT-006 — edge

Request: Fictional company Cattail's procedure says a bracket change invalidates the earlier alignment check. Z passed alignment, then its bracket was changed. A batch task record says “all work done,” but no post-change alignment result exists. The stock screen says available and a previous rental's release is attached.

```text
Readiness boundary: Cattail Z, current return cycle, supplied bracket-change rule; intended use otherwise unspecified.
Task grid:
Task | Applicability/dependency | Evidence/result | Acceptance state | Remaining action
Bracket change | supplied work | completed after alignment | execution reported | link batch evidence to Z/current cycle
Alignment check | required after bracket change | only earlier pass | invalidated under supplied rule | obtain required post-change result and acceptance
Release | current-cycle acceptance required | previous rental's release only | not current-cycle evidence | authorized current release review
Holds: Readiness remains unresolved despite available flag; no current closure evidence supplied.
Remaining package: Responsible checker supplies Z's post-change result; process owner verifies the unit/cycle link; release owner records the applicable decision.
Recommendation: Blocked; generic batch completion and historical release do not establish the final configuration's acceptance.
Handoff: Operations must reconcile the availability claim before using Z for fulfillment.
Execution state: Review only; no inspection, release or stock update performed.
```

Observed checks: final-configuration dependency enforced; old-cycle release rejected; no physical check claimed. No blocker.

## Scope and uniqueness assessment

Catalog routing checks used sf.py show for SVC-001, WHS-002, BID-002, CTG-002, SVC-003 and SHP-001. RNT-001's core is physical-unit identity and constrained serial matching, not interval occupancy. RNT-002 accounts for a promised accessory kit and compatibility after base-unit swaps, not package aggregation or warehouse picking. RNT-003 produces comparable region observations without liability findings. RNT-004 segments counter continuity, independently of charges. RNT-005 reconstructs custody rather than appointment attendance. RNT-006 links turnaround cycle, invalidating work, acceptance and release authority, independently of reservation assignment.

All eighteen fresh text exercises produced the required decisions without an author repair request. This is evidence of the tested paths and the evaluator's substantive comparison, not universal behavioral proof, live operational validation, professional certification or a registry audited-status claim.
