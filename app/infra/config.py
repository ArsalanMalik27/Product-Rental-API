from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, validator
from typing import Any, Optional


class Settings(BaseSettings):

    PROJECT_NAME: str
    ENV: str

    API_V1_STR: str = "/api/v1"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: str | None = None
    
    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        dsn = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"{values.get('POSTGRES_DB') or ''}",
        )
        return str(dsn)

    class Config:
        case_sensitive = True
        env_nested_delimiter = "__"
        env_file = ".env"


settings = Settings()