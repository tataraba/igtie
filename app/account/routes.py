# Define all routes related to authentication/login/account creation
# from app.webtools.decorators import response
from app.webtools.mount import init_template
from app.webtools.viewmodel import DefaultView
from fastapi import APIRouter, Request

t = init_template()
user_router = APIRouter()


@user_router.get("/")
async def get_home(request: Request):
    context = DefaultView()
    return t.TemplateResponse(
            "index.html",
            {
                "request": request,
            } | context.to_dict()
    )


@user_router.get("/{nav_select}")
async def get_user_home(request: Request, nav_select: str | None = None):
    print(request.headers.get("HX-Request"))

    if not nav_select:
        return t.TemplateResponse(
            "index.html",
            {
                "request": request,
            }
        )

    return t.TemplateResponse(
            "index.html",
            {
                "request": request,
                "nav_select": nav_select,
            }
        )
