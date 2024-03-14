# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        app_label = 'dbapp'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
        app_label = 'dbapp'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
        app_label = 'dbapp'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        app_label = 'dbapp'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
        app_label = 'dbapp'


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        app_label = 'dbapp'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        app_label = 'dbapp'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        app_label = 'dbapp'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'dbapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        app_label = 'dbapp'


class FinancialFundamentalData(models.Model):
    symbol = models.CharField(db_column='Symbol', primary_key=True, max_length=10)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=25)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=2000)  # Field name made lowercase.
    cik = models.CharField(db_column='CIK', max_length=10)  # Field name made lowercase.
    exchange = models.CharField(db_column='Exchange', max_length=10)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=5)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=20)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=20)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60)  # Field name made lowercase.
    fiscalyearend = models.CharField(db_column='FiscalYearEnd', max_length=9)  # Field name made lowercase.
    latestquarter = models.CharField(db_column='LatestQuarter', max_length=10)  # Field name made lowercase.
    marketcapitalization = models.CharField(db_column='MarketCapitalization', max_length=10)  # Field name made lowercase.
    ebitda = models.CharField(db_column='EBITDA', max_length=10)  # Field name made lowercase.
    peration = models.CharField(db_column='PERation', max_length=10)  # Field name made lowercase.
    pegration = models.CharField(db_column='PEGRation', max_length=10)  # Field name made lowercase.
    bookvalue = models.CharField(db_column='BookValue', max_length=10)  # Field name made lowercase.
    dividendpershare = models.CharField(db_column='DividendPerShare', max_length=45)  # Field name made lowercase.
    dividendyield = models.CharField(db_column='DividendYield', max_length=10)  # Field name made lowercase.
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
    exdividenddate = models.CharField(db_column='ExDividendDate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financial_fundamental_data'
        app_label = 'dbapp'


class LastPull(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase. The composite primary key (Date, Time) found, that is not supported. The first column is selected.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'last_pull'
        unique_together = (('date', 'time'),)
        app_label = 'dbapp'


class PricingData(models.Model):
    symbol = models.OneToOneField(FinancialFundamentalData, models.DO_NOTHING, db_column='Symbol', primary_key=True)  # Field name made lowercase.
    open = models.CharField(db_column='Open', max_length=10)  # Field name made lowercase.
    high = models.CharField(db_column='High', max_length=10)  # Field name made lowercase.
    low = models.CharField(db_column='Low', max_length=10)  # Field name made lowercase.
    close = models.CharField(db_column='Close', max_length=10)  # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=10)  # Field name made lowercase.
    currentprice = models.CharField(db_column='CurrentPrice', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pricing_data'
        app_label = 'dbapp'
