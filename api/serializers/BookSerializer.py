from api.serializers.AuthorSerializer import AuthorSerializer
from rest_framework import serializers
from rest_framework.serializers import Serializer

from api.models import Book


class BookSerializer(Serializer):
    name = serializers.CharField()
    publication_id = serializers.CharField()
    copyright = serializers.CharField(source='copyright_id')
    publication = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()

    def get_authors(self, row):
        authors = row.authors.all()
        return [{'id': item.id, 'name': item.name} for item in authors]

    def get_publication(self, row):
        return {'id': row.publication.id, 'name': row.publication.name}

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
