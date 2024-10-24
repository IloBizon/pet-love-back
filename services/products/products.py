from bson import ObjectId
from fastapi import HTTPException

from models.products import ProductCollection
from services.database import database
from mocks.products import products


async def get_products(sort_query, filter_query):
    services = ProductCollection(services=await database.products_collection.find(
        filter_query
    ).sort(sort_query).to_list())
    return services.services


async def get_product_by_id(object_id: str):
    product = await database.products_collection.find_one({
        "_id": ObjectId(object_id)
    })
    return serialize_product(product)



async def toggle_product_selection(product_id:str, select: bool):
    res = await database.products_collection.update_one({
        "_id": ObjectId(product_id)
    },
    [{
        "$set":{
            "selected": select
        }
    }])
    return res.modified_count


async def get_selected_products():
    products = await database.products_collection.find({
        "selected": True
    }).to_list()
    return [serialize_product(i) for i in products]



def serialize_product(product):
    return {
        "id": str(product["_id"]),
        "title": product["title"],
        "description": product["description"],
        "category": product["category"],
        "price": product["price"],
        "selected": product["selected"]
    }


async def insert_fake_products():
    if await database.products_collection.count_documents({}) == 0:
        return await database.products_collection.insert_many(products)
    else:
        raise HTTPException(status_code=403, detail="Database already has this products!")