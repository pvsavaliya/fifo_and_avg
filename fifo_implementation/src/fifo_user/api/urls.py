from django.urls import path
from .views import UserRegisterApi

urlpatterns = [
    path('register/', UserRegisterApi.as_view())
]
