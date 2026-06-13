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

CLEAR = Clarify the Facts, Locate the Signal, Expose the Opportunity, Act on Evidence, Review the Evidence.

Use CLEAR headings:

```markdown
## Decision Summary
- Judgment: [...]
- First move: [...]

## C - Clarify the Facts
- Fact/assumption: [...] Evidence: strong/medium/weak/missing. Focus: [...]

## L - Locate the Signal
- Signal: [...] Meaning: [...]

## E - Expose the Opportunity
1. Working hypothesis 1 / 假设 1: likelihood high/medium/low. Hypothesis: [...]. Why: [...]

## A - Act on Evidence
1. First: [...]
   - Step: [...]
   - Signal: [...]
   - E/I/C: low|medium|high / low|medium|high / low|medium|high
- Not yet: [...]

## R - Review the Evidence
- Check: [...] / success: [...] / weak: [...] / by: [...]
- Risk: [...] / mitigation: [...]
- 24-72h: [...]
- Bring back: [...]
```
