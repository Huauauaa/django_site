from django.db import models


class Student(models.Model):
    name = models.CharField('名称', max_length=10)
    grade = models.IntegerField('分数')

    def __str__(self):
        return f'Stu[{self.name}]'
