# Define all routes related to authentication/login/account creation
from functools import wraps

from app.webtools.decorators import response
from app.webtools.models import DefaultPageView
from fastapi import APIRouter, Request

user_router = APIRouter()


@user_router.get("/")
@response(template_file="index.html")
async def get_home(request: Request):
    # view = DefaultPageView(request)
    context = {"request": request, "hello": "goodbye"}
    return context
