from typing import List

from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]
    SQLALCHEMY_DATABASE_URI: str = config("DATABASE_URI", cast=str)
    SQLALCHEMY_TEST_DATABASE_URI: str = config("TEST_DATABASE_URI", cast=str)
    PROJECT_NAME: str = "ShyftLabs-Assignment"

    class Config:
        case_sensitive = True


settings = Settings()
