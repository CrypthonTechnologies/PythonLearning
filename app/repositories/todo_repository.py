from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.todo import Todo


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_todo(self):
        todo_lists = self.db.query(Todo).all()
        if todo_lists:
            return todo_lists
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo item not found")


    def create_my_todo(self,title:str,description:str,published:bool):
        todo = Todo( title=title, description=description,published=published)
        if not todo:
            self.db.add(todo)
            self.db.commit()
        if todo:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="this todo already exists")

        return todo


    def update_my_todo(self, todo_id: int,title:str,description:str,published:bool):
        todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo item not found")
        if todo:
            self.db.query(Todo).filter(Todo.id == todo_id).update({"title": title, "description": description, "published": published})
            self.db.commit()

        return todo


    def delete_my_todo(self,todo_id: int):
        todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo item  not found")
        if todo:
            self.db.query(Todo).filter(Todo.id == todo_id).delete()
            self.db.commit()

        return todo