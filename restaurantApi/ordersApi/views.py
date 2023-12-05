from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import *
from .models import *
from . import serializers

# Create your views here.
@csrf_exempt
def ordersApi(request,id=0):
    if request.method == 'GET':
        order = Orders.objects.all()
        order_serializers = serializers.OrderSerializer(order, many=True)
        return JsonResponse(order_serializers.data, safe=False)
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        OrderSerializer = serializers.OrderSerializer(data=order_data)
        if OrderSerializer.is_valid():
            OrderSerializer.save()
            return JsonResponse("Order Successfully Placed", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        get_order = Orders.objects.get(o_id=order_data['id'])
        OrderSerializer = serializers.OrderSerializer(data=order_data)
        if OrderSerializer.is_valid():
            OrderSerializer.save()
            return JsonResponse("Order Updated Successfully", safe=False)
        return JsonResponse("Failed to Updated", safe=False)
    elif request.method == 'DELETE':
        order = Orders.objects.get(o_id=id)
        order.delete()
        return JsonResponse("order Deleted Successfully", safe=False)
