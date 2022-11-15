from rest_framework import serializers
from src.fifo_manage.models import BuyAndSell

class BuySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyAndSell
        fields = [
            "id",
            "company_name",
            "trade_type",
            "commulative_allocation",
            "quantity",
            "balance_qty",
            "avg_purchase_price",
            "buy_price",
            "sell_price",
            "created_at",
            "remaining_quantity",
            "trade_price"
        ]
class SellSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyAndSell
        fields = [
            "id",
            "company_name" ,
            "trade_type",
            "quantity",
            "sell_price" ,
            "trade_price",
            "balance_qty",
            "commulative_allocation",
        ]