from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.database.const import DB_URL


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(DB_URL, pool_size=10, max_overflow=20)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise error
