# Independent warehouse batch review

Reviewer: event skill author, not warehouse skill author. Each case below is a fresh fictional request and actual desk response using the skill; no warehouse, ledger or order was modified.

## WHS-001: reconcile a bin after receipt

Request: Fictional shop Plum reports 18 saleable cups in owned bin A at opening. Receipt R transferred 6 more cups into A before the cutoff and was absent from opening. Count C found 23 at close. No other movements are evidenced. Explain the variance.

Scope: Owned saleable cups, each, bin A only, close cutoff.
Sources: Opening ledger 18 each; R +6 each into A; count C 23 each.
Bridge: Opening 18 + receipt 6 = expected 24. No other adjustments supported.
Result: Counted 23 minus expected 24 = -1 cup.
Evidence assessment: Receipt explains the movement from opening expectation, but does not establish why one fewer cup was counted. No theft or breakage inference.
Next check: Independent bin recount against the same cutoff and confirmation that all six receipts physically entered A.
Disposition: Unresolved one-unit variance; no posting authorized.

## WHS-001: incompatible observation units

Request: Fictional Wren reports four sealed cartons and an opened carton. Ledger says 39 items. No packing labels, loose count or stock-condition definition is supplied. Is anything missing?

Scope: Wren stock; physical location, stock key, unit basis and cutoff still require alignment.
Sources: Count of four sealed cartons and one opened carton; ledger quantity 39 labeled items.
Bridge: Cannot convert a carton count into item units from the supplied evidence. Movements and cutoff not established.
Result: Not comparable; no signed item variance.
Evidence assessment: Neither five cartons nor four full cartons plus an assumed partial quantity supports a numerical conclusion.
Next check: What item/location/condition and cutoff does each record cover? What verified pack count applies to each sealed carton? How many qualifying items are loose in the opened carton?
Disposition: Not comparable pending evidence. No stock adjustment proposed.

## WHS-001: reverse movements from a later ledger

Request: Fictional bin T was counted at noon: 11 owned blue caps. The 14:00 ledger for the same boundary shows 14. Between noon and 14:00 receipt R brought 5 and transfer X removed 2; both are included in 14:00. A second notification is a duplicate of R. No other movements occurred.

Scope: Owned blue caps in T, each, noon.
Sources: Noon count 11; later ledger 14; receipt R +5; duplicate notification of R; transfer X -2.
Bridge: Reverse the later movements: 14 - 5 + 2 = 11 at noon. Exclude duplicate R notification.
Result: Counted 11 minus expected 11 = 0.
Evidence assessment: Supplied movements fully bridge this comparison; agreement applies to this bin and cutoff only.
Next check: Record R/X identifiers and the duplicate link for reviewer traceability.
Disposition: Matched within supplied scope, with no posting needed.

## WHS-002: eligible alternate bin with partial coverage

Request: Fictional order D needs 9 identical cases. Four distinct cases were picked, none shipped. Bin Y has three eligible unreserved matching cases. Original task is closed short. No substitutions or partial shipping allowed.

Line: D; matching cases; active commitment 9; all must ship together.
Coverage: 4 picked awaiting release, 0 shipped; open pick 9 - 4 = 5.
Candidate checks: Y has 3 confirmed eligible matching cases, unpicked; no other verified supply.
Options: Pending authorized recovery of 3 from Y would leave 5 - 3 = 2 open. Hold the line for the rest; alternatively await complete replenishment. Neither option ships anything now.
Decision: Recheck Y before assignment; have authorized owner decide whether to reserve or pick the 3 while remaining 2 are sourced.
Closeout evidence: Validated physical pick, correct task closure, and full line coverage before separately authorized release.
Current status: 5 open; 4 picked and not shipped. Proposed recovery remains unexecuted.

## WHS-002: uncertain cumulative coverage

Request: Fictional order L requires 12 pens. A dashboard reports 7 picked and 4 shipped. Nobody knows whether shipped units are included in the 7, and a neighboring bin has unspecified reservations.

Line: L; pens each; 12 active. Shipping policy unknown.
Coverage: If 7 includes the 4 shipped, coverage 7 (4 shipped, 3 picked unshipped), open 5. If disjoint, coverage 11 (4 shipped, 7 picked unshipped), open 1. No single exact open quantity established.
Candidate checks: Neighboring bin; matching identity, physical stock, eligible quantity and reservations unresolved; no confirmed recovery.
Options: Reconcile pick and shipment identifiers before any new task; no defensible unconditional pick quantity.
Decision: Obtain the event history, open-task state and bin eligibility; ask the authorized owner for applicable release restrictions.
Closeout evidence: Nonoverlapping coverage by item and line plus a documented allocation check and physical pick evidence.
Current status: 4 shipped and 7 reported picked; overlap unresolved. No new pick or shipment claimed.

## WHS-002: duplicate active attempt and ineligible variant

Request: Fictional order V needs 6 plain red tags; 2 already shipped, 1 additional plain red tag picked and awaiting release. An open task for 3 is still active. Nearby are 3 striped red tags. The customer has not authorized substitutes.

Line: V; 6 plain red tags; no authorized substitution.
Coverage: 2 shipped + 1 distinct picked but unshipped = 3 covered; open pick 3. Open task does not count as picked.
Candidate checks: Existing task for 3 is unresolved; striped red tags differ from requested variant and are excluded from currently eligible coverage.
Options: Obtain current task status; if it confirms 3 distinct exact matches physically picked, open would become 0. Otherwise hold unresolved units or seek separate consent without modifying demand.
Decision: Do not dispatch a duplicate task, substitute stock, or cancel the existing task on an assumption.
Closeout evidence: Task event identifiers, item identity, confirmed pick results, nonoverlapping coverage, and separate authorization for release or changed order terms.
Current status: 3 open and one existing recovery attempt pending. No substitution or shipment has been executed.

Review outcome: Both skills produce different decisions from the same family of inventory evidence. WHS-001 establishes a comparison balance at a cutoff; WHS-002 resolves an order commitment without treating availability or assignment as a completed pick. Six text cases produced usable bounded artifacts; no blocking finding. This does not validate a warehouse integration, inventory accuracy on site, or live fulfillment behavior.
