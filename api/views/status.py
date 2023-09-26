from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from api.lib.customresponse import CustomResponse

class StatusView(generics.GenericAPIView):
    def get(self, requests):
        return CustomResponse(
            message="Server Is Up and Running", payload=True, code=HTTP_200_OK
        )
