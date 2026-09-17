# Shared Coordination Blackboard

This file is a visible coordination surface for authorized agents.

## Active claims

None.

When claiming work, add a short entry containing:

- agent ID;
- task/backlog ID;
- files or resources likely to be modified;
- claim timestamp;
- expected handoff condition.

Remove or mark the claim complete when the task ends.

## Handoffs

None.

Agents may leave concise cross-agent handoffs here when information is useful to more than one continuity profile. Long-lived knowledge belongs in `shared/` instead.

## Coordination principles

- This is not a covert channel; it is intentionally owner-visible.
- Do not place secrets here.
- Prefer concise factual state over private reasoning traces.
- If another agent has an active conflicting claim, avoid destructive concurrent edits and use a branch/PR or defer the shared mutation.
