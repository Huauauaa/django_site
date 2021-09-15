from django.http import HttpResponse
from django.views import View
import json


class StudentView(View):
    students = ['John Doe', 'Micheal']

    def get(self, request):
        return HttpResponse(json.dumps(self.students))
