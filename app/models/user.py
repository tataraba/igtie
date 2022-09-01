from typing import Optional

import pendulum as pnd
from app.core.security import get_password_hash, verify_password
from app.models.base import Model
from pydantic import BaseModel, EmailStr

__all__ = ["User", "UserDB"]


class _UserProfile(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    preferred_genre: Optional[list] = None


class UserBase(BaseModel):
    email: EmailStr
    username: str
    is_anonymous: bool = False
    is_active: bool = True
    is_super: bool = False
    is_admin: bool = False
    profile: Optional[_UserProfile] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str
    repeat_password: str


class UserLogin(UserBase):
    email: EmailStr
    password: str
    last_login: str = pnd.now().isoformat()


class UserUpdate(UserBase):
    password: str
    repeat_password: Optional[str] = None
    profile: Optional[_UserProfile] = None
    updated_at: Optional[str] = pnd.now().isoformat()


class User(UserBase):
    pass


class UserDB(UserBase, Model):

    salt: str = ""
    hashed_password: str = ""

    def check_password(self, password: str):
        return verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str):
        password = str(password)
        self.hashed_password = get_password_hash(password)

    class Collection:
        name = "users"
