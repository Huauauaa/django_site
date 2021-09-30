from api.serializers import AuthorSerializer
from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView

from rest_framework.decorators import action
from api.models import Author


import json


class AuthorView(APIView):
    '''
    def get(self, request):
        authors = Author.objects.all().values('name')

        return HttpResponse(json.dumps(list(authors)))

    '''

    def get(self, request):
        authors = Author.objects.all().values('name')
        serializer = AuthorSerializer(instance=authors, many=True)

        return HttpResponse(json.dumps(serializer.data))
