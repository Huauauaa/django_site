from django.db import models


class Publication(models.Model):
    name = models.CharField('名称', max_length=20)
