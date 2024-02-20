from .models import Product,reviewer,ProductTag
from rest_framework import serializers

class ProductSerizer(serializers.ModelSerializer):
    product_tag= serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = '__all__'



class ProductTagSerizer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = '__all__'


class reviwertSerizer(serializers.ModelSerializer):
    class Meta:
        model = reviewer
        fields = '__all__'