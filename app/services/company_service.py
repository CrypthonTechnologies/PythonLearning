from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate


class CompanyService:
    def __init__(self, db: Session):
        self.db = db

    def create_company(self, user_id: int, company_data: CompanyCreate):
        existing = self.db.query(Company).filter(
            Company.user_id == user_id).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="user already has a company")

        new_company = Company(
            name=company_data.name,
            location=company_data.location,
            user_id=user_id
        )
        self.db.add(new_company)
        self.db.commit()
        self.db.refresh(new_company)
        return new_company

    def get_my_company(self, user_id: int):
        company = self.db.query(Company).filter(
            Company.user_id == user_id).first()
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
        return company

    def edit_company(self, user_id: int, company_data: CompanyCreate):
        company = self.db.query(Company).filter(
            Company.user_id == user_id
        ).first()
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="company not found"
            )
        company.name = company_data.name
        company.location = company_data.location
        self.db.commit()
        self.db.refresh(company)
        return company

    def delete_company(self, user_id: int):
        company = self.db.query(Company).filter(
            Company.user_id == user_id
        ).first()
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="company not found"
            )
        self.db.delete(company)
        self.db.commit()
        return {"detail": "company deleted"}
