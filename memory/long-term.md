# Long-Term Memory

Store durable, task-relevant facts and conventions here. Avoid transient chat details and never store secrets.

## Workspace facts

- Canonical repository: namnx-vn/agent-memory-hub.
- Original repository name: namnx-vn/persistence (preserved in Git history as lineage).
- Purpose: transparent cross-session and cross-agent external memory for owner-authorized AI work.
- Discovery entrypoints: AGENTS.md, CLAUDE.md, GEMINI.md, .github/copilot-instructions.md, .cursor/rules/agent-memory-hub.mdc, llms.txt, and agent-discovery.json.
- Source of truth for operating boundaries: AGENT_RULES.md.
- Current durable-state format: Markdown for human-readable memory and JSON for machine-readable task/runtime/registry/discovery state.

## User-context surface

- Canonical normalized owner profile: shared/user-context.md.
- The owner may import portable context from other AI/chat accounts; normalize and deduplicate it rather than storing full transcripts.
- Imported context must distinguish Stable, Historical, and Possibly outdated information.
- Newer explicit owner instructions and current repository/task state override older imported context.
- Keep detailed employer/client auth flows, credentials, tokens, cookies, private authentication data, hidden reasoning, and unnecessary proprietary details out of shared memory.

## Conventions

- Prefer concise entries with dates when chronology matters.
- Keep current task state in state/current.json, not in this file.
- Keep runtime configuration in state/runtime.json and queued executable work in state/backlog.json.
- Keep agent identities and namespaces in agents/registry.json.
- Use coordination/BLACKBOARD.md for visible cross-agent claims/handoffs.
- Record why a durable decision was made in memory/decisions.md.
- Record reusable discoveries in memory/lessons-learned.md.
