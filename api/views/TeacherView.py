from django.http import JsonResponse
from rest_framework.views import APIView


class TeacherView(APIView):

    def get(self, request):
        return JsonResponse({'class_name': 'TeacherView'})
