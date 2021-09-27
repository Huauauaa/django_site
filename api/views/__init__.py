from api.views.StudentView import *
from api.views.TeacherViewSet import *


def index_view(request):
    return JsonResponse({'name': 'api'})
