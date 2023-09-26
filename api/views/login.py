from rest_framework import permissions
from rest_framework.views import APIView
from api.lib.customresponse import CustomResponse
from api.controllers.usercontroller import UserController

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        Response = UserController().login(
            request.data.get("email"), request.data.get("password")
        )
        return CustomResponse(message="Login API View", payload=Response, code=200)

