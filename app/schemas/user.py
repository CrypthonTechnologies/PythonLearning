from pydantic import BaseModel,Field
from typing import Optional

class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=2, max_length=15, description="User's unique name")
    password: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    profile: Optional[str] = None


class UserUpdateRequest(BaseModel):
    username: str = Field(..., min_length=2, max_length=15, description="User's unique name")
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


class MessageResponse(BaseModel):
    message: str
