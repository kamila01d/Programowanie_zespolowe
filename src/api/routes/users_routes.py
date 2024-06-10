import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from httpx import Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.api import models, schemas
from src.api.dependencies import get_current_user, get_repository
from src.api.routes.products_routes import ProductsRepository
from src.database import models as db_models
from src.database.database import get_db_session
from src.database.repository import DatabaseRepository

users_router = APIRouter(prefix="/users", tags=["users"])


UsersRepository = Annotated[
    DatabaseRepository[db_models.Users],
    Depends(get_repository(db_models.Users)),
]


@users_router.get("/me")
async def read_users_me(
    current_user: models.UsersModel = Depends(get_current_user),
):
    return await current_user


@users_router.post("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: uuid.UUID,
    data: schemas.UsersPayload,
    repository: UsersRepository,
) -> models.UsersModel:
    user = await repository.update(data.dict(), user_id)
    return models.UsersModel.model_validate(user)


@users_router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id: uuid.UUID,
    usr_repository: UsersRepository,
    session: AsyncSession = Depends(get_db_session),
):
    try:
        user = await usr_repository.get(user_id)
        for product in user.favourite_products:
            product.users.remove(user)

        user.favourite_products.clear()
        await session.commit()
        await session.refresh(user)
        await usr_repository.delete(user_id)
        return status.HTTP_204_NO_CONTENT
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@users_router.put(
    "/favourites/{user_id}", status_code=status.HTTP_200_OK
)
async def get_favourites(
    user_id: uuid.UUID,
    data: schemas.FavouritesPayload,
    usr_repository: UsersRepository,
    prod_repository: ProductsRepository,
    session: AsyncSession = Depends(get_db_session),
):
    user = await usr_repository.get(user_id)
    product = await prod_repository.get(data.get("product_id"))

    if product is None:
        raise HTTPException(
            detail="Indicated product not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    try:
        user.favourite_products.append(product)
        product.users.append(user)

        await session.commit()
        await session.refresh(product)
        await session.refresh(user)

        return status.HTTP_200_OK
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@users_router.put(
    "/favourites/{user_id}", status_code=status.HTTP_200_OK
)
async def delete_favourites(
    user_id: uuid.UUID,
    data: schemas.FavouritesPayload,
    usr_repository: UsersRepository,
    prod_repository: ProductsRepository,
    session: AsyncSession = Depends(get_db_session),
):
    user = await usr_repository.get(user_id)
    product = await prod_repository.get(data.get("product_id"))

    if product is None:
        return Response(
            content="No product found!",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    try:
        user.favourite_products.remove(product)
        product.users.remove(user)

        await session.commit()
        await session.refresh(product)
        await session.refresh(user)

        return status.HTTP_200_OK
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
