---
id: CLI-001
name: command-machine-stream-contract
domain: Command-Line Interaction Contracts
subdomain: Stream contracts
version: 1.0
description: Define machine-readable command input, result, diagnostic, and completion behavior when a command must work reliably in pipelines and unattended jobs.
triggers: ["make command output parseable", "separate results from progress logs", "design CLI JSON output", "specify piped command behavior", "handle partial command output", "test a machine output mode"]
not_for: ["HTTP response contract design [TAP-001]", "pipeline checkpoint recovery [TDE-005]", "literal filename parsing [CLI-002]", "implementing a particular shell integration"]
requires: []
risk_level: medium
---

# Command Machine Stream Contract

## Purpose
Define what a downstream program can consume and how it can tell complete success from partial or failed work. The output is an explicit input/output contract and test fixture, rather than an assumption that human-readable console output is suitable for automation.

## Inputs to collect
1. **Consumer task** — identify the program or person consuming results and whether streaming is necessary. This determines framing and completion needs. Default: one machine consumer; streaming requirements remain unresolved.
2. **Input grammar** — collect input encoding, framing, required fields, and malformed-input handling. This defines accepted data. Default: no inferred format; ask for an example and schema.
3. **Result meaning** — identify result records, ordering requirements, empty success, and partial results. This prevents incomplete output looking complete. Default: partial output cannot be treated as complete success.
4. **Diagnostic needs** — identify warnings, progress messages, and actionable failures. This determines what must remain outside machine results. Default: concise human diagnostics on a separate channel.
5. **Completion policy** — collect success criteria, failure classes, and documented status conventions. This tells consumers what to check. Default: propose named outcomes without inventing application-specific numeric codes.
6. **Runtime context** — identify actual interpreter, operating system, shell, and invocation method. This determines what can be tested. Default: contract preparation only; no claimed subprocess execution.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Name the machine mode explicitly and state whether it is selected by an option, a separate command, or another supplied interface choice. Do not silently change payload shape when output is redirected.
2. Specify one input grammar, including encoding, record boundaries, empty input, and validation failures. Keep interactive prompting out of unattended operation unless a separate explicit interactive mode is selected.
3. Assign result records to the result stream and progress, warnings, and explanations to the diagnostic stream. Define standard input, standard output, and standard error roles in the contract instead of relying on the appearance of a terminal.
4. ⚠️ Choose framing from the consumer requirement: one complete document or a sequence of independently framed records. Do not mix an opening document fragment with free-form status lines and call the result valid structured output.
5. Specify the schema, required fields, optional fields, and ordering rules. If order has no meaning, say so; if consumers require order, include the ordering key or guarantee that makes it testable.
6. Define empty success separately from no output caused by failure. State whether partial records may be emitted before failure and how consumers must handle them.
7. Define completion evidence using process outcome plus any required completion record. A parseable prefix cannot establish that the entire job succeeded.
8. ⚠️ Separate warning severity from process outcome. A diagnostic message does not necessarily mean failure, and an empty diagnostic stream does not establish success.
9. Specify cancellation and early-consumer-closure behavior for the actual runtime. Use `[VERIFY: process exit, stream closure, buffering, and interruption behavior in the installed runtime and shell documentation]` before assigning platform-specific details.
10. Build fixtures for ordinary input, empty input, malformed input, warning with success, and failure after partial output. Inspect result bytes, diagnostic bytes, and completion outcome independently.
11. Deliver the contract and actual observed test evidence, or label unexecuted tests pending. Preserve existing compatibility requirements when changing a command already used by consumers.

The following Python 3 fixture checks a proposed single-document result contract. It uses an in-memory output function, not a subprocess or real shell. Save and run it with the available Python 3 interpreter; record the actual version. Its passed assertions do not establish platform behavior or implementation correctness outside this fixture.

```python
import io
import json

def emit(records, result, diagnostic):
    json.dump({"records": records}, result)
    result.write("\n")
    diagnostic.write("Finished preparing result\n")

result, diagnostic = io.StringIO(), io.StringIO()
emit([{"id": "A"}], result, diagnostic)
assert json.loads(result.getvalue()) == {"records": [{"id": "A"}]}
assert "Finished" not in result.getvalue()
assert diagnostic.getvalue().startswith("Finished")
print("Result and diagnostic separation passed")
```

## Decision rules
- IF progress text would enter the machine result stream THEN move it to the diagnostic channel BECAUSE otherwise a consumer must guess which bytes are data.
- IF a command can fail after emitting records THEN specify partial-result handling and terminal outcome checks BECAUSE valid records alone do not prove complete processing.
- IF empty input is valid THEN define an explicit empty-success representation BECAUSE silence cannot distinguish that case from an early failure.
- IF a warning does not invalidate the promised result THEN preserve success while reporting the warning separately BECAUSE message presence and failure are different signals.
- IF runtime behavior has not been exercised THEN leave its evidence pending BECAUSE an in-memory fixture does not test process boundaries.

## Output template
```text
Consumer: <task and mode; one sentence>
Input contract: <encoding, framing, validation; up to four lines>
Stream roles: <input, results, diagnostics; up to four lines>
Result contract: <schema, ordering, empty and partial cases; up to six lines>
Completion: <success, warning, failure, interruption; up to four lines>
Fixtures: <case | expected results | diagnostics | outcome; up to six rows>
Evidence: <performed checks and limits, or pending>
Open questions: <up to three blocking questions>
```

## Quality checklist
- [ ] Input and output framing are explicitly defined.
- [ ] Machine results exclude free-form progress and explanations.
- [ ] Empty success has a representation distinct from failure.
- [ ] Partial-output handling is defined before consumption.
- [ ] Consumers inspect completion outcome rather than parseability alone.
- [ ] Warning behavior does not silently redefine success.
- [ ] Runtime-specific claims have verification evidence or placeholders.
- [ ] Test reports distinguish in-memory checks from actual process execution.

## Anti-patterns
- **Console scraping**: Consumers delete lines that look like progress. Fix: establish separate machine and diagnostic channels.
- **Parseable means done**: A valid early record is accepted as a complete export. Fix: require the declared completion evidence.
- **Silent empty case**: No bytes are assumed to mean no matches. Fix: define empty success and failure separately.
- **Warning equals error**: Any diagnostic text fails the job. Fix: document outcome independently from informational messages.
- **Terminal-only confidence**: Pretty output is treated as pipeline verification. Fix: capture and inspect each stream under the intended invocation.

## Worked example
**Input:**
Fictional team Cedar exports a catalog to one consumer. The supplied requirement is a single JSON document with a records list. Empty catalogs are valid. The consumer must reject partial exports. Progress is useful to a human operator. No real command is available for execution.

**Output:**
```text
Consumer: Cedar's automation consumes the explicit machine mode as one complete catalog document.
Input contract: Input format is not supplied; obtain the catalog source and validation rules before implementation.
Stream roles: Standard input reserved for the declared input if applicable. Standard output contains only the JSON result. Standard error contains operator diagnostics.
Result contract: One object with required records list; empty success is {"records": []}. Ordering requirement unresolved. Partial output must not be accepted as a complete export.
Completion: Consumer accepts only a complete valid document and documented successful process outcome. Warnings may accompany success. Failure or interruption rejects the export.
Fixtures: ordinary catalog | records document | optional progress | success
empty catalog | empty records list | optional progress | success
source failure | no accepted complete export | failure explanation | failure
interrupted output | discard partial document | diagnostic if possible | not success
Evidence: Contract only; no process, shell, or real exporter was tested.
Open questions: What input source and grammar apply? What record order is required? What existing status conventions must remain compatible?
```

**Bad output:**
“Print Starting export, then the JSON, then Done; the consumer can strip the extra lines and assume success if parsing works.”
This makes data framing ambiguous and loses the distinction between complete and interrupted output.

## Edge cases
- **Consumer closes early** — document the runtime-specific outcome and resource cleanup; do not infer successful production of the full dataset.
- **Diagnostic channel unavailable** — preserve machine framing and report diagnostic loss through the agreed outcome mechanism rather than injecting prose into data.
- **Very large results** — choose streaming only with an explicit record and completion protocol; do not silently switch format based on size.
- **Schema change** — preserve the documented compatibility boundary and provide a consumer migration test before altering required fields.

## Test case
**Input:**
> Fictional exporter Pine emits valid records, then encounters unreadable input and stops. Its progress message was written between records on standard output. The consumer currently accepts every parseable record as a successful full export. Specify the corrections.

**Assertions:**
1. Moves progress text outside the result stream.
2. Defines partial-result handling and a completion outcome check.
3. Does not equate parseable records with full-export success.
4. Leaves untested runtime behavior explicitly pending.
