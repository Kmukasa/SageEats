from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import models
from api.schemas import schemas
from typing import List, Optional


import uuid

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}/safe-menu-items", response_model=List[schemas.MenuItemOut])
def get_safe_menu_items_for_user(
    user_id: uuid.UUID,
    restaurant_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    # Get user and their allergens
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_allergen_ids = [
        allergen.id for allergen in user.allergens
    ]

    # Get restaurant and menu
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant or not restaurant.menu:
        raise HTTPException(status_code=404, detail="Restaurant or menu not found")

    query = db.query(models.MenuItem).filter(
        models.MenuItem.menu_id == restaurant.menu.id
    )

    if user_allergen_ids:
        query = query.filter(
            ~models.MenuItem.allergens.any(models.Allergen.id.in_(user_allergen_ids))
        )

    return query.all()

