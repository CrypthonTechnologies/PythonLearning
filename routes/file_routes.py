import uuid
import os
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
import db.database_model as database_model
from auth import get_current_user

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    current_user: database_model.User = Depends(
        get_current_user),  # ✅ ADD THIS
    db: Session = Depends(get_db)
):
    # 🔒 1. Sanitize: generate safe unique name
    ext = os.path.splitext(file.filename)[1].lower()
    safe_name = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(UPLOAD_DIR, safe_name)

    # 💾 2. Save file
    with open(path, "wb") as f:
        f.write(await file.read())

    # 📝 3. Save minimal metadata — now you have current_user!
    db_file = database_model.UserFile(
        filename=safe_name,
        original_name=file.filename,
        user_id=current_user.id  # ✅ Now this works!
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {"filename": file.filename, "saved_as": safe_name}


@router.get("/list/")
async def list_files(
    current_user: database_model.User = Depends(
        get_current_user),  # already there
    db: Session = Depends(get_db)
):
    files = db.query(database_model.UserFile).filter(
        database_model.UserFile.user_id == current_user.id
    ).all()
    return {"files": [f.original_name for f in files]}
