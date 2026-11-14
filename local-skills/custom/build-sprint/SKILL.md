---
name: build-sprint
description: Use while coding during a hackathon for rules on AI-assisted building under time pressure: vertical slices, commits, keeping main demo-ready, API fallbacks, seed data.
---

# build-sprint

## Top rules
1. Vertical slice first: ugly end-to-end demo path before any single step is pretty.
2. Main always works. If a merge breaks the demo path, revert first, debug second.
3. Commit every 30–45 minutes with a message that says what now works.
4. Deploy after every meaningful merge. The live URL is the truth.
5. Every external call has a timeout and a fallback.
6. Stuck for 30 minutes = say it out loud. Stuck for 60 = cut, mock, or swap approach.

## When to use
- Stack is live and the team is writing feature code.
- The build is falling behind and needs triage.
- An AI coding assistant is generating most of the code.

## Inputs needed
- SCOPE CARD (demo path, REAL/MOCKED/CUT).
- TEAM PLAN (freeze time).
- Current state: what works on the live URL right now.

## Steps

### 1. Slice plan
Break the demo path into slices, each one a thin pass through every layer.
- Slice 1: hardcoded input → real core call → raw output on screen.
- Slice 2: real input → real core → formatted output.
- Slice 3: mocks in place for everything around it.
- Slice 4+: harden, edge cases on the demo path only, UI polish.
Do not start slice N+1 until slice N runs on the deployed URL.

### 2. AI-assisted coding protocol
- Give the assistant the scope card and the file tree before asking for code.
- Ask for one file or one function at a time with explicit inputs and outputs. "Build the whole app" produces code nobody understands at H40.
- Read every generated diff before committing. Run it locally, then on deploy.
- When the assistant loops on a bug twice, stop. Read the error yourself, paste the exact error and the relevant 50 lines, and ask for a minimal fix.
- Keep a `NOTES.md` with decisions and gotchas. Feed it back into new chats instead of re-explaining.
- Never let generated code add a new dependency without a reason.

### 3. Fallback rules for external APIs
```ts
async function withFallback<T>(fn: () => Promise<T>, fallback: () => T, ms = 8000): Promise<T> {
  try {
    return await Promise.race([
      fn(),
      new Promise<T>((_, rej) => setTimeout(() => rej(new Error("timeout")), ms)),
    ]);
  } catch {
    return fallback();
  }
}
```
- Fallback order: live call → cached response for that input → canned demo response.
- Rate limits: one retry with backoff, then fallback. Never infinite retry in the UI.
- Show a subtle state ("using cached result") rather than an error toast during the demo.

### 4. Seed data rules
- Seed realistic, not lorem ipsum. Real names (fictional people), plausible numbers, local context.
- One command resets the demo state: `npm run seed`.
- Seed the "before" state of the demo story so the wow moment has contrast.

### 5. Git discipline
- Branch per slice if 2+ devs, merge within 2 hours or it rots.
- Conventional message: `feat: viva loop interrupts on gap`, `fix: stt timeout fallback`.
- Tag the last known good demo build: `git tag demo-good-1`. Revert target if things break.

### 6. Stuck protocol
| Time stuck | Action |
|---|---|
| 15 min | Re-read the error. Minimal reproduction. |
| 30 min | Tell the team. Ask a mentor or sponsor engineer. |
| 60 min | Decide: mock it, swap the library, or cut it. Write the decision in NOTES.md. |

## Checklist before each checkpoint
- [ ] Demo path runs on live URL
- [ ] No console errors on the demo path
- [ ] New code committed and pushed
- [ ] Last good build tagged
- [ ] NOTES.md updated

## Outputs
- Working slices on the live URL.
- Tagged good builds.
- NOTES.md with decisions, which the submission writer later mines for "Challenges we ran into".

## Worked example
VoiceViva, H6: slice 1 works (typed text → retrieval → Claude gap question rendered as text). STT keeps timing out on venue Wi-Fi. At 30 min stuck: told team. At 50 min: switched to browser Web Speech API for the demo with server STT as optional; added a "type instead" fallback. Logged in NOTES.md: "Venue Wi-Fi drops websockets; browser STT is primary."

## Failure modes
- Polishing slice 1 UI for 6 hours while slice 3 doesn't exist.
- Giant AI-generated commits that break three things.
- No fallback, and the sponsor's API goes down during judging (it happens every event).
- Working on a feature in the CUT list because it's fun.

## Hand-off
AI features → `ai-feature-kit`. At freeze time → `demo-architect` safety checklist.
