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
    Custom exception handler for Django Rest Framework that adds
    the `status_code` to the response and renames the `detail` key to `error`.
    """
    response = exception_handler(exc, context)

    stack = traceback.format_exc()
    # logger.exception(stack)

    if response is not None:
        """
        below code is needed because rest framework return 403 response if it gets a 401 response.
        more details here: https://github.com/encode/django-rest-framework/issues/5968
        either this way works or ensure authenticate_header does not return None in your authentication Class.
        also see line 455 of 'env/lib/python3.9/site-packages/rest_framework/views.py'
        i.e. WWW-Authenticate header for 401 responses, else coerce to 403
        """
        if isinstance(
            exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)
        ):
            response.status_code = HTTP_401_UNAUTHORIZED
            exc.status_code = 401

        response = CustomResponse(
            message=exc.detail, etype=exc.__class__.__name__, code=exc.status_code
        )

    else:
        message = None
        code = HTTP_501_NOT_IMPLEMENTED

        if exc.__class__.__name__ == "DoesNotExist":
            code = HTTP_500_INTERNAL_SERVER_ERROR
            message = exc.message

        elif (exc.__class__.__name__ == "KeyError") or (
            exc.__class__.__name__ == "MultiValueDictKeyError"
        ):
            code = HTTP_400_BAD_REQUEST
            try:
                message = "Bad request must pass %s" % exc.message
            except Exception as e:
                message = "Missing key in request data, please check"

        elif exc.__class__.__name__ == "ValidationError":
            code = HTTP_400_BAD_REQUEST
            message = exc.message

        elif exc.__class__.__name__ == "IntegrityError":
            code = HTTP_400_BAD_REQUEST
            message = exc[1]

        elif exc.__class__.__name__ == "error":
            code = HTTP_500_INTERNAL_SERVER_ERROR
            message = "socket error"

        else:
            code = HTTP_500_INTERNAL_SERVER_ERROR
            message = "Unhandled Exception"

        response = CustomResponse(
            message=message, etype=exc.__class__.__name__, code=code
        )
    return response
