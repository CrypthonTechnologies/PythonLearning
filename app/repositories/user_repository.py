from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id ).first()

    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create(self, user_model):
        self.db.add(user_model)

        return user_model

    def update_user(self,user:User,user_data):

        user.username = user_data.username
        user.full_name = user_data.full_name
        user.bio = user_data.bio
        user.profile = user_data.profile

        return user

    def delete(self, user: User):
        self.db.delete(user)

