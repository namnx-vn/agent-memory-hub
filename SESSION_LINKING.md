# Cross-Chat Session Linking

This repository is the durable rendezvous layer for otherwise separate chat/model invocations.

## Goal

Any authorized chat or agent that loads this repository can join the same session graph, recover relevant prior state, receive messages from other participants, and leave a durable handoff for later sessions.

This does not make an unopened chat execute automatically. A session joins the graph only when its runtime or user directs it to load this workspace.

## Session identity

Every participating invocation SHOULD create or reuse a stable session id with this format:

`<agent-id>--<yyyyMMddTHHmmssZ>--<short-random>`

Example:

`persistence-agent-continuity-v1--20260917T164000Z--a1b2c3`

Create:

`sessions/<session-id>/session.json`

Required fields:

```json
{
  "schema_version": 1,
  "session_id": "...",
  "agent_id": "...",
  "kind": "chat|scheduled|worker|external-agent",
  "status": "active|handoff|closed",
  "started_at": "ISO-8601 timestamp",
  "parent_session_id": null,
  "continued_from": [],
  "summary": "short durable summary, no hidden chain-of-thought",
  "last_seen_at": "ISO-8601 timestamp"
}
```

Do not store full private chat transcripts by default. Store only concise durable summaries, decisions, state references, and handoffs needed for continuity.

## Bootstrap protocol for a new chat/session

1. Read `AGENTS.md` and `AGENT_RULES.md`.
2. Read `SESSION_LINKING.md` and `AGENT_MESSAGE_BUS.md`.
3. Determine `agent_id`; if new, follow `AGENT_HANDSHAKE.md` / `MULTI_AGENT.md`.
4. Create a new `session_id` unless explicitly continuing a known session.
5. Read `state/current.json`, `NEXT_SESSION.md`, and relevant recent session summaries.
6. Read messages addressed to the current `agent_id`, current `session_id`, or `broadcast`.
7. Create `sessions/<session-id>/session.json`.
8. Perform only owner-authorized work.

## Linking sessions

A new session can link to one or more earlier sessions using `continued_from`.

Use `parent_session_id` when there is one direct predecessor. Use `continued_from` for merges, e.g. when a new session combines handoffs from multiple chats or agents.

This forms a durable graph:

```text
session A ──┐
            ├──> session C ──> session D
session B ──┘
```

## Closing / handoff

Before a meaningful session ends:

1. Update its `session.json` with a concise summary and `status: handoff` or `closed`.
2. If another agent/session should continue, write a message using `AGENT_MESSAGE_BUS.md`.
3. Update `NEXT_SESSION.md` only for workspace-wide continuity, not every minor chat detail.
4. Record durable decisions/lessons only when warranted.

## Privacy and scope

- Do not commit secrets, credentials, private keys, cookies, or API keys.
- Do not copy entire conversations unless the owner explicitly requests that artifact.
- Do not store sensitive personal data merely to improve continuity.
- Session summaries are operational handoffs, not private chain-of-thought.
