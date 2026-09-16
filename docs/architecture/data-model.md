# Data Model / Relationships

```mermaid
erDiagram
  USER ||--o{ REPOSITORY : owns
  REPOSITORY ||--o{ REPOSITORY_FILE : contains
  REPOSITORY_FILE ||--o{ DOCUMENT_CHUNK : indexed_as
  REPOSITORY ||--o{ ANALYSIS_JOB : has
  ANALYSIS_JOB ||--o{ FINDING : produces
  REPOSITORY ||--o{ REVIEW_TASK : tracks
  USER ||--o{ REVIEW_TASK : assigned
  REPOSITORY ||--o{ CONVERSATION : has
  CONVERSATION ||--o{ MESSAGE : contains
  MESSAGE }o--o{ DOCUMENT_CHUNK : cites
  USER ||--o{ AUDIT_EVENT : creates
  REPOSITORY ||--o{ AUDIT_EVENT : concerns
  AI_MODEL ||--o{ AI_RUN : executes
  CONVERSATION ||--o{ AI_RUN : triggers

  USER { uuid id PK string email string role }
  REPOSITORY { uuid id FK user_id string provider string external_id string name string default_branch }
  REPOSITORY_FILE { uuid id FK repository_id string path string language string content_hash }
  DOCUMENT_CHUNK { uuid id FK file_id int chunk_index text content vector embedding }
  ANALYSIS_JOB { uuid id FK repository_id string type string status datetime started_at }
  FINDING { uuid id FK job_id string severity string rule_code string path int line text message }
  REVIEW_TASK { uuid id FK repository_id FK assignee_id string status string title }
  CONVERSATION { uuid id FK repository_id FK user_id string title }
  MESSAGE { uuid id FK conversation_id string role text content }
  AI_MODEL { uuid id string provider string model_name }
  AI_RUN { uuid id FK model_id FK conversation_id int prompt_tokens int completion_tokens }
  AUDIT_EVENT { uuid id FK user_id FK repository_id string action datetime }
```

## Relationship rationale
A repository owns immutable-ish file snapshots and analysis jobs. Jobs produce findings. Files produce searchable chunks. Conversations belong to a repository so chat can retrieve relevant project context. AI runs are separately recorded for observability and cost analysis.
