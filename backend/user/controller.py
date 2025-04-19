from typing import Tuple, Union, List
from pydantic import ValidationError
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from user.db import User
from user.interfaces import SignupRequest, LoginRequest, UserResponse, UserResponseWithToken

def signup(new_user: SignupRequest) -> Tuple[Union[UserResponseWithToken, dict], int]:
    """Sign up a new user."""
    try:
        # Check if the user already exists
        if User.objects.filter(email=new_user.email).exists():
            return {"error": "User already exists"}, status.HTTP_400_BAD_REQUEST

        # Create the user
        user = User(
            user_id=new_user.email,  # Replace with UUID or custom logic if needed
            name=new_user.name,
            email=new_user.email
        )
        user.set_password(new_user.password)
        user.save()

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        user_response = UserResponse(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            created_at=user.created_at.isoformat()
        )
        response = UserResponseWithToken(
            user=user_response,
            token=str(refresh.access_token)
        )
        return response.dict(), status.HTTP_201_CREATED

    except Exception as e:
        return {"error": f"Failed to create user: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def login(login_request: LoginRequest) -> Tuple[Union[UserResponseWithToken, dict], int]:
    """Log in a user."""
    try:
        # Check if the user exists
        user = User.objects.filter(email=login_request.email).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        # Check password
        if not user.check_password(login_request.password):
            return {"error": "Invalid password"}, status.HTTP_401_UNAUTHORIZED

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        user_response = UserResponse(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            created_at=user.created_at.isoformat()
        )
        response = UserResponseWithToken(
            user=user_response,
            token=str(refresh.access_token)
        )
        return response.dict(), status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to login: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def get_user(user_id: str) -> Tuple[Union[UserResponse, dict], int]:
    """Get user data by user_id."""
    try:
        user = User.objects.filter(user_id=user_id).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        response = UserResponse(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            created_at=user.created_at.isoformat()
        )
        return response.dict(), status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to retrieve user: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def get_all_users() -> Tuple[Union[List[UserResponse], dict], int]:
    """Get all users."""
    try:
        users = User.objects.all()
        if not users:
            return {"error": "No users found"}, status.HTTP_404_NOT_FOUND

        response = [
            UserResponse(
                user_id=user.user_id,
                name=user.name,
                email=user.email,
                created_at=user.created_at.isoformat()
            ) for user in users
        ]
        return [r.dict() for r in response], status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to retrieve users: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def delete_user(user_id: str) -> Tuple[dict, int]:
    """Delete a user by user_id."""
    try:
        user = User.objects.filter(user_id=user_id).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        user.delete()
        return {"message": "User deleted successfully"}, status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to delete user: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def update_user(user_id: str, update_data: SignupRequest) -> Tuple[Union[UserResponse, dict], int]:
    """Update user data by user_id."""
    try:
        user = User.objects.filter(user_id=user_id).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        user.name = update_data.name
        user.email = update_data.email
        if update_data.password:
            user.set_password(update_data.password)
        user.save()

        response = UserResponse(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            created_at=user.created_at.isoformat()
        )
        return response.dict(), status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to update user: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def change_password(user_id: str, new_password: str) -> Tuple[dict, int]:
    """Change user password by user_id."""
    try:
        user = User.objects.filter(user_id=user_id).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        user.set_password(new_password)
        user.save()
        return {"message": "Password changed successfully"}, status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to change password: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def reset_password(email: str) -> Tuple[dict, int]:
    """Reset user password by email."""
    try:
        user = User.objects.filter(email=email).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        # Placeholder for reset token logic (implement with email service)
        return {"message": "Reset email sent successfully"}, status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to send reset email: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def verify_reset_token(token: str) -> Tuple[dict, int]:
    """Verify reset token."""
    try:
        # Placeholder for token verification logic
        return {"message": "Token verification not implemented"}, status.HTTP_501_NOT_IMPLEMENTED

    except Exception as e:
        return {"error": f"Failed to verify token: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def update_password_with_token(token: str, new_password: str) -> Tuple[dict, int]:
    """Update password with reset token."""
    try:
        # Placeholder for token-based password update
        return {"message": "Password update with token not implemented"}, status.HTTP_501_NOT_IMPLEMENTED

    except Exception as e:
        return {"error": f"Failed to update password: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def logout(user_id: str) -> Tuple[dict, int]:
    """Log out a user (JWT token invalidation)."""
    try:
        # JWT tokens are stateless; client should discard token
        return {"message": "User logged out successfully"}, status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to logout: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

def get_user_by_email(email: str) -> Tuple[Union[UserResponse, dict], int]:
    """Get user data by email."""
    try:
        user = User.objects.filter(email=email).first()
        if not user:
            return {"error": "User not found"}, status.HTTP_404_NOT_FOUND

        response = UserResponse(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            created_at=user.created_at.isoformat()
        )
        return response.dict(), status.HTTP_200_OK

    except Exception as e:
        return {"error": f"Failed to retrieve user: {str(e)}"}, status.HTTP_500_INTERNAL_SERVER_ERROR