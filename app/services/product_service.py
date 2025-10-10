from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, company_id: int, product_data: ProductCreate):
        new_product = Product(
            name=product_data.name,
            price=product_data.price,
            description=product_data.description,
            company_id=company_id
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def list_products(self):
        products = self.db.query(Product).all()
        return products

    def get_product(self, product_id: int):
        product = self.db.query(Product).filter(
            Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def update_product(self, product_id: int, product_data: ProductCreate):
        product = self.get_product(product_id)
        product.name = product_data.name
        product.price = product_data.price
        product.description = product_data.description
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int):
        product = self.get_product(product_id)
        self.db.delete(product)
        self.db.commit()
        return {"detail": "Product deleted"}
