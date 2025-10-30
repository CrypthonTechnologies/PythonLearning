from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.company import Company


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_company_by_user_id(self, user_id: int):
        return self.db.query(Company).filter(Company.user_id == user_id).first()

    def create(self, company_model):
        self.db.add(company_model)
        return company_model

    def update(self,company_model):
        updated_company = self.db.query(Company).filter(Company.user_id == company_model.user_id).first()
        updated_company.name = company_model.name
        updated_company.company_type = company_model.company_type
        updated_company.location = company_model.location

        return updated_company

    def delete(self, company:Company):
        self.db.delete(company)
