from pydantic import BaseModel, Field
from typing import Optional

from app.models.todo import Todo


class TodoRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    published: Optional[bool] = Field(default=True)



    def to_model(self):
        return Todo(
            title=self.title,
            description=self.description,
            published=self.published
        )


