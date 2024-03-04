from rest_framework.viewsets import ModelViewSet

from apps.teams.models import Team
from apps.teams.api.serializers import TeamSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer