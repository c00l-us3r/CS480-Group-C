# URL configuration for the stocks app
from django.urls import path
from . import views
urlpatterns = [
    # Import the home view for the stocks app
    path('', views.home, name="home"),
    path('detailed/', views.detailed, name="detailed"),
    path('XOM/', views.XOM, name="EXXON"),
    path('CVX/', views.CVX, name="CHEVRON"),
    path('NVDA/', views.NVDA, name="NVIDIA"),
    path('WMT/', views.WMT, name="WALMART"),
    path('KO/', views.KO, name="COCACOLA"),
    path('PFE/', views.PFE, name="PFIZER"),
    path('VZ/', views.VZ, name="VERIZON"),
    path('HD/', views.HD, name="HOMEDEPOT"),
    path('ZG/', views.ZG, name="ZILLOW"),
    path('META/', views.META, name="META"),
    path('GOOGL/', views.GOOGL, name="GOOGLE"),
    path('tradingview-widget/', views.test, name='test'),

]