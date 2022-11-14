from http import HTTPStatus
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import BuySerializer
from src.fifo_manage.models import BuyAndSell
# Create your views here.

class BuyStocksrView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset           = BuyAndSell.objects.all()
    serializer_class   = BuySerializer

    def post(self, request, *args, **kwargs):

        try:
            data = request.data
            if not data:
                response = {"message":"Payload not found."}
            else:
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                breakpoint()
                
                buy_data = BuyAndSell.objects.get(id=serializer.data.get("id"))
                buy_data.balance_qty += data.get("quantity",0)
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
                'message': 'somthing is worng.',
                'error': str(e)
            }
        return Response(response, content_type="application/json")

class SellStocksView(generics.ListAPIView):
    permissions_classes = [permissions.AllowAny]
    queryset = BuyAndSell.objects.all()
    serializer_class = BuySerializer
