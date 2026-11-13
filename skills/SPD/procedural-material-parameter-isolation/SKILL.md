---
id: SPD-002
name: procedural-material-parameter-isolation
domain: Spatial Asset Preparation
subdomain: Material diagnosis
version: 1.0
description: Design a controlled material comparison that isolates a procedural parameter from lighting, geometry, and rendering changes when a material behaves unexpectedly.
triggers: ["why did this material change", "isolate a shader parameter", "compare procedural materials", "debug a material look", "material looks different in another scene", "test material variation"]
not_for: ["spatial coordinate transfer [SPD-001]", "general configuration capture [TRP-006]", "final visual composition and art direction"]
requires: []
risk_level: low
---

# Procedural material parameter isolation

## Purpose
Produce a controlled comparison that tests whether a selected procedural material input explains an observed appearance change. Separate material behavior from lighting, geometry, coordinate mapping, and viewing conditions so the result supports a bounded diagnosis rather than a preferred-looking image.

## Inputs to collect
1. **Observed difference** — affected region and visible symptom, such as enlarged patches or changed highlight width. This defines what to compare. Default: ask for a concrete description or supplied comparison images.
2. **Material evidence** — parameter values, relevant dependency connections, coordinate source, and material revision. These establish the candidate cause. Default: unknown connections remain unknown rather than reconstructed from a screenshot.
3. **Comparison environment** — geometry, object scale, camera, lights, background, render settings, and display transform. These identify confounders. Default: preserve a supplied baseline; do not invent identical conditions.
4. **Candidate change** — one suspected parameter or explicitly named parameter interaction. This bounds the experiment. Default: choose a hypothesis only from available evidence and label it provisional.
5. **Evaluation criterion** — observable feature and comparison region. This defines the decision. Default: qualitative comparison with no fabricated numeric score.
6. **Execution capability** — access to a scene copy and renderer or only planning inputs. This determines the evidence available. Default: plan only, with no claim of rendered results.

If a required input is missing and has no safe default, ask in one message with at most three questions.

## Procedure
1. Describe the symptom without naming a cause; replace “broken shader” with an observable difference in a named region.
2. Confirm the visible surface's active material assignment and trace the candidate input through supplied connections to that material's output, distinguishing connected dependencies from guesses or unused controls.
3. Record a baseline condition including geometry scale, coordinate source, camera, lighting, render settings, and display conditions.
4. ⚠️ Separate variables that changed together in the reported example; do not attribute the difference to roughness, color, or pattern scale merely because its control was edited last.
5. Write a falsifiable hypothesis linking one candidate parameter to one observed feature while naming the controls that must remain fixed.
6. Specify a baseline and intervention pair using user-supplied or explicitly proposed values; change only the candidate parameter between that pair.
7. Choose inspection regions that include both the affected area and an unaffected control area, so an overall exposure change is not mistaken for a local material effect.
8. Run the paired comparison on a scene copy if authorized and available; otherwise provide exact conditions for a human or another capable agent to execute.
9. Record the actual comparison output, including unexpected changes, missing evidence, and settings that could not be held constant.
10. ⚠️ Interpret the result as support, contradiction, or inconclusive for the hypothesis; a visually preferable result does not demonstrate physical material accuracy.
11. If an interaction is plausible, design a separate follow-up comparison crossing the relevant settings while retaining the original baseline as a reference.
12. Deliver the comparison specification and bounded conclusion, preserving the original material rather than overwriting it with an unverified replacement.

Describe appearance with observable features: patch size relative to the surface, directional streaks, highlight extent, edge contrast, or repetition across the object. Avoid words such as realistic or premium as acceptance criteria unless the user supplies a reference and a way to judge the match.

Use `[VERIFY: parameter semantics and coordinate behavior in the documentation for the installed material system and rendering version]` before relying on tool-specific controls. Record the actual application and renderer versions if execution occurs. A numeric slider name alone does not establish its mathematical effect.

The following standalone Python 3 check verifies a fictional comparison table, not a rendered result. Record the interpreter version when executing it. Its purpose is to detect accidentally changed controls before spending time on a render.

```python
baseline = {"pattern": 4, "light": "L1", "mesh": "M1", "view": "V1"}
trial = {"pattern": 8, "light": "L1", "mesh": "M1", "view": "V1"}
changed = [key for key in baseline if baseline[key] != trial[key]]
assert changed == ["pattern"]
print("Only the declared pattern parameter differs")
```

## Decision rules
- IF lighting and material settings changed together THEN hold lighting fixed in a new comparison BECAUSE the original result cannot isolate the material change.
- IF object scaling changes the procedural pattern THEN inspect the coordinate source and mapping dependencies BECAUSE the effect may originate outside the exposed material control.
- IF no render or measured output exists THEN report a test specification and an untested hypothesis BECAUSE a planned intervention provides no observation.
- IF an unchanged render uses a disconnected input or inactive material THEN correct the test assignment before judging the parameter BECAUSE the comparison did not exercise the intended visible dependency.
- IF two inputs interact THEN compare their combinations in a follow-up BECAUSE one isolated change may not explain behavior at another setting.
- IF the desired look is achieved but the hypothesis remains untested THEN separate aesthetic selection from causal diagnosis BECAUSE preference does not establish which variable caused the difference.

## Output template
```text
Symptom: <visible feature and region; maximum two lines>
Hypothesis: <parameter, expected effect, and uncertainty; maximum three lines>
Controls: <held conditions and unresolved confounders; maximum six lines>
Comparison: <baseline and intervention values, inspection regions; maximum six lines>
Evidence: <actual observations and references, or not executed; maximum four lines>
Conclusion: <supported / contradicted / inconclusive / untested, with reason>
Follow-up: <next discriminating comparison; maximum three lines>
```

## Quality checklist
- [ ] The symptom describes an observable feature in a named region.
- [ ] The proposed cause is labeled as a hypothesis until evidence supports it.
- [ ] Baseline material and environment conditions are recorded separately.
- [ ] The initial pair changes only its declared candidate parameter.
- [ ] Coordinate source and object scale are included in control review.
- [ ] Inspection includes an affected region and a control region.
- [ ] Rendered observations are not invented when execution is unavailable.
- [ ] The conclusion distinguishes causal evidence from aesthetic preference.

## Anti-patterns
- **Everything at once**: several controls are changed until the material looks better. Fix: isolate the candidate change before interpreting cause.
- **Slider literalism**: a parameter's name is treated as proof of its behavior. Fix: inspect the relevant graph and verified documentation.
- **Lighting blindness**: appearance differences are attributed to the material while lights differ. Fix: preserve and record lighting conditions.
- **Screenshot certainty**: hidden node connections are inferred as fact. Fix: request connection evidence or label the dependency unknown.
- **Beauty as proof**: a pleasing render is called physically accurate. Fix: state only the supported appearance outcome and its reference conditions.

## Worked example
**Input:**
> Fictional artist Ivo reports larger surface patches on a ceramic prop after changing a pattern control from 4 to 8 and switching the light from L1 to L2. The material graph, geometry M1, coordinate source C1, and camera V1 are supplied and unchanged. No new render can be performed in this session. Ivo wants to test the pattern control rather than select a final look.

**Output:**
```text
Symptom: Surface patches appear larger on the front panel of the ceramic prop.
Hypothesis: Changing the pattern control from 4 to 8 may change patch size; direction and magnitude remain unverified.
Controls: Hold geometry M1, coordinates C1, camera V1, and light L1 fixed. Copy baseline render and display settings unchanged; confirm their actual values before execution.
Comparison: Baseline pattern 4 with L1; intervention pattern 8 with L1. Inspect front-panel patch size and a plain edge region for unrelated overall appearance changes.
Evidence: Not executed. The original report changed both pattern and lighting and cannot isolate the pattern effect.
Conclusion: untested; the comparison specification removes the reported lighting confound but supplies no new observation.
Follow-up: Render the controlled pair. If the original effect is not reproduced, compare L1 and L2 while holding pattern at 4, then investigate any interaction.
```

**Bad output:**
> Doubling the slider necessarily halves the patch size, so use 8 for a more realistic ceramic material.

This invents the control's mathematical behavior and substitutes aesthetic advice for the requested test.

## Edge cases
- **Randomized procedural output** — preserve the random seed or record repeated comparisons; do not treat uncontrolled variation as a parameter effect.
- **Different viewing transforms** — compare under the same confirmed viewing conditions before interpreting changes in contrast or color.
- **Animated materials** — fix the comparison time and animation state, then test another time separately if the effect depends on motion.
- **Only final images available** — offer a hypothesis list and discriminating tests; do not invent hidden parameter settings.

## Test case
**Input:**
> A fictional artist changes roughness and light size together and reports a wider highlight. The artist cannot provide the node graph and asks which material value is definitely responsible.

**Assertions:**
1. Declines to assign definite causation from the confounded comparison.
2. Specifies a paired comparison holding light size and other relevant controls fixed.
3. Marks missing graph connections and parameter semantics as unresolved.
4. Defines highlight extent in a named region as an observation rather than promising physical accuracy.
