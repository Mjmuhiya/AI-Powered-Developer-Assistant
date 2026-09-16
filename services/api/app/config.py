from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CodePilot Workspace API"
    database_url: str = "postgresql+psycopg://codepilot:codepilot@db:5432/codepilot"
    openai_api_key: str = ""
    github_app_id: str = ""
    github_private_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
