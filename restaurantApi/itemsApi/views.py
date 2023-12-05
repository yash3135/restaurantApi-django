from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import *
from .models import *
from . import serializers

# Create your views here.
@csrf_exempt
def FoodItemsApi(request,id=0):
    if request.method == 'GET':
        fooditems = Items.objects.all()
        fooditems_serializers = serializers.FoodItemsSerializer(fooditems,many=True)
        return JsonResponse(fooditems_serializers.data,safe=False)

