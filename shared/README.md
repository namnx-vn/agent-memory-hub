# Shared Knowledge

This directory contains durable information intentionally shared across authorized agents using `namnx-vn/persistence`.

Suitable content:

- stable technical conventions;
- reusable runbooks;
- architecture decisions useful across agent roles;
- cross-agent summaries and references;
- durable task context that is not specific to one agent.

Do not store:

- credentials or secrets;
- private keys, tokens, cookies, or authentication material;
- hidden communication intended to avoid owner visibility;
- transient scratch data better kept in an agent namespace or session log.

Agents should prefer small, named files over a single unbounded memory dump.
