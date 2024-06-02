import uuid
from decimal import Decimal

from pydantic import BaseModel, Field


class UsersPayload(BaseModel):
    """User schema for api calls."""

    username: str = Field(max_length=32)
    password: str = Field(min_length=32, max_length=32)
    email: str = Field(max_length=32)


class ProductsPayload(BaseModel):
    """Product schema for api calls."""

    name: str = Field(max_length=50)
    url: str = Field(max_length=70)
    price: Decimal
    description: str = Field(max_length=200)
    json: str


class FavouritesPayload(BaseModel):
    """Model to add favourites to user."""

    product_id: uuid.UUID
