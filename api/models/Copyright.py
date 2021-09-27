from django.db import models


class Copyright(models.Model):
    content = models.CharField('内容', max_length=200)

    def __str__(self) -> str:
        return f'[Copyright]-{self.content}'