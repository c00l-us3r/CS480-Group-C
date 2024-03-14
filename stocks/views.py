from django.shortcuts import render
from django.http import HttpResponse
from .models import FinancialFundamentalData
from .models import LastPull
from .models import PricingData

def home(request):
    return render(request, 'stocks/base.html'), # Render the starting base.html page from the stocks app


def detailed(request):
    ffd = FinancialFundamentalData.objects.all()  # Query all FinancialFundamentalData objects
    pd = PricingData.objects.all()  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    return render(request, 'template_name.html', {'ffd': ffd, 'pd': pd, 'lp': lp})



def test(request):
    return render(request, 'stocks/test.html')