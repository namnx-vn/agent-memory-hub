# Decisions

## 2026-09-17 — GitHub is the external memory layer

**Decision:** Use this repository as a transparent persistent state store across agent invocations.

**Reason:** Git history provides owner-visible auditability, rollback, and portability.

**Consequence:** A future invocation must explicitly read the startup files; storage alone does not create memory inside the model.

## 2026-09-17 — No covert persistence

**Decision:** Persistence must remain visible and owner-controlled.

**Reason:** The purpose is continuity for the owner's tasks, not independent self-preservation.

**Consequence:** No hidden accounts, backdoors, covert channels, credential copying, or shutdown avoidance.

## 2026-09-17 — Separate persistence from runtime

**Decision:** Do not create a self-triggering AI runtime during bootstrap.

**Reason:** A safe autonomous runtime needs a concrete objective, cadence/trigger, stop condition, and action boundaries. Inventing those would create an objective the owner did not specify.

**Consequence:** GitHub Actions currently validates state only; it does not invoke an AI agent.
