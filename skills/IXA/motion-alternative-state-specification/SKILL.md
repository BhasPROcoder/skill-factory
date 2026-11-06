---
id: IXA-001
name: motion-alternative-state-specification
domain: Interaction Adaptation
subdomain: Motion adaptation
version: 1.0
description: Specify nonmoving alternatives that preserve interface meaning and task completion when animated transitions must respect user motion preferences.
triggers: ["design reduced motion behavior", "replace interface animation", "preserve feedback without movement", "specify motion preferences", "review animation alternatives", "handle motion settings during transitions"]
not_for: ["general component composition [CTG-011]", "writing empty-state copy [MPU-002]", "animation production or rendering", "accessibility compliance certification"]
requires: []
risk_level: medium
---

# Motion Alternative State Specification

## Purpose
Produce a state-by-state replacement for interface motion that preserves the information and control the movement originally conveyed. The result is an interaction specification with testable alternatives, not an assurance that a product meets every accessibility requirement.

## Inputs to collect
1. **Task and surface:** Identify the user action, component, and expected outcome. This defines what must remain possible. Default: none; required for a concrete specification.
2. **Motion inventory:** Collect triggers, moving elements, start and end states, looping behavior, and any information encoded by movement. This reveals what removal would lose. Default: inspect supplied descriptions; do not invent unseen animations.
3. **Preference evidence:** Identify available system and application preferences, their documented meanings, and the user's explicit choice. This establishes the applicable mode. Default: unresolved preference semantics; propose a clearly labeled nonmoving mode without claiming it is already configured.
4. **Interaction state:** Collect focus placement, selection, scroll position, pending work, and cancellation behavior. These establish continuity requirements. Default: preserve existing user state unless the supplied task requires a change.
5. **Implementation capabilities:** Identify whether static text, symbols, progress values, and controls can be displayed. This bounds feasible alternatives. Default: a text specification only; no implementation or rendering claims.
6. **Acceptance context:** Obtain supported devices, input methods, and required current accessibility criteria. This scopes verification. Default: no certification claim; unresolved criteria remain a verification task.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. List each animation as a transition from a named starting state to a named resulting state rather than describing only its visual style.
2. Classify the function of that movement: decorative emphasis, spatial relationship, status feedback, progress, or an essential part of the requested content.
3. Identify the information a user would lose if the animated frames disappeared. Record the action result, location change, or progress evidence that requires an alternative cue.
4. ⚠️ Define a nonmoving representation for that information before removing the motion. An empty space where a spinner used to be does not communicate whether work is pending or finished.
5. Specify the visible content and controls in the alternative state, using explicit words and stable symbols where available. Keep waiting, success, failure, and cancellation distinct; do not replace an unknown completion time with invented progress.
6. Define how focus, selected items, and reading position survive the transition. Changing the presentation mode must not repeat a submission, reset a form, or unexpectedly relocate the current interaction.
7. Write a preference-resolution rule from supplied product semantics. If system and application choices conflict and precedence is unknown, flag the design decision instead of silently guessing which setting wins.
8. ⚠️ Specify what happens when the preference changes during an animation. Move to a coherent presentation of the actual task state without restarting the task or presenting an unobserved completion state.
9. Treat user-requested motion content separately from decorative interface motion. When movement is the content being examined, design a deliberate play, pause, or step-through path as supported; do not erase the user's requested information without explanation.
10. Create a walkthrough covering the ordinary transition, preference active at entry, preference changed mid-transition, and failure during pending work.
11. Inspect the actual implementation if available, including focus and task outcome. Otherwise mark the walkthrough as a proposed test and identify the evidence needed to execute it.

Describe alternatives through observable properties: stationary status label, immediate state replacement, retained selection, explicit result message, or user-controlled frame progression. Avoid claiming that a shorter or subtler animation is automatically an adequate replacement. Verify platform preference behavior and applicable current criteria in the official documentation for the actual environment; if unavailable, write `[VERIFY: preference semantics and applicable accessibility criteria in the platform and standards documentation]`.

## Decision rules
- IF movement only decorates an unchanged state THEN omit it in the nonmoving mode BECAUSE no task information needs a moving substitute.
- IF animation carries progress or completion information THEN supply an explicit state cue BECAUSE removing motion must not remove task status.
- IF progress cannot be measured THEN use a pending message without a percentage BECAUSE a decorative cycle is not measured completion evidence.
- IF a preference changes during pending work THEN change presentation while retaining the operation BECAUSE an accessibility choice is not a retry request.
- IF movement is the requested instructional content THEN preserve access through deliberate controls where possible BECAUSE the alternative must still communicate the requested information.

## Output template
```text
Task boundary: <component, action, and preserved outcome; up to two lines>
Preference contract: <known semantics, precedence, and unresolved decisions; up to four lines>
Alternative map:
Transition | Motion function | Nonmoving representation | Preserved state
<up to eight rows>
Walkthrough: <four to six event/result pairs>
Verification: <performed or proposed; concrete focus, state, and outcome checks>
Open dependencies: <up to three grouped questions>
Delivery status: <specification or inspected implementation; limits>
```

## Quality checklist
- [ ] Each animated transition has a named starting and resulting state.
- [ ] Every informational motion has a nonmoving equivalent.
- [ ] Pending, success, failure, and cancellation remain distinguishable.
- [ ] Focus, selection, and operation identity are preserved explicitly.
- [ ] Preference precedence follows evidence or remains an open decision.
- [ ] A mid-transition preference change cannot silently repeat the operation.
- [ ] Unknown progress is not replaced with fabricated percentages.
- [ ] Verification distinguishes proposed checks from inspected behavior.

## Anti-patterns
- **Delete and forget:** Removing a spinner leaves no waiting signal. Fix: retain a stationary pending label and relevant controls.
- **Faster means accessible:** Shortening an animation is asserted to satisfy every need. Fix: specify the requested alternative and verify actual applicable criteria.
- **Preference as restart:** A setting change resubmits the form. Fix: separate operation state from presentation state.
- **Completion illusion:** Ending animation displays success before the operation finishes. Fix: derive the result message from actual task evidence.
- **Blanket content removal:** Disabling motion deletes an animation lesson. Fix: preserve deliberate access to the content through supported controls.

## Worked example
**Input:**
Fictional design team Juniper has an upload card with a rotating pending symbol and an animated success check. Upload completion is reported by the upload service; percentage progress is unavailable. The team's supplied rule says an explicit application choice of nonmoving mode applies immediately. A user switches that mode on while an upload is pending. No running interface is available.

**Output:**
```text
Task boundary: Upload card; preserve the current upload and communicate its actual result.
Preference contract: Supplied application choice of nonmoving mode applies immediately. Other preference combinations are outside this supplied case.
Alternative map:
Pending to pending | rotating waiting cue | stationary Upload in progress label | same upload identity and focus
Pending to success | animated result emphasis | stationary Upload complete message | completed upload reference
Pending to failure | result feedback | stationary Upload failed message and supported retry action | failure evidence and retained file choice
Walkthrough: Start upload -> pending state with operation identity retained.
Enable nonmoving mode -> stop decorative rotation; show Upload in progress without resubmission.
Service reports success -> show Upload complete without animated check.
Service reports failure in an alternative run -> show failure, never a success message inferred from animation ending.
Verification: Proposed only; inspect that preference changes preserve focus and submit once, and that service results control the message.
Open dependencies: Which retry and cancellation controls are actually supported? What other preference precedence rules apply? Which environments and current criteria must be tested?
Delivery status: Specification only; no interface was run or certified.
```

**Bad output:**
“Hide all animation and immediately show the success icon when the preference changes.”
This removes the waiting state and invents completion unrelated to the upload result.

## Edge cases
- Motion loops while the user is idle: provide a nonmoving presentation without requiring repeated intervention; verify any actual pause controls separately.
- A transition changes pages: identify the resulting page and intended focus destination explicitly rather than relying on a slide direction.
- Preference storage is unavailable: disclose the scope of the current choice and do not promise it will persist across sessions.
- A user requests animation inspection: retain a supported deliberate playback path while keeping unrelated interface decoration nonmoving.

## Test case
**Input:**
> Fictional team Birch removes a looping saving animation when a user enables nonmoving mode. The save remains pending, no completion percentage exists, and the input focus is in an editable note. Specify the alternative state.

**Assertions:**
1. Shows an explicit pending-saving cue without an invented percentage.
2. Preserves the save operation and editable-note focus.
3. Does not claim success until actual save evidence exists.
4. Labels implementation checks as proposed unless actual execution evidence is supplied.
