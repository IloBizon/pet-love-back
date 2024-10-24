from fastapi import HTTPException
from fastapi import APIRouter
from services.products import products

router = APIRouter(prefix="/products")

@router.get("/get-products")
async def get_products(sort: str = "1", category: str = None):
    query = {
        "filters": {

        }
    }
    if category != "null" and category != "all" and category:
        query["filters"] = {
            "category": str(category)
        }

    if sort == "null":
        query["sort"] = {
            "price": 1
        }
    else:
        query["sort"] = {
            "price": int(sort)
        }

    print(query["filters"])
    return await products.get_products(sort_query=query["sort"], filter_query=query["filters"])



@router.post("/select-product/{product_id}")
async def select_product(product_id: str,select: bool):
    if select and  len(await get_selected_products()) >= 3:
        raise HTTPException(status_code=400, detail="Выбранных продуктов не может быть больше 3")

    return await products.toggle_product_selection(product_id,select)

@router.get("/get-selected-products")
async def get_selected_products():
    return await products.get_selected_products()


@router.post("/insert-fake-products")
    #Наполняет базу данных услугами
async def insert_fake_products():
    result = await products.insert_fake_products()
    return  len(result.inserted_ids)