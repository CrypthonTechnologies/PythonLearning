from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self, db):
        self.repo = TodoRepository(db)

    def get_all_todo(self):
        todo_lists = self.repo.list_todo()
        return todo_lists

    def create_todo(self,title:str,description:str,published:bool):
        created = self.repo.create_my_todo(title,description,published)
        return created

    def update_product(self, todo_id:int,title:str,description:str,published:bool):
        updated = self.repo.update_my_todo(todo_id,title,description,published)
        return updated

    def delete_product(self,todo_id):
        deleted = self.repo.delete_my_todo(todo_id)
        return deleted