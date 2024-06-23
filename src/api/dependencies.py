from collections.abc import Callable
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import AppenderQuery

from src import utils
from src.api.models import ProductsModel, UsersModel
from src.database import database, models, repository
from src.database.database import get_db_session
from src.database.models import Products
from src.database.repository import DatabaseRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_repository(
    model: type[models.BaseTableModel],
) -> Callable[[AsyncSession], repository.DatabaseRepository]:
    def func(session: AsyncSession = Depends(database.get_db_session)):
        return repository.DatabaseRepository(model, session)

    return func


RepositoryDB = Annotated[
    DatabaseRepository[models.Users],
    Depends(get_repository(models.Users)),
]


async def get_current_user(
    user_repository: RepositoryDB,
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = utils.decode_access_token(token)
    if payload is None:
        raise credentials_exception

    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception

    try:
        user = await user_repository.filter_user_name(username=username)
        if user is None:
            raise credentials_exception

        products = user.favourite_products
        result = UsersModel.model_validate(user)
        result.favourites = products

        return result
    except ValueError as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=e
        )
