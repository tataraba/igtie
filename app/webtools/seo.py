from pydantic import BaseModel, Field


# TODO: Shouldn't assign values here (content_type, charset)
class BaseSEOData(BaseModel):
    meta_title: str = Field(None, min_length=3, max_length=60)
    meta_description: str = Field(None, min_length=10, max_length=160)
    meta_robots_index: bool = True
    meta_robots_follow: bool = True
    meta_content_type: str = "text/html"
    meta_charset: str = "utf-8"
    meta_view_ratio: int = 1

    class Config:
        allow_mutations = False


class SEOData:
    def __call__(self, seo: BaseSEOData) -> dict:
        robots_index = "index"
        robots_follow = "follow"
        if not seo.meta_robots_index:
            robots_index = "noindex"
        if not seo.meta_robots_follow:
            robots_follow = "nofollow"
        seo_context = {
            "meta_title": seo.meta_title,
            "meta_description": seo.meta_description,
            "meta_robots_index": robots_index,
            "meta_robots_follow": robots_follow,
            "meta_charset": seo.meta_charset,
            "meta_content_type": seo.meta_content_type,
            "meta_view_ratio": seo.meta_view_ratio
        }
        return seo_context
