from sqlalchemy import Column, Integer, String, Float, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserFile(Base):
    __tablename__ = "user_files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)          # safe unique name like "a1b2c3.jpg"
    original_name = Column(String)     # "my_photo.jpg"
    user_id = Column(Integer, ForeignKey("users.id"))

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
