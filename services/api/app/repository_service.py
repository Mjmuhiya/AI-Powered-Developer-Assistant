from pathlib import PurePosixPath

ALLOWED_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx", ".java", ".cs", ".go", ".sql", ".md"}


def validate_repository_path(path: str) -> str:
    """Reject traversal and normalize repository-relative paths."""
    normalized = str(PurePosixPath(path))
    if normalized.startswith("../") or normalized == ".." or "/../" in normalized:
        raise ValueError("Repository path traversal is not allowed")
    return normalized


def is_indexable(path: str) -> bool:
    return PurePosixPath(path).suffix.lower() in ALLOWED_EXTENSIONS
