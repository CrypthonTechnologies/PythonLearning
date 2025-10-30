from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user_request import UserCreateRequest, UserLoginRequest, UserUpdateRequest
from app.schemas.user_response import UserResponse, UserJWTPayload, UserProfileResponse, MessageResponse
from app.services.user_service import UserService
from app.database import get_db
from app.auth import create_access_token, verify_password, get_current_user
from app.models.user import User
from app.validations import invalid_credentials_exception, handle_value_error
from config import config_reader

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreateRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    user_model = user.to_model()
    try:
        return service.create_user(user_model)
    except ValueError as e:
        handle_value_error(e)


@router.post("/token")
def login(user: UserLoginRequest, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    db_user = repo.get_by_username(user.username)

    if not db_user or not verify_password(user.password, db_user.password):
        invalid_credentials_exception()

    user_token = UserJWTPayload(
        id=db_user.id,
        username=db_user.username,
        full_name=db_user.full_name,
    )

    token = create_access_token(user_token)
    return {"access_token": token}


@router.get("/", response_model=UserResponse)
def get_me(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)):
    service = UserService(db)
    return service.get_user(current_user.id)

@router.put("/update", response_model=UserProfileResponse)
def update(
        user:UserUpdateRequest,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
        ):
    service = UserService(db)
    return service.updated_user(current_user.id,user)


@router.delete("/delete",response_model=MessageResponse)
def delete( db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    service = UserService(db)
    service.delete_user(current_user.id)
    return MessageResponse(message=config_reader.get_value("USER_DELETED_SUCCESSFULLY"))