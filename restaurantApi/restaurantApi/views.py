from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

@csrf_exempt
def restaurantApi(request):
    if request.method == 'GET':
        return JsonResponse({'name':'chiraag'})