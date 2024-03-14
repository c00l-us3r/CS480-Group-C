
import requests

def pull (endpoint, symbol, apikey):
    
    url = 'https://www.alphavantage.co/query?function='+ endpoint 
    if(endpoint == 'TIME_SERIES_INTRADAY'):
        url = url + '&interval=5min'
        
    url = url + '&symbol=' + symbol + '&apikey='+ apikey
   
    r = requests.get(url)
    
    data = r.json()
    
    dataString = str(data)
    
    return dataString

def stripPastComma(token):
    commaIndex = token.rfind(',')
    if commaIndex != -1:
        token = token[0:commaIndex]
    token = token[1:-1]
    return token

"""
Returns array of data from the OVERVIEW Alpha Vantage Endpoint.
Indexes are as follows:
0 = Symbol
1 = AssetType
2 = Name
3 = Description
4 = CIK
5 = Exchange
6 = Currency
7 = Country
8 = Sector
9 = Industry
10 = Address
11 = FiscalYearEnd
12 = LatestQuarter
13 = MarketCapitalization
14 = EBITDA
15 = PERatio
16 = PEGRatio
17 = BookValue
18 = DividendPerShare
19 = DividendYield
20 = EPS
21 = RevenuePerShareTTM
22 = ProfitMargin
23 = OperatingMarginTTM
24 = ReturnOnAssetsTTM
25 = ReturnOnEquityTTM
26 = RevenueTTM
27 = GrossProfitTTM
28 = DilutedEPSTTM
29 = QuarterlyEarningsGrowthYOY
30 = QuarterlyRevenueGrowthYOY
31 = AnalystTargetPrice
32 = AnalystRatingStrongBuy
33 = AnalystRatingBuy
34 = AnalystRatingHold
35 = AnalystRatingSell
36 = AnalystRatingStrongSell
37 = TrailingPE
38 = ForwardPE
39 = PriceToSalesRatioTTM
40 = PriceToBookRatio
41 = EVToRevenue
42 = EVToEBITDA
43 = Beta
44 = 52WeekHigh
45 = 52WeekLow
46 = 50DayMovingAverage
47 = 200DayMovingAverage
48 = SharesOutstanding
49 = DividendDate
50 = ExDividendDate
"""
def getFinancialFundamentalData(symbol, apikey):
    
    dataString = pull("OVERVIEW", symbol, apikey)
    
    tokens = dataString.split(": ")
    
    del tokens[0] 
    
    tokens[len(tokens)-1] = tokens[len(tokens)-1][0:-1] #remove the last }
    
    count = -1
    for i in range(0, len(tokens)): #remove unnecesarry info from each token
        count += 1
        tokens[i] = stripPastComma(tokens[i])
        
        if tokens[i].isdigit(): #format numbers over 1 billion and 1 million into 1.0B and 1.0M respectively
            number = float(tokens[i])
            if number >= 1e9:
                tokens[i] = "{:.1f}B".format(number / 1e9)
            elif number >= 1e6:
                tokens[i] = "{:.1f}M".format(number / 1e6)
    return tokens

"""
Returns array of data from the TIME_SERIES_INTRADAY Alpha Vantage Endpoint.
Indexes are as follows:
0 = Open
1 = High
2 = Low
3 = Close
4 = Volume
5 = CurrentPrice
"""
def getPricingData(symbol, apiKey):
        
    dataStringFive = pull("TIME_SERIES_INTRADAY", symbol, apiKey)
    dataStringDay = pull("TIME_SERIES_DAILY", symbol, apiKey)

    tokensFive = dataStringFive.split(": ")
    tokensDay = dataStringDay.split(": ")
    
    currentPrice = tokensFive[10]
    tokensDay = tokensDay[9:14]
    
    for i in range(0,5):
        tokensDay[i] = stripPastComma(tokensDay[i])
        
    tokensDay[4] = tokensDay[4][0:len(tokensDay[4])-1]
    currentPrice = stripPastComma(currentPrice)
    
    tokens = [' '] * 6
    
    for i in range(0,5):
        tokens[i] = tokensDay[i]
    tokens[5] = currentPrice
    

    for i in range(0,6):
        if i != 4:
            tokens[i] = tokens[i][0:len(tokens[i])-2]
    
    return tokens   