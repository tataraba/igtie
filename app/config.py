import logging
import secrets
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseModel, BaseSettings, Field

logger = logging.getLogger(__name__)

APP_ROOT = Path(__file__).resolve().parent


class AppConfig(BaseModel):
    """Application configuration using pydantic BaseModel ('more_settings').

    Args:
        BaseModel: pydantic BaseModel class.

    Attributes:
        title: Application title.
        version: Application version.
        debug: Application debug mode.
        static_dir: Name of the static directory folder.
        templates_dir: Name of the templates directory folder.
        docs_url: URL to the documentation. Hidden in production.
        redoc_url: URL to the ReDoc documentation. Hidden in production.
        openapi_url: URL to the OpenAPI documentation. Hidden in production.
        author (:obj:`str`, optional): Author's name.
        description (str): Application description. Used as default meta
        description in HTML.

    Note:
        The `more_settings` attribute is used to access these settings.
    """

    title: str = "MegaNemesis"
    version: str = "0.1.0"
    debug: bool = False
    static_dir: str = "static"
    templates_dir: str = "templates"

    docs_url: Optional[str | None] = "/docs"  # Auto-hidden in PRD
    redoc_url: Optional[str] = "/redoc"  # Auto-hidden in PRD
    openapi_url: Optional[str] = "/openapi.json"

    author: Optional[str] = "Mario Munoz"
    description: str = "Large Opponent."


class GlobalConfig(BaseSettings):
    """Provides configuration elements that can vary between dev, stage, and
    production tiers. This class is inherited by Dev, Stg, Prd variants which
    determine the value of the environment variable to be loaded, based on the
    appropriate prefix. See References for more info.

    References:
        [Rednafi's Blog](https://rednafi.github.io/digressions/python/
        2020/06/03/python-configs.html)

    Args:
        BaseSettings: pydantic BaseSettings.
    """

    more_settings: AppConfig = AppConfig()

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    DISABLE_DOCS: bool = False

    APP_DIR = APP_ROOT

    LOGGER_DIRECTORY: Path = Path(APP_ROOT.parent, "logs")
    LOGGER_FILENAME: str = "igtie.log"
    LOGGER_FILE_MODE: str = "a"  # use `a` for append, `w` for overwrite

    SECRET_KEY: str = secrets.token_urlsafe(32)
    SIGNATURE_ALGORITHM: str | None = "HS256"
    ACCESS_TOKEN_EXPIRES_MINUTES: int | None = None
    CRYPTCONTEXT_SCHEMES: str | None = "bcrypt"

    MONGO_DB_URI: AnyUrl | None = None  # Use this for testing

    MONGO_SCHEME: str = "mongodb"
    MONGO_HOST: str = "localhost"
    MONGO_PORT: str | None = None
    MONGO_USER: str | None = None
    MONGO_PASS: str | None = None
    MONGO_DB: str | None = None
    MONGO_AUTH_DB: str | None = None

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """Creates dictionary of values to pass to FastAPI app
        as **kwargs. Suppress API documentation when in production.

        Returns:
            dict: Includes properties in `AppConfig` and
            disables docs if `prd` is the `ENV_STATE`.
        """
        fastapi_kwargs = self.more_settings.dict()
        if self.DISABLE_DOCS:
            fastapi_kwargs.update(
                {
                    "docs_url": None,
                    "redoc_url": None,
                    "openapi_url": None,
                    "openapi_prefix": None,
                }
            )
        return fastapi_kwargs

    class Config:
        """Loads .env file."""

        env_file: Path = Path(APP_ROOT).parent / ".env"
        env_file_encoding: str = "utf-8"


class DevConfig(GlobalConfig):
    """Development configurations."""

    PYTHONASYNCIODEBUG = 1

    class Config:
        env_prefix: str = "DEV_"


class StgConfig(GlobalConfig):
    """Staging configurations."""

    class Config:
        env_prefix: str = "STG_"


class PrdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        env_prefix: str = "PRD_"


class FactoryConfig:
    """Inherits configuration from GlobalConfig. Depending on `ENV_STATE`,
    it will inherit from DevConfig or PrdConfig. The .env files with "DEV_"
    prefix are loaded for "dev", and "PRD_" prefix for "prd".
    """

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self) -> Any:
        if self.env_state == "dev" or not self.env_state:
            if not self.env_state:
                logger.warning(
                    "Environment variable not found defining the app state. "
                    "Will default to 'Dev' environment."
                )
            return DevConfig()  # type: ignore

        elif self.env_state == "stg":
            return StgConfig()  # type: ignore

        elif self.env_state == "prd":
            return PrdConfig()  # type: ignore


settings = FactoryConfig(GlobalConfig().ENV_STATE)()  # type: ignore


@lru_cache()
def get_app_settings() -> DevConfig | StgConfig | PrdConfig:
    """Returns a cached instance of the settings (config) object.

    To change env variable and reset cache during testing, use the 'lru_cache'
    instance method 'get_app_settings.cache_clear()'."""

    return settings


# print(settings.__repr__())  # Un-comment to see all settings at runtime.
