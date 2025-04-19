from typing import Tuple, Union, List
from pydantic import ValidationError
from rest_framework import status
from hotel.db import Hotel
from datetime import datetime
from hotel.interfaces import HotelRequest, HotelResponse

def create_hotel(hotel_data: HotelRequest) -> Tuple[Union[HotelResponse, dict], int]:
    """Create a new hotel."""
    try:
        # Check if the hotel already exists
        if Hotel.objects.filter(name=hotel_data.name).exists():
            return {"error": "Hotel already exists"}, status.HTTP_400_BAD_REQUEST

        current_time = datetime.now()
        
        # Create the hotel
        hotel = Hotel(
            name=hotel_data.name,
            address=hotel_data.address,
            city=hotel_data.city,
            email=hotel_data.email,
            website=hotel_data.website,
            img=hotel_data.img,
            description=hotel_data.description,
            price=hotel_data.price,
            created_at=current_time,
            updated_at=current_time,
        )
        hotel.save()

        # Prepare the response
        hotel_response = HotelResponse(
            hotel_id=hotel.hotel_id,
            name=hotel.name,
            address=hotel.address,
            city=hotel.city,
            email=hotel.email,
            website=hotel.website,
            img=hotel.img.url if hotel.img else None,
            created_at=hotel.created_at.isoformat(),
            updated_at=hotel.updated_at.isoformat(),
            description=hotel.description,
            price=str(hotel.price),
            rating=str(hotel.rating)
        )
        return hotel_response.dict(), status.HTTP_201_CREATED

    except Exception as e:
        return {"error": f"Failed to create hotel: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR
    
def get_hotel(hotel_id: str) -> Tuple[Union[HotelResponse, dict], int]:
    """Get hotel details by hotel_id."""
    try:
        # Check if the hotel exists
        hotel = Hotel.objects.filter(hotel_id=hotel_id).first()
        if not hotel:
            return {"error": "Hotel not found"}, status.HTTP_404_NOT_FOUND

        # Prepare the response
        hotel_response = HotelResponse(
            hotel_id=hotel.hotel_id,
            name=hotel.name,
            address=hotel.address,
            city=hotel.city,
            email=hotel.email,
            website=hotel.website,
            img=hotel.img.url if hotel.img else None,
            created_at=hotel.created_at.isoformat(),
            updated_at=hotel.updated_at.isoformat(),
            description=hotel.description,
            price=str(hotel.price),
            rating=str(hotel.rating)
        )
        return hotel_response.dict(), status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to retrieve hotel: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR
    
def update_hotel(hotel_id: str, hotel_data: HotelRequest) -> Tuple[Union[HotelResponse, dict], int]:
    """Update hotel details by hotel_id."""
    try:
        # Check if the hotel exists
        hotel = Hotel.objects.filter(hotel_id=hotel_id).first()
        if not hotel:
            return {"error": "Hotel not found"}, status.HTTP_404_NOT_FOUND

        # Update the hotel details
        for attr, value in hotel_data.dict().items():
            setattr(hotel, attr, value)
        hotel.save()

        # Prepare the response
        hotel_response = HotelResponse(
            hotel_id=hotel.hotel_id,
            name=hotel.name,
            address=hotel.address,
            city=hotel.city,
            email=hotel.email,
            website=hotel.website,
            img=hotel.img.url if hotel.img else None,
            created_at=hotel.created_at.isoformat(),
            updated_at=hotel.updated_at.isoformat(),
            description=hotel.description,
            price=str(hotel.price),
            rating=str(hotel.rating)
        )
        return hotel_response.dict(), status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to update hotel: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def delete_hotel(hotel_id: str) -> Tuple[dict, int]:
    """Delete a hotel by hotel_id."""
    try:
        # Check if the hotel exists
        hotel = Hotel.objects.filter(hotel_id=hotel_id).first()
        if not hotel:
            return {"error": "Hotel not found"}, status.HTTP_404_NOT_FOUND

        # Delete the hotel
        hotel.delete()
        return {"message": "Hotel deleted successfully"}, status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to delete hotel: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def list_hotels() -> Tuple[List[HotelResponse], int]:
    """List all hotels."""
    try:
        # Get all hotels
        hotels = Hotel.objects.all()
        if not hotels:
            return {"error": "No hotels found"}, status.HTTP_404_NOT_FOUND

        # Prepare the response
        hotel_response_list = [
            HotelResponse(
                hotel_id=hotel.hotel_id,
                name=hotel.name,
                address=hotel.address,
                city=hotel.city,
                email=hotel.email,
                website=hotel.website,
                img=hotel.img.url if hotel.img else None,
                created_at=hotel.created_at.isoformat(),
                updated_at=hotel.updated_at.isoformat(),
                description=hotel.description,
                price=str(hotel.price),
                rating=str(hotel.rating)
            ) for hotel in hotels
        ]
        return [h.dict() for h in hotel_response_list], status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to retrieve hotels: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR