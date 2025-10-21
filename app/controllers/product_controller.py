from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService
from app.services.company_service import CompanyService
from app.database import get_db
from app.auth import get_current_user


router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    company_service = CompanyService(db)
    product_service = ProductService(db)
    company = company_service.get_company(current_user.id)
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="no company found")

    return product_service.create_product(company.id, product.name,product.price,product.description)


@router.get("/", response_model=list[ProductResponse])
def list_product(
    skip: int = 0, limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    product_service = ProductService(db)
    return product_service.list_products(skip,limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    product_service = ProductService(db)
    return product_service.get_product(product_id)

@router.put("/{product_id}")
def update_product_by_id(
        product_id: int,
        product: ProductCreate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)):
    product_service = ProductService(db)
    return product_service.update_product(product_id,product.name,product.price,product.description)

@router.delete("/{product_id}")
def delete_product_by_id(
        product_id: int,
        db: Session = Depends(get_db),
current_user=Depends(get_current_user)
        ):
    product_service = ProductService(db)
    return product_service.delete_product(product_id)