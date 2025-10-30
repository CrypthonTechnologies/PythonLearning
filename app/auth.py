from datetime import datetime, timedelta,timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.database import get_db
from fastapi.security import HTTPAuthorizationCredentials
from app.schemas.user_response import UserJWTPayload
from config import ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer_scheme = HTTPBearer()


# ---------------- PASSWORD VERIFY ---------------- #
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# ---------------- PASSWORD GET HASH ---------------- #
def get_password_hash(password):
    return pwd_context.hash(password)


# ---------------- TOKEN CREATION ---------------- #
def create_access_token(user_obj: UserJWTPayload):
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode = {
        "sub":str (user_obj.id),
        "username": user_obj.username,
        "full_name": user_obj.full_name,
        "exp": expire
                   }

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ---------------- VERIFY CURRENT USER ---------------- #
def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token.credentials, SECRET_KEY,
                             algorithms=[ALGORITHM])
        user_id= payload.get("sub")
        if user_id is None :
            raise credential_exception

    except JWTError as e:
        print(f"JWT Error: {str(e)}")
        raise credential_exception


    db_user = db.query(User).filter(User.id == int(user_id)).first()
    if db_user is None:
        raise credential_exception
    return db_user
