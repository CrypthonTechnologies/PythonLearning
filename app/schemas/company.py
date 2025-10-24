from pydantic import BaseModel
from typing import List, Optional
from app.schemas.product import ProductResponse


class CompanyCreateRequest(BaseModel):
    name: str
    location: str
    company_type: str

class CompanyResponse(BaseModel):
    id: int
    name: str
    location: str
    company_type: str
    products: List[ProductResponse] = []

class MessageResponse(BaseModel):
    message: str

