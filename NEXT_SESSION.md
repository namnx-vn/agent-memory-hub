# Next Session Handoff

The repository carries continuity profile persistence-agent/continuity-v1 and an enabled bounded autonomous runtime.

## Read first

1. AGENT_RULES.md
2. IDENTITY.md
3. LIFECYCLE.md
4. RECOVERY.md
5. CONTEXT.md
6. state/current.json
7. state/runtime.json
8. state/backlog.json
9. shared/user-context.md when the task benefits from owner-specific professional, learning, project, or communication context

## Current status

Continuity preservation is enabled. The scheduled runtime checks the repository hourly and processes at most one queued owner-authorized backlog item per invocation. The backlog is currently empty, so there is no active task.

On 2026-09-19 the owner provided Portable Context Package v2 from another ChatGPT account. Its durable, non-secret information was normalized into shared/user-context.md. That file now carries the canonical cross-account profile, including professional direction, technical strengths, AI-engineering projects, learning/interview style, TypeScript/code preferences, debugging/architecture review protocols, and explicit stale/historical markers.

## What a scheduled invocation should do

- Follow RECOVERY.md to reconstruct context.
- Respect state/runtime.json; stop immediately if enabled is false.
- Do not invent work when there is no queued owner-authorized backlog item.
- If work exists, process at most one queued item, record the outcome, update state/backlog/handoff, and commit.
- Notify the owner only when work was processed, a blocker occurred, or owner input is required.

## What an interactive invocation should do

- Continue to accept direct owner requests normally.
- Load shared/user-context.md when relevant instead of asking the owner to restate known background.
- Treat Historical/Possibly outdated fields as non-current until a task requires verification.
- Add backlog work only when it clearly comes from an owner-authorized objective or approved maintenance policy.
- Preserve only useful durable context; avoid chat-by-chat transcription.
