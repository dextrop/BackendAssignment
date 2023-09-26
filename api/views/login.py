from rest_framework import permissions
from rest_framework.views import APIView
from api.lib.customresponse import CustomResponse
from api.controllers.usercontroller import UserController

'''
POST: /v1/login/

request_body:
{
"email": "user_email",
"password": "user_password"
}

response:
{
    "status": true,
    "payload": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTgzNDExMywiaWF0IjoxNjk1NzQ3NzEzLCJqdGkiOiJjOGM5OGU5ODkxZDA0ODQ2YjhhOTRlMDljNmIzNTE4YyIsInVzZXJfaWQiOjF9.K6coTD_zpWEk96IAdmOpwRuh_9u7hfZk8nR8Tdt5snk",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NzQ4MDEzLCJpYXQiOjE2OTU3NDc3MTMsImp0aSI6IjMxYTNjYTJlNzc0NjQ2NjJiYmQzNzJiYmQ4ZmIwNDQwIiwidXNlcl9pZCI6MX0.Sr4UX1c-tj4nrAi_1AWayznATE3wgT5lUMvzqt1VHLk"
    },
    "message": "Login API View"
}
'''
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        Response = UserController().login(
            request.data.get("email"), request.data.get("password")
        )
        return CustomResponse(message="Login API View", payload=Response, code=200)

