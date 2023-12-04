from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import *
from .models import *
from . import serializers

# Create your views here.
@csrf_exempt
def categoryApi(request,id=0):
    if request.method == 'GET':
        category = Category.objects.all()
        category_serializers = serializers.CategorySerializer(category,many=True)
        return JsonResponse(category_serializers.data,safe=False)

