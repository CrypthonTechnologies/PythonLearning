from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int, limit: int):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def get_by_id(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_by_name_and_company(self, company_id: int, name: str):
        return (
            self.db.query(Product)
            .filter(Product.company_id == company_id, Product.name == name)
            .first()
        )

    def create(self,company_id:int,name:str,price:float,description:str):
        created_product = Product(company_id=company_id,name=name,price=price,description=description)
        self.db.add(created_product)
        self.db.commit()
        self.db.refresh(created_product)
        return created_product

    def update(self,product_id:int, name:str, price:float,description:str,):
        product = self.db.query(Product).filter(Product.id == product_id).first()

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
        product.name = name
        product.price = price
        product.description = description

        self.db.commit()
        return product

    def delete(self, product: Product):
        self.db.delete(product)
        self.db.commit()
