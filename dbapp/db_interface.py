# Uses av_interface.py functions to store and pull information from the database.

import django
from django.conf import settings
settings.configure()
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
    FDDtokens = getFFD(symbol, apikey)
    PDtokens = getPD(symbol, apikey)
    currDay = today.today()
    currTime = datetime.now()
    timeFormat = currTime.strftime("%H:%M:%S")

    #store LP
    lp = LP(date=currDay, time=timeFormat)
    lp.save()

    #store FFD
    ffd = FFD(symbol=FDDtokens[0], assettype=FDDtokens[1], name=FDDtokens[2], desc=FDDtokens[3], cik=FDDtokens[4],
              exchange=FDDtokens[5], currency=FDDtokens[6], country=FDDtokens[7], sector=FDDtokens[8], industry=FDDtokens[9],
              address=FDDtokens[10], fiscalyearend=FDDtokens[11], latestquarter=FDDtokens[12], marketcapitalization=FDDtokens[13], ebitda=FDDtokens[14],
              peration=FDDtokens[15], pegration=FDDtokens[16], bookvalue=FDDtokens[17], dividendpershare=FDDtokens[18], dividendyield=FDDtokens[19],
              eps=FDDtokens[20], revenuepersharettm=FDDtokens[21], profitmargin=FDDtokens[22], operatingmarginttm=FDDtokens[23], returnonassetsttm=FDDtokens[24],
              returnonequityttm=FDDtokens[25], revenuettm=FDDtokens[26], grossprofitttm=FDDtokens[27], dilutedepsttm=FDDtokens[28], quarterlyearningsgrowthyoy=FDDtokens[29],
              quarterlyrevenuegrowthyoy=FDDtokens[30], analysttargetprice=FDDtokens[31], analystratingstrongbuy=FDDtokens[32], analystratingbuy=FDDtokens[33], analystratinghold=FDDtokens[34],
              analystratingsell=FDDtokens[35], analystratingstrongsell=FDDtokens[36], trailingpe=FDDtokens[37], forwardpe=FDDtokens[38], pricetosalesration=FDDtokens[39],
              pricetobookratio=FDDtokens[40], evtorevenue=FDDtokens[41], evtoebitda=FDDtokens[42], beta=FDDtokens[43], number_52weekhigh=FDDtokens[44],
              number_52weeklow=FDDtokens[45], number_50daymovingaverage=FDDtokens[46], number_200daymovingaverage=FDDtokens[47], sharesoutstanding=FDDtokens[48], devidenddate=FDDtokens[49],
              exdivdenddate=FDDtokens[50])
    ffd.save()

    #store PD
    pd = PD(symbol=FDDtokens[0], open=PDtokens[0], high=PDtokens[1], low=PDtokens[2], close=PDtokens[3], volume=PDtokens[4])
    pd.save()

