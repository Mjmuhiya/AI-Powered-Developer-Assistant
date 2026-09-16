CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE app_user (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL DEFAULT 'developer',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE repository (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES app_user(id),
  provider TEXT NOT NULL,
  external_id TEXT NOT NULL,
  name TEXT NOT NULL,
  default_branch TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(provider, external_id)
);

CREATE TABLE repository_file (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repository_id UUID NOT NULL REFERENCES repository(id) ON DELETE CASCADE,
  path TEXT NOT NULL,
  language TEXT,
  content_hash TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(repository_id, path)
);

CREATE TABLE analysis_job (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repository_id UUID NOT NULL REFERENCES repository(id) ON DELETE CASCADE,
  type TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'queued',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  started_at TIMESTAMPTZ,
  finished_at TIMESTAMPTZ
);

CREATE TABLE finding (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  job_id UUID NOT NULL REFERENCES analysis_job(id) ON DELETE CASCADE,
  severity TEXT NOT NULL,
  rule_code TEXT NOT NULL,
  path TEXT NOT NULL,
  line INTEGER,
  message TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE review_task (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repository_id UUID NOT NULL REFERENCES repository(id) ON DELETE CASCADE,
  assignee_id UUID REFERENCES app_user(id),
  title TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'open',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_repository_files_repo ON repository_file(repository_id);
CREATE INDEX idx_analysis_jobs_repo ON analysis_job(repository_id);
CREATE INDEX idx_findings_job ON finding(job_id);
