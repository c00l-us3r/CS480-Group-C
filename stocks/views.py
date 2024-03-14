from django.shortcuts import render
from django.http import HttpResponse
from .models import FinancialFundamentalData
from .models import LastPull
from .models import PricingData

def home(request):
    filteredXOM = PricingData.objects.filter(symbol='XOM')
    filteredCVX = PricingData.objects.filter(symbol='CVX')
    filteredNVDA = PricingData.objects.filter(symbol='NVDA')
    filteredWMT = PricingData.objects.filter(symbol='WMT')
    filteredKO = PricingData.objects.filter(symbol='KO')
    filteredPFE = PricingData.objects.filter(symbol='PFE')
    filteredVZ = PricingData.objects.filter(symbol='VZ')
    filteredHD = PricingData.objects.filter(symbol='HD')
    filteredZG = PricingData.objects.filter(symbol='ZG')
    filteredMETA = PricingData.objects.filter(symbol='META')
    filteredGOOGL = PricingData.objects.filter(symbol='GOOGL')
    return render(request, 'stocks/base.html', {
        'filteredXOM': filteredXOM,
        'filteredCVX': filteredCVX,
        'filteredNVDA': filteredNVDA,
        'filteredWMT': filteredWMT,
        'filteredKO': filteredKO,
        'filteredPFE': filteredPFE,
        'filteredVZ': filteredVZ,
        'filteredHD': filteredHD,
        'filteredZG': filteredZG,
        'filteredMETA': filteredMETA,
        'filteredGOOGL': filteredGOOGL,
    })


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

    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='XOM')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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

    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='CVX')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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

    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='NVDA')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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

    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='WMT')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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

    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='KO')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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
        
    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='PFE')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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
        
    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='VZ')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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
        
    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='HD')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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
        
    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='ZG')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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
        
    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='META')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})

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
        
    # Retrieve the stock object based on the symbol
    stock = FinancialFundamentalData.objects.get(symbol='GOOGL')
    # Retrieve a specific field value, for example, the high value
    symbol = stock.symbol
    # You can then pass this value to your template context
    context = {'symbol': symbol}

    return render(request, 'stocks/detailed.html', {'filteredFFD': filteredFFD, 'filteredPD': filteredPD, 'price_differences' : price_differences, 'lp': lp, 'context': context})


def test(request):
    return render(request, 'stocks/test.html')

filteredXOM = PricingData.objects.filter(symbol='XOM')
print(filteredXOM)