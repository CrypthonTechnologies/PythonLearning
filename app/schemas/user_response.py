from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    id: int
    username: str


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
