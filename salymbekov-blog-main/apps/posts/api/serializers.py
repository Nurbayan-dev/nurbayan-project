from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "description",
            "created_at",
            "title"
        ]