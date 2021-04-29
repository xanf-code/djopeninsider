from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import openInsider
from .serializer import openInsiderSerializer
import requests
from bs4 import BeautifulSoup


def index(request):
    return HttpResponse("Welcome to Open Insider API")


class insiderAPI(viewsets.ModelViewSet):
    queryset = openInsider.objects.all()
    serializer_class = openInsiderSerializer


def latest(request):
    response = requests.get('http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=5&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&iscoo=1&iscfo=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=200')

    soup = BeautifulSoup(response.text, "html.parser")

    main = soup.select("#tablewrapper > table > tbody > tr")

    for insider in main:
        date = insider.select_one('td:nth-child(3) > div').getText()
        ticker = insider.select_one('td:nth-child(4) > b > a').getText()
        companyName = insider.select_one('td:nth-child(5) > a').getText()
        insiderName = insider.select_one('td:nth-child(6) > a').getText()
        insiderLink = insider.select_one('td:nth-child(6) > a')['href']
        insiderID = insiderLink[len(insiderLink) - 7:]
        insiderTitle = insider.select_one('td:nth-child(7)').getText()
        tradeType = insider.select_one('td:nth-child(8)').getText()
        tradePrice = insider.select_one('td:nth-child(9)').getText()
        tradeQuantity = insider.select_one('td:nth-child(10)').getText()
        stocksOwned = insider.select_one('td:nth-child(11)').getText()
        stockPercent = insider.select_one('td:nth-child(12)').getText()
        value = insider.select_one('td:nth-child(13)').getText()

        openinsider = openInsider()
        openinsider.date = date
        openinsider.ticker = ticker
        openinsider.companyName = companyName
        openinsider.insiderName = insiderName
        openinsider.insiderLink = insiderLink
        openinsider.insiderID = insiderID
        openinsider.insiderTitle = insiderTitle
        openinsider.tradeType = tradeType
        openinsider.tradePrice = tradePrice
        openinsider.tradeQuantity = tradeQuantity
        openinsider.stocksOwned = stocksOwned
        openinsider.stockPercent = stockPercent
        openinsider.value = value

        openinsider.save()
    return HttpResponse("Latest data fetched")
