from rest_framework import serializers
from .models import Hotel 
from rating.serializers import RatingSerializer

class HotelSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)  # nested ratings

    class Meta:
        model = Hotel
        fields = [
            "id", "name", "address", "city", "email", "website",
            "img", "description", "price", "rating", "ratings"
        ]
        read_only_fields = ['id', 'rating']
