from .models import OrderProduct
from rest_framework import serializers


class OrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'