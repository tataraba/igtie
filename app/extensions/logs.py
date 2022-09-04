# TODO: Create JSON loggers for file handler

import logging
import sys
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel
from rich.logging import RichHandler

from ..config import get_app_settings

logger = logging.getLogger(__name__)

settings = get_app_settings()

# Define the formatting and level of log messages
LOGGER_LEVEL: int = logging.INFO
DATE_FORMAT: str = "%d %b %Y | %H:%M:%S"
SHELL_FORMAT: str = "%(asctime)s | %(message)s"
FILE_FORMAT: str = (
    "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
)

# Create directory if none exists
Path(settings.APP_DIR.parent, "logs").mkdir(parents=True, exist_ok=True)
# settings.LOGGER_DIRECTORY.mkdir(parents=True, exist_ok=True)
LOGGER_FILE: Path = Path(settings.LOGGER_DIRECTORY / settings.LOGGER_FILENAME)
LOGGER_FILE_MODE: str = settings.LOGGER_FILE_MODE


class LoggerConfig(BaseModel):
    """Provides the pydantic BaseModel as a place to define the various logger
    variables.

    Args:
        BaseModel: pydantic BaseModel class.
    """

    level: int
    handlers: list
    shell_format: str
    file_format: str
    date_format: str
    log_file: Path


@lru_cache()
def get_logger_config() -> LoggerConfig:
    """Configures the logger to use the RichHandler from the Rich library for
    better looking log messages and tracebacks. However, it only does so in the
    Dev and Stg tiers (and not production).

    Returns:
        LoggerConfig: Pydantic BaseModel defined above
    """

    file_handler = logging.FileHandler(LOGGER_FILE, mode=LOGGER_FILE_MODE)
    file_handler_format = logging.Formatter(FILE_FORMAT, DATE_FORMAT)
    file_handler.setFormatter(file_handler_format)

    if settings.ENV_STATE != "prd":
        shell_handler = RichHandler(
            rich_tracebacks=True, tracebacks_show_locals=True, show_time=False
        )

        return LoggerConfig(
            level=LOGGER_LEVEL,
            handlers=[shell_handler, file_handler],
            shell_format=SHELL_FORMAT,  # type: ignore
            file_format=FILE_FORMAT,  # type: ignore
            date_format=DATE_FORMAT,
            log_file=LOGGER_FILE,
        )

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(SHELL_FORMAT)  # type: ignore

    return LoggerConfig(
        level=LOGGER_LEVEL,
        handlers=[stdout_handler, file_handler],
        shell_format=SHELL_FORMAT,  # type: ignore
        file_format=FILE_FORMAT,  # type: ignore
        date_format=DATE_FORMAT,
        log_file=LOGGER_FILE,
    )


def setup_rich_logger() -> None:
    """Overrides other handlers/loggers with the configuration defined
    by `get_logger_config()`
    """

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger_config = get_logger_config()

    logging.basicConfig(
        level=logger_config.level,
        format=logger_config.shell_format,
        datefmt=logger_config.date_format,
        handlers=logger_config.handlers,
    )
