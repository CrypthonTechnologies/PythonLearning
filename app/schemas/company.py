from pydantic import BaseModel
from typing import List, Optional
from app.schemas.product import ProductResponse
from app.enum.company_enum import CompanyType

class CompanyCreateRequest(BaseModel):
    name: str
    location: str
    company_type: CompanyType

class CompanyResponse(BaseModel):
    id: int
    name: str
    location: str
    company_type: CompanyType
    products: List[ProductResponse] = []

class MessageResponse(BaseModel):
    message: str

