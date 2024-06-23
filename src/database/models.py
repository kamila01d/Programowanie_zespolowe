import uuid

from sqlalchemy import Column, ForeignKey, Table, orm
from sqlalchemy.dialects.postgresql import UUID


class BaseTableModel(orm.DeclarativeBase):
    """Base database model."""

    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )


favourites = Table(
    "favourites",
    BaseTableModel.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.pk")),
    Column("product_id", UUID(as_uuid=True), ForeignKey("products.pk")),
)


class Users(BaseTableModel):
    """Users database model."""

    __tablename__ = "users"

    username: orm.Mapped[str]
    password: orm.Mapped[str]
    email: orm.Mapped[str]
    favourite_products: orm.Mapped[list["Products"]] = orm.relationship(
        secondary=favourites
    )


class Products(BaseTableModel):
    """Products database model."""

    __tablename__ = "products"

    name: orm.Mapped[str]
    url: orm.Mapped[str]
    price: orm.Mapped[float]
    description: orm.Mapped[str]
    json: orm.Mapped[str]
    users: orm.Mapped[list["Users"]] = orm.relationship(
        secondary=favourites
    )
