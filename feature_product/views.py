from django.shortcuts import render
from django.urls import path,include
from .serializer import FeatureSerilizer
from .models import Featuere_product
from rest_framework import viewsets

class FeatureViews(viewsets.ModelViewSet):
    queryset = Featuere_product.objects.all()
    serializer_class = FeatureSerilizer
