from django.db import models


class App(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'[{self.__class__.__qualname__}]-{self.name}'
