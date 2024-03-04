from rest_framework.serializers import ModelSerializer

from apps.users.models import User 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        
        fields = [
            'id',
            "username",
            'first_name',
            "last_name",
            'age',
            'job',
            'email',
            'phone_number',
            'gender',
            'instagram',
            'tiktok',
            "password",
            'apple_id'
        ]
        
    
    def create(self, validated_data: dict):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password) # admin => pbkdf2_sha256$720000$HxgmkWv0J7oiTT9ikZInXm$4x8f8VZfs9PXpYPW5dcn1wUYVRjTaAePTgGWBqERcGw=
        user.is_active = True
        user.save()
        return user
