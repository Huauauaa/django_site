from rest_framework import serializers
from rest_framework.serializers import Serializer

from api.models import Author, Book, Copyright, Publication


class BookSerializer(Serializer):
    name = serializers.CharField(max_length=20)
    publication_name = serializers.CharField(source='publication.name')
    publication = serializers.CharField(source='publication_id')
    copyright = serializers.CharField(source='copyright_id')
    # authors = serializers.ReadOnlyField(source='authors')

    class Meta:
        model = Book
        fields = ('id', 'name', 'publication_name')

    def create(self, validated_data):
        print('validated_data', validated_data)
        return Book.objects.create(**validated_data)
