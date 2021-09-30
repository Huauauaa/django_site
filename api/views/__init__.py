from api.views.StudentView import *
from api.views.TeacherViewSet import *
from api.views.book_view import *
from api.views.AuthorView import *


def index_view(request):
    return JsonResponse({'name': 'api'})
