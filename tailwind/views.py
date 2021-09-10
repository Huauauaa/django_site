from django.shortcuts import render
from rest_framework_jwt.serializers import User


def index_view(request):
    user = User.objects.values()[0]
    return render(request, 'tailwind/index.html', locals())
