from pydantic import BaseModel,Field,field_validator
from typing import Optional
import re
class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=15)
    password: str = Field(..., min_length=3)
    full_name: Optional[str] = None
    bio: Optional[str] = "no bio provided"
    profile: Optional[str] = None


    @field_validator("username")
    def validate_username(cls, value):
        if not value:
            raise ValueError("Username cannot be empty")
        # Must start with a letter, then 2–14 more of allowed chars (total 3–15)
        pattern = r"^[A-Za-z][A-Za-z0-9_.-]{2,14}$"
        if not re.match(pattern, value):
            raise ValueError(
                "Username must start with a letter, be 3–15 characters long, "
                "and can only contain letters, digits, underscores (_), dots (.), or dashes (-)."
            )
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if not value:
            raise ValueError("Password cannot be empty")
        if len(value) < 3:
            raise ValueError("Password must be at least 3 characters long.")

        # Check for at least one uppercase letter
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")

        # Check for at least one digit
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit.")

        # ✅ Special characters are OPTIONAL — no check needed!
        return value

class UserUpdateRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=15)
    full_name: Optional[str] = None
    bio: Optional[str] = None
    profile: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserProfileResponse(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    profile: Optional[str] = None


class TokenResponse(BaseModel):
    access_token: str


class UserJWTPayload(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None

class MessageResponse(BaseModel):
    message: str


