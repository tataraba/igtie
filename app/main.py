from fastapi import FastAPI

from app.core import config, log_config, webtools
from app.routes import all_routes


def get_app() -> FastAPI:

    log_config.setup_rich_logger()
    config.get_app_settings.cache_clear()  # for development
    settings = config.get_app_settings()

    app = FastAPI(**settings.fastapi_kwargs)

    webtools.incl_static(app)
    app.include_router(all_routes)

    return app


app = get_app()
