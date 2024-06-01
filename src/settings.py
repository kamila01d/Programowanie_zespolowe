import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")


settings = Settings()
