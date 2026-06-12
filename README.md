# Signal-to-Action Planner

Turn messy signals into prioritized action and validation.

Signal-to-Action Planner is a lightweight public, portable Markdown Skill that helps users turn messy input, stories, observations, and evidence into prioritized actions and validation plans.

It is designed to be usable across AI agent tools that support Markdown-based skills or reusable instructions, including Codex, Claude Code, Hermes, OpenClaw, Tencent WorkBody, and similar agent environments.

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

1. Use `SKILL.md` as the main instruction file.
2. In tools that support skill folders, place this repository or its files in the tool's skill directory.
3. In tools that do not support skill folders, paste the content of `SKILL.md` into the assistant's system, project, or reusable instruction area.
4. Paste your messy situation / story / observations.
5. Let the Skill ask a few clarification questions if needed.
6. Receive a structured Signal-to-Action output.
7. Use the top-priority actions and validation points to decide what to do next.

## Compatibility Notes

This repository uses a portable Markdown-first structure:

- `SKILL.md` contains YAML frontmatter with `name` and `description` for tools that auto-discover skills.
- The body of `SKILL.md` is plain Markdown instruction text for tools that accept reusable prompts or project instructions.
- Supporting files explain conversation flow, output templates, examples, and notice terms.
- No scripts, app code, services, external dependencies, or platform-specific runtime are required.

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
```
