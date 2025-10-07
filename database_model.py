from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Product(Base):
    
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description= Column(String)
    price=Column(Float)
    quantity=Column(Integer)


class User(Base):
    __tablename__ = "users"

    id= Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    password=Column(String)