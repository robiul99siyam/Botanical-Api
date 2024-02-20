from .models import DailyProduct
from rest_framework import serializers

class DailyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyProduct
        fields = "__all__"
