import graphene
from graphene_django import DjangoObjectType
from .models import Price

class PriceType(DjangoObjectType):
    class Meta:
        model = Price
        fields = ("id", "date","ticker","commodity", "close", "open", "high", "low", "volume")


class Ticker(graphene.ObjectType):
    ticker = graphene.String()
    commodity = graphene.String()

class Query(graphene.ObjectType):
    prices = graphene.List(PriceType, ticker=graphene.String(required=False))
    tickers = graphene.List(Ticker)

    def resolve_prices(self, info, ticker=None):
        result = Price.objects.filter(ticker=ticker) if ticker else Price.objects.all()
        result = result.order_by('date')
        return result
    
    def resolve_tickers(self, info):
        return Price.objects.values('ticker', 'commodity').distinct()

    
    
schema = graphene.Schema(query=Query)