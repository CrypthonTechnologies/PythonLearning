from fastapi import Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from schemas.model import Product
from db.database import SessionLocal, engine
import db.database_model as database_model
from sqlalchemy.orm import Session
from auth import get_current_user

router = APIRouter()


products = [
    Product(id=1, name="Laptop", description="A high-performance laptop",
            price=999.99, quantity=10),
    Product(id=2, name="Smartphone",
            description="A latest model smartphone", price=699.99, quantity=25),
    Product(id=3, name="Headphones",
            description="Noise-cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="Monitor", description="4K UHD Monitor",
            price=299.99, quantity=8),
    Product(id=5, name="Keyboard", description="Mechanical keyboard",
            price=89.99, quantity=30),
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    count = db.query(database_model.Product).count()

    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))

        db.commit()


init_db()


@router.get("/", dependencies=[Depends(get_current_user)])
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()
    return db_products


@router.get("/{id}", dependencies=[Depends(get_current_user)])
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(
        database_model.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"


@router.post("/", dependencies=[Depends(get_current_user)])
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product


@router.put("/{id}", dependencies=[Depends(get_current_user)])
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(
        database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated successfully"
    else:
        return "product not found"


@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(
        database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
    else:
        return "product not found"
