from api.models import Post
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from api.serializers.postserializer import PostSerializer

class PostController:
    """
    Controller for handling Post related operations.
    """
    def get_post(self, post_id):
        if post_id:
            try:
                student = Post.objects.get(id=post_id)
                return PostSerializer(student).data
            except Exception as e:
                raise ValidationError("Unable to find post with id: " + post_id)

        students = Post.objects.all()
        return PostSerializer(students, many=True).data

    def add_post(self, postInfo, user):

        """
        Create a new post

        Args:
            postInfo (str): Post related information.
            user (str): user object

        Returns: Created Post Information.
        """
        required_keys = ["title", "content"]
        for key in required_keys:
            if key not in postInfo:
                raise ValidationError("Missing key {} in add post request".format(key))

        postInfo["created_by"] = user
        try:
            created_post = Post.objects.create(**postInfo)
            return PostSerializer(created_post, many=False).data
        except Exception as e:
            if (str(e) == "UNIQUE constraint failed: post.title, post.content, post.created_by_id"):
                raise ValidationError("Duplicate Post")
            raise ValidationError(str(e))
