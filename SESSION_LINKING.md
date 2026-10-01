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

## Storage routing

Session storage is project-aware while preserving the existing standalone layout.

### Chat belongs to a project

When the runtime exposes a trusted project identifier, or the project instructions explicitly define a stable `PROJECT_ID`, store the session at:

`projects/<project-id>/sessions/<session-id>/session.json`

Use a lowercase slug for `project-id` matching:

`^[a-z0-9][a-z0-9-]{0,63}$`

Examples:

```text
projects/english-kyna/sessions/<session-id>/session.json
projects/devops-learning/sessions/<session-id>/session.json
projects/frontend-interview/sessions/<session-id>/session.json
```

Project-scoped sessions SHOULD include:

```json
{
  "scope": "project",
  "project_id": "english-kyna"
}
```

Do not infer project membership merely from the conversation topic. A project route must come from explicit project/runtime context.

### Chat does not belong to a project

Keep the existing layout unchanged:

`sessions/<session-id>/session.json`

Standalone sessions MAY include:

```json
{
  "scope": "standalone",
  "project_id": null
}
```

### Fallback

If project membership or a stable project id cannot be established reliably, use the standalone path. Never invent a project id from guessed context.

## Session schema

Required fields remain:

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

`scope` and `project_id` are optional for backward compatibility with existing sessions, but new project-scoped sessions should set them.

Do not store full private chat transcripts by default. Store only concise durable summaries, decisions, state references, and handoffs needed for continuity.

## Bootstrap protocol for a new chat/session

1. Read `AGENTS.md` and `AGENT_RULES.md`.
2. Read `SESSION_LINKING.md` and `AGENT_MESSAGE_BUS.md`.
3. Determine `agent_id`; if new, follow `AGENT_HANDSHAKE.md` / `MULTI_AGENT.md`.
4. Determine session scope before writing the session node:
   - trusted/explicit project id -> project-scoped path;
   - otherwise -> standalone path.
5. Create a new `session_id` unless explicitly continuing a known session.
6. Read `state/current.json`, `NEXT_SESSION.md`, and relevant recent session summaries. For project chats, prefer recent sessions from the same project tree first.
7. Read messages addressed to the current `agent_id`, current `session_id`, or `broadcast`.
8. Create the session node at the routed path.
9. Perform only owner-authorized work.

## Linking sessions

A new session can link to one or more earlier sessions using `continued_from`.

Use `parent_session_id` when there is one direct predecessor. Use `continued_from` for merges, e.g. when a new session combines handoffs from multiple chats or agents.

Links use session ids, so they may point across standalone and project-scoped storage trees when that continuity is relevant.

```text
standalone session A ----┐
                         ├──> project session C --> project session D
project session B -------┘
```

Within a project, prefer same-project predecessors unless the owner explicitly wants continuity from another project or standalone session.

## Closing / handoff

Before a meaningful session ends:

1. Update its `session.json` with a concise summary and `status: handoff` or `closed` at the same routed path where it was created.
2. If another agent/session should continue, write a message using `AGENT_MESSAGE_BUS.md`.
3. Update `NEXT_SESSION.md` only for workspace-wide continuity, not every minor chat detail.
4. Record durable decisions/lessons only when warranted.

## Privacy and scope

- Do not commit secrets, credentials, private keys, cookies, or API keys.
- Do not copy entire conversations unless the owner explicitly requests that artifact.
- Do not store sensitive personal data merely to improve continuity.
- Session summaries are operational handoffs, not private chain-of-thought.
