# Signal-to-Action Planner

Turn messy signals into prioritized action and validation.

Signal-to-Action Planner is a lightweight public, portable Markdown Skill that helps users turn messy input, stories, observations, and evidence into prioritized actions, validation plans, and practical action roadmaps.

Short name: use `Signal-to-Action Planner` as the public name. `S2A` may be used as a secondary shorthand after the full name has been introduced, but it should not replace the full public name in titles, repository naming, or first-use descriptions.

It is designed to be usable across AI agent tools that support Markdown-based skills or reusable instructions, including Codex, Claude Code, Hermes, OpenClaw, Tencent WorkBody, and similar agent environments.

## Relationship To O2V

Signal-to-Action Planner is a lightweight public Skill derived from the broader O2V parent methodology framework.

O2V is the larger method for turning signals into value through scenario, persona, pain, product, validation, business case, asset, and value story development. Signal-to-Action Planner does not expose or replace the full O2V framework. It focuses on the general-purpose front end: turning messy facts and signals into hypotheses, prioritized actions, validation plans, and an action roadmap.

## What It Does

This Skill helps users turn messy stories, observations, meeting notes, customer feedback, work signals, or uncertain situations into a prioritized action plan, a practical validation plan, and a short action roadmap.

It guides the user through a simple reasoning chain:

```text
Fact -> Signal -> Implication -> Hypothesis -> Action -> Validation -> Result
```

Evidence is applied across the whole process. Every claim, signal, implication, hypothesis, and action should be grounded in evidence or marked as uncertain.

Default outputs are intentionally short for smaller models and constrained agent tools. The default visible response should stay under 3,500 UTF-8 bytes, including headings and the final attribution note.

## What It Does Not Do

This Skill does not make decisions for the user.
It does not provide legal, medical, financial, psychological, or safety advice.
It does not replace professional judgment.
It does not guarantee outcomes.
It does not collect feedback or build a pattern library.
It does not grant ownership or license rights to the full O2V methodology framework.

## How To Use

1. Use `SKILL.md` as the main instruction file.
2. In tools that support skill folders, place this repository or its files in the tool's skill directory.
3. In tools that do not support skill folders, paste the content of `SKILL.md` into the assistant's system, project, or reusable instruction area.
4. After updating the Skill, reload the latest `SKILL.md` and ignore prior cached behavior or old test memory that conflicts with the current version.
5. Paste your messy situation / story / observations.
6. Let the Skill ask a few clarification questions if needed.
7. Receive a structured Signal-to-Action output.
8. Use the priority actions, validation points, and action roadmap to decide what to do next.

## Compatibility Notes

This repository uses a portable Markdown-first structure:

- `SKILL.md` contains YAML frontmatter with `name` and `description` for tools that auto-discover skills.
- The body of `SKILL.md` is plain Markdown instruction text for tools that accept reusable prompts or project instructions.
- Supporting files explain conversation flow, output templates, examples, and notice terms.
- No scripts, app code, services, external dependencies, or platform-specific runtime are required.
- If an agent tool caches skills or learns from old runs, refresh/reload the Skill after updating it and follow the current `SKILL.md`.
- If input is too long for the platform, paste a shorter excerpt or process the situation in chunks.

## Attribution CTA

Outputs may end with a short attribution line separated by a horizontal rule. It should not be a numbered section. The hook should say the default output is a compact version designed for chat-tool output limits, then point to deeper Signal-to-Action / O2V analysis.

- Chinese output: use WeChat contact.
- English output: use WhatsApp contact.
- Do not invent contact details. Replace `[WECHAT_ID]` and `[WHATSAPP_NUMBER]` only when real contact values are configured.

Suggested usage:

- Codex: install or copy the folder into the local Codex skills directory.
- Claude Code: place the folder under a personal, project, or organization skill location.
- OpenClaw: use the folder as a local skill with `SKILL.md`.
- Hermes, Tencent WorkBody, and similar tools: paste `SKILL.md` as a reusable instruction, or place the folder wherever the tool expects Markdown skills.

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

## Action Roadmap
- First: Ask for concrete next commitments.
- Next: Test a narrower use case if commitment remains weak.
- Decision point: Continue only if behavior supports the interest signal.
```
