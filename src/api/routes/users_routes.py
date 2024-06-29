import uuid
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src import utils
from src.api import models, schemas
from src.api.dependencies import get_current_user, get_repository
from src.api.routes.products_routes import ProductsRepository
from src.database import models as db_models
from src.database.database import get_db_session
from src.database.repository import DatabaseRepository
from src.settings import settings
from src.utils import get_password_hash

users_router = APIRouter(prefix="/users", tags=["users"])


UsersRepository = Annotated[
    DatabaseRepository[db_models.Users],
    Depends(get_repository(db_models.Users)),
]


@users_router.get("/me")
async def read_users_me(
    current_user: models.UsersModel = Depends(get_current_user),
):
    del current_user.password
    return current_user


@users_router.post("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: uuid.UUID,
    data: schemas.UsersPayload,
    repository: UsersRepository,
    current_user: models.UsersModel = Depends(get_current_user),
) -> dict:
    data.password = get_password_hash(data.password)
    user = await repository.update(data.dict(), user_id)
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = utils.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {
        "user": models.UsersModel.model_validate(user),
        "token": models.Token(access_token=access_token, token_type="bearer")
    }


@users_router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id: uuid.UUID,
    usr_repository: UsersRepository,
    current_user: models.UsersModel = Depends(get_current_user),
):
    await usr_repository.delete(user_id)
    return status.HTTP_204_NO_CONTENT


@users_router.put(
    "/favourites/{user_id}", status_code=status.HTTP_200_OK
)
async def add_favourites(
    user_id: uuid.UUID,
    data: schemas.FavouritesPayload,
    usr_repository: UsersRepository,
    prod_repository: ProductsRepository,
    session: AsyncSession = Depends(get_db_session),
    current_user: models.UsersModel = Depends(get_current_user),
):
    user = await usr_repository.get(user_id)
    product = await prod_repository.get(data.product_id)

    if product is None:
        raise HTTPException(
            detail="Indicated product not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    user.favourite_products.append(product)

    await session.commit()
    await session.refresh(user)

    return status.HTTP_200_OK


@users_router.delete(
    "/favourites/{user_id}", status_code=status.HTTP_200_OK
)
async def remove_favourites(
    user_id: uuid.UUID,
    data: schemas.FavouritesPayload,
    usr_repository: UsersRepository,
    prod_repository: ProductsRepository,
    session: AsyncSession = Depends(get_db_session),
    current_user: models.UsersModel = Depends(get_current_user),
):
    user = await usr_repository.get(user_id)
    product = await prod_repository.get(data.product_id)

    if product is None:
        raise HTTPException(
            detail="Indicated product not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    user.favourite_products.remove(product)

    await session.commit()
    await session.refresh(user)

    return status.HTTP_200_OK
