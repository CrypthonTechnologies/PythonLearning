from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database_model
from schemas.model import Post
from db.database import SessionLocal
from auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_all_post(db: Session = Depends(get_db)):
    db_posts = db.query(database_model.Post).all()
    return db_posts


@router.get("/{post_id}", dependencies=[Depends(get_current_user)])
async def get_by_id(post_id: int, db: Session = Depends(get_db)):
    db_posts = db.query(database_model.Post).filter(
        database_model.Post.post_id == post_id).first()
    if db_posts:
        return db_posts
    return "Post not found"


@router.post("/", dependencies=[Depends(get_current_user)])
async def create_post(post: Post, db: Session = Depends(get_db)):
    db.add(database_model.Post(**post.model_dump()))
    db.commit()
    return post


@router.put("/{post_id}", dependencies=[Depends(get_current_user)])
async def update_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    db_post = db.query(database_model.Post).filter(
        database_model.Post.post_id == post_id).first()
    if db_post:
        db_post.title = post.title
        db_post.description = post.description
        db.commit()
        return "Post updated successfully"
    else:
        return "Post not found"


@router.delete("/{post_id}", dependencies=[Depends(get_current_user)])
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(database_model.Post).filter(
        database_model.Post.post_id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return "Post deleted successfully"
    else:
        return "Post not found"
