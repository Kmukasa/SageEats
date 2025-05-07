from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import models
from api.schemas import schemas
from typing import List
import uuid

router = APIRouter(prefix="/menu-items", tags=["Menu Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MenuItemOut)
def create_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    db_item = models.MenuItem(
        name=item.name,
        description=item.description,
        menu_id=item.menu_id,
        macros_id=item.macros_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    # Attach allergens
    for allergen_id in item.allergen_ids:
        db.add(models.MenuItemAllergens(menu_item_id=db_item.id, allergen_id=allergen_id))
    db.commit()

    return db_item

@router.get("/", response_model=List[schemas.MenuItemOut])
def get_menu_items(db: Session = Depends(get_db)):
    return db.query(models.MenuItem).all()

@router.patch("/{menu_item_id}/allergens", response_model=schemas.MenuItemOut)
def update_menu_item_allergens(
    menu_item_id: uuid.UUID,
    assignment: schemas.AllergenAssignment,
    db: Session = Depends(get_db)
):
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == menu_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    # Fetch allergen objects
    allergens_to_add = db.query(models.Allergen).filter(models.Allergen.id.in_(assignment.allergen_ids)).all()
    if len(allergens_to_add) != len(assignment.allergen_ids):
        raise HTTPException(status_code=400, detail="One or more allergens not found")

    if assignment.mode == "replace":
        menu_item.allergens = allergens_to_add
    elif assignment.mode == "add":
        existing = set(menu_item.allergens)
        menu_item.allergens = list(existing.union(set(allergens_to_add)))

    db.commit()
    db.refresh(menu_item)
    return menu_item


