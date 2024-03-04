from rest_framework.routers import DefaultRouter

from apps.cars.api.views import CarApiViewSet

router = DefaultRouter()
router.register(
    r'cars',
    CarApiViewSet
)

urlpatterns = router.urls
