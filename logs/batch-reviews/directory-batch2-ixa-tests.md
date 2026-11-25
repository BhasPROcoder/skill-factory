# Batch 2: interface adaptation executions

Reviewer: recover_cli, separate from the interface author. Inputs: six coordinator prompts from plans/directory-batch2-requests.md; no answer key. These are the actual design outputs from applying the two procedures. Names inside sample exchanges are placeholders to be filled from the user's actual answers. No calendar, order, speech recognizer or interface was operated.

## IXA-001: lesson transfer
Task boundary: Preserve the direction and result of the marker transfer without requiring motion.
Preference contract: The learner requests reduced motion for this lesson. No product-wide precedence or persistence policy was supplied.
Alternative map:
Transition | Motion function | Nonmoving representation | Preserved state
Before transfer | Establish origin | Static labeled region A: marker present | Current lesson step
Transfer | Communicate direction | Labeled before/after stills, A to B, with text “marker transferred from A to B” on confirmed transfer | Selected exercise and current answer
Interrupted transfer | Motion can otherwise imply completion | Display last confirmed step or “transfer pending” | Actual transfer state
Walkthrough: Open with preference active → stills available; initiate transfer → indicate pending if not yet confirmed; confirmation arrives → show destination and direction; preference changes mid-transition → switch to the matching still without replay; transfer fails → show failure and prior confirmed location.
Verification: Proposed: compare learner identification of source, destination and sequence; retain focus on the active control and verify one transfer only.
Open dependencies: What region labels and result evidence exist? How are preferences resolved and retained? Is examining the exact path a learning objective requiring optional step-through?
Delivery status: Specification; no live lesson or learner outcome verified.

## IXA-001: missing motion inventory
Task boundary: Plan an inventory before authorizing removal that could hide state or destroy instructional content.
Preference contract: No known precedence, override or persistence behavior. Ask the product owner; no universal platform behavior assumed.
Alternative map:
Transition | Motion function | Nonmoving representation | Preserved state
Unidentified transition | Unknown pending inventory | Record start, end, user action and meaning; defer removal | Existing task
Confirmed decoration, if found | Emphasis only | Omit decoration | Content/action unchanged
Confirmed status animation, if found | Feedback | Persistent text for actual status | Task ID, selection and focus
Walkthrough: Inventory screen → identify transition owner; remove frames in draft → identify lost information; preference changes mid-action → preserve state; result unavailable → show pending or unknown, never success.
Verification: Proposed: exercise each identified transition with preference set before and during interaction. Inspect focus, reading position, duplicate submissions and semantic loss.
Open dependencies: Which screens, transitions and journeys are in scope? Which movements communicate status, location or instructional content? What preference inputs and precedence apply?
Delivery status: Inventory method and conditional examples only; no actual animation identified or removed.

## IXA-001: stationary loading indicator
Task boundary: Keep work status intelligible after disabling motion.
Preference contract: Reduced motion changes presentation, not the operation. No timeout or failure policy supplied.
Alternative map:
Transition | Motion function | Nonmoving representation | Preserved state
Request started | Activity | “Request pending” text; identifier if available | Existing request
No further evidence | Spinner implies activity | Retain last known status; show verification uncertainty if status channel unavailable | Original request identity
Confirmed result | Completion feedback | Explicit success or failure based on returned result | Focus and result
Walkthrough: Submit once → pending label; switch presentation → preserve label without restarting; receive no updates → cannot distinguish active backend from unavailable status; confirmed failure → failure message; confirmed success → result message. Offer a status check only if supported; no automatic repeated submission.
Verification: Proposed: simulate pending, disconnected and completed states; check visible state and count submissions.
Open dependencies: Which source confirms the eventual result? What status check or cancel action exists? How does the product distinguish known failure from missing status?
Delivery status: Specification, no application or timed behavior test.

## IXA-002: calendar ambiguity
Action boundary: Prepare a possible meeting move; no calendar edit authorized or performed in the fixture.
Dialogue record: action=move, candidate; target=two possible meetings, unresolved; date=Friday without exact date, unresolved; timezone and resulting time=unresolved.
Turn contract:
Event | Spoken response | Draft update | Commit permission
Ambiguous reference | “Which of the two meetings do you mean?” | Set target only from answer | None
Ambiguous date | “What date and time zone should I use, and should the meeting keep its start time?” | Collect explicit timing | None
Correction | “I'll update the draft and read it back.” | Invalidate earlier readback | None
Complete draft | “Move [meeting] to [date and time, zone]?” | Bind reply to this draft | Only within granted action authority
Example exchange: User: “Move it to Friday.” Assistant: “Which meeting do you mean?” User: “[Identifies a meeting].” Assistant: “Which Friday date, time and time zone should I use?” User: “[Supplies timing].” Assistant: “Draft: move [meeting] to [timing]. No change has been made.”
Recovery limit: On silence leave draft uncommitted; offer a supported alternate channel if identification fails.
Verification: Text review only; no calendar or speech execution.
Open dependencies: Which meeting, exact date and intended local time/zone apply? Is a draft or authorized change requested?

## IXA-002: unclear item name
Action boundary: Recover an order draft's item field without selecting an invented product or submitting an order.
Dialogue record: item=unclear speech, not confirmed; catalog match=unavailable; other order details=retain only if supplied.
Turn contract:
Event | Spoken response | Draft update | Commit permission
Unclear name | “I didn't get the item name. Can you repeat or spell it?” | Keep item unresolved | None
Clear repeat | “I heard [name]. Is that what you said?” | Candidate string only | None
Name confirmed | “I have the name; I can't verify it against the catalog yet.” | Separate confirmed words from catalog match | None
Silence/rejection | “I'll leave the item unselected.” | Preserve other draft fields | None
Example exchange: User: “[Unclear item].” Assistant: “Could you spell the item name?” User: “[Spells name].” Assistant: “I heard [name]. Is that right?” User: “Yes.” Assistant: “Name recorded in the draft; item availability and identity are not verified.”
Recovery limit: Offer text entry or staff review only if supported; otherwise explain the unresolved field and stop the order attempt.
Verification: No catalog lookup, recognition confidence calculation, audio test or purchase.
Open dependencies: What source can confirm item identity? Which fallback input channel exists? What confirmations are required before ordering?

## IXA-002: correction during pending submission
Action boundary: Record corrected intent while reconciling the earlier pending request; no cancellation, revision or second submission assumed.
Dialogue record: original destination=previously confirmed for original request; original result=pending; corrected destination=new candidate; revised submission permission=none.
Turn contract:
Event | Spoken response | Draft update | Commit permission
Correction heard | “I heard a destination change. The earlier request still shows pending.” | Retain original request and new candidate separately | None
User verifies correction | “I'll keep the corrected destination in the draft while the first request is checked.” | Confirm field, not an action | None
Status unavailable | “I can't confirm whether the earlier request completed.” | Original remains unresolved | None
Authoritative result arrives | “Here is the original request's confirmed status: [status].” | Choose supported amend/cancel/new path from actual result | Fresh readback required
Example exchange: User: “Change the destination to [new place].” Assistant: “The original request is pending. I heard [new place]; is that the correction?” User: “Yes.” Assistant: “Correction noted in the draft. I can't confirm a change or cancellation while the original result is unknown.”
Recovery limit: Do not retry the submission or promise recall; check an authorized status source or hand off the unresolved request.
Verification: Text state transitions reviewed; no request, cancellation, speech interaction, or destination change executed.
Open dependencies: Can original status be queried? Are pending amendments or cancellations supported? What confirmation and authority are needed for any subsequent action?

Review: Each request produced its promised alternative-state or spoken-turn contract. Missing product semantics stayed unresolved and corrections did not retroactively authorize external actions. No blocking issue found in these six cases. Not a usability, accessibility-compliance, or cross-runtime audit.
