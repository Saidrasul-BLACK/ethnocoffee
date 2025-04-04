from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import MenuItem, MenuAvailability

router = APIRouter()

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