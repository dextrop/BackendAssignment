from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    is_success,
)


class CustomResponse(Response):
    """
    Custom Response Class for standardizing the API's responses.

    The class provides a consistent response structure for all API responses,
    separating successful operations from errors. In case of errors, it also
    provides an appropriate error code.

    Attributes:
        message (str): Optional message, typically used to describe the response.
        code (int): HTTP status code. Default is 200 (HTTP_200_OK).
        payload (dict): The main content of the response.
        etype (str): Error type. Used to describe specific error types.
        template_name (str): The name of a template to use if rendering HTML content.
        headers (dict): Any HTTP headers to add to the response.
        exception (bool): If True, treat `data` as an exception instance.
        content_type (str): The content type of the response payload.
    """

    def __init__(
            self,
            message=None,
            code=HTTP_200_OK,
            payload=None,
            etype=None,
            template_name=None,
            headers=None,
            exception=False,
            content_type=None,
    ):
        data = {
            "status": True,
            "payload": payload,
            "message": message
        }

        # Check if the response indicates a successful operation.
        # If not, adjust the response structure for errors.
        if not is_success(code):
            data["status"] = False
            error_data = {"code": code}

            # Map specific error codes to their corresponding HTTP constants
            if code == 401:
                code = HTTP_401_UNAUTHORIZED
            elif code == 403:
                code = HTTP_403_FORBIDDEN
            else:
                code = HTTP_400_BAD_REQUEST

            data["error"] = error_data

        # Initialize the parent class with the formatted response data
        super(CustomResponse, self).__init__(
            data=data,
            status=code,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
        )
