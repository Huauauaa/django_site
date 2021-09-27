from django.db import models


class Author(models.Model):
    name = models.CharField('姓名', max_length=10)
