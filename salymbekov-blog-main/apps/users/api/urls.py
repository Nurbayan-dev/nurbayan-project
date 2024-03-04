from rest_framework.routers import DefaultRouter
from apps.users.api.veiws import UserViewSet

router = DefaultRouter()

router.register(
    r'users',
    UserViewSet
)

urlpatterns = router.urls
