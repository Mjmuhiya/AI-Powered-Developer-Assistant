# ADR-001: Start as a Modular Monolith

## Status
Accepted

## Context
The platform contains repository, analysis, review, documentation and chat capabilities. Splitting every capability into a network service immediately increases operational complexity.

## Decision
Start with a modular FastAPI backend and a separate asynchronous worker. Enforce package/module boundaries and stable interfaces. Extract services later when scale, deployment independence or team ownership justifies it.

## Consequences
**Positive:** simpler local development, fewer network failure modes, faster feature delivery, easier testing.

**Trade-off:** strict architecture boundaries must be maintained to avoid an unstructured monolith.
