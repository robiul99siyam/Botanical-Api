from django.shortcuts import render
from rest_framework import viewsets
from .models import DailyProduct
from .serializer import DailyProductSerializer


class DailyProductViewset(viewsets.ModelViewSet):
    queryset = DailyProduct.objects.all()
    serializer_class  = DailyProductSerializer