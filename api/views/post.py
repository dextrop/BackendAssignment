from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from api.lib.customresponse import CustomResponse
from api.controllers.postcontroller import PostController
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

    def put(self, requests):
        return CustomResponse(
            message="Server Is Up and Running", payload=True, code=HTTP_200_OK
        )

    def delete(self, requests):
        return CustomResponse(
            message="Server Is Up and Running", payload=True, code=HTTP_200_OK
        )
