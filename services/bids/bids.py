from bson import ObjectId

from models.bids import Bid
from services.database import database

async def send_bid(bid: Bid):
    resp = await database.bids_collection.insert_one(bid.model_dump())
    return resp.acknowledged
async def get_bids():
    bids = await database.bids_collection.find({}).to_list()
    return [serialize_bid(bid) for bid in bids]

async def delete_bid(bid_id: str):
    resp = await database.bids_collection.delete_one(
        {
            "_id": ObjectId(bid_id)
        }
    )
    return resp.deleted_count

def serialize_bid(bid):
    return {
        "id": str(bid["_id"]),
        "date": bid["date"],
        
        "email": bid["email"],
        "name": bid["name"],
        "petName": bid["petName"],
        "phone": bid["phone"],
        "product": bid["product"]
    }
