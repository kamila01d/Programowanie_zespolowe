from datetime import timedelta

from fastapi import APIRouter, HTTPException, status

from src import utils
from src.api import models, schemas
from src.api.routes.users_routes import UsersRepository
from src.api.schemas import LoginPayload
from src.settings import settings

auth_router = APIRouter(prefix="/users", tags=["auth"])


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: schemas.UsersPayload, user_repository: UsersRepository
):
    db_user = await user_repository.filter_user_name(user.username)

    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered"
        )
    user.password = utils.get_password_hash(user.password)
    new_user = await user_repository.create(user.dict())

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = utils.create_access_token(
        data={"sub": new_user.username},
        expires_delta=access_token_expires,
    )
    return models.Token(access_token=access_token, token_type="bearer")


@auth_router.post("/token", status_code=status.HTTP_200_OK)
async def login_for_access_token(
    user_repository: UsersRepository,
    form_data: LoginPayload,
) -> models.Token:

    user = await user_repository.filter_user_name(form_data.username)

    if not user or not utils.verify_password(
        form_data.password, user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return models.Token(access_token=access_token, token_type="bearer")
