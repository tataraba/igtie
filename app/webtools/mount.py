from functools import lru_cache

import jinja_partials
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from ..config import get_app_settings

settings = get_app_settings()
app_settings = settings.more_settings
ROOT = settings.APP_DIR


@lru_cache
def init_template() -> Jinja2Templates:
    """Initializes Jinja2 templates."""
    templates = Jinja2Templates(ROOT / app_settings.templates_dir)
    jinja_partials.register_starlette_extensions(templates)
    return templates


@lru_cache
def incl_static(app) -> None:
    """Mount directory for static files."""
    app.mount(
        "/static", StaticFiles(directory=ROOT / app_settings.static_dir), name="static"
    )
