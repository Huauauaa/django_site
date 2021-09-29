from django.http.response import JsonResponse
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from api.models.Teacher import Teacher
from api.serializers.TeacherSerializer import TeacherSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all().order_by('-id')

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    @action(detail=False, methods=['get'])
    def get_all(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_test(self, request):
        target = get_object_or_404(self.get_queryset(), pk=2)
        serializer = self.serializer_class(target)
        return Response(serializer.data)
