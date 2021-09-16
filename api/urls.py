from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('student', views.StudentView.as_view()),
    path('teacher', views.TeacherView.as_view()),
]
