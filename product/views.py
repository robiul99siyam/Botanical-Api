from django.shortcuts import render
from rest_framework import filters,pagination
from .models import Product,reviewer,ProductTag
from rest_framework import viewsets

from .models import Product,ProductTag,reviewer
from .serializer import ProductSerizer,ProductTagSerizer,reviwertSerizer





class ProductTagViewset(viewsets.ModelViewSet):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerizer


class reviewViewset(viewsets.ModelViewSet):
    queryset = reviewer.objects.all()
    serializer_class = reviwertSerizer

class ProductPagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = page_size
    max_page_size = 10


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerizer

    filter_backends = [filters.SearchFilter]
    pagination_class = ProductPagination

    search_fields = ['product_tag__name','name']

  