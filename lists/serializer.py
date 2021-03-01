# Serializers define the API representation.
from rest_framework import serializers, viewsets

from .models import List, ListItem


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"

class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = "__all__"