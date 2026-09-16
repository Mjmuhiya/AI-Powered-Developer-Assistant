from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CodePilot Workspace API", version="1.0.0")


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="codepilot-api")


@app.get("/v1")
def api_info() -> dict[str, str]:
    return {"name": "CodePilot Workspace API", "version": "v1"}
