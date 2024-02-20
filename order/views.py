from django.shortcuts import render
from .models import OrderProduct
from .serializer import OrderSerialzer
from rest_framework import viewsets


class OrderProductViewset(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderSerialzer

    