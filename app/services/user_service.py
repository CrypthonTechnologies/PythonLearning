from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.auth import get_password_hash, verify_password, create_access_token
from fastapi import HTTPException, status


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = self.db.query(User).filter(
            User.username == user.username).first()
        if db_user:
            raise ValueError("Username already registered")
        hashed_pw = get_password_hash(user.password)
        new_user = User(username=user.username, password=hashed_pw)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
