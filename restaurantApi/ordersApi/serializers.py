from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orders
        fields = ('__all__')
