---
name: hack-orchestrator
description: Use when the user says they're at or entering a hackathon without naming a step; detects the current phase from time and artifacts and routes to the right hackathon-os skill.
---

# hack-orchestrator

## Top rules
1. Always establish time first: current local time, deadline, hours left.
2. Check which artifacts exist (recon brief, idea decision, scope card, team plan, demo script, video, submission). The first missing one is usually the next step.
3. Time overrides sequence: if under 4 hours remain, skip straight to demo, video and submission regardless of what's missing.
4. Route to one skill at a time. Say which and why in one line.

## When to use
- "I'm at a hackathon", "help me win this hackathon", "what should I do now", or the user pastes a hackathon page with no instruction.

## Inputs needed
- Current time and deadline.
- What exists so far (ask: "Do you have a chosen idea? Is anything deployed? Is there a video?").
- The hackathon page if recon hasn't happened.

## Routing table

| Situation | Route to |
|---|---|
| No recon brief | `hack-recon` |
| Recon done, no committed idea | `idea-forge` |
| Idea chosen, no written scope/done | `scope-razor` |
| Scope done, no roles or timeline | `team-ops` |
| No repo or deploy | `stack-launcher` |
| Building | `build-sprint` (+ `ai-feature-kit` for LLM features) |
| Feature freeze reached or < 30% time left | `demo-architect` |
| Demo script exists, slides needed | `pitch-builder` |
| Freeze passed, no video | `demo-video` |
| < 5 h left, no submission draft | `submission-writer` immediately |
| Judging in < 3 h | `judge-qa-prep` |
| Event over | `post-hack-leverage` |

## Emergency mode (< 4 hours left)
1. Freeze features now.
2. Make the demo path run once end-to-end, mocking anything broken.
3. Record a video of whatever works (`demo-video`, 30-min version: one take, captions, no music).
4. Submit (`submission-writer`, minimal version) by T−1h.
5. Use leftover time for polish and Q&A prep.

## Phase check-in template
```
PHASE CHECK — <time>, <h> left
Exists: recon ✓/✗, idea ✓/✗, scope ✓/✗, plan ✓/✗, deploy ✓/✗, demo path runs ✓/✗, demo script ✓/✗, video ✓/✗, submitted ✓/✗
Next: <skill> — because <one line>
Then: <skill>
```

## Worked example
User at H30 of 36: "app mostly works, haven't done anything else."
```
PHASE CHECK — Sun 16:00, 6 h left
Exists: recon ✓, idea ✓, scope ✓, plan ✗, deploy ✓, demo path runs ✓, demo script ✗, video ✗, submitted ✗
Next: demo-architect — freeze was 3 h ago; lock the 2-min story.
Then: demo-video (record by 18:30), submission-writer (submit draft by 19:00), judge-qa-prep.
```

## Failure modes
- Continuing to build at H34 because "one more feature".
- Running full recon when 3 hours remain.

## Hand-off
To the routed skill. Re-run the phase check at every team checkpoint.
