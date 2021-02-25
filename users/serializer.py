# Serializers define the API representation.
from rest_framework import serializers, viewsets

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
