from pydantic import BaseModel
from typing import List
from app.enum.company_enum import CompanyType
from app.schemas.product_response import ProductResponse


class CompanyResponse(BaseModel):
    id: int
    name: str
    location: str
    company_type: CompanyType
    products: List[ProductResponse] = []

class MessageResponse(BaseModel):
    message: str