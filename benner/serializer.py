from rest_framework import serializers
from .models import BennerSection


class BennerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BennerSection
        fields = '__all__'