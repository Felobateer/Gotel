from django.urls import path
from . import views

urlpatterns = [
    path("hotels/", views.HotelListCreate.as_view(), name="hotel-view-create"),
    path("hotel/<int:pk>/", views.HotelDetail.as_view(), name="hotel-detail"),
]