from functools import wraps

from app.webtools.mount import init_template
from starlette.requests import Request
from starlette.responses import Response


def response(*, template_file: str | None = None):
    """Provide decorator for FastAPI html routes.

    Args:
        template_file (str | None, optional): Name of template file. Defaults to None.
    """
    def inner(func):

        template = init_template()

        @wraps(func)
        async def view_method(*args, **kwargs):
            """Wraps the FastAPI route methods to extract the `Request`
            object from `kwargs` and attach it to a view `context`. This is
            then used to create the Jinja2Template response.

            Raises:
                Exception: If template file is invalid or not given, will
                generate "Template file not found."
                Exception: If the context type is not a valid dictionary,
                will generate "Context of type {type(context)} is not valid.
                Expected dict."

            Returns:
                Response: TemplateResponse containing Jinja context
            """
            template_response: Response | None = None
            request_context = {
                    k: v for k, v in kwargs.items() if isinstance(v, Request)
                }
            view_context = await func(*args, **kwargs)

            context: dict = view_context.to_dict() | request_context

            if not template_file:
                raise Exception(
                    "Template file not found."
                )
            if isinstance(context, dict):
                template_response = template.TemplateResponse(
                    template_file,
                    context=context
                )
            else:
                raise Exception(
                    f"Context of type {type(context)} is not valid. Expected dict."
                )
            return template_response
        return view_method
    return inner
