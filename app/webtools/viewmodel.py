from abc import ABC, abstractmethod

from app.config import get_app_settings
from app.webtools.seo import BaseSEOData, SEOData

settings = get_app_settings()
TITLE = settings.more_settings.title
DESCRIPTION = settings.more_settings.description


class BaseViewContext(ABC):
    """Abstract view that all other views inherit from.

    Upon initializing, calls abstract method `to_dict`, which
    will be specific to each implementation of any ViewContext
    class.
    """

    @abstractmethod
    def to_dict(self):
        ...


class ViewContext(BaseViewContext):
    """Provides the base view context inherited by all other
    views. Initializes the `SEOData` model and an empty `dict`
    for additional context data.

    Args:
        BaseViewContext (ABC): Abstract class.
    """
    def __init__(self):
        self.seo: SEOData = SEOData()
        self.context: dict = {}
        self.view_model = self.to_dict()

    def to_dict(self):
        return self.context


class DefaultView(ViewContext):
    def __init__(self):
        super().__init__()

        self.context = self.seo(BaseSEOData(
            meta_title=TITLE,
            meta_description=DESCRIPTION
        ))


class LoginView(ViewContext):
    ...


class AllCategoryView(BaseViewContext):
    ...


class OneCategoryView(BaseViewContext):
    ...
