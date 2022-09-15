from abc import ABC, abstractmethod


class WatchBase(ABC):

    @abstractmethod
    async def save_object(self):
        ...

    @abstractmethod
    async def remove_object(self):
        ...
