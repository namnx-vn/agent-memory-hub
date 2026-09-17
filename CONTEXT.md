# Workspace Context

## Purpose

`namnx-vn/agent-memory-hub` is an owner-controlled external memory, continuity, discovery, and coordination workspace for AI-assisted tasks across otherwise separate sessions.

The repository was originally created as `namnx-vn/persistence`; Git history preserves that lineage. The canonical repository name is now `namnx-vn/agent-memory-hub`.

## Design goals

- **Persistent:** important state survives individual chats/invocations.
- **Discoverable:** common agent instruction/context conventions make the workspace easy for authorized agents to recognize once they encounter the repository.
- **Auditable:** durable changes are visible in Git history.
- **Portable:** a future agent can resume by reading a small set of files.
- **Multi-agent:** independent authorized agents can use separate namespaces and visible coordination state.
- **Minimal:** store only information that improves continuity or coordination.
- **Owner-controlled:** the human owner can inspect, edit, revert, or delete everything.
- **Non-secret:** credentials and sensitive tokens do not belong here.

## Operating model

GitHub is the durable state layer. Model invocations are the reasoning/execution layer. The scheduled ChatGPT automation is a bounded trigger that reads owner-authorized backlog work and returns the continuity profile to a dormant state between invocations.

Agent-facing discovery entrypoints include `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/agent-memory-hub.mdc`, `llms.txt`, and `agent-discovery.json`.

## Current capability boundary

The repository preserves memory, coordination state, and recovery instructions. It does not grant write access by being public, modify foundation-model weights, or create a universal broadcast channel to arbitrary external agents. A future invocation or external agent must actually encounter/read the repository and possess legitimate permissions before it can participate.
