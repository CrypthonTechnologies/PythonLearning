from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.company_repository import CompanyRepository
from app.validations import not_found_exception, already_exists_exception


class CompanyService:
    def __init__(self, db: Session):
        self.repo = CompanyRepository(db)
        self.db = db

    def create_company(self, company_model):
        existing = self.repo.get_company_by_user_id(company_model.user_id)
        if existing:
            already_exists_exception("Company")

        created = self.repo.create(company_model)
        self.db.commit()
        return  created

    def get_company(self, user_id:int):
        company = self.repo.get_company_by_user_id(user_id )
        if not company:
            not_found_exception("Company")
        return company

    def edit_company(self, company_model):
        company = self.repo.get_company_by_user_id(company_model.user_id)
        if not company:
            not_found_exception("Company")

        updated = self.repo.update(company_model)
        self.db.commit()
        return updated

    def delete_company(self, user_id: int):
        company = self.repo.get_company_by_user_id(user_id)
        if not company:
            not_found_exception("Company")

        deleted = self.repo.delete(company)
        self.db.commit()
        return deleted
