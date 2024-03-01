from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'stocks/detailed.html', {}) # Render the starting detailed.html page from the stocks app