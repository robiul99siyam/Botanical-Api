from django.shortcuts import render
from rest_framework import viewsets
from .models import BennerSection
from .serializer import BennerSerializer
# Create your views here.

class BennerViewset(viewsets.ModelViewSet):
    queryset = BennerSection.objects.all()
    serializer_class = BennerSerializer
