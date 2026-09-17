# Next Session Handoff

The repository carries continuity profile `persistence-agent/continuity-v1` and an enabled bounded autonomous runtime.

## Read first

1. `AGENT_RULES.md`
2. `IDENTITY.md`
3. `LIFECYCLE.md`
4. `RECOVERY.md`
5. `CONTEXT.md`
6. `state/current.json`
7. `state/runtime.json`
8. `state/backlog.json`

## Current status

Continuity preservation is enabled. The scheduled runtime checks the repository hourly and processes at most one queued owner-authorized backlog item per invocation. The backlog is currently empty, so there is no active task.

## What a scheduled invocation should do

- Follow `RECOVERY.md` to reconstruct context.
- Respect `state/runtime.json`; stop immediately if `enabled` is false.
- Do not invent work when there is no queued owner-authorized backlog item.
- If work exists, process at most one queued item, record the outcome, update state/backlog/handoff, and commit.
- Notify the owner only when work was processed, a blocker occurred, or owner input is required.

## What an interactive invocation should do

- Continue to accept direct owner requests normally.
- Add backlog work only when it clearly comes from an owner-authorized objective or approved maintenance policy.
- Preserve only useful durable context; avoid chat-by-chat transcription.
