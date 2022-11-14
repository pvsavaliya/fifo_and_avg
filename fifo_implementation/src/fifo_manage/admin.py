from django.contrib import admin
from src.fifo_manage.models import BuyAndSell

class BuyAndSellManagement(admin.ModelAdmin):
    field = (
            "id",
            "company_name",
            "trade_type",
            "quantity",
            "commulative_allocation",
            "quantity",
            "balance_qty",
            "quantity",
            "avg_purchase_price",
            "buy_price",
            "sell_price",
            "buy_at",
            "sell_at",
        )
admin.site.register(BuyAndSell)