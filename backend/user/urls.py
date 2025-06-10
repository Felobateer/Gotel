from django.urls import path
from . import views

urlpatterns = [
    path('/signup', views.signup),
    path('/login', views.login),
    path('/reset-password', views.reset_password),
    path('/verify-reset-token', views.verify_reset_token),
    path('/update-password-with-token', views.update_password_with_token),
    path('/update-user/<int:id>', views.update_user),
    path('/delete-user/<int:id>', views.delete_user),
    path('/get-all-users/', views.get_all_users),
    path('/get-user/<int:id>/', views.get_user),
]
