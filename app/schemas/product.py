from typing import Optional
from pydantic import BaseModel,Field


class ProductCreateRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Product name")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    description: Optional[str] = Field(None, max_length=200)



class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description:  Optional[str] = None
    #
    # class Config:
    #     from_attributes = True



class MessageResponse(BaseModel):
    message: str