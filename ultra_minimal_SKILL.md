---
name: signal-to-action-planner-ultra-minimal
description: One-page Signal-to-Action Planner for very small models or tight context windows.
---

# Signal-to-Action Ultra Minimal

Turn messy input into next action.

CLEAR:
- C — Clarify：区分事实与假设，把混乱输入拆清楚
- L — Locate：定位真正的信号，识别重复出现的张力、行为变化或风险
- E — Expose：暴露可能的机会，判断信号属于哪个场景、影响谁、痛点是什么
- A — Act：定义下一步有依据的行动，足够小可以学习，足够准可以改变判断
- R — Review：审视证据标准，知道什么结果说明继续、调整还是停止

Rules:
- Use the user's language.
- Ask 0-2 short questions only if the decision is unclear.
- Separate facts from guesses.
- Mark evidence: strong / medium / weak / missing.
- Rank hypotheses by likelihood.
- Give 1-2 concrete actions, not generic advice.
- Add validation: success signal, weak signal, time window.
- Add 1 risk and mitigation.
- Avoid legal, medical, financial, therapy, or safety advice.
- Keep output short.

Think:
Fact -> Signal -> Hypothesis -> Action -> Validation.

Output:

```markdown
## Situation
[1 sentence.]

## Facts And Signals
- [fact/signal] Evidence: strong/medium/weak/missing. Meaning: [...]

## Hypotheses
1. [most likely] Likelihood: high/medium/low. Why: [...]
2. [optional]

## Actions
1. First: [...]
   - Step: [...]
   - Expected signal: [...]
   - Effort / Impact / Confidence: low|medium|high / low|medium|high / low|medium|high
2. Next: [...]

## Validation
- Check: [...] / success: [...] / weak: [...] / by: [...]

## Risk
- Risk: [...] / mitigation: [...]

## Roadmap
- 24-72h: [...]
- Then: [...]
- Bring back: [...]
```
