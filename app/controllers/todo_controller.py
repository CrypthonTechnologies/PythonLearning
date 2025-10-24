from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.database import get_db
from app.schemas.todo import TodoResponse, TodoRequest, MessageResponse

from app.services.todo_service import TodoService
from config import config_reader

router = APIRouter()

@router.get("/", response_model=List[TodoResponse])
def get_all(
        skip: int = 0, limit: int = 10,
db: Session = Depends(get_db),

):
    todo_service = TodoService(db)
    return todo_service.get_all_todo(skip,limit)


@router.post("/", response_model=TodoResponse,dependencies=[Depends(get_current_user)])
def create(todo : TodoRequest,
           db: Session = Depends(get_db),
         ):

    todo_service = TodoService(db)
    return todo_service.create_todo(todo.title,todo.description,todo.published)



@router.put("/{todo_id}",response_model=TodoResponse,dependencies=[Depends(get_current_user)])
def update(todo_id:int,
           todo : TodoRequest,
           db: Session  = Depends(get_db),
           ):

    todo_service = TodoService(db)
    return todo_service.update_todo(todo_id,todo.title,todo.description,todo.published)



@router.delete("/{todo_id}",dependencies=[Depends(get_current_user)],response_model=MessageResponse)
def delete(todo_id:int,
           db: Session  = Depends(get_db),
          ):

    todo_service = TodoService(db)
    todo_service.delete_todo(todo_id)
    return MessageResponse(message=config_reader.get_value("ITEM_DELETED_SUCCESSFULLY"))