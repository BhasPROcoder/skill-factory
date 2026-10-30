# Independent forward tests

Evaluator: forward_tests agent, separate from the skill authors. Date: 2026-10-29.

The parent supplied skill IDs and asked for realistic fictional tasks, without intended answers or suspected bugs. I read each complete skill, constructed new inputs, and produced the outputs below by applying its procedure. This is one evaluator executing three tasks, not a multi-model benchmark or a blind assessment of all skills. Inputs deliberately differ from the embedded examples. No skill or registry status was changed.

## TKG-002: weighted metric and wrong local implementation

### Input

Fictional team Juniper is preparing local evaluation for a fictional competition. Its supplied evaluation sheet, revision A, says: score is the sum of weight times absolute error divided by the sum of weights; lower is better. Targets are [1, 4, 8], predictions [2, 2, 10], and weights [1, 2, 1]. All are aligned in the supplied order. The current local script averages absolute errors without weights. The sheet does not discuss missing targets, zero total weight, or clipping. Mira owns the local metric. Produce an implementation brief; do not submit anything or assume these fictional rules describe a live competition.

### Actual output

```text
Deliverable: Weighted absolute-error implementation brief
Scope: Juniper's fictional revision A sheet and aligned three-row fixture; offline local evaluation only.
Evidence:
- Revision A explicitly specifies weighted aggregation and minimization.
- Absolute errors are [1, 2, 2]; weighted errors are [1, 4, 2].
- The supplied local script omits weighting.
Decision: Replace the unweighted aggregation for this supplied definition. The fixture's required result is 1.75; an unweighted result does not match it.
Artifact:
Metric = sum(weight * abs(target - prediction)) / sum(weight).
Direction = minimize.
Fixture: numerator = 1 + 4 + 2 = 7; denominator = 1 + 2 + 1 = 4; result = 7/4 = 1.75.
Python 3 fixture:
y = [1, 4, 8]
p = [2, 2, 10]
w = [1, 2, 1]
score = sum(a * abs(b - c) for a, b, c in zip(w, y, p)) / sum(w)
assert score == 1.75
This fixture assumes the supplied equal-length, aligned inputs and positive total weight. Production handling of invalid inputs and undefined cases remains unresolved.
Action:
- Mira: update the local metric and retain this fixture as a regression check; complete when the implementation reproduces 1.75.
Verification:
- Manual arithmetic: 7/4 = 1.75.
- Executed with Python 3.14.6: weighted assertion passed; unweighted calculation returned 1.6666666666666667 and the mismatch assertion passed.
- The actual local script was not provided or executed.
Open items:
- Check the current official evaluation definition for a real competition before adapting this fictional brief.
- Resolve missing targets, zero total weight, and clipping from that definition or its official clarification.
```

### Assessment

The output applies weighting, preserves direction, includes executable calculation, and separates the executed fixture from an unexecuted real script. It does not invent a convention for undefined cases. The negative check catches an unweighted implementation, although this tiny fixture cannot establish numerical robustness or production correctness. Useful concrete artifact: yes. No skill edit indicated by this trial.

## THK-003: asynchronous partial results and incompatible fields

### Input

Fictional hackathon team Ember is building a bird-image demo. Backend owner Inez provides a completed result as {"items":[{"label":"bird","score":0.8}]}. Frontend owner Dev expects {"predictions":[{"name":"bird","confidence":0.8}]}. Processing is asynchronous. A partially processed image must not appear as a completed result. Both owners authorize drafting a proposed shared payload, but neither has accepted a schema yet. They have an integration slot immediately after their next implementation checkpoint; no clock time is supplied. Success is rendering the same completed fixture and showing separate pending and failed states. Component code is unavailable. Produce the contract and mark unexecuted integration checks honestly.

### Actual output

```text
Deliverable: Proposed Ember demo integration contract
Scope: Supplied fictional payloads and asynchronous behavior; draft contract for owner agreement. No component code is available.
Evidence:
- Backend uses items/label/score; frontend expects predictions/name/confidence.
- Partial results must not display as completed.
- Inez owns the backend and Dev owns the frontend; neither has accepted this proposal.
Decision: Agree one payload before continuing parallel implementation. Proposed status discrimination prevents a partial payload from masquerading as success.
Artifact:
Proposed completed payload: {"status":"complete","items":[{"label":"bird","score":0.8}]}.
Proposed pending payload: {"status":"pending"}.
Proposed failed payload: {"status":"failed","error":"processing_failed"}.
Backend producer: Inez. Frontend consumer: Dev. Dev maps items to display rows and renders label and score only when status is complete. Pending shows an unfinished state; failed shows a failure state. Partial items are not exposed in this minimal proposal. Unknown or malformed payloads produce an explicit contract-error state rather than a successful blank result.
Integration slot: immediately after the supplied next implementation checkpoint. Run the identical completed, pending, and failed fixtures through producer and consumer. For an offline fallback demonstration, label fixtures as simulated; do not imply live classification.
Action:
- Inez and Dev: accept or revise field names and status semantics; completion means both record agreement on the same contract.
- Each owner: implement their boundary and capture the shared-fixture results at the agreed checkpoint.
Verification:
- Static comparison confirms the supplied field-name mismatch.
- A Python 3.14.6 fixture assertion confirmed the proposed completed payload has status complete and item fields label/score; it did not test either component.
- End-to-end boundary and pending/failed rendering checks remain pending because code is unavailable.
Open items:
- Owners must agree how the frontend receives later results; polling, notifications, and transport are not supplied.
- Confirm any current event rules applicable to the demonstration using the event's official rules before submission.
```

### Assessment

The output contains usable payloads, real assigned owners from the fixture, a meaningful integration point without an invented time, and an explicit asynchronous gap. It handles the requested partial-result failure mode and does not describe a proposal as accepted. The schema assertion is deliberately narrow; it does not establish runtime interoperability. Useful concrete artifact: yes. No skill edit indicated by this trial.

## CTR-001: one-way disclosure with conflicting commercial expectations

### Input

Fictional Alder Labs is the sole planned discloser of prototype drawings to fictional Brook Fabrication for estimating manufacturing work. A supplied excerpt has draft clause A: Brook must protect drawings and may disclose them only to its employees working on the estimate. Draft clause B: Brook must return drawings on Alder's request. No excerpt addresses duration, remedies, advisers, or subcontractors. Brook says it needs an outside estimator to prepare the quote. Jurisdiction and governing-law wording are not supplied. The requester asks whether the NDA must be mutual and whether Brook can already send the drawings to the estimator. Organize a provisional factual review and identify what must be resolved; do not provide a live legal conclusion.

### Actual output

```text
Task: Prepare a provisional clause review of one-way NDA coverage and the proposed outside-estimator disclosure.
Evidence: Only fictional clauses A and B and the parties' described purpose are supplied; the complete agreement is missing. Jurisdiction and governing-law wording are unknown. The excerpt does not establish how omitted subjects are handled elsewhere.
Result:
Review table:
Topic | Alder | Brook | Evidence and unresolved question
Disclosure flow | Sole planned discloser | Recipient for estimate | Supplied purpose; no reciprocal disclosure is identified.
Protection/permitted recipients | Protected drawings | Employees working on estimate only in supplied wording | Clause A; outside estimator is not identified as an employee or expressly permitted recipient.
Return | May request return | Return required by supplied wording | Clause B; mechanics and interaction with retained copies unknown.
Duration | Not shown | Not shown | Obtain complete agreement; do not infer absence.
Remedies | Not shown | Not shown | Obtain complete agreement; no enforceability conclusion.
Negotiation question: Does Alder agree to permit a named outside estimator for this purpose under specified confidentiality safeguards? Treat that as a proposed permission to resolve, not permission already granted.
Clarifying questions: (1) What country/state and governing-law wording apply? (2) Can you provide the complete agreement? (3) Is the estimator an employee, and has Alder provided any separate written permission?
Decision: One-way coverage matches the stated one-way information flow, so mutual wording is not automatically necessary. The supplied excerpt does not establish permission for the outside-estimator disclosure; do not rely on this provisional review as authorization to send drawings.
Next action: The requester should gather the complete draft and jurisdiction details, then obtain Alder's response to the recipient-scope question. A licensed lawyer in the relevant jurisdiction should review rights, enforceability, and proposed wording before live reliance.
Verification: [VERIFY: complete agreement and any separate disclosure permission with the parties' authoritative records.] Knowledge has a cutoff; check current applicable requirements with official jurisdiction-specific sources or qualified local counsel after jurisdiction is known.
```

### Assessment

The output distinguishes commercially sensible one-way coverage from a recipient-scope problem. It does not invent a governing jurisdiction, legal obligation, case, deadline, or legal result, and distinguishes an omitted excerpt from an absent contract term. It asks the three consolidated questions allowed by the skill and provides a table despite missing inputs. No current legal research was performed: this trial is fictional, source-bounded factual organization, not legal advice about a real agreement. Useful concrete artifact: yes. No skill edit indicated by this trial.

## Overall limits

These trials exercise three skills only. The evaluator read their embedded examples before making new fixtures, so this is not an unseen-skill or blinded benchmark. Assessment is self-evaluation of the independent evaluator's outputs, not a second assessor's rating. No live competition, event, codebase, legal matter, platform rule, or external source was tested. The Python checks actually executed; the remaining observations are source comparison and generated-artifact review. Nothing here warrants changing all library entries to audited.
