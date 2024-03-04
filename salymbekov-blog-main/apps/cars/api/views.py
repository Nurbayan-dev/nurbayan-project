from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.cars.models import Car
from apps.cars.api.serializers import CarSerializer


class CarApiViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)