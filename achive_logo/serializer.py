from rest_framework import serializers
from .models import Achive_logo


class AchiveSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = Achive_logo
        fields = '__all__'