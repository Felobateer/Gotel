from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserListCreate.as_view(), name="user-view-create"),
    path("user/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]