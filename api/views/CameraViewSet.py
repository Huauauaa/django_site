from api.models.Camera import Camera
from api.serializers.CameraSerializer import CameraSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CameraViewSet(ModelViewSet):
    serializer_class = CameraSerializer

    def get_queryset(self):
        return Camera.objects.all().order_by('-id')

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'message': next(iter(serializer.errors.values()))[0]})

