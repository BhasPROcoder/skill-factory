# Judge Question Bank

Pick the 15–20 most likely for your project. Answer each in ≤ 20 seconds.

## Technical
1. Walk me through what happens when I click <main action>.
2. What part did you actually build vs use off the shelf?
3. Isn't this just a wrapper around <model/API>?
4. How do you handle hallucinations / wrong answers?
5. What happens if the API is down or slow?
6. How did you evaluate quality? Any numbers?
7. Why this model / database / framework over <alternative>?
8. What was the hardest bug and how did you fix it?
9. What's mocked or hardcoded right now?
10. Can I try it with my own input?

## Viability and business
11. Who exactly is the user? Have you talked to any?
12. Why would they switch from what they use now?
13. How does this make money, or who pays?
14. What does it cost to run per user?
15. Who are the competitors? Why will you win?
16. What's the biggest risk to this working in the real world?

## Scale
17. What breaks at 10,000 users?
18. How would you handle many documents / many users / real-time load?
19. What would you change in the architecture with another month?

## Ethics, safety, privacy
20. What data do you store, and for how long?
21. Could this be misused? How would you prevent it?
22. What happens when it's wrong in a high-stakes case?
23. Is there bias in the data or model? How would you check?
24. How do users consent / delete their data?

## "Why not X?"
25. Why not just use ChatGPT / Google / <incumbent> for this?
26. Why is AI needed here at all?
27. Why a web app and not <mobile / extension / bot>?
28. Why did you pick this problem over <adjacent problem>?

## Team and future
29. Will you keep working on this?
30. What would you do with the prize / credits?
31. What did each person build?

## Sponsor-specific (adapt per sponsor)
32. Why did you choose <sponsor product>? What would be hard without it?
33. What feature of <sponsor product> did you wish existed?
34. How would this scale on <sponsor product>?

## Answer formula
`<Direct answer>. <One piece of evidence or design choice>. <Optional next step>.`

Example (hallucinations): "We only answer from retrieved sources and cite them, and the schema forces it to say 'not in your notes' when retrieval scores are low. On 30 test questions we saw two unsupported claims; next step is a verifier pass."
