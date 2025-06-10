from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def signup(request):
    return Response({"message": "User created"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def login(request):
    return Response({"message": "Login sucessful"}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_user(request):
    return Response({"message": "user updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_user(request):
    return Response({"message": "User deleted"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request):
    return Response({"message": "User details"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_users(request):
    return Response({"message": "All users"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_password(request):
    return Response({"message": "Password reset initiated"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def verify_reset_token(request):
    return Response({"message": "Reset token verified"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def update_password_with_token(request):
    return Response({"message": "Password updated with token"}, status=status.HTTP_200_OK)
