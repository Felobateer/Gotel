from django.urls import path
from . import views

urlpatterns = [
    path("ratings/", views.RatingListCreate.as_view(), name="rating-view-create"),
    path("rating/<int:pk>/", views.RatingDetail.as_view(), name="rating-detail"),
]