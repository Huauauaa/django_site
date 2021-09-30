from api.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    author_name = serializers.CharField(source='name')

    class Meta:
        model = Author
        fields = '__all__'
