import uuid
from decimal import Decimal

from pydantic import BaseModel, Field


class BaseOrmModel(BaseModel):
    """Orm model for all objects."""

    class Config:
        from_attributes = True


class BaseTableObjectModel(BaseOrmModel):
    """Base table item model."""

    pk: uuid.UUID = Field(default_factory=uuid.uuid4)


class ProductsModel(BaseTableObjectModel):
    """Product model."""

    name: str = Field(max_length=50)
    url: str = Field(max_length=70)
    price: Decimal
    description: str = Field(max_length=200)
    json_: str


class UsersModel(BaseTableObjectModel):
    """User Model."""

    username: str = Field(max_length=50)
    password: str
    email: str = Field(max_length=50)
    favourites: list[ProductsModel]


class Token(BaseModel):
    access_token: str
    token_type: str
