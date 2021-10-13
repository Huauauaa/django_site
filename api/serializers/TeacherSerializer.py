from api.models.Teacher import Teacher
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from drf_yasg import openapi


class InfoField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "info",
            "properties": {
                "school": openapi.Schema(
                    title="毕业院校",
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "name": openapi.Schema(
                            title="名称",
                            type=openapi.TYPE_STRING,
                        ),
                        "address": openapi.Schema(
                            title="地址",
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                "maritalStatus": openapi.Schema(
                    title="婚姻状况",
                    type=openapi.TYPE_BOOLEAN,
                ),
            },
            "required": [
                "school",
            ],
        }


class TeacherSerializer(ModelSerializer):
    name = serializers.CharField(max_length=10)
    info = InfoField()

    class Meta:
        model = Teacher
        fields = '__all__'
