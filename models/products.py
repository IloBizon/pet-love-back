from typing import Optional, List, Annotated
from pydantic import BaseModel, Field, BeforeValidator


class ProductModel(BaseModel):
    id: Annotated[str, BeforeValidator(str)] = Field(alias="_id", default=None)
    title: str
    description: str
    category: str
    price: int
    selected: Optional[bool] = False


class ChangeProductModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    price: Optional[int]
    selected: Optional[bool]



class ProductCollection(BaseModel):
    services: List[ProductModel]