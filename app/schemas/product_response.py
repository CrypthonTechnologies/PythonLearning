from typing import Optional

from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description:  Optional[str] = None



class MessageResponse(BaseModel):
    message: str