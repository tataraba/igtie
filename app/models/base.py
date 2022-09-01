from typing import Optional

import pendulum as pnd
from beanie import Document


class Model(Document):
    """Base class for database models. Inherits from beanie `Document` class
    and is used as drop-in replacement. Adds `created_at` and `updated_at`
    fields.
    """

    created_at: Optional[str] = pnd.now().isoformat()
    updated_at: Optional[str] = pnd.now().isoformat()

    @property
    def class_name(self):
        return self.__class__.__name__.lower()

    @classmethod
    def __ignore__(cls):
        """Custom class attribute that lets us control which models we can ignore."""
        return cls.__name__ in ("Model",)  # can add abstract base classes here

    def __repr__(self):
        """Returns a string representation of every object. Useful for
        logging/errors."""

        return f"{self.class_name}.{self.id}"
