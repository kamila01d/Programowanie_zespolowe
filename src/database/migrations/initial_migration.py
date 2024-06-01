import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine

from src.database.const import DB_URL
from src.database.models import BaseTableModel

logger = logging.getLogger()


async def migrate_tables() -> None:
    logger.info("Starting to migrate")

    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(BaseTableModel.metadata.create_all)

    logger.info("Done migrating")


if __name__ == "__main__":
    asyncio.run(migrate_tables())
