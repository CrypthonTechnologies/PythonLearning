from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.company import Company


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_company_by_user_id(self, user_id: int):
        return self.db.query(Company).filter(Company.user_id == user_id).first()

    def create(self, company: Company):
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return company

    def update(self, company: Company):
        self.db.commit()
        self.db.refresh(company)
        return company

    def delete(self, company: Company):
        self.db.delete(company)
        self.db.commit()
