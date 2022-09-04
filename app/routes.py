# Use to register all routes

from fastapi.routing import APIRouter

from app.account.routes import user_router

all_routes = APIRouter()

all_routes.include_router(user_router, tags=["account"])
