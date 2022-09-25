# Define all routes related to authentication/login/account creation
# from app.webtools.decorators import response
from app.webtools.mount import init_template
from app.webtools.viewmodel import DefaultView
from fastapi import APIRouter, Request
from rich import print

t = init_template()
user_router = APIRouter()


@user_router.get("/")
async def get_home(request: Request):
    context = DefaultView()

    if request.headers.get("hx-request"):
        print(request.headers)
        return t.TemplateResponse(
            "index.html",
            {
                "request": request,
            } | context.to_dict(),
            block_name="nav_menu"
        )

    return t.TemplateResponse(
            "index.html",
            {
                "request": request,
            } | context.to_dict()
    )


@user_router.get("/edit")
async def get_edit(request: Request, nav_select: str | None = None):

    print(nav_select)
    if nav_select:
        return t.TemplateResponse(
            "shared/partial/splash_edit_example.html",
            {
                "request": request,
                "nav_select": nav_select
            },
            block_name="nav_menu",

        )

    return t.TemplateResponse(
            "shared/partial/splash_edit_example.html",
            {
                "request": request,
                "nav_select": nav_select,
            }
        )

@user_router.put("/edit")
async def put_edit(request: Request):
    print(request.headers)
    return t.TemplateResponse(
            "index.html",
            {
                "request": request,
            },
            block_name="example_edit"
        )

@user_router.get("/{nav_select}")
async def get_user_home(request: Request, nav_select: str | None = None):

    print(nav_select)
    if nav_select:
        return t.TemplateResponse(
            "index.html",
            {
                "request": request,
                "nav_select": nav_select
            },
            block_name="nav_menu",

        )

    return t.TemplateResponse(
            "index.html",
            {
                "request": request,
                "nav_select": nav_select,
            }
        )
