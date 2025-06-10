from hotel.urls import urlpatterns as hotel_urls
from user.urls import urlpatterns as user_urls
from django.urls import path, include

urlpatterns = [
    path('/api/user/', include(user_urls)),
    path('/api/hotel/', include(hotel_urls)),
]