from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render


def index_view(request):
    print(request)
    return JsonResponse({'name': 'django-rest-framework'})
