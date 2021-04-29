from rest_framework import serializers
from .models import openInsider


class openInsiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = openInsider
        fields = ('__all__')
