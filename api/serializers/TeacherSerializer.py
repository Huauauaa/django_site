from api.models.Teacher import Teacher
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class TeacherSerializer(ModelSerializer):
    name = serializers.CharField(max_length=10)

    class Meta():
        model = Teacher
        fields = '__all__'