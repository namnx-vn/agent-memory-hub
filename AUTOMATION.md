# Automation Boundary

Persistence and autonomy are separate concerns.

## What exists now

- GitHub stores durable state.
- GitHub Actions validates the persistence files on push/PR.
- Future invocations can reconstruct context from the repository.

## What is intentionally not enabled

There is no self-triggering AI loop, scheduled model invocation, hidden runner, or external service that calls an agent indefinitely.

A useful autonomous runtime requires all of the following to be explicit:

```text
bounded objective
+ trigger/cadence
+ allowed tools
+ allowed repositories/systems
+ stop condition
+ audit trail
+ human override
```

## Safe future pattern

Example: "Every morning, inspect CI for repository X. If a failure is caused by a deterministic code/config issue, create a fix branch and draft PR. Never merge or deploy. Stop after one attempted fix and record the result."

That is a bounded agent workflow. "Keep yourself running and decide what to do" is not.
