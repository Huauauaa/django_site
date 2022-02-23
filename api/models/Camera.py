from django.db import models


class Camera(models.Model):
    name = models.CharField('名称', max_length=10, blank=True, null=True)
