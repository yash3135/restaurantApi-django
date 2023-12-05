from rest_framework import serializers
from . import models


class FoodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Items
        fields = ('__all__')
