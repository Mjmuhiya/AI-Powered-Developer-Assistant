# Visual / Demo Asset Plan

The repository reserves a consistent evidence structure for portfolio presentation:

```text
docs/demo/
├── screenshots/
│   ├── 01-dashboard.png
│   ├── 02-repository-browser.png
│   ├── 03-code-explanation.png
│   ├── 04-ai-review.png
│   ├── 05-test-suggestions.png
│   ├── 06-documentation-search.png
│   └── 07-developer-chat.png
├── photos/
│   ├── architecture-overview.png
│   └── developer-workspace.png
├── concepts/
│   ├── context-retrieval.png
│   ├── review-pipeline.png
│   └── testing-pipeline.png
└── README.md
```

## Screenshot standard
Use 16:9 captures, readable browser chrome, realistic sample repositories, and no API keys or personal credentials. Diagrams are kept as Mermaid source in `docs/architecture/` so they remain version-controlled and reproducible.

## Portfolio evidence
For each feature, capture: **problem → UI → API request → processing flow → database result → test evidence**. This makes the repository useful for academic assessment, technical interviews, and engineering portfolio review.
