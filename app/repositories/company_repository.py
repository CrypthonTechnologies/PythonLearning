from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.models.company import Company


class CompanyRepository:
    def __init__(self ,db: Session):
        self.db = db



    def create_my_company(self, user_id: int, name: str, company_type: str, location: str):
        existed=self.db.query(Company).filter(Company.user_id == user_id).first()
        company = Company(user_id=user_id, name=name, company_type=company_type, location=location)
        if existed:
            raise HTTPException(status_code=400, detail="Company already exists")
        if not existed:
            self.db.add(company)
            self.db.commit()
        return company




    def get_my_company(self, user_id: int):
        company = self.db.query(Company).filter(Company.user_id == user_id).first()
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="company not found"
            )
        return company



    def edit_my_company(self, user_id: int,name: str, company_type: str, location: str ):
        existed = self.db.query(Company).filter(Company.user_id == user_id).first()
        if not existed:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="company not found"
            )
        if existed:
            self.db.query(Company).filter(Company.user_id == user_id).update(
                {"name": name, "company_type": company_type, "location": location}
            )
            self.db.commit()

        return existed


    def delete_my_company(self, user_id: int):
        existed = self.db.query(Company).filter(Company.user_id == user_id).first()
        if not existed:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="company not found"
            )
        if existed:
            self.db.query(Company).filter(Company.user_id == user_id).delete()
            self.db.commit()

        return existed


