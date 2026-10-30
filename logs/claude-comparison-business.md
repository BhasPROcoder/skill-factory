# Business and artifact workflow migration review

The coordinator read all twenty-five assigned source skills and compared their procedures with the existing library. Source instructions were treated as material, not authorization to contact people, install software, change accounts, or retain personal business details. The exact source-to-destination mapping is in `staging/claude_business_mapping.json` and the generated migration table.

Fifteen distinct additions cover transcript behavior, regional access, community operations, workbook/document/presentation/PDF creation and editing, decision journals, delegation acceptance, initiative continuation, bottom-up market sizing, primary-metric guardrails, daily briefings, package negotiation, and offer packaging. Existing skills cover competitor comparison, discovery, case studies, cohorts, experiments, campaign delivery, content repurposing, difficult workplace messages and bounded pilot scoping. Portfolio management combines existing capacity and calendar procedures with the new continuation gate rather than creating another capacity synonym.

## Procedure and evidence review

The coordinator read all fifteen new task records, their procedures, conditions, fictional inputs and concrete artifacts. The four artifact workflows initially described review only. They were expanded to create or edit the requested output, select compatible available tooling, save and reopen it, and verify calculations or rendered pages as appropriate. Their text examples are explicit specifications or mock-ups, not invented claims that binary files were produced. Runtime tool availability remains an input. They do not depend on a named vendor skill or guessed library function.

The fictional workbook calculation is 3 times 4 = 12; its zero-quantity boundary is 0. The fictional market segments are explicitly disjoint: 40 + 60 = 100; 100 buyers times 10 currency units times one annual purchase = 1000 annual currency units. Two purchases under the same assumptions yield 2000. The builder executes these arithmetic assertions. Potential spending is not forecast revenue, and no real market counts or prices are asserted.

The meeting workflow does not infer speaking duration or interruptions from an untimed transcript. The daily brief does not treat an acknowledgment as resolution. The regional workflow tests actual access and buying roles instead of assigning preferences from geography. The negotiation workflow trades scope under actual authority, distinct from reviewing contract clauses. The offer workflow requires supported proof and controllable deliverables, distinct from merely arranging marketing messages.

## Removed assumptions

Removed source-specific companies, cities, personal schedules, fixed posting frequencies, mandatory demographic channels, arbitrary pricing and retention targets, guaranteed outcomes, unsupported conversion statistics, purported universal sample-size rules, score-based shutdown thresholds, and vendor invocation commands. Current legal, platform, recipient and application requirements are verification inputs. Quantities in retained examples are explicitly fictional and internally checked. No external source claim was presented as verified current fact.

## Validation and limits

`sf.py validate --file` emitted PASS for each of the fifteen CBG files after the creation/editing scope repair. Registry validation then emitted 15/15 passed and marked those entries validated. This is structural validation plus source/example review, not a rendered office-file test, professional certification, or execution by every AI agent. Existing counterparts were inspected selectively by actual procedure, not merely title; the mapping is a reasoned coverage assessment rather than a promise that every incidental source instruction is preserved.

The original source folders are eligible for removal only after the combined migration check finds a validated destination for every source. Raw source files and personal details are not copied into this repository.
