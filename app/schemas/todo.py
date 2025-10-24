from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class TodoRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    published: Optional[bool] = Field(default=True)

    @validator('title')
    def no_empty_title(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v



class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    published: bool
    created_at: datetime

    class Config:
        from_attributes  = True



class MessageResponse(BaseModel):
    message: str