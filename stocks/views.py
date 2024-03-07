from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'stocks/base.html', {}), # Render the starting base.html page from the stocks app


def detailed(request):
    return render(request, 'stocks/detailed.html', {}), # Render the detailed.html page from the stocks app