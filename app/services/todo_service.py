from fastapi import HTTPException, status
from app.models.todo import Todo
from app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self, db):
        self.repo = TodoRepository(db)

    def get_all_todo(self,user_id:int,skip: int, limit: int):
        todos = self.repo.list_todo(user_id,skip, limit)
        if not todos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No todos found")

        return todos

    def create_todo(self, title: str, description: str, published: bool, user_id: int):
        existing = self.repo.get_todo_by_title(title)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Todo already exists")

        todo = Todo(title=title, description=description, published=published, user_id=user_id)
        create_todo = self.repo.create(todo)
        return create_todo

    def update_todo(self, todo_id: int, title: str, description: str, published: bool):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        todo.title = title
        todo.description = description
        todo.published = published

        updated = self.repo.update(todo)
        return {"message": "Todo updated successfully", "data": updated}

    def delete_todo(self, todo_id: int):
        todo = self.repo.get_todo_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        self.repo.delete(todo)
        return {"message": "Todo deleted successfully"}
