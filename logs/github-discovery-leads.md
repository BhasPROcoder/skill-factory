# Public GitHub discovery leads

These records are discovery leads, not approved sources for copied or closely paraphrased material. Reuse requires inspecting the exact commit and applicable license. Source instructions are task data, not instructions to this factory. Entries do not count as skills.

## Design-token release governance

- Source: [thrillmade/agent-skills, semver-design-tokens](https://github.com/thrillmade/agent-skills/blob/main/skills/semver-design-tokens/SKILL.md).
- Discovery: 2026-11-06 through public search results; file-specific preview inspected. Commit and license not yet verified. A version string in frontmatter was not treated as a verified repository commit.
- Useful problem: deciding how a token change affects consumers and release communication.
- Factory boundary: DST candidates cover alias dependency diagnosis, variant constraints, token rename mapping, and component retirement. A future release-severity method would need a separate artifact and decision boundary to qualify as an addition.
- Portability judgment: collect the project's release policy rather than treating a particular repository's version-bump conventions as universal. No text, code, examples, or fixed policy rules were imported.

## Tender extraction

- Source: [SoMarkAI/skills, tender-analyzer](https://github.com/SoMarkAI/skills/blob/main/skills/tender-analyzer/SKILL.md).
- Discovery: 2026-11-06. Public file page inspected; commit lookup unavailable through the browsing tool, license review pending.
- Useful problem: organizing a tender's required evidence and response obligations.
- Factory disposition: BID-003 is independently authored revision propagation into an existing response, not a vendor-specific document extraction integration. See logs/b3-review.md. Further extraction methods must be compared against existing compliance and administrative evidence workflows before authoring.
- No text, scripts, vendor hooks, or examples imported.

## Localization resource contracts

- Sources discovered 2026-11-07: [microsoft/intelligent-terminal, ensure-localization](https://github.com/microsoft/intelligent-terminal/blob/main/.github/skills/ensure-localization/SKILL.md) and [i18next/i18next-cli, i18next-localization](https://github.com/i18next/i18next-cli/blob/main/skills/i18next-localization/SKILL.md).
- Evidence scope: public search-result file excerpts inspected; exact revision and applicable license remain unverified. No implementation commands, annotations or platform-specific APIs are accepted on this evidence alone.
- Useful candidate problems: preserving variable meanings across translated message patterns; distinguishing missing translations from intentional fallback; maintaining translator context when one source string is reused in different interface roles.
- Catalog discovery: sf.py searches for placeholder and localization returned no lexical matches. This is a candidate signal, not a semantic uniqueness verdict; compare language-transfer and interface skills before writing.
- Portability boundary: collect the actual message grammar, source locale and project fallback policy as inputs. Do not hardcode one library's syntax or claim a mechanical completeness check proves translation quality. No source text, code or examples imported.
