from django.db import models

class Dividend(models.Model):
    symbol = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=255 ,null=False)
    value = models.FloatField(null=False) 
