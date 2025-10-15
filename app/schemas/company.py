from pydantic import BaseModel
from typing import List, Optional
from app.schemas.product import ProductResponse


class CompanyCreate(BaseModel):
    name: str
    location: str
    company_type: Optional[str] = None

class CompanyResponse(BaseModel):
    id: int
    name: str
    location: str
    company_type: Optional[str] = None
    products: List[ProductResponse] = []
    #
    # class Config:
    #     from_attributes = True
