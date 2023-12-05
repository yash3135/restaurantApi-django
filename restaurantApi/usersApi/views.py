from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import *
from .models import *
from . import serializers


# Create your views here.
@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        User = Users.objects.all()
        UserSerializer = serializers.UserSerializer(User, many=True)
        return JsonResponse(UserSerializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        UserSerializer = serializers.UserSerializer(data=user_data)
        if UserSerializer.is_valid():
            UserSerializer.save()
            return JsonResponse("User Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        users = Users.objects.get(user_id=user_data['id'])
        UserSerializer = serializers.UserSerializer(users,data=user_data)
        if UserSerializer.is_valid():
            UserSerializer.save()
            return JsonResponse("User Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        users = Users.objects.get(user_id=id)
        users.delete()
        return JsonResponse("User Deleted Successfully", safe=False)


