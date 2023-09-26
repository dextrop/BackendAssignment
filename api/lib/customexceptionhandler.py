import traceback
from rest_framework import exceptions
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_501_NOT_IMPLEMENTED,
)
from rest_framework.views import exception_handler
from api.lib.customresponse import CustomResponse


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django Rest Framework.

    This handler:
    - Modifies the standard DRF exception response to include status_code.
    - Renames the 'detail' key to 'error'.
    - Addresses an issue with DRF converting 401 responses to 403.

    Args:
        exc: The exception instance.
        context: A dictionary containing keys for the view, request, args, and kwargs.

    Returns:
        CustomResponse: A modified response for the exception.
    """

    response = exception_handler(exc, context)
    stack = traceback.format_exc()
    # Uncomment the next line to log the exception stack trace.
    # logger.exception(stack)

    if response:
        # DRF converts a 401 (unauthorized) response to 403 (forbidden).
        # The workaround ensures that exceptions related to authentication
        # correctly return a 401 status.
        # Refer: https://github.com/encode/django-rest-framework/issues/5968
        # Another approach would be to ensure `authenticate_header` doesn't return None in your authentication class.
        if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)):
            response.status_code = HTTP_401_UNAUTHORIZED
            exc.status_code = 401

        response = CustomResponse(
            message=exc.detail, etype=exc.__class__.__name__, code=exc.status_code
        )

    else:
        # Handle various exceptions and set appropriate response messages and codes.
        message = None
        code = HTTP_501_NOT_IMPLEMENTED

        exc_name = exc.__class__.__name__
        if exc_name == "DoesNotExist":
            code = HTTP_500_INTERNAL_SERVER_ERROR
            message = exc.message
        elif exc_name in ["KeyError", "MultiValueDictKeyError"]:
            code = HTTP_400_BAD_REQUEST
            try:
                message = "Bad request must pass %s" % exc.message
            except Exception:
                message = "Missing key in request data, please check"
        elif exc_name == "ValidationError":
            code = HTTP_400_BAD_REQUEST
            message = exc.message
        elif exc_name == "IntegrityError":
            code = HTTP_400_BAD_REQUEST
            message = exc[1]
        elif exc_name == "error":
            code = HTTP_500_INTERNAL_SERVER_ERROR
            message = "socket error"
        else:
            code = HTTP_500_INTERNAL_SERVER_ERROR
            message = "Unhandled Exception"

        response = CustomResponse(
            message=message, etype=exc_name, code=code
        )

    return response
