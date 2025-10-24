from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self, db: Session):
        self.repo = TodoRepository(db)

    def get_all_todo(self,skip: int, limit: int):
        todos = self.repo.list_todo(skip, limit)
        if not todos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No todos found")

        return todos

    def create_todo(self, title: str, description: str, published: bool):
        existing = self.repo.get_todo_by_title(title)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Todo already exists")

        create_todo = self.repo.create(title,description,published)
        return create_todo

    def update_todo(self, todo_id: int, title: str, description: str, published: bool):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        updated = self.repo.update(todo_id,title,description,published)
        return updated

    def delete_todo(self, todo_id: int):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        deleted = self.repo.delete(todo)
        return deleted
