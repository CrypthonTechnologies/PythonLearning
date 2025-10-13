from typing import Optional
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description:  Optional[str] = None
    #
    # class Config:
    #     from_attributes = True
