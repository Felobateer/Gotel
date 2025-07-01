from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserListCreate.as_view(), name="user-view-create"),
    path("user/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("", views.home, name="home"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
]