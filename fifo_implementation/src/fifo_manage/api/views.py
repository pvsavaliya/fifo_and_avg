from http import HTTPStatus
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import BuySerializer, SellSerializer
from src.fifo_manage.models import BuyAndSell
from django.db.models import Q
# Create your views here.

class BuyStocksView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset           = BuyAndSell.objects.all()
    serializer_class   = BuySerializer

    def post(self, request, *args, **kwargs):

        try:
            data = request.data
            if not data:
                response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Payload not found.'
                }
                return Response(response, content_type="application/json")

            buy_data = BuyAndSell.objects.filter(company_name = data["company_name"]).order_by("-created_at").first()

            if buy_data:
                bal_qty       = buy_data.balance_qty + data["quantity"]
                avg_price     = (( (buy_data.avg_purchase_price * buy_data.balance_qty) 
                                + (data["quantity"] * data["buy_price"]) )
                                / (data["quantity"] + buy_data.balance_qty)
                                )
                remaining_qty = data["quantity"]

                data.update({
                    "balance_qty": bal_qty ,
                    "avg_purchase_price": avg_price,
                    "remaining_quantity" : remaining_qty
                    })
            else:
                data.update({
                    "balance_qty": data["quantity"] ,
                    "avg_purchase_price": data["buy_price"],
                    "remaining_quantity" : data["quantity"]
                    })

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
                
            response = {
                'success': True,
                'status_code': HTTPStatus.OK,
                'message': 'Your order place successfully.',
                'data': serializer.data
            }
            
        except Exception as e:
            response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'something is wrong.',
                'error': str(e)
            }
        return Response(response, content_type="application/json")

class SellStocksView(generics.UpdateAPIView):
    permissions_classes = [permissions.AllowAny]
    queryset = BuyAndSell.objects.all()
    serializer_class = SellSerializer

    def post(self, request, *args, **kwargs):

        try:
            data = request.data
            if not data:
                response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Payload not found.'
                }
                return Response(response, content_type="application/json")

            sell_data = BuyAndSell.objects.filter(Q(trade_type = "buy") | Q(remaining_quantity__gt = 0)).filter(company_name = data["company_name"],is_sold = False).order_by("created_at")

            if not sell_data:
                response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'User not found.'
                }
                return Response(response, content_type="application/json")

            sell_count = data["quantity"]
            last_len = len(sell_data)-1

            if sell_count > sell_data[last_len].balance_qty :
                response = {
                            'success': False,
                            'status_code': HTTPStatus.BAD_REQUEST,
                            'message': 'You do not have enough credit.'
                            }
                return Response(response, content_type="application/json")
                
            for sell in sell_data:
                if sell_count > sell.remaining_quantity:
                    sell_count -= sell.remaining_quantity
                    sell.remaining_quantity = 0
                    sell.is_sold = True
                    sell.save()
                else:
                    sell.remaining_quantity -= sell_count
                    sell.save()
                    break
            data.update({ 
                "balance_qty": sell_data[last_len].balance_qty - data["quantity"] ,
                "commulative_allocation": sell_data[last_len].commulative_allocation})    
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
                
            response = {
                'success': True,
                'status_code': HTTPStatus.OK,
                'message': 'Your order sold successfully.',
                'data': serializer.data
            }

        except Exception as e:
            response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'something is wrong.',
                'error': str(e)
            }
        return Response(response, content_type="application/json")

class SplitStocksView(generics.UpdateAPIView):
    permissions_classes = [permissions.AllowAny]
    queryset = BuyAndSell.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            if not data:
                response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Payload not found.'
                }
                return Response(response, content_type="application/json")

            split_ratio = data["split_ratio"]
            split_data = BuyAndSell.objects.filter(company_name = data["company_name"]).order_by("-created_at").first()
            if not split_data:
                response = {
                    'success': False,
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'message': 'User not found.'
                    }
                return Response(response, content_type="application/json")

            split_data.balance_qty = (split_data.balance_qty * int(split_ratio.split(":")[0])) / int(split_ratio.split(":")[1])

            split_data.save()
            response = {
                    'success': True,
                    'status_code': HTTPStatus.OK,
                    'message': 'Split successfully.'
                }

        except Exception as e:
            response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'something is wrong.',
                'error': str(e)
            }
        return Response(response, content_type="application/json")