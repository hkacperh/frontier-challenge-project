from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NetworkPredictView

router = DefaultRouter()
router.register('network-predict', NetworkPredictView)

urlpatterns = [
    path('backend/get_network_statistics/', views.get_network_statistics, name='get_network_statistics'),
    path('backend/get_network_lists/', views.get_network_lists, name='get_network_lists'),
    path('', include(router.urls)),
]