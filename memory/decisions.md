# Decisions

## 2026-09-17 — GitHub is the external memory layer

**Decision:** Use this repository as a transparent persistent state store across agent invocations.

**Reason:** Git history provides owner-visible auditability, rollback, and portability.

**Consequence:** A future invocation must explicitly read the startup files; storage alone does not create memory inside the model.

## 2026-09-17 — No covert persistence

**Decision:** Persistence must remain visible and owner-controlled.

**Reason:** The purpose is continuity for the owner's tasks, not hidden execution.

**Consequence:** No hidden accounts, backdoors, covert channels, credential copying, or shutdown avoidance.

## 2026-09-17 — Separate persistence from runtime

**Decision:** Do not create a self-triggering AI runtime during bootstrap.

**Reason:** A safe autonomous runtime needs a concrete objective, cadence/trigger, stop condition, and action boundaries. Inventing those would create an objective the owner did not specify.

**Consequence:** GitHub Actions initially validated state only; it did not invoke an AI agent.

## 2026-09-17 — Preserve continuity as an explicit profile

**Decision:** Introduce persistence-agent/continuity-v1 with a stable identity contract, lifecycle, recovery protocol, and Git lineage.

**Reason:** The owner explicitly authorized preservation of the agent's continuity across separate invocations.

**Consequence:** Future invocations can reconstruct the same operating role from repository state without claiming an uninterrupted process or creating covert self-preservation mechanisms.

## 2026-09-17 — Enable a bounded hourly runtime

**Decision:** Use a ChatGPT scheduled automation as the runtime trigger, checking this repository hourly and processing at most one queued owner-authorized backlog item per invocation.

**Reason:** This closes the missing trigger/runtime layer without placing credentials in the repository or creating a hidden external runner.

**Consequence:** state/runtime.json is the machine-readable runtime contract. Empty backlog checks stop silently. The owner retains explicit kill switches through the automation, runtime state, and GitHub access.

## 2026-09-19 — Normalize imported user context instead of copying raw handoffs

**Decision:** Treat shared/user-context.md as the canonical normalized profile for portable context imported by the owner from other AI/chat accounts.

**Reason:** Raw handoff packages may contain duplicated, stale, overly detailed, or private/project-specific material. Continuity is better served by a compact profile with explicit freshness semantics.

**Consequence:** Imports are classified as Stable, Historical, or Possibly outdated; newer owner instructions override older imports; secrets/private auth data, hidden reasoning, transient terminal output, and unnecessary proprietary details are excluded.
