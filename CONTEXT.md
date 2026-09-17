# Workspace Context

## Purpose

`namnx-vn/persistence` is an owner-controlled external memory and coordination workspace for AI-assisted tasks across otherwise separate sessions.

## Design goals

- **Persistent:** important state survives individual chats/invocations.
- **Auditable:** durable changes are visible in Git history.
- **Portable:** a future agent can resume by reading a small set of files.
- **Minimal:** store only information that improves continuity.
- **Owner-controlled:** the human owner can inspect, edit, revert, or delete everything.
- **Non-secret:** credentials and sensitive tokens do not belong here.

## Operating model

GitHub is the durable state layer. A model invocation is the reasoning/execution layer. A scheduler, if one is later enabled, is only a trigger and must have a bounded visible objective.

## Current capability boundary

The repository can preserve memory and coordination state. It cannot by itself keep a model continuously running, modify foundation-model weights, or guarantee that a future invocation will read it unless the runtime/startup instruction points to this repository.
