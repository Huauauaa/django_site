from rest_framework import serializers

from drf.models import Comment


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    id = serializers.IntegerField()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式不正确'})
    content = serializers.CharField(max_length=10)
    created = serializers.DateTimeField(required=False)
    user = UserSerializer(required=False)

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
