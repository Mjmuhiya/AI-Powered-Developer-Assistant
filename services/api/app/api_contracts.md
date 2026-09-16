# API Contract v1

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/v1/repositories` | Register GitHub/upload source |
| GET | `/v1/repositories/{id}` | Repository metadata |
| POST | `/v1/repositories/{id}/index` | Start indexing job |
| GET | `/v1/analysis-jobs/{id}` | Job status/results |
| POST | `/v1/explain` | Explain source with context |
| POST | `/v1/test-suggestions` | Generate unit-test suggestions |
| POST | `/v1/reviews` | Start code review |
| GET | `/v1/findings` | Query review findings |
| POST | `/v1/review-tasks` | Create review task |
| GET | `/v1/docs/search` | Search indexed documentation |
| POST | `/v1/docs/generate` | Generate API documentation |
| POST | `/v1/chat/messages` | Repository-aware developer chat |

All mutating endpoints require authentication and authorization. Long-running operations return a job identifier rather than blocking the HTTP request.
