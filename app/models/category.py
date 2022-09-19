from pydantic import BaseModel


class Category(BaseModel):

    connect: str
    do: str
    learn: str
    listen: str
    play: str
    read: str
    visit: str
    watch: str

    class Config:
        allow_mutation = False
