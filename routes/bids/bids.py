from fastapi import APIRouter
from services.bids import bids
from models.bids import Bid

router = APIRouter(prefix="/bids")

@router.get("/get-bids")
async def get_bids():
    resp = await bids.get_bids()
    return resp


@router.post('/send-bid')
async def send_bid(bid: Bid):
    resp = await bids.send_bid(bid)
    return resp
@router.post('/delete-bid/{id}')
async def delete_bid(id:str):
    resp = await bids.delete_bid(id)
    return resp