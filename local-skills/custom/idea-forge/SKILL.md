---
name: idea-forge
description: Use after hack-recon produces a scoring map, to generate 10 hackathon ideas, score them against rubric and sponsors, and pick one with justification.
---

# idea-forge

## Top rules
1. An idea is only as good as its demo moment. No "wow" moment you can show in 30 seconds = reject.
2. Score ideas, don't vote on them. Vibes pick the idea the loudest teammate likes.
3. Boring problem + surprising angle beats exciting problem + generic angle.
4. Buildability is a gate, not a score: if the core can't run end-to-end by 40% of the time budget, kill it.
5. Decide by hour 1.5 (48h) or hour 1 (24h). Indecision is the most expensive bug.

## When to use
- Recon brief exists and the team has no committed idea.
- An idea is chosen but feels weak and there is still >70% of time left (re-run to compare).

## Inputs needed
- RECON BRIEF from `hack-recon` (scoring map, anchor criterion, sponsor angles, prize stack).
- Team skills and size; total hours remaining.
- Any domain the team has unfair access to (a real user, a dataset, a lived problem).
- Hard tech limits (no GPU, no paid APIs, offline venue, etc.).

## Steps

### 1. Generate 10 ideas across 5 lenses (15 min)
Two ideas per lens. One line each: `<who> can <do what> by <mechanism>, demo moment: <...>`.
- **Sponsor-native**: the sponsor's API is the product, not a feature.
- **Pain you own**: a problem a teammate or someone they can call has this week.
- **Unexpected interface**: same task, new modality (voice, camera, WhatsApp, browser extension, AR overlay, hardware).
- **Data nobody uses**: a public dataset or document pile turned into an answer machine.
- **Agent that acts**: AI that completes a task end-to-end, not one that just chats.

### 2. Score all 10 (10 min)
Use `references/rubric-scoring-sheet.md` section B. Score 1–5 on:

| Factor | Weight |
|---|---|
| Anchor criterion fit | ×3 |
| Other rubric criteria (avg) | ×2 |
| Sponsor prizes it qualifies for (count, max 3) | ×2 |
| Demo wow moment (can a judge feel it in 30 s?) | ×3 |
| Buildability in remaining time | gate: must be ≥3 |
| Originality (not in top 20 Devpost results for the theme) | ×2 |

Run the originality check: search Devpost and GitHub for the idea in 3 phrasings. If a near-identical winner exists, either find a sharper angle or drop 2 points.

### 3. Pressure test the top 3 (10 min)
For each:
- Write the one-line pitch. If it needs "and" twice, it's two ideas.
- Write the 30-second demo moment as a screenplay line.
- List the single riskiest technical unknown. Can it be spiked in 45 minutes?
- Sponsor test: would the sponsor repost the demo video?

### 4. Pick and commit (5 min)
Choose the highest total among ideas that pass every gate. Tie-break order: demo wow > anchor fit > buildability.
Write the decision record and stop discussing.

## Outputs
```
IDEA DECISION
Pick: <name> — <one-line pitch>
Demo moment: <30-second screenplay line>
Scores: anchor <n>/5, rubric avg <n>/5, sponsors <list>, wow <n>/5, build <n>/5, originality <n>/5 → total <n>
Riskiest unknown: <...> — spike by <time>
Runner-up (fallback if spike fails): <name>
Why not the others: <one line each for #2, #3>
```

## Worked example
Recon: anchor = Innovation 30%, sponsors = vector DB + voice API, 36h, team of 3 (2 devs, 1 designer).

Top 3 after scoring:
1. **VoiceViva** — students talk through a concept out loud; it retrieves from their own notes and asks follow-up viva questions, flagging gaps. Demo moment: student explains photosynthesis badly, app interrupts with "you skipped where the ATP comes from — your notes page 4 says…". Total 52.
2. **ScanSyllabus** — photo of syllabus → week-by-week plan. Total 38 (low originality, many exist).
3. **CanteenCast** — voice ordering for the college canteen. Total 35 (weak anchor fit).

Decision: VoiceViva. Riskiest unknown: voice latency under 2 s round-trip. Spike by hour 2. Fallback: ScanSyllabus with voice input.

## Failure modes
- Picking the "most technically interesting" idea. Judges score what they see, not what was hard.
- Ideas with no named user. "Helps people be productive" scores zero on impact.
- Spending 4 hours ideating. Ten ideas in 15 minutes is the whole trick.
- Copying last year's winner. Judges remember.

## Hand-off
Pass IDEA DECISION to `scope-razor`.
