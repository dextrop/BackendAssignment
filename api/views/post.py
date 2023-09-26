from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from api.lib.customresponse import CustomResponse
from api.controllers.postcontroller import PostController
from rest_framework.permissions import IsAuthenticatedOrReadOnly
'''
ADD Post

POST : /v1/post/
request_body:
{
    "title": "Django is best",
    "description": "this is a sample article",
    "content": "this is some content",
    "keyword": "a,b,c,d"
}

response_body:

{
    "status": true,
    "payload": {
        "id": 1,
        "created_by": {
            "id": 1,
            "name": "Saurabh Pandey",
            "email": "scoder91@gmail.com",
            "phone_no": ""
        },
        "title": "Django is best",
        "description": "this is a sample article",
        "keyword": "a,b,c,d",
        "content": "this is some content",
        "_created": "2023-09-26T17:03:33.912124Z",
        "_updated": "2023-09-26T17:03:33.912137Z"
    },
    "message": "Add Post API"
}

Get All Post API

GET : /v1/post/

response_body:
{
    "status": true,
    "payload": [
        {
            "id": 1,
            "created_by": {
                "id": 1,
                "name": "Saurabh Pandey",
                "email": "scoder91@gmail.com",
                "phone_no": ""
            },
            "title": "Django is best",
            "description": "this is a sample article",
            "keyword": "a,b,c,d",
            "content": "this is some content",
            "_created": "2023-09-26T17:03:33.912124Z",
            "_updated": "2023-09-26T17:03:33.912137Z"
        }
    ],
    "message": "Get Post API"
}

Get Specific Post API

GET : /v1/post/<post_id>

response_body:
{
    "status": true,
    "payload": {
        "id": 1,
        "created_by": {
            "id": 1,
            "name": "Saurabh Pandey",
            "email": "scoder91@gmail.com",
            "phone_no": ""
        },
        "title": "Django is best",
        "description": "this is a sample article",
        "keyword": "a,b,c,d",
        "content": "this is some content",
        "_created": "2023-09-26T17:03:33.912124Z",
        "_updated": "2023-09-26T17:03:33.912137Z"
    },
    "message": "Get Post API"
}
'''
class PostView(generics.GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, id=None):
        response = PostController().get_post(post_id=id)
        return CustomResponse(
            message="Get Post API", payload=response, code=HTTP_200_OK
        )

    def post(self, requests):
        response = PostController().add_post(
            postInfo=requests.data, user=requests.user
        )
        return CustomResponse(
            message="Add Post API", payload=response, code=HTTP_200_OK
        )
