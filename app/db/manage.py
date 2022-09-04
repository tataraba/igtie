import logging

from beanie import init_beanie

from build import ManageMongoConnection
from exceptions import DatabaseException

logger = logging.getLogger(__name__)


async def init_db(db: ManageMongoConnection | None = None) -> None:
    """Initializing database using beanie. Connection to the database
    is handled by the `ManageMongo` class.
    """
    if not db:
        db = ManageMongoConnection()
    logger.info(f"Starting {db}")
    client = db.retrieve_client
    logger.info(f'Connected to {client}')
    db_name = db.db_name
    logger.info("Initializing database...")

    try:
        await init_beanie(
            database=client[db_name],
            document_models=db.model_loader  # type:ignore
        )

    except Exception as e:
        raise DatabaseException(f"Could not initialize database: {e}")

    logger.info(f"Database {db.db_name} ready.")


def disconnect_db(db: ManageMongoConnection | None = None):
    """Disconnect the database."""
    if not db:
        db = ManageMongoConnection()
    db.close_client
