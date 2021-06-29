from rest_framework import serializers
from .models import Hike


class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "difficulty", "created_at")
        model = Hike
