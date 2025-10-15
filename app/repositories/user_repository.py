from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import HTTPException,status

class UserRepository:
    def __init__(self, db: Session):
        self.db = db


    def get_by_me(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        return user

    def create_user(self, username: str, hashed_pw: str):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            user = User(username=username, password=hashed_pw)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        if user:
            self.db.delete(user)
            self.db.commit()
        return {"message": "User deleted successfully"}