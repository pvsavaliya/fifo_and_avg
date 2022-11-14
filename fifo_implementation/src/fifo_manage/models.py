from django.db import models

# Create your models here.

class BuyAndSell(models.Model):
    id                      = models.BigAutoField(primary_key=True,unique=True)
    company_name            = models.TextField(null=True,blank=True)
    trade_type              = models.TextField(null=True,blank=True)
    quantity                = models.TextField(null=True,blank=True)
    commulative_allocation  = models.FloatField(null=True,blank=True)
    quantity                = models.FloatField(null=True,blank=True)
    balance_qty             = models.FloatField(default=0)
    quantity                = models.TextField(null=True,blank=True)
    avg_purchase_price      = models.FloatField(null=True,blank=True)
    buy_price               = models.FloatField(null=True,blank=True)
    sell_price              = models.FloatField(null=True,blank=True)
    buy_at                  = models.DateTimeField(auto_now_add=True)
    sell_at                 = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = 'Buy Sell manage'