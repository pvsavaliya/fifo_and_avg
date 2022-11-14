from rest_framework import serializers
from src.fifo_manage.models import BuyAndSell

class BuySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyAndSell
        fields = [
            "id",
            "company_name",
            "trade_type",
            "quantity",
            "commulative_allocation",
            "quantity",
            # "balance_qty",
            "quantity",
            "avg_purchase_price",
            "buy_price",
            # "sell_price",
            "buy_at",
            # "sell_at",
        ]

    # def create(self, validated_data):
        
    #     user_obj = self.Meta.model(**validated_data)
    #     user_obj.save()
    #     return user_obj