from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self, db: Session):
        self.repo = TodoRepository(db)
        self.db = db

    def get_all_todo(self,skip: int, limit: int):
        todos = self.repo.list_todo(skip, limit)
        if not todos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No todos found")

        return todos

    def create_todo(self, todo_model):
        existing = self.repo.get_todo_by_title(todo_model.title)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Todo already exists")

        create_todo = self.repo.create(todo_model)
        self.db.commit()
        return create_todo

    def update_todo(self, todo_id: int, todo_model):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        updated = self.repo.update(todo_id,todo_model)
        self.db.commit()
        return updated

    def delete_todo(self, todo_id: int):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        deleted = self.repo.delete(todo)
        self.db.commit()
        return deleted
