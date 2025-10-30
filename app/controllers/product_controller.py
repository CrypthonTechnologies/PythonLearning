from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.product_request import ProductCreateRequest
from app.schemas.product_response import ProductResponse, MessageResponse
from app.services.product_service import ProductService
from app.services.company_service import CompanyService
from app.database import get_db
from app.auth import get_current_user
from config import config_reader

router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreateRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    company_service = CompanyService(db)
    product_service = ProductService(db)
    company = company_service.get_company(current_user.id)
    product_model = product.to_model()
    product_model.company_id = company.id

    return product_service.create_product(product_model)


@router.get("/", response_model=list[ProductResponse])
def list_product(
    skip: int = 0, limit: int = 10,
    db: Session = Depends(get_db),

):
    product_service = ProductService(db)
    return product_service.list_products(skip,limit)


@router.get("/{product_id}", response_model=ProductResponse,dependencies=[Depends(get_current_user)])
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
):
    product_service = ProductService(db)
    return product_service.get_product(product_id)

@router.put("/{product_id}", response_model=ProductResponse,dependencies=[Depends(get_current_user)])
def update_product_by_id(
        product_id: int,
        product: ProductCreateRequest,
        db: Session = Depends(get_db),):
    product_service = ProductService(db)
    product_model = product.to_model()
    return product_service.update_product(product_id,product_model)

@router.delete("/{product_id}",dependencies=[Depends(get_current_user)],response_model=MessageResponse)
def delete_product_by_id(
        product_id: int,
        db: Session = Depends(get_db),
        ):
    product_service = ProductService(db)
    product_service.delete_product(product_id)
    return MessageResponse(message=config_reader.get_value("PRODUCT_DELETED_SUCCESSFULLY"))