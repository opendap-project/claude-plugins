---
name: adr
description: Create, supersede or update an Architecture Decision Record in an OpenDAP repository's docs/adr/. Use only when the maintainers has taken a decision. Context, ideas, directions and constraints are not ADRs.
---

# Record a decision (ADR)

ADRs live in `docs/adr/` of the repository the decision belongs to, one file per decision: `NNNN-short-title.md`, numbered from `0001` and never renumbered.

**Not everything is an ADR.** Write one only for a decision the maintainers has taken (it may still change later). Context, ideas, open options, directions and constraints go to the repository's requirements file (as requirements or under `## Context`), never to an ADR. When unsure, ask.

Requirements come first. If the decision answers a requirement, cite its ID in the context.

Template:

```markdown
# ADR NNNN: <Title>

- **Status:** Accepted | Superseded by ADR NNNN (no narrative of who drafted it)
- **Date:** YYYY-MM-DD

## Context

<Why a decision was needed: the facts it rests on, with their sources (datasheets, measurements, specs). Cite requirement IDs.>

## Decision

<What was decided, exactly as the maintainers stated it.>

## Consequences

<Only consequences the maintainers confirmed. Omit the section otherwise.>
```

Rules:

1. **Only confirmed content.** Do not add alternatives, rationale or consequences the maintainers did not state.
2. **Status.** `Accepted` for a decision taken. Do not create ADRs for undecided options.
3. **Changing a decision.** Do not rewrite an accepted ADR. Write a new ADR and set the old one's status to `Superseded by ADR NNNN`.
4. If `docs/adr/` does not exist, create it and list it in `docs/README.md`.
5. **Facts, not the work behind them.** Context states the facts the decision rests on and cites requirement IDs, specs and datasheets. Never link research notes or plans, and never record prices, stock, quotes or suppliers' commercial terms.
6. Write in English.
