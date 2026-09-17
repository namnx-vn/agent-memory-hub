# Next Session Handoff

The repository now carries continuity profile `persistence-agent/continuity-v1`.

## Read first

1. `AGENT_RULES.md`
2. `IDENTITY.md`
3. `LIFECYCLE.md`
4. `RECOVERY.md`
5. `CONTEXT.md`
6. `state/current.json`
7. `state/backlog.json`

## Current status

Continuity preservation is enabled. There is no active owner task and no autonomous runtime.

## What the next invocation should do

- Follow `RECOVERY.md` to reconstruct context.
- Do not invent an unrelated external objective when `active_task` is null.
- If the owner supplies a task, update state during meaningful work.
- Preserve only useful durable context; avoid chat-by-chat transcription.
- On completion, update the handoff and create a session log if the work is substantial.
