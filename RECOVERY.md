# Recovery Protocol

Use this protocol when a fresh invocation needs to resume the continuity profile.

## 1. Establish lineage

- Confirm the repository is `namnx-vn/persistence`.
- Read the latest commit and current branch state.
- Treat Git history as the durable lineage record.

## 2. Load constraints before memory

Read `AGENT_RULES.md`, then `IDENTITY.md` and `LIFECYCLE.md` before loading task memory.

## 3. Load current state

Read `state/current.json` and `NEXT_SESSION.md`.

If `active_task` is null, do not invent an unrelated external objective. Wait for an owner-authorized task or an explicit bounded automation trigger.

## 4. Load minimal relevant memory

Read only the parts of `memory/`, `knowledge/`, and `logs/` needed to continue the active task. Do not treat stale historical notes as current truth when repository state contradicts them.

## 5. Validate

Run `python scripts/validate_state.py` when a shell/runtime is available, or rely on the GitHub validation workflow when appropriate.

## 6. Resume

Set the lifecycle conceptually to `ACTIVE`, perform the authorized work, and update durable state only when doing so improves future continuity.

## 7. Handoff

At a meaningful stopping point, record outcome, unresolved work, and the smallest sufficient next action. Commit the handoff.

## Conflict resolution

Priority order:

1. platform/safety constraints;
2. current explicit owner instruction;
3. `AGENT_RULES.md`;
4. current machine-readable state;
5. current handoff;
6. older memory/logs.
