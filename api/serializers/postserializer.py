from api.models import Post
from rest_framework import serializers
from api.serializers.userserializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Post
        fields = "__all__"
