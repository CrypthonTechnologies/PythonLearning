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
db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    todo_service = TodoService(db)
    return todo_service.get_all_todo()


@router.post("/", response_model=TodoResponse)
def create(todo : TodoRequest,
           db: Session = Depends(get_db),
           current_user=Depends(get_current_user)):

    todo_service = TodoService(db)
    return todo_service.create_todo(todo.title,todo.description,todo.published)



@router.put("/{todo_id}", response_model=TodoResponse)
def update(todo_id:int,
           todo : TodoRequest,
           db: Session = Depends(get_db),
           current_user=Depends(get_current_user)):

    todo_service = TodoService(db)
    return todo_service.update_product(todo_id,todo.title,todo.description,todo.published)



@router.delete("/{todo_id}", response_model=TodoResponse)
def delete(todo_id:int,
           db: Session = Depends(get_db),
           current_user=Depends(get_current_user)):

    todo_service = TodoService(db)
    return todo_service.delete_product(todo_id)