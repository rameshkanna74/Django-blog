from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["name"]


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "id", "email"]
