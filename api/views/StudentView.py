import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.views import APIView

from api.models import Student


class StudentSerializer(serializers.Serializer):
    username = serializers.CharField(source='name')
    id = serializers.IntegerField()


class StudentView(APIView):
    students = Student.objects.all()
    student = Student.objects.all().first()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # ser = StudentSerializer(instance=self.students, many=1)
        # return HttpResponse(json.dumps(ser.data))
        ser1 = StudentSerializer(instance=self.student, many=0)
        return HttpResponse(json.dumps(ser1.data), content_type=json)

    def post(self, request):
        return HttpResponse('POST')
