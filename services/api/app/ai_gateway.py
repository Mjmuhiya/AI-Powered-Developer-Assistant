from dataclasses import dataclass

from .config import settings


@dataclass(frozen=True)
class AIResult:
    content: str
    model: str
    prompt_tokens: int = 0
    completion_tokens: int = 0


class AIGateway:
    """Single server-side boundary for LLM calls.

    Production implementation should add prompt versioning, timeouts, retries,
    structured outputs, token budgets, redaction and audit metadata here.
    """

    def __init__(self) -> None:
        self.api_key = settings.openai_api_key

    def build_code_explanation_prompt(self, path: str, source: str) -> str:
        return (
            "Explain the following source file for a software engineer. "
            "Identify responsibility, important functions, dependencies, risks, "
            "and suggested tests. Do not invent behavior.\n\n"
            f"FILE: {path}\nSOURCE:\n{source}"
        )
