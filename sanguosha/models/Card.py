from django.db import models

from sanguosha.enums.Rank import Rank

from sanguosha.enums.Suit import Suit


class Card(models.Model):
    name = models.CharField('名称', max_length=10)
    rank = models.IntegerField('点数', choices=[(item.value, item.name) for item in Rank], default=0)
    suit = models.IntegerField('花色', choices=[(item.value, item.name) for item in Suit], default=0)
    desc = models.CharField('功能', max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{Suit(self.suit).name}{Rank(self.rank).name}'
