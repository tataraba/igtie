# Include aggregate model (pydantic) and value objects (smallest units)
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class WatchType(str, Enum):
    TV_SERIES = "TV Series"
    TV_SHOW = "TV Show"
    MOVIE = "Movie"
    SHORT_FILM = "Short Film"
    DOCUMENTARY = "Documentary"
    WEB_VIDEO = "Web Video"
    MUSIC_VIDEO = "Music Video"
    MISC = "Miscellaneous"


class WatchTitle(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)


class WatchGenre(BaseModel):
    genre: str = Field(None, min_length=1, max_length=65)
    sub_genre: Optional[str] = Field(None, min_length=1, max_length=100)


class Watch(BaseModel):
    type: WatchType
    title: WatchTitle
    category: WatchCategory
    genre: WatchGenre
    url: WatchURL
    platform: WatchPlatform
    properties: WatchProperties
++
