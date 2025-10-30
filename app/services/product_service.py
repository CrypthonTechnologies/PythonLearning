from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)
        self.db = db

    def create_product(self, product_model):
        existing_product = self.repo.get_by_name_and_company(product_model.company_id, product_model.name)
        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This product already exists for the company"
            )

        created_product = self.repo.create(product_model)
        self.db.commit()
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

    def update_product(self, product_id: int, product_model):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        updated = self.repo.update(product_id,product_model)
        self.db.commit()
        return  updated

    def delete_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        deleted = self.repo.delete(product)
        self.db.commit()
        return deleted
