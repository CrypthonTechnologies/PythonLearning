from pydantic import BaseModel
from app.enum.company_enum import CompanyType
from app.models.company import Company

class CompanyCreateRequest(BaseModel):
    name: str
    location: str
    company_type: CompanyType

    def to_model(self):

        return Company(
            name=self.name,
            location=self.location,
            company_type=self.company_type
        )



