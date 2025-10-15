from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.company_repository import CompanyRepository



class CompanyService:
    def __init__(self, db: Session):
        self.repo =  CompanyRepository(db)

    def create_company(self, user_id: int,name: str, company_type: str, location: str):

        existed = self.repo.create_my_company(user_id, name, company_type, location)
        if not existed:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
        return existed

    def get_company(self, user_id: int):
        company = self.repo.get_my_company(user_id)
        return company

    def edit_company(self, user_id: int, name: str, company_type: str, location: str):
        updated  =self.repo.edit_my_company(user_id, name, company_type, location)
        return updated

    def delete_company(self, user_id: int):
        deleted  = self.repo.delete_my_company(user_id)
        return deleted
