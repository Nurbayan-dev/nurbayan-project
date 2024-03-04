from rest_framework.routers import DefaultRouter

from apps.posts.api.views import PostViewSet

router = DefaultRouter()
router.register(
    r'posts',
    PostViewSet
)

urlpatterns = router.urls