from rest_framework.serializers import ModelSerializer

from apps.cars.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "image",
            "brand",
            "model",
            "fuel",
            "mileage",
            "price_per_hour",
            "price_per_day",
            "price_per_month",
            "description",
        ]
        