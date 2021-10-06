from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from drf.models import Comment
from drf.serializers import CommentSerializer

import json


def index_view(request):
    return JsonResponse({'name': 'django-rest-framework'})


@csrf_exempt
def comment_view(request):
    method = request.method
    if method == 'POST':
        payload = json.loads(request.body)
        serializer = CommentSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
    elif method == 'PUT':
        payload = json.loads(request.body)
        serializer = CommentSerializer(data=payload)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
    else:
        comment = Comment(email='harvey0379@163.com', content='Hello World')

        serializer = CommentSerializer(comment)

        return JsonResponse(serializer.data)
