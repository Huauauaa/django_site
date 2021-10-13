from django.db import models
import jsonfield


class Teacher(models.Model):
    name = models.CharField(max_length=10)
    info = jsonfield.JSONField(default=dict, null=False)
