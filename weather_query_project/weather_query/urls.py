from .views import search_weather, get_query_history
from django.urls import path

urlpatterns = [
    path('', search_weather, name="search_weather"),
    path('history/', get_query_history, name="get_query_history")
]