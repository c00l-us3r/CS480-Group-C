# URL configuration for the stocks app
from django.urls import path
from . import views
urlpatterns = [
    # Import the home view for the stocks app
    path('', views.home, name="home"),
    
    #Creating a urls for each stock /'urlname'
    path('detailed/<str:symbol>', views.detailed, name="detailed"),


]