# Independent CLI case outputs

Reviewer: recover_spatial, independent of the CLI author. Requests: plans/directory-batch2-requests.md. These are actual responses to the six requests using the procedures. Fixture rows are proposed expected behavior, not observed application tests.

## CLI-001 — Single machine result

Consumer: An unattended caller needs exactly one result document for a successful batch.
Input contract: Propose UTF-8 JSON array input on standard input with explicit machine mode. Reject malformed input without prompting. Batch-item fields await the caller's schema.
Stream roles: Standard input carries the request; standard output carries the result document only. Standard error carries progress, warnings and errors for the human.
Result contract: Proposed envelope is an object with an items array in input order. Represent valid empty input by an empty array in that envelope. Finish the computation before emission where feasible; a truncated write is never accepted as a complete result.
Completion: Accept only a successful process outcome and exactly one valid schema-conforming document. Warnings may accompany success. On failure or interruption, reject even a parseable result and inspect diagnostics.
Fixtures: Ordinary array | one complete envelope | progress allowed | success. Empty array | empty envelope | optional progress | success. Invalid JSON | no result | explanation | failure. Output write interrupted | possibly truncated bytes | if deliverable | incomplete.
Evidence: Contract design only; no program or transport exercised.
Open questions: What item schema must consumers parse? What size limits affect buffering? Which runtime defines failure and interruption reporting?

## CLI-001 — Banner before payload

Consumer: Existing parser needs the established structured result without a text prefix.
Input contract: Preserve the existing input grammar; encoding, framing and empty-input semantics have not been supplied.
Stream roles: Remove the welcome banner from machine stdout. Send useful startup information and diagnostics to stderr when requested; do not merge streams when consuming the result.
Result contract: Preserve the existing payload schema and ordering. A visible banner is not a result record. Do not teach consumers to discard the first line: that could discard legitimate data when no banner appears.
Completion: Consumers check process outcome and parse the complete payload. A diagnostic banner alone does not indicate failure. Do not present a partial payload as successful.
Fixtures: Valid input | payload only | optional welcome | success. Warning | valid payload | warning | success if result meets contract. Invalid input | existing failure representation | explanation | failure. Human mode | explicitly documented human output | appropriate diagnostics | outcome unchanged.
Evidence: Reproducing the reported parser failure and capturing stdout/stderr independently remain pending; no installed command supplied.
Open questions: Which consumers depend on existing stdout? What payload and empty-result contract must stay compatible? Does the caller currently combine the channels?

## CLI-001 — Late item failure

Consumer: Caller needs to determine whether the entire batch finished after a prefix was emitted.
Input contract: Input framing and parser not supplied. Preserve the actual input boundary and identify the failing item by an appropriate supplied identifier if available.
Stream roles: Result bytes remain stdout data. Error context and recovery instructions go to stderr.
Result contract: With the reported prefix already delivered, do not promise rollback. Treat a single-document prefix as unusable. For explicitly agreed independent-record framing, retain completed records as provisional only under a caller-approved partial-consumption policy.
Completion: Report failure. Consumers requiring all-or-nothing completion must stage effects until successful terminal outcome and complete framing. Retrying after external side effects requires reconciliation; this output contract alone cannot guarantee safe replay.
Fixtures: Failure before first result | no accepted batch | failing item context | failure. Failure after valid prefix | prefix quarantined | remaining work incomplete | failure. Full success | valid complete batch | optional progress | success.
Evidence: Specification only. No input items, process, or emitted bytes were inspected.
Open questions: Which framing is in use? Are partial records independently useful? Have consumers already acted on them?

## CLI-002 — Option-like and spaced paths

Scope: Define a proposed token grammar for a file-processing command; this is not a claim about an installed parser.
Grammar: Proposed explicit end-of-options token is "--". After that boundary each nonempty token is one literal input operand; this operation accepts several ordered inputs. Reject unknown options before the boundary. Do not split a path containing whitespace.
Special inputs: No implicit stdin marker in this proposed mode; "-" after the delimiter is a literal filename. Reject missing operands before opening files.
Token cases: ["--","-draft.txt","annual report.txt"] => two inputs in that order. ["-draft.txt"] => unknown pre-boundary option. ["--","annual report.txt"] => one input. ["--"] => missing operands.
Invocation handling: Preserve these token boundaries in an argument vector. Verify target shell conventions separately if a shell-facing example is needed.
Evidence: Token cases specified only; no application, shell or files accessed.
Open questions: Is there an existing grammar to preserve? How should stdin be selected? Which invocation environments require examples?

## CLI-002 — Ambiguous dash

Scope: Distinguish an undocumented current behavior from a proposed unambiguous source-selection grammar.
Grammar: Existing "-" behavior is unknown. Proposed alternative: explicit "--stdin" selects the stream; "--" ends option parsing; exactly one source is required. Reject mixed sources and repeated stream selection.
Special inputs: Under this proposal, ["--","-"] names the literal file and ["--stdin"] reads stdin once. Empty input content is distinct from supplying no source. A lone pre-boundary "-" is rejected with guidance.
Token cases: ["--stdin"] => stream. ["--","-"] => file named dash. ["-"] => ambiguous spelling rejected. ["--stdin","--","-"] => conflicting sources rejected. [] => source missing.
Invocation handling: Verify the current parser/documentation and compatibility needs before adopting this proposal. No assumption that "--" already works.
Evidence: Proposed grammar only; existing command behavior has not been observed.
Open questions: Is stdin actually supported? Must a legacy dash invocation keep working? Which parser and version should be checked?

## CLI-002 — Untrusted literal helper operand

Scope: Specify parent-to-helper token transfer without constructing or executing a shell command.
Grammar: Fix the helper program identity in trusted configuration. Use the target runtime's verified literal argument-vector interface; pass the entire supplied path as one operand. Only insert an end-of-options marker if the helper's documented grammar supports it. Reject unsupported ambiguous inputs instead of guessing.
Special inputs: Do not interpret spaces, separators or expansion characters in literal filenames. Handle stdin or reserved marker names only through an explicit verified helper contract.
Token cases: Hypothetical helper grammar with "--" support: ["--","notes & drafts.txt"] => one operand; ["--","-notes;v2.txt"] => one operand; ["--","notes","&","drafts.txt"] => fails intended one-operand count. If helper literal mode is unverified, block option-like paths.
Invocation handling: Avoid a shell intermediary; verify actual runtime argument preservation and any secondary parsing performed inside the helper. Test a harmless argument-reporting fixture before allowing filesystem operations. Literal transport does not authorize access to the file.
Evidence: No invocation or filename executed. Inspect returned token count and exact content in an isolated process-boundary test before claiming the runtime preserves the vector.
Open questions: Which helper grammar applies? Does the runtime launch through a shell or wrapper? What source paths are authorized?

Review result: All six requests produced actionable channel/framing or operand contracts with observable tests and explicit execution boundaries. The procedures route separately: failures in result consumption belong to CLI-001; failures preserving a path's literal identity belong to CLI-002. No blocking finding. No actual CLI implementation, shell behavior, or cross-model portability was certified.
