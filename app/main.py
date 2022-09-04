from fastapi import FastAPI

from app.extensions import logs
from app.webtools import mount

from .config import get_app_settings
from .routes import all_routes

logs.setup_rich_logger()


def get_app() -> FastAPI:

    get_app_settings.cache_clear()  # for development
    settings = get_app_settings()

    app = FastAPI(**settings.fastapi_kwargs)

    mount.incl_static(app)
    app.include_router(all_routes)

    return app


app = get_app()
