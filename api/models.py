from django.db import models
from enum import Enum


class Gender(Enum):
    male: '男'
    female: '女'


class Character(models.Model):
    name = models.CharField('名称', max_length=10, )
    group = models.CharField('势力', max_length=1, default='-', )
    gender = models.CharField('性别', max_length=1, choices=[(g.value, g.name) for g in Gender])

    def __str__(self):
        return f'[{self.name}]-[{self.group}]-[{self.gender}]'
