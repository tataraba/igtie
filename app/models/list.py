from abc import ABC, abstractmethod

from .category import Category


class List(ABC):

    @abstractmethod
    def init_list(
        self,
        user_id: int,
        category: Category,
    ):
        ...
