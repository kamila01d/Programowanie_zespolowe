import uuid
from decimal import Decimal

from pydantic import BaseModel, Field


class BaseOrmModel(BaseModel):
    """Orm model for all objects."""
    class Config:
        orm_mode = True

class BaseTableObjectModel(BaseOrmModel):
    """Base table item model."""
    pk: uuid.UUID


class UsersModel(BaseTableObjectModel):
    """User Model."""
    username: str = Field(max_length=32)
    password: str = Field(min_length=32, max_length=32)
    email: str = Field(max_length=32)


class ProductsModel(BaseTableObjectModel):
    """Product model."""
    name: str = Field(max_length=50)
    url: str = Field(max_length=70)
    price: Decimal
    description: str = Field(max_length=200)
    json: str


class Favourites(BaseOrmModel):
    Product: ProductsModel
    User: UsersModel
