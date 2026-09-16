# CodePilot Workspace

> AI-powered developer workspace for understanding, reviewing, testing, documenting, and navigating software projects.

## Engineering Goal
CodePilot Workspace is designed as a portfolio-grade software engineering system, not only a chatbot. It demonstrates requirements engineering, modular architecture, API design, data modelling, repository integration, AI orchestration, static analysis, automated testing, security, observability, Docker deployment, and CI/CD.

## Core Features
1. Connect or upload a repository.
2. Explain source code with repository context.
3. Generate unit-test suggestions and test cases.
4. Detect potential code-quality and security issues.
5. Search project documentation using indexed chunks.
6. Generate API documentation from source and OpenAPI metadata.
7. Track code-review tasks and findings.
8. Provide developer chat with file/symbol context.
9. Record analysis jobs and audit events.

## Architecture
- **Frontend:** Next.js + TypeScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **AI:** OpenAI API behind an application-level AI gateway
- **Repository integration:** GitHub API
- **Analysis:** language-aware adapters + Ruff/Pytest/other linters
- **Deployment:** Docker Compose; production-ready container boundaries
- **Testing:** Pytest, Vitest, Playwright, API contract tests
- **CI/CD:** GitHub Actions

## Repository Structure
```text
CodePilot Workspace/
├── apps/web/                 # Next.js frontend
├── services/api/             # FastAPI application
├── services/worker/          # asynchronous analysis jobs
├── packages/contracts/       # shared API schemas and types
├── docs/architecture/        # C4, ERD, sequence and deployment diagrams
├── docs/sdlc/                # requirements, design, testing and delivery plan
├── docs/decisions/           # architecture decision records
├── docs/demo/                # screenshots, photos and demo assets
├── tests/                    # integration/e2e test planning
├── infra/                    # Docker and deployment configuration
└── .github/workflows/        # CI/CD
```

## SDLC
**Discover → Specify → Design → Implement → Test → Secure → Deploy → Observe → Improve**.

The detailed implementation roadmap is in `docs/sdlc/implementation-roadmap.md`.

## Security
Never expose API keys in the browser. Treat repository content as untrusted input. Use least-privilege GitHub permissions, input validation, rate limits, audit logging, secret scanning, and sandboxed execution for any future generated-code execution capability.

## Responsible AI
AI output is advisory. Every generated explanation, test suggestion, documentation block, or review finding should expose relevant source context and allow a developer to verify the result.

## License
See `LICENSE`.
