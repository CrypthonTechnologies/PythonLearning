from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.company import Company
from app.repositories.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, db: Session):
        self.repo = CompanyRepository(db)

    def create_company(self, user_id: int, name: str, company_type: str, location: str):
        existing = self.repo.get_company_by_user_id(user_id)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Company already exists")

        company = Company(user_id=user_id, name=name, company_type=company_type, location=location)
        created = self.repo.create(company)
        return {"message": "Company created successfully", "data": created}

    def get_company(self, user_id: int):
        company = self.repo.get_company_by_user_id(user_id)
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
        return company

    def edit_company(self, user_id: int, name: str, company_type: str, location: str):
        company = self.repo.get_company_by_user_id(user_id)
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

        company.name = name
        company.company_type = company_type
        company.location = location

        self.repo.update(company)
        return {"message": "Company updated successfully"}

    def delete_company(self, user_id: int):
        company = self.repo.get_company_by_user_id(user_id)
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

        self.repo.delete(company)
        return {"message": "Company deleted successfully"}
