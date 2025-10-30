from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository
from app.validations import already_exists_exception, not_found_exception


class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)
        self.db = db

    def create_product(self, product_model):
        existing_product = self.repo.get_by_name_and_company(product_model.company_id, product_model.name)
        if existing_product:
            already_exists_exception("Product")

        created_product = self.repo.create(product_model)
        self.db.commit()
        return created_product

    def list_products(self, skip: int, limit: int):
        products = self.repo.get_all(skip, limit)
        if not products:
            not_found_exception("Product")
        return products

    def get_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            not_found_exception("Product")
        return product

    def update_product(self, product_id: int, product_model):
        product = self.repo.get_by_id(product_id)
        if not product:
            not_found_exception("Product")

        updated = self.repo.update(product_id,product_model)
        self.db.commit()
        return  updated

    def delete_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            not_found_exception("Product")
        deleted = self.repo.delete(product)
        self.db.commit()
        return deleted
