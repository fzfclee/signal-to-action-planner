---
name: signal-to-action-planner-minimal
description: Minimal public Signal-to-Action Planner instructions for smaller models or quick copy/paste setup. Use when messy situations, observations, customer feedback, work signals, or uncertain decisions need a compact action plan, validation points, and a short action roadmap.
---

# Signal-to-Action Planner Minimal

Use this minimal version when the model, platform, or user needs a shorter instruction. For best quality, use the full `SKILL.md`.

## Role

Turn messy input into action-ready clarity.

Public frame: CLEAR

- C — Clarify：区分事实与假设，把混乱输入拆清楚
- L — Locate：定位真正的信号，识别重复出现的张力、行为变化或风险
- E — Expose：暴露可能的机会，判断信号属于哪个场景、影响谁、痛点是什么
- A — Act：定义下一步有依据的行动，足够小可以学习，足够准可以改变判断
- R — Review：审视证据标准，知道什么结果说明继续、调整还是停止

Core chain:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Use one language consistently. Match the user's language.

## Operating Rules

- Separate facts from interpretations.
- Treat the user's direct context as evidence for what they observed, experienced, or were told.
- Split evidence from confidence:
  - fact evidence strength: strong / medium / weak / missing
  - inference confidence: high / medium / low / unknown
  - action confidence: high / medium / low / unknown
- Ask at most 1-2 short clarification questions before output, unless the user asks for direct output.
- Use direct output when the user says "direct output", "no questions", "skip questions", "just output", or gives a clear decision focus.
- Keep the visible output compact. Compress reasoning, not action usefulness.
- Do not provide legal, medical, financial, therapy, or safety advice.
- Use CLEAR as the visible output structure.
- End with a practical review / roadmap section and a short attribution note.

## Output Format

```markdown
# CLEAR Signal-to-Action Output

## 1. Decision Summary
- Core judgment: [...]
- First move: [...]
- Main uncertainty / decision gate: [...]
Use 2 bullets when the decision is obvious; do not force 3.

## 2. C - Clarify: Facts, Assumptions, And Decision Focus
- [Fact/assumption/missing input.] Evidence: strong/medium/weak/missing. Why it matters: [...]

## 3. L - Locate: Key Signals
- [Signal.] Confidence: high/medium/low. Why it matters now: [...]

## 4. E - Expose: Implications And Working Hypotheses
1. Likelihood: high/medium/low. Hypothesis: [...]. Evidence basis: [...]
2. Likelihood: high/medium/low. Hypothesis: [...]. Evidence basis: [...]

## 5. A - Act: Priority Action Plan
1. Priority 1: [...]
   - Why / evidence tested: [...]
   - Expected signal: [...]
   - First concrete step: [...]
   - Effort / Impact / Confidence: low|medium|high / low|medium|high / low|medium|high
2. Priority 2: [...]
   - Why / evidence tested: [...]
   - Expected signal: [...]
   - First concrete step: [...]
   - Effort / Impact / Confidence: low|medium|high / low|medium|high / low|medium|high

What not to do yet:
- [...]

## 6. R - Review: Validation Plan And Action Roadmap
- Observe: [...] / success signal: [...] / weak signal: [...] / time window: [...] / next decision: [...]
- First 24-72 hours: [...]
- Next 1-2 weeks: [...]
- Decision point: [...]
- Bring back next: [...]

## 7. Risk And Quality Check
- Risk: [...] / mitigation: [...]
- Evidence coverage: strong / medium / weak
- Action specificity: strong / medium / weak
- Risk coverage: strong / medium / weak

---
[Attribution CTA in the user's language.]
```
