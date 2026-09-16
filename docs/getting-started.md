# Getting Started

## Prerequisites
- Node.js 20+
- Python 3.12+
- Docker Desktop
- PostgreSQL 16+ (or Docker)
- Git
- GitHub OAuth/App credentials for repository integration
- OpenAI API key stored only on the server

## Development Sequence
1. Start PostgreSQL and API dependencies with Docker Compose.
2. Create backend environment variables from `.env.example`.
3. Run database migrations.
4. Start FastAPI.
5. Start Next.js.
6. Connect a test repository.
7. Run repository indexing.
8. Test explain, review, test-generation, docs, and chat workflows.

## Quality Gates
`ruff check`, `mypy`, `pytest`, frontend lint/typecheck/tests, Playwright smoke tests, dependency scanning, and secret scanning should pass before merge.
