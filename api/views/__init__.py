from api.views.StudentView import *
from api.views.TeacherView import *


def index_view(request):
    return JsonResponse({'name': 'api'})
