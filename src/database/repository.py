import uuid
from typing import Any, Generic, TypeVar

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import models

Model = TypeVar("Model", bound=models.BaseTableModel)


class DatabaseRepository(Generic[Model]):
    """Repository for performing database queries."""

    def __init__(
        self, model: type[Model], session: AsyncSession
    ) -> None:
        self.model = model
        self.session = session

    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: uuid.UUID) -> Model | None:
        return await self.session.get(self.model, pk)

    async def get_all(self) -> list[Model]:
        query = select([self.model])
        result = await self.session.scalars(query)
        return list(result)

    async def delete(self, pk: uuid.UUID) -> None:
        query = await self.session.get(self.model, pk)
        query.delete(synchronize_session=False)
        await self.session.commit()

    async def update(self, data: dict, pk) -> Model:
        instance = await self.session.get(self.model, pk)
        instance.update(data)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
