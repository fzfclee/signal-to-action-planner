# Output Templates

## A. Standard Output Template

```markdown
# Signal-to-Action Output

## 1. Situation Summary
Briefly summarize the user's situation in plain language.

## 2. Key Facts
List observable facts from the user's input. Do not mix facts with interpretation.

## 3. Evidence Check
Classify evidence as:
- Strong evidence
- Medium evidence
- Weak evidence
- Missing / uncertain evidence

## 4. Signals That Matter
Identify the signals that deserve attention. Explain why each signal matters.

## 5. Possible Implications
Explain what the signals may imply. Mark uncertainty clearly.

## 6. Working Hypotheses
Generate 2-3 testable hypotheses.

Each hypothesis should follow this pattern:
If [action / condition] happens in [context], then [observable change] should happen, because [assumed mechanism].

## 7. Priority Action Plan
Rank 1-3 actions by priority.

For each action, include:
- Action
- Why this action
- What evidence it tests
- Expected signal
- Risk / caution

## 8. Validation Plan
For each top-priority action, define:
- What to observe
- Success signal
- Weak / negative signal
- Suggested time window

## 9. What Not To Do Yet
List actions that are premature, risky, or unsupported by evidence.

## 10. Final Note
Remind the user that the output supports clearer action and validation, but the user remains responsible for decisions.
```

## B. Compact Output Template

```markdown
# Compact Signal-to-Action Output

## Situation
## Facts
## Evidence Check
## Signals
## Hypotheses
## Top 3 Actions
## Validation Points
## Not Yet
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
- Include one optional free-text choice.
- Keep the question easy to answer.
- Do not turn clarification into a long form.
```
