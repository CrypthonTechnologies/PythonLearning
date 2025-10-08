from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from model import CreateUser, User, Token
from database import SessionLocal
import database_model
from auth import bcrypt_context, create_access_token, get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create user api
@router.post("/register", response_model=User)
def register_user(user: CreateUser, db: Session = Depends(get_db)):
    db_user = db.query(database_model.User).filter(
        database_model.User.username == user.username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="username already exists"
        )
    hashed_pass = bcrypt_context.hash(user.password)
    new_user = database_model.User(
        username=user.username, password=hashed_pass  )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



# login for user api
@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(database_model.User).filter(
        database_model.User.username == form_data.username).first()
    if not db_user or not bcrypt_context.verify(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials"
        )
    token = create_access_token(
        username=form_data.username, user_id=db_user.id)
    return {"access_token": token, "token_type": "bearer"}


# get current user api and protected route
@router.get("/me", response_model=User)
def get_me(current_user: database_model.User = Depends(get_current_user)):
    return current_user

@router.post("/logout")
def logout():
    return {"message": "logout successfully"}


