from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository
from app.validations import not_found_exception, already_exists_exception


class TodoService:
    def __init__(self, db: Session):
        self.repo = TodoRepository(db)
        self.db = db

    def get_all_todo(self,skip: int, limit: int):
        todos = self.repo.list_todo(skip, limit)
        if not todos:
            not_found_exception("Todo")

        return todos

    def create_todo(self, todo_model):
        existing = self.repo.get_todo_by_title(todo_model.title)
        if existing:
            already_exists_exception("Todo")

        create_todo = self.repo.create(todo_model)
        self.db.commit()
        return create_todo

    def update_todo(self, todo_id: int, todo_model):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            not_found_exception("Todo")

        updated = self.repo.update(todo_id,todo_model)
        self.db.commit()
        return updated

    def delete_todo(self, todo_id: int):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            not_found_exception("Todo")

        deleted = self.repo.delete(todo)
        self.db.commit()
        return deleted
