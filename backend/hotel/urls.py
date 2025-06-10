from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_hotel),
    path('get/<int:id>', views.get_hotel),
    path('update/<int:id>', views.update_hotel),
    path('delete/<int:id>', views.delete_hotel),
    path('list/', views.list_hotels),
]
