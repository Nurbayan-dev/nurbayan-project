from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)