import uvicorn
import asyncio
from fastapi import FastAPI
from routes.producs import products
from routes.bids import bids
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(bids.router)


async def start():
    uvicorn.run("main:app",log_level="debug" ,port=8000, reload=True)
if __name__ == "__main__":
    asyncio.run(start())


