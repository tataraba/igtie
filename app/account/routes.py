# Define all routes related to authentication/login/account creation
from fastapi import APIRouter, Request

user_router = APIRouter()


@user_router.get("/")
async def get_home(request: Request):
    return {"test": "complete"}
