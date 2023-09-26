from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from api.lib.customresponse import CustomResponse
from api.controllers.usercontroller import UserController

class SignupView(generics.GenericAPIView):
    def post(self, request):
        Response = UserController().signup(request.data)
        return CustomResponse(message="Signup API View", payload=Response, code=HTTP_200_OK)
