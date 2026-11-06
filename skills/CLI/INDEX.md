# Command-Line Interaction Contracts (CLI)

Specify machine streams, completion evidence, literal operands and argument boundaries for command-line tools.

Macro-area: Software Engineering

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| CLI-001 | [command-machine-stream-contract](command-machine-stream-contract/SKILL.md) | Define machine-readable command input, result, diagnostic, and completion behavior when a command must work reliably in pipelines and unattended jobs. | make command output parseable; separate results from progress logs; design CLI JSON output | validated |
| CLI-002 | [literal-operand-parsing-contract](literal-operand-parsing-contract/SKILL.md) | Specify how a command distinguishes options from literal operands when filenames, spaces, delimiters, and standard-input markers could otherwise change their meaning. | handle filenames starting with a dash; design command operand parsing; test CLI argument boundaries | validated |
