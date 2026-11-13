---
id: IPR-002
name: asynchronous-result-generation-ownership
domain: Interactive Prototype Behavior
subdomain: Asynchronous results
version: 1.0
description: Implement and test request-generation ownership when delayed responses must not replace results for a user's newer input.
triggers: ["stop old search results replacing new ones", "prototype asynchronous result states", "test out-of-order responses", "ignore stale request errors", "handle repeated queries safely"]
not_for: ["telemetry observation freshness [UST-001]", "network retry policy design", "backend transaction concurrency", "general responsive layout [CTG-011]"]
requires: []
risk_level: medium
---

# Asynchronous Result Generation Ownership

## Purpose
Build an executable model tying each visible asynchronous result to the user intent that requested it. Distinguish a superseded callback from a current success or error, including when the same query text appears again after an intervening edit.

## Inputs to collect
1. **Result context** — identify input fields and other context that determines a result, such as selected scope or locale. Default: required; do not assume text alone identifies a request.
2. **Refresh triggers** — obtain events that replace intent, including clearing input and leaving the view. Default: every relevant input change invalidates the former generation.
3. **Visible-state policy** — obtain whether prior results remain during loading and how they are labeled. Default: clear the active result on a new intent; retained-history behavior requires a separate explicit policy.
4. **Response shape** — collect success, empty and error representations for the prototype. Default: fictional string items and error messages, with no actual service integration.
5. **Execution boundary** — identify the framework and authorized test environment. Default: Python 3 transition model; current framework cancellation and lifecycle behavior must be checked in its official documentation before integration.

If a required input is missing and has no safe default, ask in one message, max 3 questions. Model only the supplied context rather than inventing service behavior.

## Procedure
1. Define a complete intent key from the result-determining inputs. Keep a monotonically advancing local generation independent of that key; returning to the same text is still a new intent.
2. Specify the state transition at input change, before any debounce or request begins. ⚠️ Delaying invalidation until a new request is sent leaves a window in which an old callback can publish against edited input.
3. Attach the current generation to each dispatched request. Keep the snapshot of context associated with it so debugging can establish which input produced a callback.
4. Guard every callback that mutates the display, including errors, loading indicators and completion handlers. Reject superseded generations without clearing current loading state or replacing current content.
5. Treat cancellation as an optional resource-management action rather than the only correctness guard. The model must remain correct if a canceled operation still delivers a callback.
6. Implement the Python 3 model below. Its begin function represents immediate intent invalidation plus dispatch for nonempty text; if the actual UI debounces dispatch, preserve the immediate invalidation event and model dispatch separately.
7. Run traces in deliberately reversed completion order. Include repeated text across different generations, clearing the input while pending and a late error after a newer success.
8. Connect accepted model outcomes to the interface and verify the actual integration. Record how pending, empty, success and error appear, and do not count a model pass as evidence that framework callbacks obey the guard.

```python
def initial():
    return dict(generation=0, query="", status="idle", items=(), error=None)

def begin(state, query):
    updated = dict(state, generation=state["generation"] + 1,
                   query=query, status="pending" if query else "idle",
                   items=(), error=None)
    return updated, updated["generation"] if query else None

def settle(state, token, items=(), error=None):
    if token != state["generation"] or state["status"] != "pending":
        return state, "ignored"
    if error is not None:
        return dict(state, status="error", items=(), error=error), "accepted"
    values = tuple(items)
    return dict(state, status="success" if values else "empty",
                items=values, error=None), "accepted"

s, first = begin(initial(), "oak")
s, second = begin(s, "elm")
s, outcome = settle(s, second, ["Elm result"])
assert outcome == "accepted" and s["items"] == ("Elm result",)
assert settle(s, first, error="late failure") == (s, "ignored")
s, third = begin(s, "oak")
assert settle(s, first, ["Old oak"]) == (s, "ignored")
s, outcome = settle(s, third, [])
assert outcome == "accepted" and s["status"] == "empty"
s, fourth = begin(s, "ash")
s, no_request = begin(s, "")
assert no_request is None and s["status"] == "idle"
assert settle(s, fourth, ["Ash result"]) == (s, "ignored")
assert settle(s, None) == (s, "ignored")
print("generation ownership checks passed")
```

This reference intentionally uses a single active request per view and immutable tuple results. Paginated or parallel result sections require distinct ownership scopes; do not reuse one token to decide unrelated sections unless the product actually replaces them together.

## Decision rules
- IF a response belongs to a superseded generation THEN ignore its display mutation BECAUSE completion time does not establish ownership of current intent.
- IF query text returns to an earlier value THEN issue a new generation BECAUSE the prior request may have used different context or a different point in the workflow.
- IF current input becomes empty THEN invalidate pending work immediately BECAUSE a late callback must not refill a deliberately cleared view.
- IF a stale callback reports failure THEN ignore its error and loading mutation BECAUSE it cannot determine the state of the current request.
- IF several sections load independently THEN give each section its own ownership boundary BECAUSE one section's completion must not invalidate another's current work.

## Output template
```text
Intent scope: <result-determining inputs and ownership boundary; two sentences>
State contract: <up to eight event, generation guard and visible-outcome rows>
Implementation: <runnable model or implementation reference>
Executed schedule: <up to eight ordered events with observed state>
Assertions: <up to six checked invariants and results>
Integration checks: <up to four remaining framework/view checks>
Limit: <model versus actual runtime evidence; two sentences>
```

## Quality checklist
- [ ] Every relevant input change invalidates prior ownership immediately.
- [ ] Generation identity is distinct from equality of query text.
- [ ] Success, error and completion mutations use the ownership guard.
- [ ] Clearing input prevents a late result from refilling the view.
- [ ] Empty results remain distinguishable from an error and from idle input.
- [ ] Tests include reversed completions and repeated text.
- [ ] Cancellation is not the sole reason an obsolete callback is safe.
- [ ] Any unexecuted integration behavior is explicitly pending.

## Anti-patterns
- **Last callback wins**: arrival order selects visible content. Fix: require current generation ownership.
- **Text-only equality**: an old request for the same text is accepted. Fix: preserve distinct generation identity across edits.
- **Error bypass**: only success handlers check ownership. Fix: guard every callback that changes current state.
- **Late invalidation**: debouncing delays retirement of old intent. Fix: invalidate at input change and defer only dispatch.
- **Spinner theft**: an obsolete completion hides a newer loading indicator. Fix: let only the owning request settle its state.

## Worked example
**Input:**
> Fictional catalog Cedar starts oak request A, changes to elm request B and receives B successfully. A then fails. The user returns to oak, starting C; A also delivers an old success callback. Use the model only.

**Output:**
```text
Intent scope: Cedar single catalog-result view, with query as the supplied context. Every input change creates a new ownership generation.
State contract: input change -> retire prior generation and show pending; owning success -> success or empty; stale success/error -> no mutation; clear -> idle.
Implementation: begin and settle functions in the supplied Python model.
Executed schedule: A oak pending; B elm pending; B success shows Elm result; A error ignored; C oak pending; A old success ignored; C empty response shows empty; later clear invalidates pending work.
Assertions: Newest intent owns display; stale errors preserve Elm result; repeated oak text does not revive A; empty differs from idle; cleared input rejects late callbacks.
Integration checks: Verify guards in real success/error/completion handlers and immediate invalidation before any debounce.
Limit: Python state transitions were exercised. No service, framework callback or rendered catalog was tested.
```

**Bad output:**
> Cancel request A and accept any later callback whose query equals the text box.

This still accepts A when the text returns to oak and leaves cancellation as an untested assumption.

## Edge cases
- **View is left and reopened**: use a new view-lifetime identity or otherwise invalidate the old generation before new callbacks may publish.
- **Cached result appears immediately**: label its source and bind it to current intent; a cache hit does not authorize callbacks from an old generation.
- **Parallel facets**: define separate facet ownership if they update independently; aggregate completion only under a specified combined contract.
- **Additional pages**: include page identity and the active query generation so an old query's page cannot append to a newer result set.

## Test case
**Input:**
> Fictional search moves from red to blue to red. The first red request completes while the newest red request is pending. Then the user clears the field and the newest request fails.

**Assertions:**
1. The first red response is ignored despite matching current text.
2. Clearing input invalidates the newest pending generation.
3. Its later error does not replace idle state.
4. The output includes an executable trace and distinguishes model evidence from integration evidence.
