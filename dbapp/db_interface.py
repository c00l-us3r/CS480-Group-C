# Uses av_interface.py functions to store and pull information from the database.

import django
from django.conf import settings
settings.configure(DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stock_data',   #name of the database
        'USER': 'root',         #change to your username
        'PASSWORD': '2003',     #change to your password
        'HOST': 'localhost',    #change to your host
        'PORT': '3306',         #change to your port
    }
})
django.setup()
from av_interface import getFinancialFundamentalData as getFFD
from av_interface import getPricingData as getPD
from models import FinancialFundamentalData as FFD
from models import PricingData as PD
from models import LastPull as LP
from datetime import date as today
from datetime import datetime

def updateDB(symbol, apikey):
    #pull data
    FFDtokens = getFFD(symbol, apikey)
    PDtokens = getPD(symbol, apikey)
    currDay = today.today()
    currTime = datetime.now()
    timeFormat = currTime.strftime("%H:%M:%S")

    #store LP
    lp = LP(date=currDay, time=timeFormat)
    lp.save()

    #store FFD
    if FFD.objects.filter(symbol=FFDtokens[0]).exists:
        FFD.objects.filter(symbol=FFDtokens[0]).update(
            assettype=FFDtokens[1], name=FFDtokens[2], desc=FFDtokens[3], cik=FFDtokens[4],
            exchange=FFDtokens[5], currency=FFDtokens[6], country=FFDtokens[7], sector=FFDtokens[8], industry=FFDtokens[9],
            address=FFDtokens[10], fiscalyearend=FFDtokens[11], latestquarter=FFDtokens[12], marketcapitalization=FFDtokens[13], ebitda=FFDtokens[14],
            peration=FFDtokens[15], pegration=FFDtokens[16], bookvalue=FFDtokens[17], dividendpershare=FFDtokens[18], dividendyield=FFDtokens[19],
            eps=FFDtokens[20], revenuepersharettm=FFDtokens[21], profitmargin=FFDtokens[22], operatingmarginttm=FFDtokens[23], returnonassetsttm=FFDtokens[24],
            returnonequityttm=FFDtokens[25], revenuettm=FFDtokens[26], grossprofitttm=FFDtokens[27], dilutedepsttm=FFDtokens[28], quarterlyearningsgrowthyoy=FFDtokens[29],
            quarterlyrevenuegrowthyoy=FFDtokens[30], analysttargetprice=FFDtokens[31], analystratingstrongbuy=FFDtokens[32], analystratingbuy=FFDtokens[33], analystratinghold=FFDtokens[34],
            analystratingsell=FFDtokens[35], analystratingstrongsell=FFDtokens[36], trailingpe=FFDtokens[37], forwardpe=FFDtokens[38], pricetosalesrationttm=FFDtokens[39],
            pricetobookratio=FFDtokens[40], evtorevenue=FFDtokens[41], evtoebitda=FFDtokens[42], beta=FFDtokens[43], number_52weekhigh=FFDtokens[44],
            number_52weeklow=FFDtokens[45], number_50daymovingaverage=FFDtokens[46], number_200daymovingaverage=FFDtokens[47], sharesoutstanding=FFDtokens[48], dividenddate=FFDtokens[49],
            exdividenddate=FFDtokens[50]
        )
    else:
        ffd = FFD(symbol=FFDtokens[0], assettype=FFDtokens[1], name=FFDtokens[2], desc=FFDtokens[3], cik=FFDtokens[4],
                exchange=FFDtokens[5], currency=FFDtokens[6], country=FFDtokens[7], sector=FFDtokens[8], industry=FFDtokens[9],
                address=FFDtokens[10], fiscalyearend=FFDtokens[11], latestquarter=FFDtokens[12], marketcapitalization=FFDtokens[13], ebitda=FFDtokens[14],
                peration=FFDtokens[15], pegration=FFDtokens[16], bookvalue=FFDtokens[17], dividendpershare=FFDtokens[18], dividendyield=FFDtokens[19],
                eps=FFDtokens[20], revenuepersharettm=FFDtokens[21], profitmargin=FFDtokens[22], operatingmarginttm=FFDtokens[23], returnonassetsttm=FFDtokens[24],
                returnonequityttm=FFDtokens[25], revenuettm=FFDtokens[26], grossprofitttm=FFDtokens[27], dilutedepsttm=FFDtokens[28], quarterlyearningsgrowthyoy=FFDtokens[29],
                quarterlyrevenuegrowthyoy=FFDtokens[30], analysttargetprice=FFDtokens[31], analystratingstrongbuy=FFDtokens[32], analystratingbuy=FFDtokens[33], analystratinghold=FFDtokens[34],
                analystratingsell=FFDtokens[35], analystratingstrongsell=FFDtokens[36], trailingpe=FFDtokens[37], forwardpe=FFDtokens[38], pricetosalesrationttm=FFDtokens[39],
                pricetobookratio=FFDtokens[40], evtorevenue=FFDtokens[41], evtoebitda=FFDtokens[42], beta=FFDtokens[43], number_52weekhigh=FFDtokens[44],
                number_52weeklow=FFDtokens[45], number_50daymovingaverage=FFDtokens[46], number_200daymovingaverage=FFDtokens[47], sharesoutstanding=FFDtokens[48], dividenddate=FFDtokens[49],
                exdividenddate=FFDtokens[50])
        ffd.save()

    #store PD
    if PD.objects.filter(symbol=FFDtokens[0]).exists:
        PD.objects.filter(symbol=FFDtokens[0]).update(
            open=PDtokens[0], high=PDtokens[1], low=PDtokens[2], close=PDtokens[3], volume=PDtokens[4]
        )
    else:
        pd = PD(symbol=FFDtokens[0], open=PDtokens[0], high=PDtokens[1], low=PDtokens[2], close=PDtokens[3], volume=PDtokens[4])
        pd.save()