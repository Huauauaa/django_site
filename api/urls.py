from django.urls import path
from rest_framework import routers

from api.views import AuthorView, StudentView, TeacherViewSet, book_view
from api.views.CameraViewSet import CameraViewSet
from api.views.ContainerView import ContainerView

from . import views

router = routers.DefaultRouter()
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('camera', CameraViewSet, basename='camera')

urlpatterns = router.urls + [
    path('', views.index_view),
    path('student/', StudentView.as_view()),
    path('container/', ContainerView.as_view()),
    path('book/', book_view),
    path('author/', AuthorView.as_view()),
]
