from rest_framework.viewsets import ModelViewSet

from apps.posts.models import Post
from apps.posts.api.serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer