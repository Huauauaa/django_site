from django.http import HttpResponse
from django.views import View
import json

from django.views.decorators.csrf import csrf_exempt


class StudentView(View):
    students = ['John Doe', 'Micheal']

    def get(self, request):
        return HttpResponse(json.dumps(self.students))

    @csrf_exempt
    def post(self, request):
        return HttpResponse('POST')
