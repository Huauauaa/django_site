from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from api.models.Teacher import Teacher
from api.serializers.TeacherSerializer import TeacherSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': request.data})
        else:
            return HttpResponse({'data': 'wrong'})

    @action(detail=False, methods=['get'])
    def get_test(self, request):
        target = get_object_or_404(self.get_queryset(), pk=2)
        serializer = self.serializer_class(target)
        return Response(serializer.data)
