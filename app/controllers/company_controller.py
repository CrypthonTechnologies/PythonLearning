from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import CompanyService
from app.database import get_db
from app.auth import get_current_user

router = APIRouter()


@router.post("/", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    return service.create_company(current_user.id, company.name,company.company_type, company.location)


@router.get("/me", response_model=CompanyResponse)
def get_my_company(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    return service.get_company(current_user.id)


@router.put("/me", response_model=CompanyResponse)
def edit_my_company(
        company: CompanyCreate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    return service.edit_company(current_user.id, company.name, company.company_type, company.location)


@router.delete("/me", dependencies=[Depends(get_current_user)])
def delete_my_company(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    return service.delete_company(current_user.id)
