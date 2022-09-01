# TODO: Routes here should include requests/responses
# pertaining to a user's account management/profile

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def user_home(request: Request):
    return "<h2>Hi User</h2>"
