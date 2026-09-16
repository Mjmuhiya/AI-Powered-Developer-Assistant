from dataclasses import dataclass
from enum import StrEnum


class JobStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class FindingSeverity(StrEnum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class CodeFinding:
    path: str
    line: int
    severity: FindingSeverity
    rule_code: str
    message: str


@dataclass(frozen=True)
class AnalysisJob:
    repository_id: str
    job_type: str
    status: JobStatus = JobStatus.QUEUED
