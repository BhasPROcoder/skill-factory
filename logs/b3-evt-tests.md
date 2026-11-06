# Event operations: independent text executions

Reviewer: procurement skill author, separate from the EVT author. Requests below were invented for this review. All people, shows and assets are fictional. The calls below are draft scripts, not instructions issued to an actual crew.

## EVT-001: ordinary handoff

Request: For the Moss awards program, caller Ari can hear host Teo say “Let's see the finalists”; operator Paz then advances to slide Final-A on the room screen. Teo waits to read names until Ari sees Final-A and calls the reading. All three use a shared channel. Draft the handoff in relative time.

Session: Moss awards, review draft A; relative time. Caller Ari.
Cue sheet:
ID | Target | Standby and acknowledgment | Release trigger and call | Action owner and action | Completion witness
A | End of introduction | Ari: Standby Final-A; Paz confirms asset ready | Ari hears the agreed line and receives Paz's ready; Ari: Final-A go | Paz advances | Ari sees Final-A on audience screen
B | After A witness | Ari requests Teo's readiness to read; acknowledgment required | With Final-A visible and Teo ready, Ari: Read go | Teo begins reading | Ari hears first name
Hold rules: If the line or readiness is missing, hold A. If screen output is not witnessed, hold B; do not infer successful projection from Paz's keystroke.
Timing: Relative sequence; no hard finish supplied.
Verification: Desk walkthrough of supplied dependencies only. Crew channel and screen not tested.
Open checks: Who owns any program-change decision if the slide fails?

Finding: The produced cues distinguish resource readiness from audience-side completion and avoid inventing a clock time.

## EVT-001: missing release information

Request: “At our gala there is a toast followed by music. Make a caller sheet.” No caller, track, acknowledgment channel or cue line is specified.

Session: Gala toast-to-music transition; working draft pending assignment, relative time.
Cue sheet:
ID | Target | Standby and acknowledgment | Release trigger and call | Action owner and action | Completion witness
M | After toast | Proposed caller requests standby for approved track; proposed operator acknowledges exact asset when known | Release blocked until an observable handoff and channel are agreed | Proposed playback operator starts only on confirmed go | Proposed observer confirms intended music at audience destination
Hold rules: No confirmed asset, operator or release trigger: hold. Do not infer the toast is over because a guest pauses.
Timing: No fixed clock or authorized cut supplied.
Verification: Proposed sheet only; no show operated or tested.
Open checks: Who calls, plays and witnesses the cue, and on what channel? Which track/revision and destination are approved? What observable signal releases playback and who may change the sequence?

Finding: The output supports planning despite missing prerequisites and does not fabricate a toast line or approved operator.

## EVT-001: concurrent duties

Request: At the Birch showcase, operator Kai must manually unmute a remote guest and manually play a sting at exactly the same producer signal; the team says Kai cannot perform the actions simultaneously. Producer Iza alone can change ordering. Draft the exception.

Session: Birch remote introduction; draft, relative signal-based timing. Caller not assigned.
Cue sheet:
ID | Target | Standby and acknowledgment | Release trigger and call | Action owner and action | Completion witness
G | Producer signal | Proposed caller requests guest-feed/ready acknowledgment from Kai | Blocked pending Iza's staffing or ordering decision | Kai to unmute guest only on resolved call | Remote guest audible at program destination
S | Same signal | Proposed caller requests sting readiness from Kai | Blocked pending same decision | Kai to play approved sting only on resolved call | Sting audible at intended destination
Hold rules: Shared release does not solve incompatible manual duties. Escalate to Iza for another operator or approved sequence; do not silently choose one action first.
Timing: Simultaneity is a supplied constraint, not a verified capability.
Verification: Desk conflict identified; neither audio path was exercised.
Open checks: Who will call and monitor output? What assignment or sequence does Iza approve? How will guest speech remain discernible if both outputs run together?

Finding: The procedure exposes the conflict rather than promising an impossible pair of actions.

## EVT-002: approved spoken alternate

Request: At Cedar's rehearsal, the room projection screen is declared blank before the clip starts. The host has an approved spoken summary of the clip's sole essential message. Caller Uma may switch once tech Ren confirms playback stopped. The host's final phrase “Back to the panel” is the approved rejoin marker. Desk exercise only.

Cue under test: Intro clip at the room projection screen; essential message can be delivered by the approved host summary.
Dependency check: Primary needs projected clip; spoken summary bypasses projection but requires audible host speech. Audience-side audio and primary isolation must be verified in a rehearsal setup.
Recovery script:
Condition | Caller decision | Operator or presenter action | Evidence before proceeding
Blank screen reported | Uma holds clip-dependent cues | Ren checks actual destination and isolates primary | Ren confirms primary stopped; do not infer silence from blank picture
Isolation confirmed | Uma calls approved spoken summary | Host speaks approved text | Observer confirms audience heard essential message
Summary delivered | Uma waits for rejoin marker | Host says agreed end phrase | Phrase heard and following panel ready
Rejoin: On “Back to the panel,” retire any stale clip-end trigger; release panel only after the approved marker and readiness.
Test record: Tabletop branch walked; blank screen was a scenario premise. No actual isolation, microphone or room reception observed.
Disposition: Untested live path. Rehearse isolation and host audibility before relying on the fallback.

Finding: A plausible fallback is distinguished from tested capability, and a delayed primary cannot silently release the next segment.

## EVT-002: no authorized alternate

Request: “The keynote animation might fail. Can we just skip it?” No content owner, permission, essential message, equipment or rejoin point supplied.

Cue under test: Keynote animation, revision and destination unknown; required audience outcome unresolved.
Dependency check: No confirmed primary path or authorized replacement. Omission is proposed only.
Recovery script:
Condition | Caller decision | Operator or presenter action | Evidence before proceeding
Audience result unavailable | Hold dependent releases | Assigned operator when known inspects destination | Confirm actual failure symptom
Alternate requested | Do not skip or substitute without a decision | Ask program owner for essential message and acceptable replacement | Document authority and content
Rejoin proposed | Hold until marker and content disposition established | Identify any stale automatic end signal | Confirm following cue and release authority
Rejoin: Not supplied; no timed return inferred.
Test record: Desk assessment only; no media or rehearsal system supplied.
Disposition: Blocked. What must reach which audience? Who can approve omission or alternate delivery? Which marker and roles release the next cue?

Finding: Missing content authority leads to a bounded hold rather than an invented skip policy.

## EVT-002: split audience, stale primary

Request: At the Reed stream, a clip's picture freezes in the room while stream listeners still hear its audio. An alternate file is on the same player; nobody has confirmed primary isolation. The next segment starts automatically on the original clip-end signal. Draft the fault branch.

Cue under test: Clip feeding room and stream; audience outcomes differ and essential content remains unspecified.
Dependency check: Both files share the player. Frozen room picture does not establish player failure or cessation of stream audio. A file switch could repeat content or overlap active output.
Recovery script:
Condition | Caller decision | Operator or presenter action | Evidence before proceeding
Room picture frozen, stream audio active | Hold alternate and following release | Seek authority to inhibit automatic next cue; check room and stream separately | Actual auto-trigger state and each output witnessed
Original isolation unknown | No switch | Assigned operator tests isolation in approved rehearsal only | Independent confirmation primary cannot return on either feed
Same-player alternate proposed | Do not assume recovery | Determine failure location, alternate dependency, authorized content and remaining message per audience | Viable route and bounded rejoin approved
Rejoin: Do not act on delayed original end signal. Identify a manual rejoin marker with producer and confirm which audience still needs which content.
Test record: Tabletop review of supplied symptoms; no physical inhibition, signal routing or replay tested.
Disposition: Blocked pending isolation authority, stale-trigger control, content decision and destination-specific evidence.

Finding: The script does not equate two files with independent playback or assume the room and stream need identical material replayed.

No blocking issue found in these six text tasks. Routing boundary: use EVT-001 for normal standby and release calls, EVT-002 for a failure branch requiring isolation, alternate delivery and rejoin. These records do not verify any live performance, equipment operation, accessibility certification or other model's behavior.
