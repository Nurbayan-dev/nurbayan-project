from rest_framework.serializers import ModelSerializer

from apps.teams.models import Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "id",
            "description",
            'position',
            "fullname",
            
        ]