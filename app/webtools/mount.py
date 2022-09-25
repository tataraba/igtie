from functools import lru_cache

from jinja2_fragments.fastapi import Jinja2Blocks
from starlette.staticfiles import StaticFiles

from ..config import get_app_settings

settings = get_app_settings()
app_settings = settings.more_settings
ROOT = settings.APP_DIR


@lru_cache
def init_template() -> Jinja2Blocks:
    """Initializes Jinja2 templates."""
    templates = Jinja2Blocks(
        ROOT / app_settings.templates_dir,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        )  # type:ignore
    return templates


@lru_cache
def incl_static(app) -> None:
    """Mount directory for static files."""
    app.mount(
        "/static", StaticFiles(directory=ROOT / app_settings.static_dir), name="static"
    )
