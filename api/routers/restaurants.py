from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from geoalchemy2.functions import ST_DWithin
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from typing import List, Optional
from api.database import SessionLocal
from api.models import models
from api.schemas import schemas

import uuid

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.RestaurantOut)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

@router.get("/", response_model=List[schemas.RestaurantOut])
def get_all_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Restaurant).all()

@router.get("/{restaurant_id}", response_model=schemas.RestaurantOut)
def get_restaurant(restaurant_id: str, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@router.get("/nearby", response_model=List[schemas.RestaurantOut])
def get_nearby_restaurants(
    latitude: float = Query(...),
    longitude: float = Query(...),
    radius_meters: int = Query(1000),
    db: Session = Depends(get_db)
):
    point = from_shape(Point(longitude, latitude), srid=4326)

    # Join restaurant + location and filter by radius
    query = (
        db.query(models.Restaurant)
        .join(models.Location)
        .filter(ST_DWithin(models.Location.coordinates, point, radius_meters))
        .all()
    )

    return query

@router.get("/{restaurant_id}/menu-items", response_model=List[schemas.MenuItemOut])
def get_menu_items_for_restaurant(
    restaurant_id: uuid.UUID,
    exclude_allergen_ids: Optional[List[uuid.UUID]] = Query(default=None),
    db: Session = Depends(get_db)
):
    # Get restaurant and menu
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant or not restaurant.menu:
        raise HTTPException(status_code=404, detail="Restaurant or menu not found")

    query = db.query(models.MenuItem).filter(models.MenuItem.menu_id == restaurant.menu.id)

    if exclude_allergen_ids:
        # Exclude items that have any of the allergens
        query = query.filter(
            ~models.MenuItem.allergens.any(models.Allergen.id.in_(exclude_allergen_ids))
        )

    return query.all()