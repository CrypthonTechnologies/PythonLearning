from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, username: str, hashed_pw: str):
        if self.repo.create_user(username, hashed_pw):
            raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User created successfully")

        return self.repo.create_user(username, hashed_pw)

    def get_user(self, user_id: int):
        me = self.repo.get_by_me(user_id)
        return me


    def delete_user(self, user_id: int):
        me = self.repo.delete_user(user_id)
        return me
