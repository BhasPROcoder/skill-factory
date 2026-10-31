---
name: team-ops
description: Use once scope is set to assign roles, build an hour-by-hour hackathon timeline with checkpoints and feature freeze, including a solo-mode plan.
---

# team-ops

## Top rules
1. One owner per thing. Shared ownership means nobody owns it.
2. Feature freeze is sacred: 75% of total time for 24–36h events, 80% for 48h. After freeze, only bug fixes and polish.
3. Checkpoint every 4 hours: what's done, what's blocked, what gets cut. 10 minutes, standing.
4. Sleep is scheduled, not earned. A 3-hour block for everyone in a 36–48h event. Tired teams ship broken demos.
5. The pitcher starts on the story at hour 0, not at hour 30.

## When to use
- Scope card exists and the team needs a plan.
- At any checkpoint when the plan slipped by more than 2 hours (re-plan from now).
- Solo entry.

## Inputs needed
- SCOPE CARD from `scope-razor`.
- Start time and deadline (local), event length.
- Team members with strongest skill each, and anyone arriving late or leaving early.
- Judging format (live, video-only, both).

## Steps

### 1. Assign roles (5 min)

| Role | Owns | Typical person |
|---|---|---|
| Builder (core) | the REAL items tied to the wow moment, backend, AI loop | strongest dev |
| Builder (surface) | frontend, demo path UI, deploy | second dev |
| Designer / UX | screens, copy, slide visuals, video edit | designer or most visual person |
| Pitcher / domain | rubric tracking, user research, story, pitch, video script, submission text, sponsor conversations | best speaker |

Team of 2: Builder (core+deploy) and Builder (surface)+Pitcher.
Team of 3: core, surface+design, pitcher+design.
Team of 4: one per role.
Solo: see solo mode below.

### 2. Lay out the timeline
Use the template matching the event length. Times are offsets from kickoff (H0).

**48h template**
| Window | Goal | Checkpoint output |
|---|---|---|
| H0–H2 | recon, idea, scope, roles | scope card signed |
| H2–H4 | repo + deploy hello world, riskiest spike | live URL, spike verdict |
| H4–H16 | vertical slice of demo path end-to-end (ugly) | demo path runs once |
| H16–H19 | sleep block A | |
| H19–H32 | make REAL items solid, mocks in place | demo path runs 3× clean |
| H32–H35 | sleep block B | |
| H35–H38 | **feature freeze at H38** | |
| H38–H42 | polish UI, demo safety, record backup video | backup video exists |
| H42–H45 | final video, submission text, slides | submitted draft |
| H45–H48 | rehearse pitch ×3, buffer | final submit by H47 |

**36h template**: compress: idea done by H1.5, slice by H12, sleep H13–H16, freeze at H27, video by H31, submit by H35.

**24h template**
| Window | Goal |
|---|---|
| H0–H1 | recon, idea, scope |
| H1–H2 | repo, deploy, spike |
| H2–H10 | vertical slice end-to-end |
| H10–H12 | nap block (stagger: 90 min each) |
| H12–H18 | harden, mocks, **freeze at H18** |
| H18–H21 | polish, backup video, demo safety |
| H21–H23 | final video, submission, slides |
| H23–H24 | rehearse, submit by H23.5 |

### 3. Checkpoint script (every 4h, 10 min)
Each person answers, in order:
1. Done since last checkpoint (demo-visible only).
2. Blocked on.
3. Will finish by next checkpoint.
Then the pitcher asks: "Is the demo path still runnable end-to-end?" If no, that's the only priority until it is.
Slip rule: if an item is >2h behind, cut or mock it now. Not later.

### 4. Communication rules
- One channel for status, one for links (deploy URL, repo, Figma, video drafts).
- Pin the scope card and the scoring map.
- Merges to main only when the demo path still works.

## Solo mode
- Do everything in single-threaded order: recon → idea → scope (45 min total), then the template above with all roles you.
- Swap roles by time block, not by mood: build blocks of 3h, then 30 min of pitcher work (story, screenshots, script) every 6h.
- Cut scope 30% harder than a team would.
- Use Claude as the second builder for boilerplate and as the designer for copy and slide outlines.
- Record the backup video at freeze time. Solo builders run out of energy first.

## Outputs
```
TEAM PLAN — <project>
Roles: <name → role → owns>
Timeline: <table with absolute local times>
Feature freeze: <absolute local time>
Checkpoints: <times>
Sleep blocks: <who, when>
Submit target: <time, 1h before deadline>
```

## Worked example
36h, kickoff Sat 10:00, deadline Sun 22:00. Team: Lakshya (core), Aman (surface+design), Riya (pitcher+design).
- Freeze: Sun 13:00 (H27). Submit target: Sun 21:00.
- Checkpoints: 14:00, 18:00, 22:00 Sat; 06:00, 10:00, 14:00, 18:00 Sun.
- Sleep: Lakshya 02:00–05:00, Aman 03:00–06:00, Riya 01:00–04:00 (staggered so one dev is always up).
- Riya by Sat 14:00: user interviews with 3 students in the venue, hook line drafted.

## Failure modes
- No freeze, so features land at H46 and break the demo.
- Everyone coding, nobody writing the story. The pitch then looks like an afterthought.
- Silent blocking: someone stuck for 3 hours without saying it. The checkpoint exists to catch this.
- All-nighters. They feel heroic and produce demo bugs.

## Hand-off
Builders go to `stack-launcher` then `build-sprint`. Pitcher goes to `demo-architect` immediately.
