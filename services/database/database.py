import os
from logging import info
from dotenv import load_dotenv,find_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv(find_dotenv())

_CONNECTION_STRING = os.getenv("MONGODB_URL")

_client = AsyncIOMotorClient(_CONNECTION_STRING)
_database = _client.get_database("main")
products_collection = _database.get_collection("products")
bids_collection = _database.get_collection("bids")


async def ping_database():
    ping_response = await _database.command("ping")
    if int(ping_response["ok"]) != 1:
        print("Problem connecting to the database!")
        raise Exception("Problem connecting to the database!")
    else:
        info("Connected to database cluster.")