import json
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.views import APIView

from api.models.ContainerStatus import ContainerStatus


class ContainerView(APIView):
    def get_queryset(self):
        return ContainerStatus.objects.all()

    def get(self, request):
        container_status_list = self.get_queryset()
        agents = list(map(lambda item: item.agent, container_status_list))
        apps = list(map(lambda item: item.app, container_status_list))

        data = serializers.serialize('json', agents)
        return HttpResponse(data, content_type="application/json")
