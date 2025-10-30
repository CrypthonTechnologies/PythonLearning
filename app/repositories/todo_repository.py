from sqlalchemy.orm import Session
from app.models.todo import Todo
from fastapi import HTTPException, status
class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_todo(self,  skip: int, limit: int):
        return self.db.query(Todo).offset(skip).limit(limit).all()

    def get_todo_by_title(self, title: str):
        return self.db.query(Todo).filter(Todo.title == title).first()

    def get_todo_by_id(self, todo_id: int):
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def create(self, todo_model):

        self.db.add(todo_model)
        return todo_model

    def update(self,todo_id:int,todo_model):
        updated_todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        updated_todo.title = todo_model.title
        updated_todo.description = todo_model.description
        updated_todo.published = todo_model.published

        return updated_todo

    def delete(self, todo: Todo):
        self.db.delete(todo)

