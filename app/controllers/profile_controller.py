from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.services.profile_service import ProfileService

from app.schemas.user import UserProfileResponse

router = APIRouter()


@router.get("/",response_model=UserProfileResponse)
def get_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = ProfileService(db)
    return service.get_profile(current_user.id)
