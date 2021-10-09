from django.db import models
from api.models.Agent import Agent
from api.models.App import App


class ContainerStatus(models.Model):
    app = models.ForeignKey(App, null=False, on_delete=models.CASCADE, related_name='container_status_app')
    agent = models.ForeignKey(Agent, null=False, on_delete=models.CASCADE, related_name='container_status_agent')

    def __str__(self):
        return f'[{self.__class__.__qualname__}]-({self.app}-{self.agent})'
