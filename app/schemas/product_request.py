from typing import Optional
from pydantic import BaseModel,Field

from app.models.product import Product


class ProductCreateRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=200)

    def to_model(self):
        return Product(
            name=self.name,
            price=self.price,
            description=self.description
        )



