import logging

from passlib.context import CryptContext

from .config import get_app_settings

settings = get_app_settings()

logger = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=[settings.CRYPTCONTEXT_SCHEMES], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
