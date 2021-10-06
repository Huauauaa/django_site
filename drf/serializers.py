from rest_framework import serializers

from drf.models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=10)
    created = serializers.DateTimeField(required=False)

    def validate_content(self, value):
        if '.' not in value:
            raise serializers.ValidationError('内容格式不正确')
        return value

    def create(self, validated_data):
        return Comment(**validated_data)
        # return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        # instance.save()
        return instance
