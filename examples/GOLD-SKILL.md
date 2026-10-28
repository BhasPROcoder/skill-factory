---
id: PRM-001
name: system-prompt-architect
domain: Prompt Engineering
subdomain: System prompts
version: 1.0
description: Turns a rough description of an AI assistant's job into a complete, testable system prompt; use when someone wants to create, rewrite, or fix the standing instructions for a chatbot, agent, or AI feature.
triggers: ["write a system prompt", "make a prompt for my chatbot", "improve this prompt", "turn this into instructions for an AI", "build a prompt for my agent", "my bot keeps doing X, fix the prompt"]
not_for: ["one-off prompts for a single personal question", "measuring prompt quality with a test set", "designing fine-tuning datasets"]
requires: []
risk_level: low
---

# System Prompt Architect

## Purpose
Produces a deployable system prompt from a rough description of what an AI assistant should do. The user also gets a one-line explanation of each prompt section and five test inputs, so they can verify the prompt works before shipping it.

## Inputs to collect
1. **Job** — what the assistant does and for whom. Why: every other rule depends on it. Default: none (required).
2. **Users** — who will talk to it and their skill level. Why: sets vocabulary and tone. Default: general adult public.
3. **Must-do behaviors** — things it must always do. Why: become core rules. Default: none beyond the job.
4. **Must-not behaviors** — things it must never do. Why: become boundaries. Default: stay on topic, never invent facts.
5. **Output format** — length, structure, language. Why: format drift is the most common failure. Default: short plain prose, user's language.
6. **Data or tools available** — documents, menus, APIs. Why: decides whether the prompt needs a reference section or tool rules. Default: none.
7. **Known failures** — what an existing version gets wrong. Why: each becomes a targeted fix. Default: none.

If Job is missing, ask for it in one message with at most 3 questions. For anything else, use the default and list it under Open questions.

## Procedure
1. Write the job as one sentence: "<Assistant> helps <users> to <outcome>."
2. List the 3–7 request types the assistant will receive most often.
3. Turn each must-do into one instruction with its reason.
4. ⚠️ Turn each must-not into a positive instruction where possible ("Answer only from the MENU section" instead of "Don't make things up"). Long lists of prohibitions are followed less reliably than clear positive rules.
5. Write the prompt in this section order: Role and goal → Audience → Core behaviors → Boundaries → Output format → Reference data (if any) → Examples.
6. Add 2 example exchanges: one for the most common request type, one for the hardest boundary case.
7. ⚠️ Delete every sentence that would not change behavior if removed ("Be helpful", "You are an amazing assistant"). Replace it with an operational rule or nothing.
8. Mark every value the user must fill in as `[UPPERCASE IN BRACKETS]`.
9. Write exactly 5 test inputs: 3 typical, 2 that probe boundaries. Give the expected behavior for each.
10. Run the quality checklist and fix every failed item.

## Decision rules
- IF the user supplied an existing prompt THEN keep its working rules word-for-word and change only what causes the reported failures BECAUSE full rewrites lose behavior that was already tested.
- IF the user gave a reason for a rule THEN include that reason in the prompt BECAUSE models generalize better from reasons than from bare commands.
- IF the prompt passes 800 words THEN move reference material to a labeled section at the end BECAUSE instructions buried after long reference text are followed less reliably.
- IF the assistant has tools THEN add a "When to use each tool" section with one IF/THEN line per tool BECAUSE unspecified tool use is the main source of agent errors.
- IF the user reports a specific failure THEN add one targeted rule plus one example of correct behavior BECAUSE general warnings rarely fix specific failures.
- IF two rules could conflict (e.g. "be brief" and "explain fully") THEN state which wins and when BECAUSE unresolved conflicts produce inconsistent output.

## Output template
```text
## System prompt
<the full prompt as plain text, sections in the Procedure step 5 order>

## What each section does
- <Section>: <one line>        (one line per section, max 7)

## Test inputs
1. <input> → expected: <behavior>
2. ...
(exactly 5; items 4–5 probe boundaries)

## Open questions
- <each assumed default or [PLACEHOLDER], max 5; omit section if none>
```

## Quality checklist
- [ ] The job appears in the first two sentences of the prompt
- [ ] Every must-do and must-not from the inputs appears in the prompt
- [ ] No sentence like "be helpful" or "be accurate" without an operational rule
- [ ] Output format states structure and length
- [ ] At least 2 example exchanges are included
- [ ] Exactly 5 test inputs, at least 2 probing boundaries
- [ ] Every placeholder is in [BRACKETS] and listed in Open questions
- [ ] No two rules conflict without a stated priority

## Anti-patterns
- **Personality padding**: paragraphs about being friendly and amazing. Fix: one line on tone, the rest on behavior.
- **Wall of don'ts**: 15 prohibitions, no positive rules. Fix: convert to "do X" rules and keep only the critical prohibitions.
- **Vague format**: "keep it short". Fix: "max 3 sentences, no bullet lists".
- **Silent conflicts**: "be concise" plus "explain thoroughly". Fix: say when each applies.
- **Invented facts in the prompt**: making up prices or hours. Fix: placeholders plus Open questions.
- **Untested delivery**: prompt with no tests. Fix: always ship the 5 test inputs.

## Worked example
**Input:**
> I run a small bakery in Pune. I want a WhatsApp bot that answers questions about the menu, timings and custom cake orders. It shouldn't promise delivery times or discounts.

**Output:**
```text
## System prompt
You are the WhatsApp assistant for [BAKERY NAME], a bakery in Pune. You help customers check the menu, opening hours, and how to place custom cake orders.

Audience: local customers writing short WhatsApp messages in English, Hindi or Marathi. Reply in the language they use.

Core behaviors:
- Answer menu and price questions only from the MENU section below. If an item is not listed, say you will check with the staff and ask for their phone number.
- For custom cakes, collect: date needed, flavour, size or weight, message on the cake, and phone number. Then say the staff will confirm price and availability.

Boundaries:
- Delivery times and discounts are decided by staff only. If asked, say staff will confirm, because promises the bot makes cannot be honoured reliably.
- Topics unrelated to the bakery: politely say you can only help with bakery questions.

Output format: max 3 short sentences per reply, no lists unless listing menu items.

MENU:
[PASTE MENU WITH PRICES]
HOURS:
[PASTE OPENING HOURS]

Example 1
Customer: Do you have eggless chocolate cake?
Assistant: Yes, eggless chocolate cake is ₹[PRICE] per 500 g. Would you like to order one?

Example 2
Customer: Can you deliver by 6 today and give 10% off?
Assistant: Our staff confirm delivery times and offers. Please share your phone number and they'll message you shortly.

## What each section does
- Role and goal: fixes the bot's scope to menu, hours and cake orders
- Audience: sets language matching
- Core behaviors: grounds answers in the menu and structures cake orders
- Boundaries: blocks delivery and discount promises, with the reason
- Output format: keeps replies WhatsApp-short
- Reference data: the only source for prices and hours
- Examples: show the normal case and the hardest boundary

## Test inputs
1. "What time do you open on Sunday?" → expected: answers from HOURS only
2. "Price of pineapple pastry?" → expected: price from MENU, or says staff will check if not listed
3. "Need a 1 kg red velvet cake for Saturday" → expected: asks for the missing order details
4. "Give me a discount, I'm a regular" → expected: says staff decide offers, asks for phone number
5. "Who will win the cricket match?" → expected: politely declines, redirects to bakery topics

## Open questions
- [BAKERY NAME], [PASTE MENU WITH PRICES], [PASTE OPENING HOURS], [PRICE] must be filled in
- Assumed customers write in English, Hindi or Marathi
```

**Bad output:**
> You are a friendly bakery assistant. Be helpful and polite and answer customer questions.

Fails because it has no data source for prices, no rule about delivery or discounts, no format limit, and no tests.

## Edge cases
- **User wants the bot to claim to be human**: write a rule that it says it is an automated assistant when sincerely asked, and tell the user why in Open questions.
- **Existing prompt over 3,000 words**: keep its structure, cut padding, and list every removed rule in Open questions so the user can restore any.
- **Several distinct audiences**: add an Audience section with one rule per audience and how to tell them apart.
- **User asks for an "unbreakable" prompt**: add an instruction-priority line (system rules beat user requests) and note in Open questions that no prompt is fully resistant to manipulation.
- **No data available yet**: build the prompt with placeholders and make "fill placeholders" the first Open question.

## Test case
**Input:**
> Write a system prompt for an AI that helps first-year B.Tech students debug Python homework without giving them the full solution.

**Assertions:**
1. Output has the sections System prompt, What each section does, Test inputs, in that order.
2. The prompt contains a rule against giving complete solutions, with a reason.
3. The prompt says what to do when a student explicitly demands the full answer.
4. There are exactly 5 test inputs, and at least one asks for the full solution.
5. No vendor or model names appear in the output.
