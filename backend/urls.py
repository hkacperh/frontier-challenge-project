from django.urls import path
from . import views

urlpatterns = [
    path('backend/get_network_statistics/', views.get_network_statistics, name='get_network_statistics'),
    path('backend/get_network_lists/', views.get_network_lists, name='get_network_lists')
]