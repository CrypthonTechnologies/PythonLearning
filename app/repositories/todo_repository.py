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

    def create(self, title:str,description:str,published:bool):
        created_todo = Todo(title=title,description=description,published=published)
        self.db.add(created_todo)
        self.db.commit()
        return created_todo

    def update(self,todo_id:int,title:str,description:str,published:bool):
        updated_todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        if not updated_todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="todo item not found")

        updated_todo.title = title
        updated_todo.description = description
        updated_todo.published = published
        self.db.commit()
        return updated_todo

    def delete(self, todo: Todo):
        self.db.delete(todo)
        self.db.commit()
