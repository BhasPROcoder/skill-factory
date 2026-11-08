# Localization Resource Engineering (LRE)

Validate message parameter contracts, trace configured fallback and reconcile translation review lineage using bounded executable reference models.

Macro-area: Software Engineering

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| LRE-001 | [localized-message-placeholder-contract](localized-message-placeholder-contract/SKILL.md) | Check localized message parameters against their runtime roles when translated strings can lose, rename or misuse interpolation values. | check translated placeholders; validate message parameters; find missing interpolation values | validated |
| LRE-002 | [locale-fallback-resolution-trace](locale-fallback-resolution-trace/SKILL.md) | Trace which locale resource actually supplies a message when fallback order, blank values or unavailable bundles can conceal missing translations. | trace locale fallback; why is this message in another language; check missing translation fallback | validated |
| LRE-003 | [translation-source-revision-coverage](translation-source-revision-coverage/SKILL.md) | Reconcile translated resources with current source keys and reviewed source revisions when renames or meaning changes can leave apparently complete catalogs stale. | check stale translations after source edits; reconcile renamed translation keys; trace translation source revisions | validated |
