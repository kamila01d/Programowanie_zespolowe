import uuid
from typing import Generic, TypeVar

from fastapi import HTTPException, status
from sqlalchemy import BinaryExpression, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import models
from src.database.models import Users

Model = TypeVar("Model", bound=models.BaseTableModel)


class DatabaseRepository(Generic[Model]):
    """Repository for performing database queries."""

    def __init__(
        self, model: type[Model], session: AsyncSession
    ) -> None:
        self.model: type[Model] = model
        self.session: AsyncSession = session

    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: uuid.UUID) -> Model | None:
        return await self.session.get(self.model, pk)

    async def get_all(self) -> list[Model]:
        query = select(self.model)
        result = await self.session.execute(query)
        return list(result.scalars())

    async def delete(self, pk: uuid.UUID) -> None:
        instance: Model = await self.session.get(self.model, pk)
        await self.session.delete(instance)
        await self.session.commit()

    async def update(self, data: dict, pk: uuid.UUID) -> Model:
        instance: Model = await self.session.get(self.model, pk)
        query = update(self.model).values(**data).where(self.model.pk == instance.pk)
        await self.session.execute(query)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def filter_user_name(self, username) -> Model:
        query = select(models.Users)
        query = query.where(models.Users.username == username)
        result = await self.session.execute(query)
        return result.scalars().first()
