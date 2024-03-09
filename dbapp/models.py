# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FinancialFundamentalData(models.Model):
    symbol = models.CharField(db_column='Symbol', primary_key=True, max_length=10)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=25)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=2000)  # Field name made lowercase.
    cik = models.CharField(db_column='CIK', max_length=10)  # Field name made lowercase.
    exchange = models.CharField(db_column='Exchange', max_length=10)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=5)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=20)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=10)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=25)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    fiscalyearend = models.CharField(db_column='FiscalYearEnd', max_length=9)  # Field name made lowercase.
    latestquarter = models.CharField(db_column='LatestQuarter', max_length=10)  # Field name made lowercase.
    marketcapitalization = models.CharField(db_column='MarketCapitalization', max_length=10)  # Field name made lowercase.
    ebitda = models.CharField(db_column='EBITDA', max_length=10)  # Field name made lowercase.
    peration = models.CharField(db_column='PERation', max_length=10)  # Field name made lowercase.
    pegration = models.CharField(db_column='PEGRation', max_length=10)  # Field name made lowercase.
    bookvalue = models.CharField(db_column='BookValue', max_length=10)  # Field name made lowercase.
    dividendpershare = models.CharField(db_column='DividendPerShare', max_length=45)  # Field name made lowercase.
    divdendyield = models.CharField(db_column='DivdendYield', max_length=10)  # Field name made lowercase.
    eps = models.CharField(db_column='EPS', max_length=10)  # Field name made lowercase.
    revenuepersharettm = models.CharField(db_column='RevenuePerShareTTM', max_length=10)  # Field name made lowercase.
    profitmargin = models.CharField(db_column='ProfitMargin', max_length=10)  # Field name made lowercase.
    operatingmarginttm = models.CharField(db_column='OperatingMarginTTM', max_length=10)  # Field name made lowercase.
    returnonassetsttm = models.CharField(db_column='ReturnOnAssetsTTM', max_length=10)  # Field name made lowercase.
    returnonequityttm = models.CharField(db_column='ReturnOnEquityTTM', max_length=10)  # Field name made lowercase.
    revenuettm = models.CharField(db_column='RevenueTTM', max_length=10)  # Field name made lowercase.
    grossprofitttm = models.CharField(db_column='GrossProfitTTM', max_length=10)  # Field name made lowercase.
    dilutedepsttm = models.CharField(db_column='DilutedEPSTTM', max_length=10)  # Field name made lowercase.
    quarterlyearningsgrowthyoy = models.CharField(db_column='QuarterlyEarningsGrowthYOY', max_length=10)  # Field name made lowercase.
    quarterlyrevenuegrowthyoy = models.CharField(db_column='QuarterlyRevenueGrowthYOY', max_length=10)  # Field name made lowercase.
    analysttargetprice = models.CharField(db_column='AnalystTargetPrice', max_length=10)  # Field name made lowercase.
    analystratingstrongbuy = models.CharField(db_column='AnalystRatingStrongBuy', max_length=3)  # Field name made lowercase.
    analystratingbuy = models.CharField(db_column='AnalystRatingBuy', max_length=3)  # Field name made lowercase.
    analystratinghold = models.CharField(db_column='AnalystRatingHold', max_length=3)  # Field name made lowercase.
    analystratingsell = models.CharField(db_column='AnalystRatingSell', max_length=3)  # Field name made lowercase.
    analystratingstrongsell = models.CharField(db_column='AnalystRatingStrongSell', max_length=3)  # Field name made lowercase.
    trailingpe = models.CharField(db_column='TrailingPE', max_length=10)  # Field name made lowercase.
    forwardpe = models.CharField(db_column='ForwardPE', max_length=10)  # Field name made lowercase.
    pricetosalesrationttm = models.CharField(db_column='PriceToSalesRationTTM', max_length=10)  # Field name made lowercase.
    pricetobookratio = models.CharField(db_column='PriceToBookRatio', max_length=10)  # Field name made lowercase.
    evtorevenue = models.CharField(db_column='EVToRevenue', max_length=10)  # Field name made lowercase.
    evtoebitda = models.CharField(db_column='EVToEBITDA', max_length=10)  # Field name made lowercase.
    beta = models.CharField(db_column='Beta', max_length=10)  # Field name made lowercase.
    number_52weekhigh = models.CharField(db_column='52WeekHigh', max_length=10)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_52weeklow = models.CharField(db_column='52WeekLow', max_length=10)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_50daymovingaverage = models.CharField(db_column='50DayMovingAverage', max_length=10)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_200daymovingaverage = models.CharField(db_column='200DayMovingAverage', max_length=10)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    sharesoutstanding = models.CharField(db_column='SharesOutstanding', max_length=10)  # Field name made lowercase.
    dividenddate = models.CharField(db_column='DividendDate', max_length=10)  # Field name made lowercase.
    exdivedenddate = models.CharField(db_column='ExDivedendDate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financial_fundamental_data'


class LastPull(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase. The composite primary key (Date, Time) found, that is not supported. The first column is selected.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'last_pull'
        unique_together = (('date', 'time'),)


class PricingData(models.Model):
    symbol = models.OneToOneField(FinancialFundamentalData, models.DO_NOTHING, db_column='Symbol', primary_key=True)  # Field name made lowercase.
    open = models.CharField(db_column='Open', max_length=10)  # Field name made lowercase.
    high = models.CharField(db_column='High', max_length=10)  # Field name made lowercase.
    low = models.CharField(db_column='Low', max_length=10)  # Field name made lowercase.
    close = models.CharField(db_column='Close', max_length=10)  # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pricing_data'
