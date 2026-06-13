# Roadmap

Signal-to-Action Planner will stay a compact public Skill. The goal is to make the public version easier to adopt, easier to test, and more useful across agent tools, while keeping the complete O2V methodology separate.

## Near Term

- Improve public benchmark coverage with more diverse test cases.
- Keep the CLEAR 7-section public structure consistent across instructions, templates, examples, benchmark cases, and checker scripts.
- Add more compatibility notes for Codex, Claude Code, Cursor, Windsurf, Hermes, OpenClaw, and WorkBody.
- Keep reducing output bloat while preserving useful action detail.
- Improve `minimal_SKILL.md` for smaller models and limited-context tools.
- Explore a simple web demo or hosted playground as the main public trial surface.

## Medium Term

- Build a lightweight hosted playground or demo page if public interest justifies it.
- Add optional export formats such as concise Markdown, JSON-like structured output, and Obsidian-friendly blocks.
- Add a public compatibility matrix for agent tools.
- Add more multilingual examples after the English and Chinese templates are stable.
- Create a lightweight issue template for bug reports, output quality reports, and benchmark submissions.

## Later

- Explore optional Tool Use extensions for fact checking, calendar follow-up, or note-system integration.
- Explore versioned public releases once the workflow stabilizes.

## Non-Goals

- Do not expose the full O2V methodology.
- Do not make the public default output long or exhaustive.
- Do not add mandatory runtime dependencies.
- Do not automate posting, messaging, or external actions from this public Skill.
