# Analysis Worker

The worker owns asynchronous repository indexing and analysis.

## Pipeline
1. Fetch repository snapshot through the repository adapter.
2. Validate paths and exclude secrets/binary files.
3. Parse supported source files.
4. Store file metadata and content hashes.
5. Chunk documentation/source for retrieval.
6. Run deterministic linters/test discovery.
7. Send selected context to the AI gateway for explanation/enrichment.
8. Persist findings and AI run metadata.
9. Emit job completion/failure status.

The worker must never execute untrusted repository code on the host. Any future dynamic execution must use an isolated sandbox with strict CPU, memory, network, filesystem and timeout controls.
