import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = os.getenv("ENV_FILE", "config/local")


settings = Settings()
