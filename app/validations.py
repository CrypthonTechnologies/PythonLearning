# app/validations/common_validation.py
from fastapi import HTTPException, status

def not_found_exception(entity: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity} not found"
    )

def already_exists_exception(entity: str):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"{entity} already exists"
    )

def invalid_credentials_exception():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User Invalid credentials"
    )

def handle_value_error(e: ValueError):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(e)
    )