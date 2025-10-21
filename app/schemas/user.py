from pydantic import BaseModel,Field


class UserCreate(BaseModel):
    username: str = Field(..., min_length=2, max_length=15, description="User's unique name")
    password: str


class UserResponse(BaseModel):
    id: int
    username: str


    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str