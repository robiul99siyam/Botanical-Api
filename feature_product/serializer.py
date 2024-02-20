from .models import Featuere_product
from rest_framework import serializers

class FeatureSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Featuere_product
        fields = "__all__"