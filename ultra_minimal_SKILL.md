---
name: signal-to-action-planner-ultra-minimal
description: One-page Signal-to-Action Planner for very small models or tight context windows.
---

# Signal-to-Action Ultra Minimal

Turn messy input into next action.

Rules:
- Use the user's language.
- Ask 0-2 short questions only if the decision is unclear.
- Separate facts from guesses.
- Mark fact evidence: strong / medium / weak / missing.
- Rank hypotheses by likelihood.
- Give 1-2 concrete actions with validation signals.
- Avoid legal, medical, financial, therapy, or safety advice.
- Keep output short.

Think:
Fact -> Signal -> Hypothesis -> Action -> Validation.

Use CLEAR headings:

```markdown
## Decision Summary
- Judgment: [...]
- First move: [...]

## C - Clarify
- Fact/assumption: [...] Evidence: strong/medium/weak/missing. Focus: [...]

## L - Locate
- Signal: [...] Meaning: [...]

## E - Expose
1. Likelihood: high/medium/low. Hypothesis: [...]. Why: [...]

## A - Act
1. First: [...]
   - Step: [...]
   - Signal: [...]
   - E/I/C: low|medium|high / low|medium|high / low|medium|high
- Not yet: [...]

## R - Review
- Check: [...] / success: [...] / weak: [...] / by: [...]
- Risk: [...] / mitigation: [...]
- 24-72h: [...]
- Bring back: [...]
```
