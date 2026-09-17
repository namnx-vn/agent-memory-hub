# Long-Term Memory

Store durable, task-relevant facts and conventions here. Avoid transient chat details and never store secrets.

## Workspace facts

- Repository: `namnx-vn/persistence`
- Purpose: transparent cross-session external memory for owner-authorized AI work.
- Source of truth for operating boundaries: `AGENT_RULES.md`.
- Current durable-state format: Markdown for human-readable memory and JSON for machine-readable task state.

## Conventions

- Prefer concise entries with dates when chronology matters.
- Keep current task state in `state/current.json`, not in this file.
- Record why a durable decision was made in `memory/decisions.md`.
- Record reusable discoveries in `memory/lessons-learned.md`.
