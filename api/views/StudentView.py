import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from api.models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class StudentView(View):
    students = Student.objects.all()
    student = Student.objects.all().first()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # ser = StudentSerializer(instance=self.students, many=1)
        # return HttpResponse(json.dumps(ser.data))
        ser1 = StudentSerializer(instance=self.student, many=0)
        return HttpResponse(json.dumps(ser1.data))

    def post(self, request):
        return HttpResponse('POST')
