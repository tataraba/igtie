# Define all routes related to authentication/login/account creation
from app.webtools.decorators import response
from app.webtools.viewmodel import DefaultView
from fastapi import APIRouter, Request

user_router = APIRouter()


@user_router.get("/")
@response(template_file="index.html")
async def get_home(request: Request, x="another thing"):
    context = DefaultView()
    return context

@user_router.get("/home")
@response(template_file="home.html")
async def get_user_home(request: Request):
    ...
