# Serializers define the API representation.
from rest_framework import serializers, viewsets

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"