import uuid
from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field

from src.api.schemas import ProductsPayload


class BaseTableObjectModel(BaseModel):
    """Base table item model."""

    pk: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Config:
        from_attributes = True


class ProductsModel(BaseTableObjectModel):
    """Product model."""

    name: str = Field(max_length=50)
    url: str = Field(max_length=70)
    price: Decimal
    json_: str


class UsersModel(BaseTableObjectModel):
    """User Model."""

    username: str = Field(max_length=50)
    password: str
    email: str = Field(max_length=50)
    favourites: List[ProductsModel] = Field(default_factory=list)


class Token(BaseModel):
    access_token: str
    token_type: str
