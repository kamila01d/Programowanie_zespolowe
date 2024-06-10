import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from src.api import models, schemas
from src.api.dependencies import get_repository
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
) -> models.ProductsModel:
    try:
        product = await repository.create(data.dict())
        return models.ProductsModel.model_validate(product)
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@products_router.delete(
    "/{product_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_id: uuid.UUID,
    repository: ProductsRepository,
):
    try:
        await repository.delete(product_id)
        return status.HTTP_204_NO_CONTENT
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
