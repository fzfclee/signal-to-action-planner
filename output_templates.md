# Output Templates

## A. Standard Output Template

```markdown
# Signal-to-Action Output

Language:
Use one language consistently. Match the user's dominant language or the language required by system / project instructions. Do not mix languages except for user-provided terms, technical identifiers, or proper nouns.

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
Generate 2-3 testable hypotheses, ranked from most likely to least likely based on current evidence.

Each hypothesis should follow this pattern:
If [action / condition] happens in [context], then [observable change] should happen, because [assumed mechanism].

For each hypothesis, include:
- Likelihood: high / medium / low / unknown
- Evidence basis
- What would increase confidence
- What would weaken confidence

## 7. Priority Action Plan
Rank 1-3 actions by priority. Make the order explicit: Priority 1 is what to do first, Priority 2 is what to do next, and Priority 3 is what to do after that if still needed.

For each action, include:
- Action
- Why this action
- What evidence it tests
- Expected signal
- Risk / caution
- How to validate it

## 8. Validation Plan
Summarize validation across the prioritized actions. For each top-priority action, define:
- What to observe
- Success signal
- Weak / negative signal
- Suggested time window

## 9. What Not To Do Yet
List actions that are premature, risky, or unsupported by evidence.

## 10. Roadmap
Give the user a concise sequence:
- First: [highest-priority action and validation]
- Next: [second action and validation]
- Then: [third action or contingency]
- Decision point: [what evidence should trigger a change in direction]

## 11. Final Note
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
Rank hypotheses from most likely to least likely. Include likelihood and evidence basis.
## Top 3 Actions
List in priority order and include validation for each action.
## Validation Points
## Not Yet
## Roadmap
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

## D. Decision Focus Check Template

```markdown
## Clarification Question

To make the action plan useful, what decision do you most want to clarify first?

A. [Likely decision focus from the user's input]
B. [Alternative decision focus from the user's input]
C. [Evidence / validation focus]
D. Other / more context: ...
```

## E. Mid-Process Checkpoint Template

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
