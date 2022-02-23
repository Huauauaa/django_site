from api.models.Camera import Camera
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CameraSerializer(ModelSerializer):
    name = serializers.CharField(max_length=10, error_messages={'blank': '名称不能为空'})

    class Meta:
        model = Camera
        fields = '__all__'
