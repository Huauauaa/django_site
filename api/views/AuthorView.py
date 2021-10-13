from functools import partial
from api.serializers import AuthorSerializer
from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView

from rest_framework.decorators import action
from api.models import Author


import json
from drf_yasg.utils import swagger_auto_schema


class AuthorView(APIView):
    '''
    def get(self, request):
        authors = Author.objects.all().values('name')

        return HttpResponse(json.dumps(list(authors)))

    '''

    @swagger_auto_schema(responses={200: AuthorSerializer(many=True)})
    def get(self, request):
        authors = Author.objects.all().values('name')
        serializer = AuthorSerializer(instance=authors, many=True)

        return HttpResponse(json.dumps(serializer.data))

    @swagger_auto_schema(operation_description="This is POST method for author")
    def post():
        return HttpResponse()
