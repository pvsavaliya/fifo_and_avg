from http import HTTPStatus
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import UserRegisterSerializer
from src.fifo_user.models import UserDetail
import jwt
import datetime
# Create your views here.

class UserRegisterApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = UserDetail.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()
            payload = {
            'id': serializer.data,
            'int': str(datetime.datetime.utcnow()),
            'exp': str(datetime.datetime.utcnow() + datetime.timedelta(minutes=1)),
            }
            token = jwt.encode(payload, 'secret',
                                algorithm='HS256')

            response = Response()
            # response.set_cookie(key='jwt', value=token, httponly=True)

            status_code = HTTPStatus.OK 
            response = {
                'status': True,
                'status_code': status_code,
                'message': 'You are registered successfully.',
                'data': {
                    'user': serializer.data,
                    'token': token,
                }
            }
        except Exception as exc:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Please, enter valid data',
                'error': str(exc),
            }
        return Response(response, status=status_code)

