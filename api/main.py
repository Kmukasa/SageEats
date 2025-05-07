from fastapi import FastAPI
from api.routers import users, restaurants, menu, menu_items, location, allergens

app = FastAPI()

app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(menu.router)
app.include_router(menu_items.router)
app.include_router(location.router)
app.include_router(allergens.router)