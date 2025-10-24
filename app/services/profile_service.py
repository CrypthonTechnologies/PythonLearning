from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.profile_repository import ProfileRepository

class ProfileService:
    def __init__(self, db: Session):
        self.repo = ProfileRepository(db)


    def get_profile(self, user_id: int):
        profile = self.repo.get_by_user_id(user_id)
        if not profile:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
        return profile
