from fastapi import FastAPI

from src.api.routes.auth_routes import auth_router
from src.api.routes.products_routes import products_router
from src.api.routes.users_routes import users_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)


@app.get("/healtz")
def read_root():
    return {"Status": "Ok!"}
