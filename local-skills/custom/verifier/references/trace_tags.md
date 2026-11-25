# Trace tags

Every number that reports a result, a statistic, a count, or a figure from another paper must carry a trace tag in the draft. Tags are stripped when building the final PDF (paper-writer/review-submit handle that); in LaTeX define `\newcommand{\rosnum}[2]{#1}` so they render as the bare value.

| Kind | Markdown | LaTeX | Checked against |
|---|---|---|---|
| Own result | `{{0.83\|R20261028-120000-abc123:accuracy}}` | `\rosnum{0.83}{R20261028-120000-abc123:accuracy}` | `results/<run_id>/metrics.json` key (dotted path allowed) |
| Own result from CSV row | `{{0.83\|R…:acc@model=bert}}` | same | `metrics.csv` column `acc` in the row where `model == bert` |
| Number from a cited paper | `{{72%\|S-0004:p5}}` | `\rosnum{72\%}{S-0004:p5}` | source exists; support checked by the claims pass |
| Review statistic | `{{0.68\|state:screening.stages.full_text.kappa_human_ai}}` | same | value in `research_state.json` |
| PRISMA count | `{{57\|prisma:included}}` | same | `screening/prisma.json` |
| Design constant | `{{3\|D-007}}` | same | decision exists in the log (e.g. "3 conditions") |

Matching: the text value is compared at its displayed precision. `0.83` matches `0.8312`; `83.1%` matches `0.8312`; `0.84` does not.

Runs must be `complete` in `registry/runs.jsonl`. A run that was superseded or failed fails the check.

Untagged numbers that are fine: years, section/table/figure/equation/appendix numbers, RQ/H labels, list markers, numbers inside math, code, URLs and citation keys. Everything else is reported as untagged.
