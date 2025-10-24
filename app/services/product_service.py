from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def create_product(self, company_id: int, name: str, price: float, description: str):
        existing_product = self.repo.get_by_name_and_company(company_id, name)
        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This product already exists for the company"
            )

        created_product = self.repo.create(company_id,name,price,description)
        return created_product

    def list_products(self, skip: int, limit: int):
        products = self.repo.get_all(skip, limit)
        if not products:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found")
        return products

    def get_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return product

    def update_product(self, product_id: int, name: str, price: float, description: str):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        updated = self.repo.update(product_id,name, price, description)
        return  updated

    def delete_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        deleted = self.repo.delete(product)
        return deleted
