from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, db: Session):
        self.repo = CompanyRepository(db)
        self.db = db

    def create_company(self, company_model):
        existing = self.repo.get_company_by_user_id(company_model.user_id)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Company already exists")

        created = self.repo.create(company_model)
        self.db.commit()
        return  created

    def get_company(self, user_id:int):
        company = self.repo.get_company_by_user_id(user_id )
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
        return company

    def edit_company(self, company_model):
        company = self.repo.get_company_by_user_id(company_model.user_id)
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

        updated = self.repo.update(company_model)
        self.db.commit()
        return updated

    def delete_company(self, user_id: int):
        company = self.repo.get_company_by_user_id(user_id)
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

        deleted = self.repo.delete(company)
        self.db.commit()
        return deleted
