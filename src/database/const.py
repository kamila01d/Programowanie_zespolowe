from src.settings import settings

DB_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@localhost/{settings.DB_NAME}"
