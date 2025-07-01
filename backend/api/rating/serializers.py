from rest_framework import serializers
from .models import Rating
from user.serializers import UserSerializer

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = [
            "id",
            "comment",
            "quantity",
            "rate",
            "user",
            "hotel"
        ]
        read_only_fields = ['id']