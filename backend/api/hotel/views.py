from django.shortcuts import render
from rest_framework import generics, permissions, pagination, filters
from .models import Hotel
from .serializers import HotelSerializer

# Create your views here.
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'price', 'rating']
    ordering = ['name']

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    
    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            self.permission_denied(self.request)
        return obj