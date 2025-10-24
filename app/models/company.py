from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Company(Base):
    __tablename__ = "company"

    id =Column(Integer, primary_key=True,  index=True)
    name= Column(String)
    location = Column(String)
    company_type = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))


    user= relationship("User", back_populates="company")
    products= relationship("Product", back_populates="company")