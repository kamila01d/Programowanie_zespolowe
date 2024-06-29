import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.api import models, schemas
from src.api.dependencies import get_current_user, get_repository
from src.database import models as db_models
from src.database.repository import DatabaseRepository

products_router = APIRouter(prefix="/products", tags=["products"])

ProductsRepository = Annotated[
    DatabaseRepository[db_models.Products],
    Depends(get_repository(db_models.Products)),
]


@products_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_product(
    data: schemas.ProductsPayload,
    repository: ProductsRepository,
    current_user: models.UsersModel = Depends(get_current_user),
) -> models.ProductsModel:
    product = await repository.create(data.dict())
    return models.ProductsModel.model_validate(product)


@products_router.delete(
    "/{product_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_id: uuid.UUID,
    repository: ProductsRepository,
    current_user: models.UsersModel = Depends(get_current_user),
):
    await repository.delete(product_id)
    return status.HTTP_204_NO_CONTENT
