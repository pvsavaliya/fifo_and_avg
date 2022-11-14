from django.urls import path
from src.fifo_manage.api.views import BuyStocksrView, SellStocksView

urlpatterns = [
    path("buy_order",BuyStocksrView.as_view()),
    path("sell_order",SellStocksView.as_view())
]
