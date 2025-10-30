from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.validations import already_exists_exception, not_found_exception


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)
        self.db = db

    def create_user(self,user_model):
        existing_user = self.repo.get_by_username(user_model.username)
        if existing_user:
            already_exists_exception("User")

        create = self.repo.create(user_model)
        self.db.commit()
        return create

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            not_found_exception("User")
        return user

    def updated_user(self, user_id:int ,user_data):
        user = self.get_user(user_id)
        if not user:
            not_found_exception("User")
        updated = self.repo.update_user(user,user_data)
        self.db.commit()
        return updated

    def delete_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            not_found_exception("User")

        deleted = self.repo.delete(user)
        self.db.commit()
        return deleted
