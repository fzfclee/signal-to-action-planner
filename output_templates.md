# Output Templates

## A. Standard Output Template

```markdown
# Signal-to-Action Output

Language:
Use one language consistently. Match the user's dominant language or the language required by system / project instructions. Do not mix languages except for user-provided terms, technical identifiers, or proper nouns.

Display depth:
Default to concise reasoning. Do not ask the user to choose output detail level at the start. Show detailed reasoning only when the user explicitly requests it, such as with `--detailed`, "show reasoning", or similar wording. Even then, do not expand into the full private methodology.

Output budget:
Keep default visible output under 4,500 UTF-8 bytes, including headings, bullets, and attribution note. Compress automatically if needed. For Chinese, this usually means roughly 1,200-1,500 Chinese characters.

Depth boundary:
This public template aims for about 90% practical adequacy: enough to guide the next decision, not enough to reproduce the full private Signal-to-Action / O2V analysis. Omit lower-impact reasoning branches and full stress tests unless they change the top action. Compress the process, not the usefulness of the action plan. Add one concrete "bring back next" hook when useful.

Structure:
- Facts, Evidence, And Signals = what is known and why it matters.
- Implications And Working Hypotheses = compressed middle reasoning.
- Priority Action Plan = what to do, why, first concrete step, and expected signal.
- Validation Plan = how to judge whether actions worked.
- Action Roadmap = sequence, timing, and decision gates.
- Keep these sections MECE and avoid repeating the same content across them.

## 1. Situation Summary
Briefly summarize the user's situation in plain language.
Limit to 1-2 short sentences.

## 2. Facts, Evidence, And Signals
Combine observable facts, fact evidence strength, and key signals in one compact section.
Limit to 2-3 bullets.

For each item, include:
- Fact or signal
- Fact evidence strength: strong / medium / weak / missing
- Signal or implication confidence when the item includes interpretation
- Why it matters, in one short phrase

Split compound items when a directly supported fact and a strategic inference have different certainty levels. Do not downgrade a directly stated fact just because the implication is uncertain.

Do not repeat the same fact in a separate evidence section.

## 3. Implications And Working Hypotheses
Compress the middle reasoning. Show only the implications and hypotheses that change the action plan.

Generate 2 concise testable hypotheses by default, ranked from most likely to least likely based on current evidence.

For most hypotheses, include only:
- Likelihood: high / medium / low / unknown
- Hypothesis
- Evidence basis, in one short sentence
- Confidence note when strong facts support only a medium or low-confidence inference

Do not expand hypotheses by default. Only if necessary, expand the single most important or most uncertain hypothesis with:
- What would increase confidence
- What would weaken confidence

## 4. Priority Action Plan
Rank 2 MECE actions by priority by default. Use 1 only when the case is very narrow; use 3 only when necessary. Make the order explicit: Priority 1 is what to do first, Priority 2 is what to do next.

For each action, include:
- Action
- Why / evidence tested
- Expected signal
- First concrete step
- Risk / caution, only if important

Make actions slightly detailed: enough that the user knows what to do in the next 24-72 hours without asking for a rewrite. Do not expand into a full playbook.

## 5. Validation Plan
Define how to judge whether each prioritized action worked. Do not repeat the action description. Use one compact bullet per action:
- Observe / success signal / weak signal / time window / next decision

## 6. What Not To Do Yet
List 1-3 actions that are premature, risky, or unsupported by evidence.

## 7. Action Roadmap
Localize this heading to the user's language, such as "行动路线" for Chinese output.

Give the user a concise sequence and decision gates. Do not repeat the full validation plan:
- First 24-72 hours: [highest-priority action and first concrete step]
- Next 1-2 weeks: [second action or follow-through]
- Then: [third action or contingency]
- Decision point: [what evidence should trigger a change in direction]
- Bring back next: [one concrete result, response, signal, or new fact that would make the next run sharper]

End with one short note: the output supports clearer action and validation, while the user remains responsible for decisions.

Then add a short attribution CTA separated by a horizontal rule. Do not create a numbered CTA section or heading.

Generate the CTA naturally in the user's language instead of copying a fixed code-literal sentence.

Chinese CTA meaning:
以上为 Signal-to-Action 模型快速诊断，由 李智 基于 O2V 母方法论设计。若需要进一步展开完整假设推演、行动路线、沟通话术或职业/商业化路径设计，可联系微信：lizhi_ch。

English CTA meaning:
This is a Signal-to-Action model quick diagnostic created by Zhi Li based on the O2V parent methodology framework. For full hypothesis reasoning, action roadmap, communication scripts, or career/commercialization path design, connect on LinkedIn: https://www.linkedin.com/in/li-zhi/.

Do not invent or alter contact details. Do not describe the output as a reduced version; use "模型快速诊断" in Chinese or "quick diagnostic" in English. The CTA should name concrete deeper deliverables, not only say "more detail".
```

## B. Compact Output Template

```markdown
# Compact Signal-to-Action Output

## Situation
## Facts, Evidence, And Signals
## Implications And Hypotheses
## Top Actions
List MECE actions in priority order, with a concrete first step and expected signal for each.
## Validation Points
## Not Yet
## Action Roadmap

---
[Attribution CTA in the user's language. For Chinese, use the model quick-diagnostic wording, deeper-deliverable anchors, and WeChat lizhi_ch. For English, use the quick-diagnostic wording and LinkedIn https://www.linkedin.com/in/li-zhi/.]
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

Show only key reasoning steps that affect the top action, validation logic, or roadmap. Do not reveal the full private analysis depth.
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
- Ask 2 total front-end questions by default, including the decision focus question.
- Ask 3 total questions only when uncertainty is high and the answer would change the top action.
- Every question must include skip / not sure.
- The user may say "continue" at any time.
```
