from collections.abc import Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database, models, repository


def get_repository(
    model: type[models.BaseTableModel],
) -> Callable[[AsyncSession], repository.DatabaseRepository]:
    def func(session: AsyncSession = Depends(database.get_db_session)):
        return repository.DatabaseRepository(model, session)

    return func
