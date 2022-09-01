from fastapi.routing import APIRouter

from .user import router

all_routes = APIRouter()

all_routes.include_router(router, tags=["main"])
