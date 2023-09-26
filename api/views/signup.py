from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from api.lib.customresponse import CustomResponse
from api.controllers.usercontroller import UserController

'''
POST: /v1/login/

request_body:
{
"name:"user_name",
"email": "user_email",
"password": "user_password",
"phone_no": "optional_field" 
}

response:
{
    "status": true,
    "payload": "Signup successful, kindly login to start posting!",
    "message": "Signup API View"
}
'''

class SignupView(generics.GenericAPIView):
    def post(self, request):
        Response = UserController().signup(request.data)
        return CustomResponse(message="Signup API View", payload=Response, code=HTTP_200_OK)
