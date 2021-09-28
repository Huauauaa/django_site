from api.models.Author import Author
from api.models.Publication import Publication
from api.models.Copyright import Copyright
from django.db import models


class Book(models.Model):
    name = models.CharField('书名', max_length=20)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    copyright = models.OneToOneField(Copyright, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return f'[Book]-{self.name}'
