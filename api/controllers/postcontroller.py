from api.models import Post
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from api.serializers.postserializer import PostSerializer


class PostController():
    """
    Controller for handling Post related operations.
    """

    def get_post(self, post_id):
        """
        Retrieve a specific post by its ID or all posts if no ID is provided.

        Args:
            post_id (str) (optional): The ID of the post to retrieve.

        Returns:
            dict: Serialized data of the specified post or all posts.

        Raises:
            ValidationError: If the post with the specified ID is not found.
        """
        if post_id:
            try:
                post = Post.objects.get(id=post_id)
                return PostSerializer(post).data
            except ObjectDoesNotExist:
                raise ValidationError("Unable to find post with id: " + post_id)

        all_posts = Post.objects.all()
        return PostSerializer(all_posts, many=True).data

    def add_post(self, postInfo, user):
        """
        Create a new post entry in the database.

        Args:
            postInfo (dict): Dictionary containing the post's information.
                             It should include keys such as "title" and "content".
            user (User): The user object indicating who is creating the post.

        Returns:
            dict: Serialized data of the created post.

        Raises:
            ValidationError: If required keys are missing or if a duplicate post is detected.
        """
        required_keys = ["title", "content"]
        for key in required_keys:
            if key not in postInfo:
                raise ValidationError("Missing key {} in add post request".format(key))

        postInfo["created_by"] = user
        try:
            created_post = Post.objects.create(**postInfo)
            return PostSerializer(created_post).data
        except Exception as e:
            if str(e) == "UNIQUE constraint failed: post.title, post.content, post.created_by_id":
                raise ValidationError("Duplicate Post")
            raise ValidationError(str(e))
