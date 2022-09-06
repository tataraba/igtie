from functools import wraps

from app.webtools.mount import init_template
from fastapi.responses import Response


def response(*, template_file: str | None = None):
    def inner(func):
        template = init_template()

        @wraps(func)
        async def view_method(*args, **kwargs):
            context: dict = await func(*args, **kwargs)
            resp: Response | None = None

            if not template_file:
                raise Exception(
                    "Template file not found."
                )
            if isinstance(context, dict):
                resp = template.TemplateResponse(
                    template_file,
                    context=context
                )
            else:
                raise Exception(
                    f"Context of type {type(context)} is not valid. Expected dict."
                )
            return resp
        return view_method
    return inner
