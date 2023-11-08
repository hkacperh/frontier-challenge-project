from django.urls import path
from . import views as apiviews

urlpatterns = [
    path('backend/statistics/', apiviews.get_network_statistics),
    path('backend/lists/', apiviews.get_network_lists)
]