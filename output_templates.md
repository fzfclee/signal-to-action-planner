# Output Templates

## A. Standard Output Template

```markdown
# Signal-to-Action Output

Language:
Use one language consistently. Match the user's dominant language or the language required by system / project instructions. Do not mix languages except for user-provided terms, technical identifiers, or proper nouns.

Display depth:
Default to concise reasoning. Do not ask the user to choose output detail level at the start. Show detailed reasoning only when the user explicitly requests it, such as with `--detailed`, "show reasoning", or similar wording.

Structure:
- Facts, Evidence, And Signals = what is known and why it matters.
- Implications And Working Hypotheses = compressed middle reasoning.
- Priority Action Plan = what to do and why.
- Validation Plan = how to judge whether actions worked.
- Action Roadmap = sequence, timing, and decision gates.
- Keep these sections MECE and avoid repeating the same content across them.

## 1. Situation Summary
Briefly summarize the user's situation in plain language.

## 2. Facts, Evidence, And Signals
Combine observable facts, fact evidence strength, and key signals in one compact section.

For each item, include:
- Fact or signal
- Fact evidence strength: strong / medium / weak / missing
- Signal or implication confidence when the item includes interpretation
- Why it matters, in one short phrase

Split compound items when a directly supported fact and a strategic inference have different certainty levels. Do not downgrade a directly stated fact just because the implication is uncertain.

Do not repeat the same fact in a separate evidence section.

## 3. Implications And Working Hypotheses
Compress the middle reasoning. Show only the implications and hypotheses that change the action plan.

Generate 2-3 concise testable hypotheses, ranked from most likely to least likely based on current evidence.

For most hypotheses, include only:
- Likelihood: high / medium / low / unknown
- Hypothesis
- Evidence basis, in one short sentence
- Confidence note when strong facts support only a medium or low-confidence inference

Expand only the most important or most uncertain hypothesis with:
- What would increase confidence
- What would weaken confidence

## 4. Priority Action Plan
Rank 1-3 MECE actions by priority. Make the order explicit: Priority 1 is what to do first, Priority 2 is what to do next, and Priority 3 is what to do after that if still needed.

For each action, include:
- Action
- Why this action
- What evidence it tests
- Expected signal
- Risk / caution

## 5. Validation Plan
Define how to judge whether each prioritized action worked. Do not repeat the action description. For each top-priority action, define:
- What to observe
- Success signal
- Weak / negative signal
- Suggested time window

## 6. What Not To Do Yet
List actions that are premature, risky, or unsupported by evidence.

## 7. Action Roadmap
Localize this heading to the user's language, such as "行动路线" for Chinese output.

Give the user a concise sequence and decision gates. Do not repeat the full validation plan:
- First: [highest-priority action]
- Next: [second action]
- Then: [third action or contingency]
- Decision point: [what evidence should trigger a change in direction]

End with one short note: the output supports clearer action and validation, while the user remains responsible for decisions.

Optionally add one subtle line: this is a lightweight slice of a broader signal-to-action method. Do not pitch, explain, or introduce extra modules unless the user asks.
```

## B. Compact Output Template

```markdown
# Compact Signal-to-Action Output

## Situation
## Facts, Evidence, And Signals
## Implications And Hypotheses
## Top 3 Actions
List MECE actions in priority order.
## Validation Points
## Not Yet
## Action Roadmap
```

## C. Dynamic Clarification Questions Template

```markdown
## Clarification Questions

Use this only when the current input is not clear enough to produce a useful Signal-to-Action output.

Reason for asking:
[State the specific missing piece: decision, fact, evidence, implication, hypothesis, action, or validation.]

Question:
[Ask 1 tailored question based on the user's actual words.]

Answer options:
A. [Short option]
B. [Short option]
C. [Short option]
D. Other / more context: ...

Rules:
- Prefer 2-4 options.
- Include a skip / not sure option when asking a dynamic intake question.
- Include one optional free-text choice.
- Keep the question easy to answer.
- Do not turn clarification into a long form.
```

## D. Detailed Reasoning Mode Template

```markdown
## Detailed Reasoning Mode

Use this only when the user explicitly asks for detailed reasoning, such as with `--detailed`, "show reasoning", "explain the reasoning", or similar wording.

Do not ask a detail-level question at the start of a run.
```

## E. Decision Focus Check Template

```markdown
## Clarification Question

To make the action plan useful, what decision do you most want to clarify first?

A. [Likely decision focus from the user's input]
B. [Alternative decision focus from the user's input]
C. [Evidence / validation focus]
D. Other / more context: ...
```

Use this before the 7-section output unless the user explicitly asks to skip questions or continue to output.

## F. Mid-Process Checkpoint Template

```markdown
## Clarification Question

Reason for asking:
[State why this intermediate result changes the roadmap.]

Question:
[Ask 1 short question tied to evidence, hypothesis ranking, or roadmap constraints.]

Answer options:
A. [Short option]
B. [Short option]
C. [Short option]
D. Other / more context: ...
```

## G. Dynamic Intake Loop Template

```markdown
## Clarification Question

To make the roadmap more accurate, I will ask one question at a time. You can choose skip / not sure or say "continue".

Question [number]:
[Question tailored to the user's latest answer and remaining uncertainty]

A. [Short option]
B. [Short option]
C. [Short option]
D. Skip / not sure.
E. Other / more context: ...

Rules:
- Ask one question per message.
- Choose the next question based on the user's latest answer.
- Aim for 3 questions for simple cases.
- Ask 4-5 questions only when uncertainty is high.
- Every question must include skip / not sure.
- The user may say "continue" at any time.
```
