from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.company_request import CompanyCreateRequest
from app.schemas.company_response import CompanyResponse, MessageResponse
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
    company_model = company.to_model()
    company_model.user_id = current_user.id
    return service.create_company(company_model)


@router.get("/me", response_model=CompanyResponse)
def get_my_company(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    return service.get_company(current_user.id)


@router.put("/update-me",response_model=CompanyResponse,dependencies=[Depends(get_current_user)])
def edit_my_company(
        company: CompanyCreateRequest,
        db: Session = Depends(get_db),

):
    service = CompanyService(db)
    company_model = company.to_model()
    return service.edit_company(company_model)


@router.delete("/delete-me",response_model=MessageResponse)
def delete_my_company(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = CompanyService(db)
    service.delete_company(current_user.id)
    return MessageResponse(message=config_reader.get_value("COMPANY_DELETE_MESSAGE"))
