from api.database import Base
from sqlalchemy import Column, Table, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from geoalchemy2 import Geography
from shapely import wkb

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    macro_goal_protein = Column(Float)
    macro_goal_fat = Column(Float)
    macro_goal_carbs = Column(Float)

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    location_id = Column(UUID(as_uuid=True), ForeignKey("location.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    location = relationship("Location", back_populates="restaurants")
    menu = relationship("Menu", back_populates="restaurant", uselist=False)

class Menu(Base):
    __tablename__ = "menu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey("restaurants.id"))

    restaurant = relationship("Restaurant", back_populates="menu")
    items = relationship("MenuItem", back_populates="menu")

class Macros(Base):
    __tablename__ = "macros"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    protein = Column(Float)
    fat = Column(Float)
    carbs = Column(Float)

menu_item_allergens = Table(
    "menu_item_allergens",
    Base.metadata,
    Column("menu_item_id", UUID(as_uuid=True), ForeignKey("menu_items.id", ondelete="CASCADE"), primary_key=True),
    Column("allergen_id", UUID(as_uuid=True), ForeignKey("allergens.id", ondelete="CASCADE"), primary_key=True)
)

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menu.id"))
    macros_id = Column(UUID(as_uuid=True), ForeignKey("macros.id"), nullable=True)

    menu = relationship("Menu", back_populates="items")
    macros = relationship("Macros")
    allergens = relationship(
    "Allergen",
    secondary=menu_item_allergens,
    back_populates="menu_items"
)

class Allergen(Base):
    __tablename__ = "allergens"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)

    menu_items = relationship(
    "MenuItem",
    secondary=menu_item_allergens,
    back_populates="allergens"
)

# class MenuItemAllergens(Base):
#     __tablename__ = "menu_item_allergens"
#     menu_item_id = Column(UUID(as_uuid=True), ForeignKey("menu_item.id"), primary_key=True)
#     allergen_id = Column(UUID(as_uuid=True), ForeignKey("allergens.id"), primary_key=True)

class Location(Base):
    __tablename__ = "location"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    coordinates = Column(Geography(geometry_type="POINT", srid=4326))

    restaurants = relationship("Restaurant", back_populates="location")

    @property
    def latitude(self):
        if self.coordinates:
            point = wkb.loads(bytes(self.coordinates.data))
            return point.y

    @property
    def longitude(self):
        if self.coordinates:
            point = wkb.loads(bytes(self.coordinates.data))
            return point.x



