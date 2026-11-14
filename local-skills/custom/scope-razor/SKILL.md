---
name: scope-razor
description: Use right after an idea is chosen to cut it to a demo-path MVP, split features into real / mocked / cut, and write the definition of done.
---

# scope-razor

## Top rules
1. Build only what the demo path touches. Everything else is a mock or doesn't exist.
2. Fake the edges, never the core. The core is whatever the anchor criterion and the wow moment depend on. That must be real.
3. Never lie. A mocked feature is either hidden or labelled "coming next" in the pitch. Judges who catch a fake core will zero you.
4. Cut until it hurts, then cut one more thing.
5. "Done" is written down before code. If you can't say what done is, you will polish forever.

## When to use
- An idea decision exists and nobody has written code yet.
- Mid-hack at the 50% mark when the team is behind (re-run with remaining hours).

## Inputs needed
- IDEA DECISION from `idea-forge`.
- Hours remaining and team composition.
- Hard submission requirements from the recon brief (video, repo, live URL).

## Steps

### 1. Write the demo path first (10 min)
List every screen and action a judge will see, in order. This is the spine.
Example format:
```
1. Landing → click "Start viva"
2. Speak answer (mic) → live transcript appears
3. AI interrupts with a gap question citing notes page
4. Student answers → score card with 3 gaps
5. "Export revision sheet" → PDF
```

### 2. Sort every feature into three buckets (10 min)

| Bucket | Rule | Examples |
|---|---|---|
| REAL | On the demo path AND tied to anchor/wow | retrieval, voice loop, gap detection |
| MOCKED | On the demo path but not judged | login (hardcode user), payments, settings, notifications, history of past sessions (seeded) |
| CUT | Not on the demo path | admin panel, multi-language, mobile app, analytics, onboarding tour, dark mode |

Mocking toolkit (pick the cheapest that holds up on screen):
- Hardcoded user, auto-logged in.
- Seed data script that fills realistic records.
- Static JSON response for non-core API calls.
- A button that works only for the demo account.
- Pre-computed results cached for the demo input, with live fallback.

### 3. Size it (5 min)
Estimate each REAL item in hours. Sum it. Multiply by 1.5. If total > 55% of remaining hours, cut the lowest-value REAL item to MOCKED, or simplify it, and resize.

### 4. Define done (5 min)
Done = the three statements below are all true:
1. The demo path runs end-to-end on the deployed URL, three times in a row, without touching code.
2. The wow moment works on a fresh input that wasn't hardcoded.
3. The video is recorded and the submission form is filled.

Then add 2–3 stretch goals, ordered, only to be touched after done.

## Outputs
```
SCOPE CARD — <project>
Demo path: <numbered steps>
REAL: <item — est hours>
MOCKED: <item — how>
CUT: <items>
Total REAL est ×1.5: <h> of <h> remaining
Definition of done: <3 statements>
Stretch (only after done): 1. <...> 2. <...>
Honesty line for pitch: "<what is mocked and how we'd build it>"
```

## Worked example
VoiceViva, 36h, 3 people.
- REAL: speech-to-text streaming (3h), retrieval over uploaded notes (4h), gap-detection prompt with structured output (3h), interrupting voice reply (3h), score card UI (3h). Total 16h ×1.5 = 24h of ~30 usable dev-hours. Tight but OK with 2 devs in parallel.
- MOCKED: auth (single demo user), note upload (pre-indexed 2 PDFs plus live upload for one small file), session history (seeded 5 sessions).
- CUT: teacher dashboard, leaderboard, Hindi support, mobile.
- Honesty line: "History and accounts are seeded for the demo; the viva loop and retrieval are live on whatever you upload."

## Failure modes
- Building auth first. Nobody ever won on login.
- "We'll just add X quickly." Every quick add costs 3× in integration.
- Mocking the core and getting asked "can you try it with my input?"
- No written done line, so the team polishes until the deadline and never records the video.

## Hand-off
Pass SCOPE CARD to `team-ops` (timeline) and `stack-launcher` (setup) in parallel.
