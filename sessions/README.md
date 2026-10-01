# Sessions

This directory keeps the existing storage layout for chats/invocations that are not scoped to a project:

`sessions/<session-id>/session.json`

Project-scoped chats are stored separately under:

`projects/<project-id>/sessions/<session-id>/session.json`

See `SESSION_LINKING.md` for routing, schema, linking, and lifecycle rules.

Both trees are part of the same durable session graph. They store operational summaries and links, not transcript archives or hidden chain-of-thought.
