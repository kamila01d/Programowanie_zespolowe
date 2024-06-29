from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.api.routes.auth_routes import auth_router
from src.api.routes.comapre_products import compare_product_router
from src.api.routes.products_routes import products_router
from src.api.routes.users_routes import users_router

app = FastAPI(root_path="/p1")
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(compare_product_router)

app.mount(
    "/",
    StaticFiles(
        directory="./Programowanie_zespolowe/src/frontend", html=True
    ),
    name="frontend",
)


@app.get("/healtz")
def read_root():
    return {"Status": "Ok!"}
