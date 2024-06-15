from src.scrapping_data.scrapping_data import *
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

comapre_product = APIRouter(prefix="/compare-products")


@comapre_product.get("/", status_code=status.HTTP_200_OK)
def compare_product(product: str):
    product_shop1 = search_komputronik(product)
    product_shop2 = search_morele_net(product)
    product_shop3 = search_euro_agd(product)

    # Create response
    response = {
        "product_name": product,
        "shops": {
            "komputronik": product_shop1,
            "morele": product_shop2,
            "euro": product_shop3
        }
    }

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
