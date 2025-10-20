from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_my_product(self,company_id:int, name: str, price: float, description: str) -> Product:
        product = Product(company_id=company_id, name=name, price=price, description=description)
        self.db.add(product)
        self.db.commit()

        return product

    def list_my_product(self):
        products = self.db.query(Product).all()
        return products

    def get_product_by_id(self, product_id: int):
        product=  self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def update_my_product(self, product_id: int, name: str, price: float, description: str):
        product = self.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        if product:
            self.db.query(Product).filter(Product.id == product_id).update({"name": name, "price": price, "description": description})
            self.db.commit()

        return product


    def delete_my_product(self, product_id: int):
        product = self.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        if product:
            self.db.query(Product).filter(Product.id == product_id).delete()
            self.db.commit()

        return product