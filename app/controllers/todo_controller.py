from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.database import get_db
from app.schemas.todo import TodoResponse,TodoRequest

from app.services.todo_service import TodoService

router = APIRouter()

@router.get("/", response_model=List[TodoResponse])
def get_all(
        skip: int = 0, limit: int = 10,
db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    todo_service = TodoService(db)
    return todo_service.get_all_todo(current_user.id,skip,limit)


@router.post("/", response_model=TodoResponse)
def create(todo : TodoRequest,
           db: Session = Depends(get_db),
           current_user=Depends(get_current_user)):

    todo_service = TodoService(db)
    return todo_service.create_todo(todo.title,todo.description,todo.published,current_user.id)



@router.put("/{todo_id}")
def update(todo_id:int,
           todo : TodoRequest,
           db: Session = Depends(get_db),
           ):

    todo_service = TodoService(db)
    return todo_service.update_todo(todo_id,todo.title,todo.description,todo.published)



@router.delete("/{todo_id}")
def delete(todo_id:int,
           db: Session = Depends(get_db),
          ):

    todo_service = TodoService(db)
    return todo_service.delete_todo(todo_id)