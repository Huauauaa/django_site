from django.db import models

from sanguosha.enums.Gender import Gender

from sanguosha.enums.Group import Group


class Character(models.Model):
    name = models.CharField('名称', max_length=10, )
    group = models.IntegerField('势力', choices=[(item.value, item.name) for item in Group], )
    gender = models.IntegerField('性别', choices=[(item.value, item.name) for item in Gender], )

    def __str__(self):
        return f'[{self.name}]-[{Group(self.group).name}]-[{Gender(self.gender).name}]'

    class Meta:
        app_label = 'api'
