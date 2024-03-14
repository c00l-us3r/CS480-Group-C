from django.shortcuts import render
from django.http import HttpResponse
from .models import FinancialFundamentalData
from .models import LastPull
from .models import PricingData

def home(request):
    filteredPD = PricingData.objects.filter(symbol='XOM')
    return render(request, 'stocks/detailed.html', {'filteredPD': filteredPD})

def detailed(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='XOM')
    pd = PricingData.objects.all()  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'pd': pd, 'lp': lp})

def XOM(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='XOM')
    filteredPD = PricingData.objects.filter(symbol='XOM')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects

    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def CVX(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='CVX')
    filteredPD = PricingData.objects.filter(symbol='CVX')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def NVDA(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='NVDA')
    filteredPD = PricingData.objects.filter(symbol='NVDA')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def WMT(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='WMT')
    filteredPD = PricingData.objects.filter(symbol='WMT')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def KO(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='KO')
    filteredPD = PricingData.objects.filter(symbol='KO')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def PFE(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='PFE')
    filteredPD = PricingData.objects.filter(symbol='PFE')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def VZ(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='VZ')
    filteredPD = PricingData.objects.filter(symbol='VZ')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def HD(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='HD')
    filteredPD = PricingData.objects.filter(symbol='HD')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def ZG(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='ZG')
    filteredPD = PricingData.objects.filter(symbol='ZG')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def META(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='META')
    filteredPD = PricingData.objects.filter(symbol='META')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})

def GOOGL(request):
    filteredFFD = FinancialFundamentalData.objects.filter(symbol='GOOGL')
    filteredPD = PricingData.objects.filter(symbol='GOOGL')  # Query all PricingData objects
    lp = LastPull.objects.all()  # Query all LastPull objects
    
    # Calculate the difference between open and close prices for each PricingData object
    price_differences = []
    for stock in filteredPD:
        open_price = float(stock.open)
        close_price = float(stock.close)
        difference = open_price - close_price
        price_differences.append(difference)

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp})


def test(request):
    return render(request, 'stocks/test.html')