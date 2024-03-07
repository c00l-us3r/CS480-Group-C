# URL configuration for the stocks app
from django.urls import path
from . import views
urlpatterns = [
    # Import the home view for the stocks app
    path('', views.home, name="home"),
    path('detailed', views.detailed, name="detailed"),
]