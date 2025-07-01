from django.shortcuts import render
from rest_framework import generics, permissions, pagination, filters
from .models import Rating
from .serializers import RatingSerializer

# Create your views here.
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RatingListCreate(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rate', 'quantity']
    ordering = ['-rate']

    def get_queryset(self):
        queryset = Rating.objects.all()
        hotel_id = self.request.query_params.get('hotel_id')
        if hotel_id is not None:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    
    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            self.permission_denied(self.request)
        return obj