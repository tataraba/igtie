from importlib import import_module
from pathlib import Path
from typing import Iterator

import jinja_partials  # type: ignore
from app.core.config import get_app_settings
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

settings = get_app_settings()
app_settings = settings.more_settings
ROOT = settings.APP_DIR


def init_template() -> Jinja2Templates:
    """Initializes Jinja2 templates."""
    templates = Jinja2Templates(ROOT / app_settings.templates_dir)

    jinja_partials.register_starlette_extensions(templates)

    return templates


def incl_static(app) -> None:
    """Mount directory for static files."""
    app.mount(
        "/static", StaticFiles(directory=ROOT / app_settings.static_dir), name="static"
    )


def get_modules(module) -> Iterator[str]:
    """Returns all .py modules in given file_dir

    Args:
        module (str): Name of directory to begin recursive search

    Yields:
        Iterator[str]: The generator contains paths to modules
        with dot notation starting at project root.
        (For example: "app.models.user")
    """
    file_dir = Path(settings.APP_DIR / module)
    idx_app_root = len(settings.APP_DIR.parts) - 1  # index of app root
    modules = [f for f in list(file_dir.rglob("*.py")) if not f.stem == "__init__"]
    for filepath in modules:
        yield (".".join(filepath.parts[idx_app_root:])[0:-3])


def dynamic_loader(module, compare) -> list:
    """Iterates over all .py files in `module` directory, finding all classes that
    match `compare` function.

    Other classes/objects in the module directory will be ignored.

    Returns unique items found.

    Args:
        module (str): Directory name to search recursively
        compare (function): Boolean comparison of all py files in
        `module` directory

    Returns:
        list: All modules that match the `compare` function.
    """
    items = []
    for mod in get_modules(module):
        module = import_module(mod)
        if hasattr(module, "__all__"):
            objs = [getattr(module, obj) for obj in module.__all__]
            items += [o for o in objs if compare(o) and o not in items]
    return items
