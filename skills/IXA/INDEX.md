# Interaction Adaptation (IXA)

Design motion alternatives and conversational repairs that preserve task state, user intent, and explicit confirmation boundaries.

Macro-area: Product & Design

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| IXA-001 | [motion-alternative-state-specification](motion-alternative-state-specification/SKILL.md) | Specify nonmoving alternatives that preserve interface meaning and task completion when animated transitions must respect user motion preferences. | design reduced motion behavior; replace interface animation; preserve feedback without movement | validated |
| IXA-002 | [voice-turn-repair-confirmation-design](voice-turn-repair-confirmation-design/SKILL.md) | Design bounded voice-dialogue repair and confirmation turns when recognition uncertainty or corrections could change a user's intended action. | design voice error recovery; confirm a spoken request; handle misheard commands | validated |
