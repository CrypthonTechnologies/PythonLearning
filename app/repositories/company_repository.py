from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.company import Company


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_company_by_user_id(self, user_id: int):
        return self.db.query(Company).filter(Company.user_id == user_id).first()

    def create(self, user_id:int, name:str, company_type:str, location:str):
        created_company = Company(user_id=user_id,name=name, company_type=company_type, location=location)
        self.db.add(created_company)
        self.db.commit()
        return created_company

    def update(self,user_id:int,name: str, company_type: str, location: str):
        updated_company = self.db.query(Company).filter(Company.user_id == user_id).first()
        if not updated_company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Company not found")
        updated_company.name = name
        updated_company.company_type = company_type
        updated_company.location = location

        self.db.commit()

        return updated_company

    def delete(self, company:Company):
        self.db.delete(company)
        self.db.commit()
