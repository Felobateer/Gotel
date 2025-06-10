from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_hotel(request):
    return Response({"message": "Hotel created"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_hotel(request):
    return Response({"message": "Hotel details"}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_hotel(request):
    return Response({"message": "Hotel updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_hotel(request):
    return Response({"message": "Hotel deleted"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_hotels(request):
    return Response([{"hotel_id": 1, "name": "Hotel One"}, {"hotel_id": 2, "name": "Hotel Two"}], status=status.HTTP_200_OK)