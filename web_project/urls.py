from django.contrib import admin
from django.urls import path, include  # Ensure views are correctly imported within each app's urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),  # Include the stocks app URLs at the root
    # Removed the direct path to 'home' and 'detailed' here to avoid duplication and conflicts
]
