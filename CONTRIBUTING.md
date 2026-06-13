# Contributing

Contributions are welcome when they improve the public Skill without turning it into the complete methodology.

## Good Contributions

- New real-world example cases with private details removed.
- Compatibility notes for agent tools such as Codex, Claude Code, Cursor, Windsurf, Hermes, OpenClaw, or WorkBody.
- Benchmark cases and scoring improvements.
- Fixes for unclear instructions, language consistency, or output bloat.
- Improvements that help smaller models follow the public workflow.
- Changes that keep the public CLEAR 7-section output consistent across `SKILL.md`, templates, examples, and benchmark guidance.

## What To Avoid

- Do not add private, confidential, or identifiable user situations.
- Do not expose the full O2V methodology or deeper advisory workflow.
- Do not make default output longer than necessary.
- Do not replace the public CLEAR structure with a different visible framework unless the whole repo is intentionally rebranded.
- Do not add platform-specific dependencies unless they are optional.
- Do not turn the public Skill into legal, medical, financial, psychological, or safety advice.

## Suggested Pull Request Shape

Use a small, focused pull request:

1. State the problem.
2. Explain the change.
3. Show one before/after example or benchmark case.
4. Confirm that the public output remains compact.
5. Confirm that any affected surrounding files stay aligned with the CLEAR 7-section output.

## Public Benchmark Check

Before submitting a major instruction change, run at least three cases from [`BENCHMARK.md`](BENCHMARK.md):

- one business or product case;
- one career or organization case;
- one personal decision case.

Report the model / agent tool used, the number of clarification questions, and the scores by dimension.

## Language

Keep public documentation in clear English unless the file is specifically a localized template or example. The Skill itself should match the user's language during use.
