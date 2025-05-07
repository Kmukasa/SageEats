from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from api.models import models
from api.schemas import schemas
from api.database import SessionLocal
from typing import List

router = APIRouter(prefix="/locations", tags=["Locations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.LocationOut)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    point = from_shape(Point(location.longitude, location.latitude), srid=4326)
    db_location = models.Location(
        street_address=location.street_address,
        city=location.city,
        state=location.state,
        zip_code=location.zip_code,
        coordinates=point
    )
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@router.get("/", response_model=List[schemas.LocationOut])
def get_all_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()
