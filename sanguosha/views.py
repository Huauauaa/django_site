from django.http import JsonResponse
from django.shortcuts import render


def index_view(request):
    return JsonResponse({'name': 'sanguosha'})
