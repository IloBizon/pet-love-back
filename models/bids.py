from pydantic import BaseModel
from datetime import date


class Bid(BaseModel):
    date: str
    email: str
    name: str
    petName: str
    phone: str
    product: str