import uuid
from decimal import Decimal

from pydantic import BaseModel, Field


class UsersPayload(BaseModel):
    """User schema for api calls."""

    username: str
    password: str
    email: str


class ProductsPayload(BaseModel):
    """Product schema for api calls."""

    name: str = Field(max_length=50)
    url: str = Field(max_length=70)
    price: Decimal
    json_: str


class FavouritesPayload(BaseModel):
    """Model to add favourites to user."""

    product_id: uuid.UUID


class LoginPayload(BaseModel):
    """Model for user authentication."""
    username: str
    password: str


class TokenData(BaseModel):
    username: str | None = None
