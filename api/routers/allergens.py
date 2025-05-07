from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.models import models
from api.schemas import schemas
from api.database import SessionLocal

router = APIRouter(prefix="/allergens", tags=["Allergens"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AllergenOut)
def create_allergen(allergen: schemas.AllergenCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Allergen).filter_by(name=allergen.name.lower()).first()
    if existing:
        raise HTTPException(status_code=400, detail="Allergen already exists")

    new_allergen = models.Allergen(name=allergen.name.lower())
    db.add(new_allergen)
    db.commit()
    db.refresh(new_allergen)
    return new_allergen

@router.get("/", response_model=List[schemas.AllergenOut])
def list_allergens(db: Session = Depends(get_db)):
    return db.query(models.Allergen).all()
