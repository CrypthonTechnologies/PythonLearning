from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create(self, username: str, hashed_pw: str, full_name: str, bio: str, profile: str):
        new_user = User(username=username, password=hashed_pw, full_name=full_name, bio=bio, profile=profile)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update(self, user_id:int,username: str, full_name: str,bio:str, profile:str,):
        updated_user= self.db.query(User).filter(User.id == user_id).first()
        updated_user.username = username
        updated_user.full_name = full_name
        updated_user.bio = bio
        updated_user.profile = profile

        self.db.commit()
        return updated_user

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()
