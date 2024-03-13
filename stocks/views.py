from django.shortcuts import render
import requests
import json

#key and stocks to be be used
api_key = 'CMWOB2MD080MAVB7'  
stocks = ['CVX', 'NVDA', 'WMT', 'KO', 'PFE', 'VZ', 'HD', 'ZG', 'META', 'GOOGL']

# Function to extract city and state from the overview address
def clean_address(address):
    parts = address.split(', ')
    city, state = '', ''
    if len(parts) >= 3:
        city = parts[-3]
        state = parts[-2]
    return city, state

def home(request):
    # Fetch the company overview data for each stock
    stock_data = []

    # Loop through stocks and fetch data from Alpha Vantage
    for symbol in stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Extract data from the response
            global_quote = data.get("Global Quote", {})

            # Prepare the data for the template or print null string if not available
            stock_info = {
                'symbol': global_quote.get("01. symbol", "Null"),
                'open': global_quote.get("02. open", "Null"),
                'high': global_quote.get("03. high", "Null"),
                'low': global_quote.get("04. low", "Null"),
                'close': global_quote.get("05. price", "Null"),  
                'volume': global_quote.get("06. volume", "Null"),
            }
            # Append the data to the list
            stock_data.append(stock_info)
        else:
            print(f"Failed to fetch data for {symbol}")

    # Return the render for the home page and pass the stock data
    return render(request, 'stocks/home.html', {'stock_data': stock_data})

# Function to fetch detailed stock data
def detailed(request, symbol):

    # Fetch the company overview data
    overview_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}"
    overview_response = requests.get(overview_url)
    overview_data = overview_response.json() if overview_response.status_code == 200 else {}

    # Extract city and state from the overview address
    if "Address" in overview_data:
        city, state = clean_address(overview_data["Address"])
        # Add the extracted city and state to the overview data for use in the template
        overview_data["City"] = city
        overview_data["State"] = state

    # Fetch intraday data, global quote data, and combine it with the overview data
    intraday_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"
    intraday_response = requests.get(intraday_url)
    intraday_data = intraday_response.json() if intraday_response.status_code == 200 else {}

    global_quote_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    global_quote_response = requests.get(global_quote_url)
    global_quote_data = global_quote_response.json().get("Global Quote", {}) if global_quote_response.status_code == 200 else {}

    # Extracting the latest data point from the intraday data
    time_series_key = 'Time Series (5min)'
    latest_data_point = list(intraday_data.get(time_series_key, {}).keys())[0] if intraday_data.get(time_series_key) else None
    latest_ohlcv = intraday_data[time_series_key][latest_data_point] if latest_data_point else {}

    # Combine the overview data with the latest OHLCV values and global quote data
    stock_info = {
        **overview_data,
        **latest_ohlcv,
        **global_quote_data,
        "change_percent":global_quote_data.get("10. change percent", "N/A"),
                  "open": global_quote_data.get("02. open", "N/A"),
                  "close": global_quote_data.get("05. price", "N/A"),
                  "high": global_quote_data.get("03. high", "N/A"),
                  "low": global_quote_data.get("04. low", "N/A"),
                  '52WeekHigh': overview_data.get('52WeekHigh', 'N/A'),
                  '52WeekLow': overview_data.get('52WeekLow', 'N/A'),
                  '50DayMovingAverage': overview_data.get('50DayMovingAverage', 'N/A'),
                  '200DayMovingAverage': overview_data.get('200DayMovingAverage', 'N/A'),
                  'Volume': global_quote_data.get('06. volume', 'N/A'),
                  'SharesOutstanding': overview_data.get('SharesOutstanding', 'N/A'),
                  'DividendPerShare': overview_data.get('DividendPerShare', 'N/A'),
                  'DividendYield': overview_data.get('DividendYield', 'N/A'),
                  'DividendDate': overview_data.get('DividendDate', 'N/A'),
                  'ExDividendDate': overview_data.get('ExDividendDate', 'N/A'),
                  'FiscalYearEnd': overview_data.get('FiscalYearEnd', 'N/A'),
                  'LatestQuarter': overview_data.get('LatestQuarter', 'N/A'),
                  'TrailingPE': overview_data.get('TrailingPE', 'N/A'),
                  'ForwardPE': overview_data.get('ForwardPE', 'N/A'),
                  'PriceToSalesRatioTTM': overview_data.get('PriceToSalesRatioTTM', 'N/A'),
                  'ProfitMargin': overview_data.get('ProfitMargin', 'N/A'),
                  'OperatingMarginTTM': overview_data.get('OperatingMarginTTM', 'N/A'),
                  'ReturnOnAssetsTTM': overview_data.get('ReturnOnAssetsTTM', 'N/A'),
                  'ReturnOnEquityTTM': overview_data.get('ReturnOnEquityTTM', 'N/A'),
                 
    }

    # Pass all of the stock data to the template for usage in the detailed page
    return render(request, 'stocks/detailed.html', {'stock_info': stock_info})
