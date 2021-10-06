from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('teacher', TeacherViewSet, basename='teacher')

urlpatterns = router.urls + [
    path(r'index', views.index_view),
    path('comment/', views.comment_view),
]
