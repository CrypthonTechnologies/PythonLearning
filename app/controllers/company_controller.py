from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.company import CompanyCreateRequest, CompanyResponse, MessageResponse
from app.services.company_service import CompanyService
from app.database import get_db
from app.auth import get_current_user
from config import config_reader

router = APIRouter()


@router.post("/", response_model=CompanyResponse)
def create_company(
    company: CompanyCreateRequest,
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


@router.put("/update-me",response_model=CompanyResponse)
def edit_my_company(
        company: CompanyCreateRequest,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    return service.edit_company(current_user.id, company.name, company.company_type, company.location)


@router.delete("/delete-me",response_model=MessageResponse)
def delete_my_company(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    service.delete_company(current_user.id)
    return MessageResponse(message=config_reader.get_value("COMPANY_DELETE_MESSAGE"))
