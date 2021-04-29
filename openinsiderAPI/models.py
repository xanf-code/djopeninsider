from django.db import models

# Create your models here.


class openInsider(models.Model):
    date = models.CharField(max_length=50)
    ticker = models.CharField(max_length=50, default='Null')
    companyName = models.CharField(max_length=200)
    insiderName = models.CharField(max_length=50)
    insiderLink = models.CharField(max_length=200)
    insiderID = models.CharField(max_length=50)
    insiderTitle = models.CharField(max_length=200)
    tradeType = models.CharField(max_length=50)
    tradePrice = models.CharField(max_length=200)
    tradeQuantity = models.CharField(max_length=50)
    stocksOwned = models.CharField(max_length=200)
    stockPercent = models.CharField(max_length=50)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.tradePrice
