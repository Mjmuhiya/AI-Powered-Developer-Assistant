# Test Matrix

| Area | Test | Example evidence |
|---|---|---|
| Domain | Unit | Job transitions, path validation, finding severity |
| API | Integration | Repository registration, job lifecycle |
| AI | Contract | Structured response schema and prompt version |
| GitHub | Integration | Repository metadata/content adapter |
| Retrieval | Integration | Chunk indexing and relevant context |
| Review | E2E | Review → findings → task |
| Frontend | Component | Dashboard, code viewer, chat states |
| Frontend | E2E | Connect → index → explain → review |
| Security | Negative | traversal, upload limits, authz, secret leakage |
| Performance | Load | Concurrent analysis jobs and search latency |

## Acceptance rule
A feature is not complete when the AI response works once. It is complete when deterministic behavior, failure handling, authorization, observable state, and automated regression tests are implemented.
