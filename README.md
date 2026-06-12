# Signal-to-Action Planner

Turn messy signals into prioritized action and validation.

Signal-to-Action Planner is a lightweight public Skill that helps users turn messy input, stories, observations, and evidence into prioritized actions and validation plans.

## What It Does

This Skill helps users turn messy stories, observations, meeting notes, customer feedback, work signals, or uncertain situations into a prioritized action plan and a practical validation plan.

It guides the user through a simple reasoning chain:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Evidence is applied across the whole process. Every claim, signal, implication, hypothesis, and action should be grounded in evidence or marked as uncertain.

## What It Does Not Do

This Skill does not make decisions for the user.
It does not provide legal, medical, financial, psychological, or safety advice.
It does not replace professional judgment.
It does not guarantee outcomes.
It does not collect feedback or build a pattern library.

## How To Use

1. Copy `SKILL.md` into your AI assistant.
2. Paste your messy situation / story / observations.
3. Let the Skill ask a few clarification questions if needed.
4. Receive a structured Signal-to-Action output.
5. Use the top-priority actions and validation points to decide what to do next.

## Example Input

```text
I had several conversations with potential users. Some said the idea is interesting, but nobody has committed to a follow-up. I am not sure whether this is real demand or just polite feedback. I need to decide what to do next.
```

## Example Output Preview

```markdown
## Priority Action Plan
1. Test whether interest is real by asking for one concrete next commitment.
2. Identify whether the current message is too abstract by testing a narrower use case.
3. Reduce ambiguity by separating polite feedback from behavioral evidence.

## Validation Plan
- If at least 2 people agree to a concrete next step, the demand signal strengthens.
- If people continue to praise but avoid action, treat the signal as weak.
```
