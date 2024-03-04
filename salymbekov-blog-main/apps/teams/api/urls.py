from rest_framework.routers import DefaultRouter

from apps.teams.api.views import TeamViewSet

router = DefaultRouter()
router.register(
    r'teams',
    TeamViewSet
)

urlpatterns = router.urls