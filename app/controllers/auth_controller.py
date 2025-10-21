from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.database import get_db
from app.auth import create_access_token, verify_password, get_password_hash, get_current_user
from app.models.user import User
router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    hashed_pw= get_password_hash(user.password)
    try:
        return service.create_user(user.username, hashed_pw)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/token")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Query using database model
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(db_user.id)
    return {"access_token": token}

@router.get("/me", response_model=UserResponse)
def me(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)):
    service = UserService(db)
    return service.get_user(current_user.id)

@router.delete("/delete")
def delete( db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    service = UserService(db)
    return service.delete_user(current_user.id)
