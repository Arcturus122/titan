from django.db import models

# Create your models here.
class Price(models.Model):
    ticker = models.CharField(max_length=10)
    commodity = models.CharField(max_length=100)
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    class Meta:
        unique_together = ('ticker', 'date',)

    def __str__(self):
        return f'{self.commodity}|{self.ticker} @ {self.date} - {self.close} $' 
    
