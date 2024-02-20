from django.shortcuts import render
from rest_framework import viewsets
from .models import Achive_logo
from .serializer import AchiveSeriailzer


class AchiveViewset(viewsets.ModelViewSet):
    queryset = Achive_logo.objects.all()
    serializer_class = AchiveSeriailzer