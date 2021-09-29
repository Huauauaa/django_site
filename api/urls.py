from api.views import StudentView, TeacherViewSet
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('teacher', TeacherViewSet, basename='teacher')

urlpatterns = router.urls + [
    path('', views.index_view),
    path('student', StudentView.as_view()),
]
