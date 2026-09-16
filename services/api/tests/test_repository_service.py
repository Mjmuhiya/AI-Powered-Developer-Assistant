import pytest

from app.repository_service import is_indexable, validate_repository_path


def test_normalizes_safe_repository_path() -> None:
    assert validate_repository_path("src/main.py") == "src/main.py"


def test_rejects_path_traversal() -> None:
    with pytest.raises(ValueError):
        validate_repository_path("../../secrets.env")


def test_indexing_extension() -> None:
    assert is_indexable("src/main.py")
    assert not is_indexable(".env")
