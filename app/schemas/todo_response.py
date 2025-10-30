from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    published: bool
    created_at: datetime





class MessageResponse(BaseModel):
    message: str