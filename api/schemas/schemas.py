from pydantic import BaseModel, EmailStr
from typing import Optional, List, Literal
import uuid
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    macro_goal_protein: Optional[float]
    macro_goal_fat: Optional[float]
    macro_goal_carbs: Optional[float]

class UserOut(UserBase):
    id: uuid.UUID

class RestaurantBase(BaseModel):
    name: str
    location_id: Optional[uuid.UUID] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantOut(RestaurantBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True

class LocationBase(BaseModel):
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    latitude: float
    longitude: float

class LocationCreate(LocationBase): 
    pass

class LocationOut(LocationBase):
    id: uuid.UUID
    class Config:
        orm_mode = True

class MenuBase(BaseModel):
    title: str
    description: Optional[str] = None
    restaurant_id: uuid.UUID

class MenuCreate(MenuBase):
    pass

class MenuOut(MenuBase):
    id: uuid.UUID
    date_created: datetime

    class Config:
        orm_mode = True

class MacrosBase(BaseModel):
    protein: float
    fat: float
    carbs: float

class MacrosCreate(MacrosBase): 
    pass

class MacrosOut(MacrosBase):
    id: uuid.UUID
    class Config:
        orm_mode = True

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    menu_id: uuid.UUID
    macros_id: Optional[uuid.UUID] = None
    allergen_ids: List[uuid.UUID] = []

class MenuItemCreate(MenuItemBase): 
    pass

class MenuItemOut(MenuItemBase):
    id: uuid.UUID
    class Config:
        orm_mode = True


class AllergenBase(BaseModel):
    name: str

class AllergenCreate(AllergenBase):
    pass

class AllergenOut(AllergenBase):
    id: uuid.UUID

    class Config:
        orm_mode = True

class AllergenAssignment(BaseModel):
    allergen_ids: List[uuid.UUID]
    mode: Literal["add", "replace"] = "replace"


class NearbySearchQuery(BaseModel):
    latitude: float
    longitude: float
    radius_meters: Optional[int] = 1000  # default 1 km
