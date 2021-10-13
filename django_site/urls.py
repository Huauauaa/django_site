"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('sanguosha/', include('sanguosha.urls')),
    path('react/', include('react.urls')),
    path('tailwind/', include('tailwind.urls')),
    path('drf/', include('drf.urls')),
    path(
        'swagger-ui/',
        get_schema_view(
            openapi.Info(
                title="API Server",
                default_version='v1',
            ),
            public=True,
        ).with_ui('swagger', cache_timeout=0),
        name='swagger-ui',
    ),
]
