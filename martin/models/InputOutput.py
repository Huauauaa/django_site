from django.db import models
import datetime


class InputOutput(models.Model):
    datetime = models.DateTimeField('时间', unique=True, default=datetime.datetime.now)
    milk = models.IntegerField('奶粉(ml)', default=150)
    ad = models.BooleanField('AD')
    d3 = models.BooleanField('D3')
    ld = models.BooleanField('郎迪')
    water = models.BooleanField('水')
    excrement = models.BooleanField('大便')

    class Meta:
        verbose_name = '出入量'
