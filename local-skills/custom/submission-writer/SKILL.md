---
name: submission-writer
description: Use to write the Devpost or hackathon submission and the repo README: inspiration, what it does, how built, challenges, accomplishments, next, plus media checklist.
---

# submission-writer

## Top rules
1. Submit a complete draft 3 hours before the deadline. Edit after. Portals crash at T−10 minutes every time.
2. Always submit, even if the build feels weak. Rubrics surprise teams who think they bombed.
3. First two lines do the work. Async judges skim. Lead with what it does and for whom.
4. Tag every prize/track you qualify for and mention each sponsor's tech by name in the text.
5. Be precise about what's real. Say what's mocked in "What's next", framed as roadmap.

## When to use
- Video exists or is in progress, feature freeze passed.
- Any time after H50% to start the draft early (recommended).

## Inputs needed
- RECON BRIEF (prize stack, submission fields, character limits).
- SCOPE CARD (real/mocked), NOTES.md (challenges), DEMO SCRIPT, video link, live URL, repo URL.
- Team names and handles.
- 3–6 screenshots and 1 GIF.

## Steps

### 1. Fill the template
Use `references/devpost-template.md`. Write in this order: tagline → what it does → inspiration → how we built it → challenges → accomplishments → what we learned → what's next → built with.

### 2. Apply rubric echo
For each rubric criterion, make sure one sentence in the submission directly gives the judge evidence for it. Use the criterion's own wording where natural.

### 3. Sponsor sections
For each targeted sponsor prize, add a short sub-section: "Use of <sponsor tech>" with what it does in the product and why it was the right choice.

### 4. Media
- Cover image: 3:2, product UI with the wow moment visible plus the name. No team selfie.
- Screenshots: the demo path in order, each with a 1-line caption.
- GIF: the wow moment, under 10 s.
- Architecture diagram.

### 5. README
Repo README mirrors the submission: one-line pitch, live URL, video, screenshot, how it works, how to run locally (copy-pasteable), env keys list, team. A judge who opens the repo should understand it in 30 seconds.

### 6. Final checks
- [ ] All required fields filled
- [ ] Every eligible prize/track ticked
- [ ] Video link works in incognito
- [ ] Live URL works in incognito on mobile and desktop
- [ ] Repo public (if required), no secrets in history
- [ ] All teammates added to the submission
- [ ] Submitted, confirmation screenshot saved

## Outputs
- Submission text ready to paste.
- README.md.
- Media files list.

## Worked example
VoiceViva tagline: "A study buddy that listens to you explain, then catches what you missed — with page numbers from your own notes."
First paragraph: "VoiceViva turns revision into a 5-minute viva. You explain a topic out loud; it checks your explanation against your own notes, interrupts when you skip something important, and gives you a gap card citing the exact page."
Challenges (from NOTES.md): websocket STT dropped on venue Wi-Fi, so we moved to browser speech recognition with a typed fallback; getting the model to interrupt only on genuine gaps needed a structured gap schema and a max-3 rule.

## Failure modes
- Submitting at T−2 minutes and the form rejects the video URL.
- Generic "we used AI to help students" text.
- Forgetting to tick sponsor tracks. Sponsors can only judge what's tagged.
- README that says "npm start" and nothing else.

## Hand-off
Likely judge questions from gaps in the text → `judge-qa-prep`. After results → `post-hack-leverage`.
