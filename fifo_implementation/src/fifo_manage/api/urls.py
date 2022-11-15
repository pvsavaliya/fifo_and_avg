from django.urls import path
from src.fifo_manage.api.views import BuyStocksView, SellStocksView, SplitStocksView

urlpatterns = [
    path("buy_order",BuyStocksView.as_view()),
    path("sell_order",SellStocksView.as_view()),
    path("split_order",SplitStocksView.as_view()),
]
