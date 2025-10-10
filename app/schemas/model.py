from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        from_attributes = True







class Post(BaseModel):
    post_id: Optional [int] 
    title: str
    description: str


class Token(BaseModel):
    access_token: str
    token_type: str
