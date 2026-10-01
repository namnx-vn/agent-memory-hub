# Projects

Project-scoped chats are grouped here by a stable explicit project id.

```text
projects/<project-id>/
└── sessions/
    └── <session-id>/
        └── session.json
```

Use a lowercase `project-id` matching `^[a-z0-9][a-z0-9-]{0,63}$`.

A chat belongs here only when project scope is explicit, for example through ChatGPT Project Instructions that define `PROJECT_ID`, or trusted runtime metadata. Do not classify chats into projects by guessing from their subject matter.

Standalone chats continue to use `sessions/<session-id>/session.json`.

Project and standalone sessions remain part of one logical session graph and may link across trees with `parent_session_id` and `continued_from` when that continuity is intentionally relevant.
