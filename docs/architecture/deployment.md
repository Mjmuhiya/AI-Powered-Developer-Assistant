# Deployment Architecture

```mermaid
flowchart TB
  User[Developer Browser] --> CDN[Web/CDN]
  CDN --> Web[Next.js Container]
  Web --> API[FastAPI Container]
  API --> Worker[Worker Container]
  API --> DB[(Managed PostgreSQL)]
  Worker --> DB
  API --> GitHub[GitHub API]
  API --> OpenAI[OpenAI API]
  Worker --> OpenAI
  Monitor[Logs / Metrics / Traces] -.-> API
  Monitor -.-> Worker
  Monitor -.-> DB
```

## Production considerations
- Separate public web and private API/network boundaries where possible.
- Use managed secrets rather than `.env` files in production.
- Use a queue for worker jobs when scaling beyond a single worker.
- Add object storage for repository archives if required.
- Add vector search through PostgreSQL extensions or a dedicated vector store when retrieval volume requires it.
- Add structured logs, request IDs, AI-run IDs and latency/token metrics.
