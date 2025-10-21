from sqlalchemy.orm import Session
from app.models.todo import Todo

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_todo(self, user_id: int, skip: int, limit: int):
        return self.db.query(Todo).filter(Todo.user_id == user_id).offset(skip).limit(limit).all()

    def get_todo_by_title(self, title: str):
        return self.db.query(Todo).filter(Todo.title == title).first()

    def get_todo_by_id(self, todo_id: int):
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def create(self, todo: Todo):
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def update(self, todo: Todo):
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def delete(self, todo: Todo):
        self.db.delete(todo)
        self.db.commit()
