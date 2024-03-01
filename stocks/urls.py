from django.urls import path
from . import views
urlpatterns = [
    # Import the home view for the stocks app
    path('', views.home, name="home")
]