from functools import wraps
from typing import Any

import jinja2_fragments
from app.webtools.mount import init_template
from jinja2 import Environment
from starlette.requests import Request


def response(
    *,
    template_file: str | None = None,
    block_name: str | None = None,
    **context: Any,
):
    """Provide decorator for FastAPI html routes.

    Args:
        template_file (str | None, optional): Name of template file. Defaults to None.
        block_name (str | None, optional): Name of Jinja "block" to send HTML fragment.
        context (Any): Parameters sent to the Jinja template.
    """
    def inner(func):

        template = init_template()
        jinja_env: Environment = template.env

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
            if not template_file:
                raise Exception(
                    "Template file not found."
                )

            func_value = await func(*args, **kwargs)
            func_context = {
                    k: v for k, v in kwargs.items() if isinstance(v, Request)
                }
            response_context = func_context

            if isinstance(func_value.to_dict(), dict):
                response_context = func_value.to_dict() | func_context

            context.update(response_context)

            if not block_name:
                return template.TemplateResponse(template_file, context)

            return jinja2_fragments.render_block(
                jinja_env,
                template_file,
                block_name,
                context
            )
        return view_method
    return inner
