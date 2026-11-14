---
name: judge-qa-prep
description: Use before judging to predict the questions judges and sponsors will ask about tech, viability, ethics, scale and alternatives, and prepare tight 20-second answers.
---

# judge-qa-prep

## Top rules
1. Answer in 20 seconds: direct answer, one piece of evidence, stop.
2. Never bluff. "We didn't get to that; here's how we'd do it" beats a confident wrong answer.
3. Turn weak spots into roadmap, not excuses.
4. If a judge asks to try it, let them. Prepare a safe input to suggest.
5. Assign who answers what: tech questions to the builder, user/market to the pitcher.

## When to use
- 1–3 hours before judging.
- After a practice pitch where someone stumbled on a question.

## Inputs needed
- PITCH PACK, SCOPE CARD (especially MOCKED and CUT), DEMO SCRIPT.
- Judges and sponsors list from RECON BRIEF.
- Known weaknesses the team is worried about.

## Steps

### 1. Generate the question set
Use `references/judge-question-bank.md`. Pick 15–20 most likely for this project. Add 3 that are specific to the judges' backgrounds.

### 2. Write answers in this format
```
Q: <question>
A (20s): <direct answer>. <evidence: number, demo, design choice>. <optional: next step>.
Owner: <name>
```

### 3. Prepare for the hardest five
Rank questions by how much a bad answer would hurt. For the top 5, rehearse out loud twice.

### 4. Handle the trap categories
- "Isn't this just a wrapper around <model>?" → name the parts you built: retrieval, schema, interruption logic, evaluation, UX; show the reasoning panel.
- "Why not just use ChatGPT/<incumbent>?" → the specific thing they can't do in your flow (uses your data, acts proactively, works offline, in the user's language).
- "What's mocked?" → answer straight from the honesty line in the scope card.
- "Privacy / safety?" → what data is stored, where, for how long; what you'd add.
- "How does this make money / scale?" → one realistic model, one number, one cost driver.

### 5. Live-test readiness
- Have 2–3 suggested inputs written on a card for a judge to try.
- Know what happens if a judge types something weird. Test edge inputs now.

## Outputs
```
Q&A SHEET — <project>
Top 5 hardest with rehearsed answers
Full list (15–20) with 20-second answers and owners
Suggested judge inputs
Known limitations with honest framing
```

## Worked example
Q: "Isn't this just a ChatGPT wrapper?"
A: "The model is one part. We built retrieval over the student's own notes, a gap schema that only fires when a concept from their notes is missing, and the interruption timing. That's why it can say 'your notes, page 4' — a general chatbot can't. You can see the retrieved chunks in this panel." Owner: Lakshya.

Q: "How would you know it improves scores?"
A: "Retrieval practice has strong evidence in learning research. Our next step is a two-week pilot with one coaching batch comparing weekly test scores against a rereading control." Owner: Riya.

## Failure modes
- Two teammates answering the same question at once.
- Defensive tone when a judge points out a flaw.
- 90-second answers.
- Claiming a mocked feature is live.

## Hand-off
After judging → `post-hack-leverage`.
