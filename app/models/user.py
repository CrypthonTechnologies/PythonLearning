from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    full_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    profile = Column(String, nullable=True)

    company= relationship("Company",back_populates="user", uselist=False)

