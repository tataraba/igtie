import logging
from inspect import isclass

from app import config
from app.extensions import loaders
from app.models.base import Model
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import AnyUrl, BaseSettings, validator

from base import ManageDB
from exceptions import DatabaseInitError, InvalidURIAddress

logger = logging.getLogger(__name__)
settings = config.get_app_settings()


class DataBase(BaseSettings):
    """Load and validate Database settings by extending pydantic `BaseSettings`.
    If the `MONGO_HOST` is set as `localhost`, the validator builds URI with
    "mongodb" as `MONGO_SCHEME` and includes the port number. Otherwise, uses
    "mongodb+srv" as `MONGO_SCHEME` and excludes port number.
    """

    MONGO_DB_URI: AnyUrl | None = settings.MONGO_DB_URI
    MONGO_AUTH_DB: str | None = settings.MONGO_AUTH_DB
    MONGO_DB: str | None = settings.MONGO_DB
    db_client: AsyncIOMotorClient | None = None
    logger.info(f"Check {MONGO_DB}")

    @validator("MONGO_DB_URI", pre=True, check_fields=False)
    def uri_is_valid(cls, v):
        if isinstance(v, AnyUrl):
            return v
        if settings.MONGO_HOST in ("localhost", "127.0.0.1"):
            try:
                return AnyUrl.build(
                    scheme=settings.MONGO_SCHEME,
                    host=settings.MONGO_HOST,
                    port=settings.MONGO_PORT,
                    user=settings.MONGO_USER,
                    password=settings.MONGO_PASS,
                    path=f"/{settings.MONGO_DB}",
                    query="retryWrites=true&w=majority",
                )
            except Exception:
                raise InvalidURIAddress(v)
        try:
            return AnyUrl.build(
                scheme=settings.MONGO_SCHEME,
                user=settings.MONGO_USER,
                password=settings.MONGO_PASS,
                host=settings.MONGO_HOST,
                path=f"/{settings.MONGO_DB}",
                query="retryWrites=true&w=majority"
            )
        except Exception:
            raise InvalidURIAddress(v)

    @property
    def model_loader(self) -> list[Model]:
        """Returns list of `Model` objects (Beanie Documents) to be registered
        by `init_beanie` method."""
        logger.info("Loading beanie models...")
        return loaders.dynamic_loader(".", self.is_beanie_model)

    def is_beanie_model(self, item: Model) -> bool:
        """Detects if an object is a Model that inherits Beanie `Document` class.

        Args:
            item (Model): Model is base class extending `Document` models.

        Returns:
            bool: True if `item` is a Beanie `Document` class (and does not
            have __ignore__ attribute).
        """
        return (isclass(item) and issubclass(item, Model)
                and not item.__ignore__())  # type: ignore


class ManageMongoConnection(ManageDB, DataBase):
    """ManageMongoConnection extends abstract `ManageDB` class to
    handle database connections, as well as `DataBase` class to
    validate URI, database name, and loading models.
    """
    def __init__(
        self,
        MONGO_DB_URI: AnyUrl | None = None,
        MONGO_AUTH_DB: str | None = None,
        MONGO_DB: str | None = None,
        db_client: AsyncIOMotorClient = None,
    ):
        """Initialize the database."""
        super().__init__(
            MONGO_DB_URI=MONGO_DB_URI,
            MONGO_AUTH_DB=MONGO_AUTH_DB,
            MONGO_DB=MONGO_DB,
        )

    @property
    def create_client(self) -> AsyncIOMotorClient:
        self.db_client = AsyncIOMotorClient(self.MONGO_DB_URI)
        return self.db_client

    @property
    def close_client(self):
        logger.info("Disconnecting from MongoDB...")
        if self.db_client:
            self.db_client.close()
        logger.info("DISCONNECTED.")

    @property
    def retrieve_client(self) -> AsyncIOMotorClient:
        if not self.db_client:
            self.create_client
        return self.db_client

    @property
    def db_name(self) -> str:
        if self.MONGO_DB is None:
            raise DatabaseInitError("Database not given.")
        return self.MONGO_DB
