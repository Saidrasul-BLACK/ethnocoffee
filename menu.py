from fastapi import APIRouter, Depends, UploadFile, File
import shutil
import os
from sqlalchemy.orm import Session
from database import SessionLocal
from models import MenuItem, MenuAvailability

router = APIRouter()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
@router.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"image_url": f"/static/{file.filename}"}






def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_menu(restaurant_id: int, db: Session = Depends(get_db)):
    menu = db.query(MenuItem).join(MenuAvailability).filter(
        MenuAvailability.restaurant_id == restaurant_id,
        MenuAvailability.is_available == True
    ).all()
    return menu
