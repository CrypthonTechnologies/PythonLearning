from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate


class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def create_product(self, company_id: int,name: str,price: float,description: str):
        created = self.repo.create_my_product(company_id,name,price,description)
        return created

    def list_products(self):
        products = self.repo.list_my_product()
        return products

    def get_product(self, product_id: int):
        product = self.repo.get_product_by_id(product_id)
        return product

    def update_product(self, product_id: int, name: str,price: float,description: str):
        product = self.repo.update_my_product(product_id,name,price,description)
        return product

    def delete_product(self, product_id: int):
        product = self.repo.delete_my_product(product_id)