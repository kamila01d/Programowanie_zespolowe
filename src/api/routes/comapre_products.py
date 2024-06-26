import json

from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from src.scrapping_data.scrapping_data import *

compare_product_router = APIRouter(prefix="/compare-products")


@compare_product_router.get("/", status_code=status.HTTP_200_OK)
def compare_product(product: str):
    product_shop1 = search_komputronik(product)
    product_shop2 = search_morele_net(product)
    product_shop3 = search_euro_agd(product)

    merged_json = product_shop1 + product_shop2 + product_shop3

    sorted_json = sorted(merged_json, key=lambda x: x["price"])

    response = sorted_json

    formatted_response = json.dumps(
        response, indent=4, ensure_ascii=False
    )

    return JSONResponse(
        content=formatted_response, status_code=status.HTTP_200_OK
    )
