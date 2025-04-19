from rest_framework import status
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

class HotelRoutes:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define public endpoints that don't require authentication
        self.public_endpoints = [
            '/api/hotel/create/',
            '/api/hotel/get/',
            '/api/hotel/update/',
            '/api/hotel/delete/',
        ]

    def __call__(self, request):
        # Skip authentication for public endpoints
        if request.path in self.public_endpoints:
            return self.get_response(request)

        # Verify JWT token
        try:
            auth = JWTAuthentication()
            validated_token = auth.get_validated_token(auth.get_raw_token(auth.get_header(request)))
            request.user = auth.get_user(validated_token)
        except (InvalidToken, AuthenticationFailed) as e:
            return JsonResponse({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({"error": "Authentication error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return self.get_response(request)

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            return JsonResponse(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def process_exception(self, request, exception):
        # Handle specific exceptions if needed
        return JsonResponse(
            {"error": str(exception)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        